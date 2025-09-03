import importlib.metadata
import json
import sys
import threading
from typing import Tuple

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy, QLabel, QFileDialog, QMessageBox
import PySide6QtAds as QtAds
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRegularExpression, QSize, Slot, Signal, QThread
from serial import PortNotOpenError

from chipboard_configuration_software.command_generator.generate_command_string import generate_commands
from chipboard_configuration_software.gui.ui_files.log_window import FailureDetailsDialog
from chipboard_configuration_software.uart_link.middleware import UartMiddleware
from .adc_plot_ui_controller import ADCPlotsController
from .chipboard_configurator import threaded_configure_chipboard, ChipboardConfigurator, ChipboardResetter, \
    RealtimeConfigurator
from .debug_console_controller import DebugConsoleWindow
from .ui_files.adc_plot_ui_widget import Ui_adc_plots
from .ui_files.top_level_window import Ui_MainWindow
from .ui_files.psd_ui_widget import Ui_Widget_Psd
from .ui_files.cfd_ui_widget import Ui_Widget_Cfd
from .ui_files.chipboard_ui_widget import Ui_Widget_Chipboard

from .psd_ui_controller import PsdController
from .cfd_ui_controller import CfdController
from .chipboard_ui_controller import ChipboardController
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager

import logging

from .utilities import configure_chipboard
from ..uart_link.event_handler import DataAcquisitionThread

