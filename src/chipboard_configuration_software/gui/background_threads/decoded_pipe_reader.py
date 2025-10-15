import ctypes
import logging
import os
import time
import pyqtgraph as pg

import numpy as np
from PySide6.QtCore import Slot, Qt, QObject, Signal, QThread, QTimer
from chipboard_configuration_software.c_decoder import event_decoder_lib
from chipboard_configuration_software.gui.background_threads.decoded_pipe_reader_types import *

logger = logging.getLogger(__name__)


def open_named_pipe(path: str) -> int:
    return lib.open_pipe(path.encode('utf-8'))


def close_named_pipe(fd: int):
    lib.close_pipe(fd)


def nearest_power_of_two(x: int) -> int:
    """Round an integer to the nearest power of 2."""
    if x < 1:
        return 1
    lower = 1 << (x.bit_length() - 1)  # largest power of 2 <= x
    upper = lower << 1  # next power of 2 > x
    return lower if (x - lower) <= (upper - x) else upper


class ChannelBuffers:
    """
    A rolling ring-buffer manager for storing ADC readings per channel,
    with incremental histograms maintained in parallel using uniform,
    power-of-2 binning for fast updates.

    Motivation
    ----------
    In your data stream, each decoded packet (`DecodedPacket`) may contain
    a variable number of channels (up to 16), and the set of channels
    is not guaranteed to be the same across packets. For example:
        - Event 1 → (ch0, ch3, ch1)
        - Event 2 → (ch0, ch1)
        - Event 3 → (ch3, ch4)

    To handle this variability efficiently, each channel gets its own
    independent circular (ring) buffer of fixed length. When a packet arrives,
    we only update the buffers for the channels that are present in that packet.

    In addition to storing recent samples, each channel also maintains
    histograms for [adc_a, adc_b, adc_c, adc_t]. These histograms are updated
    incrementally at packet time, so the GUI can plot from them directly
    without recomputing histograms from scratch.

    Data Layout
    -----------
    - Rolling Buffers:
        For each channel ID (0:max_channels-1) we store a NumPy array of shape:
            (max_len, 4)
        where the 4 columns correspond to:
            [adc_a, adc_b, adc_c, adc_t]

        - New rows are written into the buffer in a circular manner.
        - The current index pointer (`indices[ch]`) tells us where to write next.
        - Once the buffer reaches `max_len`, new data overwrites the oldest entries.
        - The boolean flag `full[ch]` indicates if the buffer has wrapped.

    - Histograms:
        Each channel also has an array of shape:
            (4, n_bins)
        where each row is the histogram of one ADC type:
            row 0 → ADC-A
            row 1 → ADC-B
            row 2 → ADC-C
            row 3 → ADC-T

        The number of bins (`n_bins`) is chosen at initialization and rounded
        to the nearest power of 2 for efficient indexing. Each ADC value is
        mapped into its bin by subtracting `adc_min` and applying a right-shift,
        rather than a general integer divide, which makes updates O(1).

    Access
    ------
    - `add_packet(pkt)`: Extracts channel readings from the ctypes packet,
      writes each `[a, b, c, t]` row into the corresponding channel buffer,
      and increments the corresponding histogram bins.

    - `get_channel(ch)`: Returns a correctly ordered NumPy array of shape
      (<= max_len, 4) containing the rolling history for the given channel,
      from oldest → newest. This unwraps the ring buffer into a linear view,
      so you can plot with PyQtGraph directly.

    - `get_histogram(ch, adc_index)`: Returns `(counts, bin_edges)` for one ADC
      of a channel, where `adc_index` is 0=A, 1=B, 2=C, 3=T.
    """

    def __init__(self, max_len: int, max_channels: int = 16,
                 adc_range=(-32768, 32767), n_bins: int = None):
        """
        Parameters
        ----------
        max_len : int
            Number of rows to keep in rolling buffer per channel.
        max_channels : int
            Maximum number of channels (default: 16).
        adc_range : tuple[int, int]
            Min and max ADC value (default: full 16-bit signed range).
        n_bins : int, optional
            Desired number of bins. Will be rounded to nearest power of 2.
            If None, defaults to one bin per ADC code value.
        """
        self.max_len = max_len
        self.max_channels = max_channels
        self.adc_min, self.adc_max = adc_range
        self.adc_span = self.adc_max - self.adc_min + 1

        # Decide on bin count
        if n_bins is None:
            n_bins = self.adc_span

        self._update_bins(n_bins)

        # Rolling buffers per channel
        self.buffers = {
            ch: np.zeros((max_len, 4), dtype=np.int16)
            for ch in range(max_channels)
        }
        self.indices = {ch: 0 for ch in range(max_channels)}
        self.full = {ch: False for ch in range(max_channels)}

        # Histograms: (4 ADCs × n_bins) per channel
        self.histograms = {
            ch: np.zeros((4, self.n_bins), dtype=np.int64)
            for ch in range(max_channels)
        }

        self.hit_flags = {ch: False for ch in range(max_channels)}
        self.lifetime_hit_flags = {ch: False for ch in range(max_channels)}

    def _update_bins(self, n_bins):

        self.n_bins = nearest_power_of_two(n_bins)

        # Bin width (uniform) and shift amount for fast indexing
        self.bin_width = self.adc_span // self.n_bins
        self.bin_shift = int(np.log2(self.bin_width))

        # Bin edges (for plotting purposes)
        self.bin_edges = np.linspace(self.adc_min, self.adc_max, self.n_bins + 1)

    def add_packet(self, pkt):
        """
        Insert ADC readings from a decoded packet into buffers and histograms.

        Parameters
        ----------
        pkt : DecodedPacket
            ctypes structure with `pkt.data.adc.num_channels` and `.channels`.
        """
        n_ch = pkt.data.adc.num_channels
        # arr = np.ctypeslib.as_array(pkt.data.adc.channels)[:n_ch]
        arr = np.frombuffer(pkt.data.adc.channels, dtype=adc_reading_np_dtype, count=n_ch, )
        # channels_ptr = ctypes.addressof(pkt.data.adc.channels)
        # channels_size = ctypes.sizeof(pkt.data.adc.channels)
        # arr = np.frombuffer(
        #     (ctypes.c_char * channels_size).from_address(channels_ptr),
        #     dtype=adc_reading_np_dtype,
        #     count=n_ch
        # )
        for _, rec in enumerate(arr):
            ch = rec['channel']

            values = np.array([rec['adc_a'], rec['adc_b'], rec['adc_c'], rec['adc_t']],
                              dtype=np.int16)

            # --- Rolling buffer update ---
            idx = self.indices[ch]
            self.buffers[ch][idx] = values
            self.indices[ch] = (idx + 1) % self.max_len
            if self.indices[ch] == 0:
                self.full[ch] = True

            # --- Fast histogram update (bit-shift for power-of-2 bins) ---
            bin_indices = np.right_shift(np.subtract(values, self.adc_min, dtype=np.int32), self.bin_shift)

            for adc_idx, bin_idx in enumerate(bin_indices):
                if 0 <= bin_idx < self.n_bins:
                    self.histograms[ch][adc_idx, bin_idx] += 1

            self.hit_flags[ch] = True
            self.lifetime_hit_flags[ch] = True

    def get_channel(self, ch: int):
        """
        Retrieve rolling buffer for one channel.

        Returns
        -------
        np.ndarray
            Array of shape (N, 4), N ≤ max_len.
        """
        buf = self.buffers[ch]
        idx = self.indices[ch]

        if not self.full[ch]:
            return buf[:idx]

        return np.concatenate((buf[idx:], buf[:idx]))

    def get_histogram(self, ch: int, adc_index: int):
        """
        Get histogram counts for a specific ADC of a channel.

        Parameters
        ----------
        ch : int
            Channel number.
        adc_index : int
            Which ADC to get: 0=A, 1=B, 2=C, 3=T.

        Returns
        -------
        (np.ndarray, np.ndarray)
            Tuple of:
                - counts : 1D histogram array of length n_bins
                - bin_edges : 1D array of length n_bins+1 (edges for plotting)
        """
        return self.histograms[ch][adc_index], self.bin_edges

    def hit_channels(self):
        """
        Return a list of channel numbers that have received new data
        since the last reset.
        """
        return [ch for ch, hit in self.hit_flags.items() if hit]

    def reset_hits(self):
        """
        Reset the hit flags after data has been emitted.
        """
        for ch in self.hit_flags:
            self.hit_flags[ch] = False

    def get_hit_histograms(self, only_hits: bool = True, lifetime_hits: bool = False):
        """
        Get histogram counts for all ADCs of each channel.

        Parameters
        ----------
        only_hits : bool
            If True, returns only channels that have received new data
            since the last reset. If False, returns all channels.
        lifetime_hits: bool
            If True, only channels that Have ever been hit are returned.
        Returns
        -------
        dict[int, dict[str, (np.ndarray, np.ndarray)]]
            Mapping channel → {
                "A": (counts, bin_edges),
                "B": (counts, bin_edges),
                "C": (counts, bin_edges),
                "T": (counts, bin_edges)
            }

        """
        adc_labels = ["A", "B", "C", "T"]
        result = {}

        channels = self.hit_channels() if only_hits else range(self.max_channels)

        if lifetime_hits:
            channels = self.get_lifetime_hits()

        for ch in channels:
            ch_hists = {}
            for i, label in enumerate(adc_labels):
                ch_hists[label] = (self.histograms[ch][i], self.bin_edges)
            result[ch] = ch_hists

        return result

    def clear_histograms(self):
        self.histograms = {
            ch: np.zeros((4, self.n_bins), dtype=np.int64)
            for ch in range(16)
        }

    def get_lifetime_hits(self):
        """
        Return a list of channel numbers that have received new data
        over the lifetime.
        """
        return [ch for ch, hit in self.lifetime_hit_flags.items() if hit]
        pass


