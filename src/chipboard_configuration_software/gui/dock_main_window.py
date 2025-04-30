# chipboard_configuration_software/gui/main_window.py
import sys
from PySide6.QtWidgets import QMainWindow, QDockWidget, QApplication
from PySide6.QtCore import Qt

from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager

from ui_files.cfd_settings import Ui_DockWidget_cfd
from psd_ui_controller import PsdController
from cfd_ui_controller import CfdController
from chipboard_ui_controller import ChipboardController
from ui_files.test_main_window import Ui_MainWindow
from ui_files.psd_settings import Ui_DockWidget_psd
from ui_files.chipboard_settings import Ui_DockWidget_chipboard

import logging

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)  # wires up your central widget, menus, etc.
    #     self.config_handler = ConfigurationManager()
    #     # set up the PSD dock
    #     self.psd_dock = QDockWidget("PSD Settings", self)
    #     self.psd_dock.setAllowedAreas(
    #         Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
    #     )
    #
    #     self.cfd_dock = QDockWidget("CFD Settings", self)
    #     self.cfd_dock.setAllowedAreas(
    #         Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
    #     )
    #
    #     self.chipboard_dock = QDockWidget("Chipboard Settings", self)
    #     self.chipboard_dock.setAllowedAreas(
    #         Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
    #     )
    #     # wire up the PSD UI
    #     self.psd_ui = Ui_DockWidget_psd()
    #     self.psd_ui.setupUi(self.psd_dock)
    #
    #     self.cfd_ui = Ui_DockWidget_cfd()
    #     self.cfd_ui.setupUi(self.cfd_dock)
    #
    #     self.chipboard_ui = Ui_DockWidget_chipboard()
    #     self.chipboard_ui.setupUi(self.chipboard_dock)
    #
    #     # now attach the controller
    #     self.psd_controller = PsdController(self.psd_ui, self.config_handler)
    #     self.cfd_controller = CfdController(self.cfd_ui, self.config_handler)
    #     self.chipboard_controller = ChipboardController(self.chipboard_ui, self.config_handler)
    #
    #     # add it into the main window
    #     self.addDockWidget(Qt.RightDockWidgetArea, self.psd_dock)
    #     self.addDockWidget(Qt.LeftDockWidgetArea, self.cfd_dock)
    #     self.addDockWidget(Qt.LeftDockWidgetArea, self.chipboard_dock)
    #
    #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config_handler = ConfigurationManager()

        # create all three docks…
        self.psd_dock = QDockWidget("PSD Settings", self)
        self.cfd_dock = QDockWidget("CFD Settings", self)
        self.chipboard_dock = QDockWidget("Chipboard Settings", self)

        # limit them to left/right
        for dock in (self.psd_dock, self.cfd_dock, self.chipboard_dock):
            dock.setAllowedAreas(
                Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
            )

        # populate each one…
        self.psd_ui = Ui_DockWidget_psd()
        self.psd_ui.setupUi(self.psd_dock)
        self.cfd_ui = Ui_DockWidget_cfd()
        self.cfd_ui.setupUi(self.cfd_dock)
        self.chipboard_ui = Ui_DockWidget_chipboard()
        self.chipboard_ui.setupUi(self.chipboard_dock)

        # wire up controllers…
        self.psd_controller = PsdController(self.psd_ui, self.config_handler)
        self.cfd_controller = CfdController(self.cfd_ui, self.config_handler)
        self.chipboard_controller = ChipboardController(self.chipboard_ui, self.config_handler)

        # 1) dock all three into the *same* area…
        self.addDockWidget(Qt.RightDockWidgetArea, self.psd_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.cfd_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.chipboard_dock)

        # 2) tabify them (group into tabs)
        #    the order you call these determines the tab order
        self.tabifyDockWidget(self.psd_dock, self.cfd_dock)
        self.tabifyDockWidget(self.psd_dock, self.chipboard_dock)

        # 3) bring one tab to the front by default
        self.psd_dock.raise_()


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
