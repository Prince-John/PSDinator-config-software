import logging
import sys

from PySide6 import QtWidgets

from chipboard_configuration_software.gui.PSDinator_ui_main_window import MainWindow
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

logger = logging.getLogger(__name__)


def main():
    """
    Entry point for launching the GUI for the configuration software
    :return: None
    """

    FORMAT = "%(asctime)s [%(process)7d] %(levelname)8s - %(name)-30s - %(message)s"
    logging.basicConfig(filename='gui.log', level=logging.INFO, format=FORMAT)
    logger.info('Started')

    app = QtWidgets.QApplication(sys.argv)

    uart_link = UartMiddleware()
    configuration_manager = ConfigurationManager()

    w = MainWindow(configuration_manager, uart_link)

    w.show()
    status = app.exec()
    configuration_manager.save_current_configuration()

    sys.exit(status)


if __name__ == "__main__":
    main()