class DecodePipeReaderThread(QThread):
    histogram_ready = Signal(int, str, np.ndarray, np.ndarray, float,
                             float)

    histograms_ready = Signal(dict)

    def __init__(self, fifo_path, bins=16384, max_points=50000, refresh_rate_in_s=0.2, parent=None):
        super().__init__(parent)
        self.fifo_path = fifo_path
        self._running = True

        self.np_buffers = ChannelBuffers(max_len=max_points, max_channels=16, n_bins=bins)

        # Per-channel, per-type buffers
        self.buffers = {
            ch: {'a': [], 'b': [], 'c': [], 't': []} for ch in range(MAX_ADC_CHANNELS)
        }
        # Bin parameters
        self.bins = np.linspace(-32768, 32767, bins)
        self.max_points = max_points
        self.emit_interval = refresh_rate_in_s

    def clear_histogram_data(self, channel: int | None = None) -> None:
        """
        Clears histogram data in the buffers for the specified channel.
        If no channel is specified all buffers are cleared.

        :param channel: int channel number
        :return: None
        """

        if channel is not None:
            if 0 <= channel < MAX_ADC_CHANNELS:
                self.buffers[channel] = {'a': [], 'b': [], 'c': [], 't': []}
                return

        self.buffers = {
            ch: {'a': [], 'b': [], 'c': [], 't': []} for ch in range(MAX_ADC_CHANNELS)
        }

    def set_histogram_counts(self, counts: int):
        """
        Sets the max counts to the specified value
        :param counts:
        :return:
        """
        if counts != self.max_points:
            self.max_points = counts

    def run(self):
        # Timer for emitting histograms

        fd = open_named_pipe(self.fifo_path)

        packet = DecodedPacket()

        while self._running:
            result = decode_next_event(fd, packet, 200)

            if result == -2:
                continue
            if result == 0 and packet.type == PACKET_TYPE_ADC:
                self.np_buffers.add_packet(packet)

        close_named_pipe(fd)
        print(self.np_buffers)
        # self._emit_histograms()

    def _emit_histograms(self):
        """
        Note on multiple access:

        This function only passes the reference to the GUI thread for the `histograms` dict containing the histograms of
         the last hit channels.

        A race condition is possible if the decode thread tries to write to the histogram arrays while the gui thread
         is reading. Since the np operations performed by the decode thread are ~atomic(fast enough) that np will not
         release the GIL and prevent any issues. However, if ported for Python>=3.14, which does not require GIL, there is
         a potential for errors to creep in.

        :return:
        """

        histograms = self.np_buffers.get_hit_histograms()
        self.histograms_ready.emit(histograms)

    def stop(self):
        self._running = False
        self.quit()
        self.wait()
