import logging

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QPlainTextEdit
)
from PySide6.QtCore import QThread, Signal, Slot

from chipboard_configuration_software.gui.chipboard_configurator import ThreadedSerialReader
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

logger = logging.getLogger(__name__)


class DebugConsoleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debug Serial Console")

        self.debug_uart_link = UartMiddleware(baudrate=115200)

        self.layout = QVBoxLayout()

        # Device selection
        self.device_dropdown = QComboBox()
        self.connect_button = QPushButton("Connect")
        self.refresh_devices_button = QPushButton("Refresh Devices")

        # Console output
        self.console_output = QPlainTextEdit()
        self.console_output.setReadOnly(True)

        # Layout
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Serial Device:"))
        top_bar.addWidget(self.device_dropdown)
        top_bar.addWidget(self.refresh_devices_button)
        top_bar.addWidget(self.connect_button)

        self.layout.addLayout(top_bar)
        self.layout.addWidget(self.console_output)
        self.setLayout(self.layout)

        # Signals
        self.connect_button.clicked.connect(self.connect_to_selected_device)
        self.refresh_devices_button.clicked.connect(self._on_refresh_devices_clicked)
        # Background reader
        self.reader_thread = None

    @Slot()
    def _on_refresh_devices_clicked(self):
        """Slot for debug refresh devices """
        logger.debug(f"refresh devices clicked.")

        device_list = self.debug_uart_link.get_available_devices(print_output=False)
        self.debug_uart_link.cleanup()
        self.device_dropdown.clear()
        self.device_dropdown.addItem("None")
        self.device_dropdown.addItems(device_list)

    @Slot()
    def connect_to_selected_device(self):
        device = self.device_dropdown.currentText()
        try:
            status = self.debug_uart_link.connect_to_device(device)
            self.console_output.appendPlainText(status)

            if self.reader_thread:
                self.reader_thread.stop()

            self.reader_thread = ThreadedSerialReader(self.debug_uart_link)
            self.reader_thread.data_received.connect(self.console_output.appendPlainText)
            self.reader_thread.start()

        except Exception as e:
            self.console_output.appendPlainText(f"[Connection Error] {e}")

    def closeEvent(self, event):
        if self.reader_thread:
            self.reader_thread.stop()
        self.debug_uart_link.cleanup()
        event.accept()
