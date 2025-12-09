import time
from PySide6.QtCore import QThread, Signal

from visualizer_app.data.channel_buffers import ChannelBuffers
from visualizer_app.data.decoder_cbindings import (
    decode_next_event,
    open_named_pipe,
    close_named_pipe,
)
from visualizer_app.data.decoder_types import DecodedPacket, PACKET_TYPE_ADC


class DecodePipeReaderThread(QThread):
    data_ready = Signal(dict)  # dict[int → dict[str → (counts, bin_edges)]]

    def __init__(self, fifo_path, bins=16384, max_points=50000,
                 refresh_rate_in_s=0.2, parent=None):
        super().__init__(parent)
        self.fifo_path = fifo_path
        self._running = True

        # Use your existing buffer class
        self.np_buffers = ChannelBuffers(
            max_len=max_points,
            max_channels=16,
            n_bins=bins
        )

        self.emit_interval = refresh_rate_in_s
        self.last_emit = time.time()

    def run(self):
        fd = open_named_pipe(self.fifo_path)
        print("Running decoded pipe reader")
        packet = DecodedPacket()
        print("Waiting for event")

        while self._running:
            ret = decode_next_event(fd, packet, 200)

            if ret == -2:
                continue

            if ret == 0 and packet.type == PACKET_TYPE_ADC:

                self.np_buffers.add_packet(packet)

        close_named_pipe(fd)

    def stop(self):
        self._running = False
        self.quit()
        self.wait()
