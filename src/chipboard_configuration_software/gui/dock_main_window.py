# chipboard_configuration_software/gui/main_window.py
import sys
from PySide6.QtWidgets import QMainWindow, QDockWidget, QApplication
from PySide6.QtCore import Qt

from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from psd_ui_controller import PsdController
from ui_files.test_main_window import Ui_MainWindow
from ui_files.psd_settings import Ui_DockWidget_psd
import logging

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # wires up your central widget, menus, etc.
        self.config_handler = ConfigurationManager()
        # set up the PSD dock
        self.psd_dock = QDockWidget("PSD Settings", self)
        self.psd_dock.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
        )

        # wire up the PSD UI
        self.psd_ui = Ui_DockWidget_psd()
        self.psd_ui.setupUi(self.psd_dock)

        # now attach the controller
        self.psd_controller = PsdController(self.psd_ui, self.config_handler)

        # add it into the main window
        self.addDockWidget(Qt.RightDockWidgetArea, self.psd_dock)


if __name__ == "__main__":
    FORMAT = "%(asctime)s [%(process)7d] %(levelname)8s - %(name)-30s - %(message)s"
    logging.basicConfig(filename='gui.log', level=logging.DEBUG, format=FORMAT)
    logger.info('Started')

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app_status: int = app.exec()
    logger.info(f'Quit GUI with exit code {app_status}')
    sys.exit(app_status)
