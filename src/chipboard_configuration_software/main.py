import logging
import sys

from PySide6 import QtWidgets

from chipboard_configuration_software.gui.PSDinator_ui_main_window import MainWindow
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    FORMAT = "%(asctime)s [%(process)7d] %(levelname)8s - %(name)-30s - %(message)s"
    logging.basicConfig(filename='gui.log', level=logging.DEBUG, format=FORMAT)
    logger.info('Started')

    app = QtWidgets.QApplication(sys.argv)

    uart_link = UartMiddleware()
    configuration_manager = ConfigurationManager()

    w = MainWindow(configuration_manager, uart_link)

    w.show()

    sys.exit(app.exec())
