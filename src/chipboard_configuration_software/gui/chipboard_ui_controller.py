import logging
from functools import partial
from typing import get_args, cast, List

from PySide6.QtCore import Slot, Qt, QObject, Signal
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QCheckBox, QComboBox, QSlider, QLineEdit, QWidget

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict, DelayConfigurationDict
from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import ChannelKey, \
    BoolStr, SubchannelKey
from chipboard_configuration_software.gui.chipboard_configurator import threaded_configure_chipboard

from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.chipboard_ui_widget import Ui_Widget_Chipboard
from chipboard_configuration_software.gui.ui_files.qt_ui_modifications import EvenNumberValidator
from chipboard_configuration_software.gui.utilities import configure_chipboard, set_checkbox_silently, \
    set_checkbox_silently, set_slider_silently
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

logger = logging.getLogger(__name__)


class ChipboardController(QWidget):
    status_message = Signal(str)

    def __init__(self, parent_ui, ui: Ui_Widget_Chipboard, config_handler: ConfigurationManager,
                 uart_link: UartMiddleware):
        super().__init__()
        self.parent_ui = parent_ui
        self.ui = ui
        self.chipboard_config: ChipboardConfigurationDict = config_handler.current_chipboard_config
        self.config_handler = config_handler
        self.uart_link = uart_link
        self.delay_sliders: List[QSlider] = []
        self.delay_texts: List[QLineEdit] = []
        self.delay_all_state = False

        self.mux_cmd_map = {
            "psd_0": "PSD 0",
            "psd_1": "PSD 1",
            "psd_0_or_psd_1": "PSD 0 or PSD 1",
            "cfd": "CFD",
        }

        self.mux_cmd_index_map = {
            0: "psd_0",
            1: "psd_1",
            2: "psd_0_or_psd_1",
            3: "cfd",
        }

        self._connect_delay_signals()
        self._connect_mux_signals()

        self._update_ui()
        logger.info("CFD GUI signals connected!")

    def _update_ui(self, config: ChipboardConfigurationDict = None):

        if config is None:
            config = self.chipboard_config

        self._update_ui_delays(config["delay"])
        self._update_ui_mux(config)
        pass

    def _connect_delay_signals(self):
        delay_validator = EvenNumberValidator()
        for channel in range(16):
            slider = getattr(self.ui, f"slider_delay_ch_{channel}")
            line = getattr(self.ui, f"text_delay_ch_{channel}")
            line.setValidator(delay_validator)

            slider.valueChanged.connect(
                partial(self._on_delay_slider_changed, channel)
            )

            # lineEdit → slider, tag with subchannel
            line.textEdited.connect(
                partial(self._on_delay_text_edited, channel)
            )

            self.delay_texts.append(line)
            self.delay_sliders.append(slider)

        self.ui.qb_delay_reset.pressed.connect(self._on_reset_delays_clicked)
        self.ui.qb_delay_configure.pressed.connect(self._on_delay_configure_clicked)
        self.ui.qrb_control_all.toggled.connect(self._on_delay_all_changed)

    @Slot()
    def _on_delay_configure_clicked(self):
        """Slot for delay configure """
        logger.debug(f"delay configure clicked")
        self.configure_delays()

    def configure_delays(self):
        self.parent_ui.configuration_thread, self.parent_ui.configuration_worker = threaded_configure_chipboard(
            parent_ui=self.parent_ui,
            config_handler=self.config_handler,
            uart_link=self.uart_link,
            component="delay")
        self.parent_ui.configuration_thread.start()

    @Slot(str)
    def _on_delay_text_edited(self, channel, value):
        """Slot for delay text """
        logger.debug(f"delay {channel} text edited with value  {value}")
        try:
            slider_pos = int(value)
        except ValueError:
            slider_pos = 0

        set_slider_silently(self.delay_sliders[channel], slider_pos)

        channel = cast(ChannelKey, str(channel))
        self.chipboard_config["delay"][channel]["value"] = value

    @Slot(bool)
    def _on_delay_all_changed(self, state):
        """Slot for delay all """

        logger.debug(f"delay all changed with value {state}")

        self.delay_all_state = state

    @Slot(int)
    def _on_delay_slider_changed(self, channel, value):
        """Slot for delay slider """
        logger.debug(f"delay {channel} slider changed with value {value}")

        if self.delay_all_state:
            for channel in range(16):
                self.delay_texts[channel].setText(str(value))

                self.delay_sliders[channel].blockSignals(True)
                self.delay_sliders[channel].setSliderPosition(int(value))
                self.delay_sliders[channel].blockSignals(False)
                channel = cast(ChannelKey, str(channel))
                self.chipboard_config["delay"][channel]["value"] = str(value)

        else:
            self.delay_texts[channel].setText(str(value))
            channel = cast(ChannelKey, str(channel))
            self.chipboard_config["delay"][channel]["value"] = str(value)

    def _connect_mux_signals(self):
        for i in range(16):
            self.ui.comboBox_pre_amp_mux.addItem(f"{i}")

        self.ui.comboBox_pre_amp_mux.currentTextChanged.connect(self._on_pre_amp_mux_changed)
        self.ui.comboBox_or_mux.currentIndexChanged.connect(self._on_or_mux_changed)
        self.ui.comboBox_intx_mux.currentIndexChanged.connect(self._on_intx_mux_changed)
        self.ui.comboBox_psd_cfd_mux.currentIndexChanged.connect(self._on_psd_cfd_mux_changed)

    @Slot(str)
    def _on_pre_amp_mux_changed(self, value):
        """Slot for pre amp mux """
        logger.debug(f"pre amp mux changed with value {value}")

        self.chipboard_config["mux"]["preamp_output"] = value

    @Slot(int)
    def _on_or_mux_changed(self, value):
        """Slot for or mux """
        logger.debug(f"or mux changed with value {value}")
        self.chipboard_config["mux"]["or_output"] = self.mux_cmd_index_map[value]

    @Slot(int)
    def _on_intx_mux_changed(self, value):
        """Slot for or mux """
        logger.debug(f"intx mux changed with value {value}")
        self.chipboard_config["mux"]["intx_output"] = self.mux_cmd_index_map[value]

    @Slot(int)
    def _on_psd_cfd_mux_changed(self, value):
        """Slot for psd cfd """
        logger.debug(f"psd cfd changed with value {value}")
        self.chipboard_config["mux"]["psd_cfd_output"] = self.mux_cmd_index_map[value]

    def _update_ui_delays(self, delay_config: DelayConfigurationDict = None):

        if delay_config is None:
            delay_config = self.chipboard_config["delay"]

        for channel in range(16):
            delay_value = delay_config[cast(ChannelKey, str(channel))]["value"]

            self.delay_sliders[channel].setSliderPosition(int(delay_value))

    @Slot()
    def _on_reset_delays_clicked(self):
        """Slot for reset delays """
        logger.debug(f"reset delays clicked")
        last_config = self.config_handler.get_currently_loaded_chipboard_config("delay")

        self._update_ui_delays(last_config)

    def _update_ui_mux(self, config):
        if config is None:
            config = self.chipboard_config

        self.ui.comboBox_pre_amp_mux.setCurrentText(str(config["mux"]["preamp_output"]))
        self.ui.comboBox_or_mux.setCurrentText(self.mux_cmd_map[config["mux"]["or_output"]])
        self.ui.comboBox_intx_mux.setCurrentText(self.mux_cmd_map[config["mux"]["intx_output"]])
        self.ui.comboBox_psd_cfd_mux.setCurrentText(self.mux_cmd_map[config["mux"]["psd_cfd_output"]])