logger = logging.getLogger(__name__)
relative_configuration_dir = r"../configurations/"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ This is the class inheriting the Qt designer UI and adding functionality """
    status_message = Signal(str)

    def __init__(self, config_handler: ConfigurationManager, uart_link: UartMiddleware):
        super().__init__()
        self.configuration_worker: ChipboardConfigurator | None = None
        self.configuration_thread: QThread | None = None
        self.reset_worker: ChipboardResetter | None = None
        self.reset_thread: QThread | None = None
        self.config_handler: ConfigurationManager = config_handler
        self.uart_link: UartMiddleware = uart_link
        self.daq_stop: threading.Event = threading.Event()
        self.daq_thread: DataAcquisitionThread | None = None

        self.real_time_configurator: RealtimeConfigurator = RealtimeConfigurator(self.config_handler, self.uart_link)

        self.setupUi(self)

        self.device_status_message = QLabel("Device Status: Not Connected")
        self.statusbar.addPermanentWidget(self.device_status_message)

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

        self.debug_window = DebugConsoleWindow()
        self.adc_plot_window = None

        self._setup_dock_widgets()

        self._connect_signals()
        self._update_build_version()

    def _setup_dock_widgets(self):
        # Create CFD Settings Page
        self.cfd_widget = QWidget()
        self.cfd_ui = Ui_Widget_Cfd()
        self.cfd_ui.setupUi(self.cfd_widget)
        self.cfd_controller = CfdController(self, self.cfd_ui, self.config_handler, self.uart_link)

        self.cfd_dock = QtAds.CDockWidget(self.dock_manager, "CFD Settings")
        self.cfd_dock.setWidget(self.cfd_widget)
        self.dock_manager.addDockWidgetTabToArea(self.cfd_dock, self.central_dock_area)

        # Create Chipboard Settings Page
        self.chipboard_widget = QWidget()
        self.chipboard_ui = Ui_Widget_Chipboard()
        self.chipboard_ui.setupUi(self.chipboard_widget)
        self.chipboard_controller = ChipboardController(self, self.chipboard_ui, self.config_handler, self.uart_link)

        self.chipboard_dock = QtAds.CDockWidget(self.dock_manager, "Chipboard Settings")
        self.chipboard_dock.setWidget(self.chipboard_widget)
        self.dock_manager.addDockWidgetTabToArea(self.chipboard_dock, self.central_dock_area)

        # Create PSD Settings Page
        self.psd_widget = QWidget()  # real widget
        self.psd_ui = Ui_Widget_Psd()  # UI builder
        self.psd_ui.setupUi(self.psd_widget)  # setup layout on widget
        self.psd_controller = PsdController(self, self.psd_ui, self.config_handler, self.uart_link)

        self.psd_dock = QtAds.CDockWidget(self.dock_manager, "PSD Settings")
        self.psd_dock.setWidget(self.psd_widget)
        self.dock_manager.addDockWidgetTabToArea(self.psd_dock, self.central_dock_area)

    def _connect_signals(self):
        self.psd_controller.status_message.connect(self.statusBar().showMessage)
        self.chipboard_controller.status_message.connect(self.statusBar().showMessage)
        self.cfd_controller.status_message.connect(self.statusBar().showMessage)
        self.status_message.connect(self.statusBar().showMessage)
        self.real_time_configurator.status_update.connect(self.statusBar().showMessage)
        self.__connect_bottom_signals()
        self.__connect_menu_signals()
        self.__connect_window_signals()
        logger.info("Connected GUI Signals!")

    def __connect_menu_signals(self):
        self.actionSave_As.triggered.connect(self.save_as_config)
        self.actionLoad.triggered.connect(self.load_config)
        self.actionSave_Configuration.triggered.connect(self.save_config)

    def __connect_window_signals(self):
        self.menuWindows.addAction(self.psd_dock.toggleViewAction())
        self.menuWindows.addAction(self.chipboard_dock.toggleViewAction())
        self.menuWindows.addAction(self.cfd_dock.toggleViewAction())
        self.actionDebug_Console.triggered.connect(self._on_show_debug_console_clicked)
        self.actionShow_ADC_Plots.triggered.connect(self.show_adc_plot_window)

    def __connect_bottom_signals(self):
        self.pushButton_configure_chipboard.pressed.connect(self._on_configure_chipboard_clicked)
        self.pushButton_refresh_devices.pressed.connect(self._on_refresh_devices_clicked)
        self.comboBox_devices.currentTextChanged.connect(self._on_device_selection_changed)
        logger.info("Connected bottom bar Signals!")

    def _update_build_version(self):
        """Updates the build version of this configuration software in the about section in the menu bar"""

        software_version = importlib.metadata.version('Psdinator-configuration-software')
        logger.info(f"GUI version updated to v{software_version}")
        self.action_version.setText(f"Build Version: v{software_version}")

    @Slot()
    def _on_show_debug_console_clicked(self):
        """Slot for show debug console """
        logger.debug(f"show debug console clicked.")
        if self.debug_window.isVisible():
            self.debug_window.hide()
        else:
            self.debug_window.show()

    @Slot()
    def _on_refresh_devices_clicked(self):
        """Slot for refresh devices """
        logger.debug(f"refresh devices clicked.")

        device_list = self.uart_link.get_available_devices(print_output=False)
        self.uart_link.cleanup()
        self.config_handler.reset_currently_loaded_chipboard_config()
        self.device_status_message.setText("Device Status: Not Connected")
        self.comboBox_devices.blockSignals(True)
        self.comboBox_devices.clear()
        self.comboBox_devices.addItem("None")
        self.comboBox_devices.addItems(device_list)
        self.comboBox_devices.blockSignals(False)

    def show_adc_plot_window(self):
        # Create the widget instance
        adc_ui = Ui_adc_plots()
        self.adc_plot_window = ADCPlotsController(self, adc_ui, self.config_handler)

        # Set up the UI (important if you're not using `setupUi` inside controller)
        #adc_ui.setupUi(self.adc_plot_window)

        # Make it behave like a top-level window
        self.adc_plot_window.setWindowTitle("ADC Plot Viewer")
        self.adc_plot_window.resize(800, 600)  # Optional: set initial size
        self.adc_plot_window.show()

    def get_chipboard_self_id(self):
        """
       Fetches the chipboard board ID

       :return: board id
    """
        data = None
        try:
            self.uart_link.send_stx()
            logger.info("Getting BID")
            self.uart_link.send_CMD(message="Get Board ID", command_string="BID:\0")
            logger.debug("Waiting for BID data")
            data = int.from_bytes(self.uart_link.get_data(1))
            self.uart_link.send_etx()
        except Exception as e:
            logger.warning(f"Could not self ID: {e}")

        logger.debug(f"Received {data}")
        return data

    def validate_chipboard_self_id(self):
        board_id = self.get_chipboard_self_id()

        if self.config_handler.current_chipboard_number != board_id:
            alert = f" - ⚠️ Chipboard Board ID:{board_id} != Current setting: {self.config_handler.current_chipboard_number}"
        else:
            alert = f""

        return board_id, alert

    def get_chipboard_firmware(self) -> str:
        """
        Fetches the chipboard firmware version

        :return: firmware_version
        """
        data = None
        try:
            self.uart_link.send_stx()
            logger.info("Getting Firmware Version")
            self.uart_link.send_CMD(message="Get Firmware", command_string="VER:\0")
            logger.debug("Waiting  Firmware Version")
            data = self.uart_link.get_data(6).decode("ascii")
            self.uart_link.send_etx()
        except Exception as e:
            logger.warning(f"Could not get Firmware Version: {e}")

        logger.debug(f"Received {data}")
        print(f"Received firmware {data}")
        return data

    def validate_chipboard_firmware(self, supported_firmware_version: Tuple[str, str, str] = (
            "v0.0.0", "v0.0.0", "v0.0.0")) -> Tuple[str, str]:
        """
        Fetches the chipboard firmware version and returns if the firmware is supported by this version of the GUI.

        :param supported_firmware_version: str tuple of (min, target, max) supported firmware versions.
        :return: (firmware_version, support_status)
        """
        pass

    @Slot(str)
    def _on_device_selection_changed(self, device):
        """Slot for device selection """
        logger.debug(f"device selection changed with value {device}")
        try:
            status = self.uart_link.connect_to_device(device)

        except IOError as e:
            status = f"Error connecting to {device}: {e}"

        board_id, alert = self.validate_chipboard_self_id()

        if board_id is not None:
            firmware_version = self.get_chipboard_firmware()
            logger.info(f"Connected to chipboard running firmware version: {firmware_version}")
            self.device_status_message.setText(
                f"Connected to Chipboard #{board_id} running firmware {firmware_version}")

        status = f"{status} {alert}"
        self.statusBar().showMessage(status, timeout=10000)
        logger.info(status)

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
        self.chipboard_controller.update_ui()
        self.cfd_controller.update_ui()
        logger.info("Updated Global UI!")

    def show_failure_details(self, failures):
        dialog = FailureDetailsDialog(failures, parent=self)
        dialog.exec()

    @Slot()
    def _on_configure_chipboard_clicked(self):
        """Slot for configure chipboard """
        logger.debug(f"configure chipboard clicked")
        self.configure_chipboard()

    @Slot(list)
    def _on_partial_chipboard_config_done(self, failures):
        logger.debug(f"Configuration thread exit!")
        self.progressBar.setValue(0)
        self.show_failure_details(failures)

    @Slot()
    def _on_chipboard_config_done(self):
        logger.debug(f"Configuration thread exit with no errors!")

    def configure_chipboard(self):
        """
        Top Level Wrapper for call to the generic chipboard configuration function.
        :return: None
        """

        self.configuration_thread, self.configuration_worker = threaded_configure_chipboard(self,
                                                                                            config_handler=self.config_handler,
                                                                                            uart_link=self.uart_link)
        self.configuration_thread.start()
