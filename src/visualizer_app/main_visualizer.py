import os
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from visualizer_app.core.plot_manager import PlotManager
from visualizer_app.data.decode_thread import DecodePipeReaderThread

FIFO_PATH = "/tmp/daq_pipe"


def create_fifo(fifo_path=None):
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
        print(f"Created new FIFO at {fifo_path}")


class VisualizerMainWindow(QMainWindow):
    def __init__(self, refresh_time_ms=150):
        super().__init__()

        self.setWindowTitle("PSDinator Visualizer")
        self.resize(600, 800)

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        # Add plot manager (tab view)
        self.plot_manager = PlotManager()
        layout.addWidget(self.plot_manager)

        # Setup reader thread
        create_fifo(FIFO_PATH)
        self.reader_thread = DecodePipeReaderThread(FIFO_PATH)
        self.reader_thread.start()

        # QTimer to poll histograms from np_buffers
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self._refresh_plots_from_buffer)
        self.refresh_timer.start(refresh_time_ms)

    def _refresh_plots_from_buffer(self):
        """
        Poll the decode thread's ChannelBuffers for new histograms,
        then forward them to all plot modules.

        """
        buffers = self.reader_thread.np_buffers

        updates = buffers.get_hit_histograms(only_hits=True, lifetime_hits=False)
        if updates:
            self.plot_manager.update_all_plots(updates)
            buffers.reset_hits()

    def closeEvent(self, event):
        self.reader_thread.stop()
        self.reader_thread.wait()
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = VisualizerMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
