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


def compute_peak_and_fwhm(counts: np.ndarray, bins: np.ndarray) -> tuple[float, float]:
    if counts.size == 0 or counts.max() == 0:
        return 0.0, 0.0

    # Get peak bin index and center
    max_idx = np.argmax(counts)
    peak_bin_center = (bins[max_idx] + bins[max_idx + 1]) / 2
    half_max = counts[max_idx] / 2.0

    # Vectorized search for all bins above half max
    above_half = np.where(counts >= half_max)[0]
    if len(above_half) == 0:
        return peak_bin_center, 0.0

    # FWHM is from the first to last bin above half max
    left_edge = bins[above_half[0]]
    right_edge = bins[above_half[-1] + 1] if above_half[-1] + 1 < len(bins) else bins[-1]

    fwhm = right_edge - left_edge
    return peak_bin_center, fwhm


class DecodePipeReaderThread(QThread):
    histogram_ready = Signal(int, str, np.ndarray, np.ndarray, float,
                             float)  # channel, 'a'/'b'/'c', bins, counts, peak, fwhm

    def __init__(self, fifo_path, bins=65536, max_points=50000, refresh_rate_in_s=0.2, parent=None):
        super().__init__(parent)
        self.fifo_path = fifo_path
        self._running = True

        # Per-channel, per-type buffers
        self.buffers = {
            ch: {'a': [], 'b': [], 'c': []} for ch in range(MAX_ADC_CHANNELS)
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
                self.buffers[channel] = {'a': [], 'b': [], 'c': []}
                return

        self.buffers = {
            ch: {'a': [], 'b': [], 'c': []} for ch in range(MAX_ADC_CHANNELS)
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

        last_emit_time = time.time()
        emit_interval = self.emit_interval

        packet = DecodedPacket()

        while self._running:
            result = decode_next_event(fd, packet, 200)

            if result == -2:
                continue
            if result == 0 and packet.type == PACKET_TYPE_ADC:
                event_adc_data = packet.data.adc.channels[:packet.data.adc.num_channels]
                for single_channel_data in event_adc_data:

                    for sub_channel in ['a', 'b', 'c']:
                        val = getattr(single_channel_data, f'adc_{sub_channel}')
                        self.buffers[single_channel_data.channel][sub_channel].append(val)

                        # Circular buffer - delete data over max specified points
                        if len(self.buffers[single_channel_data.channel][sub_channel]) > self.max_points:
                            self.buffers[single_channel_data.channel][sub_channel] = \
                                self.buffers[single_channel_data.channel][sub_channel][-self.max_points:]

            now = time.time()
            if now - last_emit_time >= emit_interval:
                self._emit_histograms()
                last_emit_time = now

        close_named_pipe(fd)
        self._emit_histograms()

    def _emit_histograms(self):
        for ch, data_dict in self.buffers.items():
            for sub_ch in ['a', 'b', 'c']:
                data = np.array(data_dict[sub_ch], dtype=np.int16)
                if len(data) > 0:
                    counts, _ = np.histogram(data, bins=self.bins)
                    peak, fwhm = compute_peak_and_fwhm(counts, self.bins)
                    self.histogram_ready.emit(ch, sub_ch, self.bins, counts, peak, fwhm)

    def stop(self):
        self._running = False
        self.quit()
        self.wait()
