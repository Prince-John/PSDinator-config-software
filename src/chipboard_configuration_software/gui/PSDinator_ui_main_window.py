import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy, QLabel, QFileDialog, QMessageBox
import PySide6QtAds as QtAds
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRegularExpression, QSize, Slot

from chipboard_configuration_software.uart_link.middleware import UartMiddleware
from .ui_files.top_level_window import Ui_MainWindow
from .ui_files.psd_ui_widget import Ui_Widget_Psd
from .ui_files.cfd_ui_widget import Ui_Widget_Cfd
from .ui_files.chipboard_ui_widget import Ui_Widget_Chipboard

from .psd_ui_controller import PsdController
from .cfd_ui_controller import CfdController
from .chipboard_ui_controller import ChipboardController
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager

import logging

logger = logging.getLogger(__name__)
relative_configuration_dir = r"../configurations/"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ This is the class inheriting the Qt designer UI and adding functionality """

    def __init__(self, config_handler: ConfigurationManager, uart_link: UartMiddleware):
        super().__init__()
        self.config_handler: ConfigurationManager = config_handler
        self.uart_link: UartMiddleware = uart_link

        self.setupUi(self)

        QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.OpaqueSplitterResize, True)
        QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.XmlCompressionEnabled, False)
        QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.FocusHighlighting, True)
        QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.DockAreaHideDisabledButtons, True)
        QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.HideSingleCentralWidgetTitleBar, True)

        self.dock_manager = QtAds.CDockManager(self)

        bottom_buttons = QtAds.CDockWidget(self.dock_manager, "Configure Chipboard")
        bottom_buttons.setWidget(self.bottom_fixed_area)
        bottom_buttons.setFeature(QtAds.CDockWidget.NoTab, True)
        self.bottom_area = self.dock_manager.setCentralWidget(bottom_buttons)
        self.bottom_area.setMaximumSize(self.bottom_fixed_area.maximumSize())

        central_dock_widget = QtAds.CDockWidget(self.dock_manager, "CFD-PSD Configuration Utility")
        central_dock_widget.setWidget(self.Widget_closed_tabs_page)
        central_dock_widget.setFeature(QtAds.CDockWidget.NoTab, True)

        self.central_dock_area = self.dock_manager.addDockWidget(QtAds.TopDockWidgetArea,
                                                                 central_dock_widget)  # self.dock_manager
        # .setCentralWidget(central_dock_widget)

        self._setup_dock_widgets()

        self._connect_signals()

    def _setup_dock_widgets(self):
        # Create CFD Settings Page
        self.cfd_widget = QWidget()
        self.cfd_ui = Ui_Widget_Cfd()
        self.cfd_ui.setupUi(self.cfd_widget)
        self.cfd_controller = CfdController(self.cfd_ui, self.config_handler)

        self.cfd_dock = QtAds.CDockWidget(self.dock_manager, "CFD Settings")
        self.cfd_dock.setWidget(self.cfd_widget)
        self.dock_manager.addDockWidgetTabToArea(self.cfd_dock, self.central_dock_area)

        self.menuWindows.addAction(self.cfd_dock.toggleViewAction())

        # Create Chipboard Settings Page
        self.chipboard_widget = QWidget()
        self.chipboard_ui = Ui_Widget_Chipboard()
        self.chipboard_ui.setupUi(self.chipboard_widget)
        self.chipboard_controller = ChipboardController(self.chipboard_ui, self.config_handler)

        self.chipboard_dock = QtAds.CDockWidget(self.dock_manager, "Chipboard Settings")
        self.chipboard_dock.setWidget(self.chipboard_widget)
        self.dock_manager.addDockWidgetTabToArea(self.chipboard_dock, self.central_dock_area)

        self.menuWindows.addAction(self.chipboard_dock.toggleViewAction())

        # Create PSD Settings Page
        self.psd_widget = QWidget()  # real widget
        self.psd_ui = Ui_Widget_Psd()  # UI builder
        self.psd_ui.setupUi(self.psd_widget)  # setup layout on widget
        self.psd_controller = PsdController(self.psd_ui, self.config_handler, self.uart_link)

        self.psd_dock = QtAds.CDockWidget(self.dock_manager, "PSD Settings")
        self.psd_dock.setWidget(self.psd_widget)
        self.dock_manager.addDockWidgetTabToArea(self.psd_dock, self.central_dock_area)

        self.menuWindows.addAction(self.psd_dock.toggleViewAction())

    def _connect_signals(self):
        self.psd_controller.status_message.connect(self.statusBar().showMessage)
        self.__connect_bottom_signals()
        self.__connect_menu_signals()
        logger.info("Connected GUI Signals!")

    def __connect_menu_signals(self):
        self.actionSave_As.triggered.connect(self.save_as_config)
        self.actionLoad.triggered.connect(self.load_config)
        self.actionSave_Configuration.triggered.connect(self.save_config)

    def __connect_bottom_signals(self):

        self.pushButton_refresh_devices.pressed.connect(self._on_refresh_devices_clicked)
        self.comboBox_devices.currentTextChanged.connect(self._on_device_selection_changed)
        logger.info("Connected bottom bar Signals!")

    @Slot()
    def _on_refresh_devices_clicked(self):
        """Slot for refresh devices """
        logger.debug(f"refresh devices clicked.")

        device_list = self.uart_link.get_available_devices(print_output=False)
        self.uart_link.cleanup()
        self.comboBox_devices.blockSignals(True)
        self.comboBox_devices.clear()
        self.comboBox_devices.addItem("None")
        self.comboBox_devices.addItems(device_list)
        self.comboBox_devices.blockSignals(False)

    @Slot(str)
    def _on_device_selection_changed(self, device):
        """Slot for device selection """
        logger.debug(f"device selection changed with value {device}")
        try:
            status = self.uart_link.connect_to_device(device)
        except IOError as e:
            status = f"Error connecting to {device}: {e}"

        self.statusBar().showMessage(status)

    def save_config(self):
        logger.debug("Save Configuration Clicked!")
        if self.config_handler.configuration_file_path is None:
            self.save_as_config()
        else:
            try:
                self.config_handler.save_current_configuration()
                QMessageBox.information(self, "Success", f"Configuration saved!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save config:\n{e}")

    def save_as_config(self):
        logger.debug("Save As Configuration Clicked!")
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Configuration",
            f"{relative_configuration_dir}",
            "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            try:
                self.config_handler.save_current_configuration(file_path)
                QMessageBox.information(self, "Success", f"Configuration saved to:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save config:\n{e}")

    def load_config(self):
        logger.debug("Load Configuration Clicked!")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load Configuration",
            f"{relative_configuration_dir}",
            "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            try:
                self.config_handler.load_saved_configuration(file_path)
                QMessageBox.information(self, "Loaded", f"Configuration loaded from:\n{file_path}")
                self.update_global_ui()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load config:\n{e}")

    def update_global_ui(self):

        self.psd_controller.update_ui()
        self.cfd_controller.update_ui()
        logger.info("Updated Global UI!")


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
