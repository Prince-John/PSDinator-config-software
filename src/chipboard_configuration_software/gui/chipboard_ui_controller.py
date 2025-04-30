import logging
from functools import partial
from typing import get_args, cast, List

from PySide6.QtCore import Slot, Qt, QObject
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QCheckBox, QComboBox, QSlider, QLineEdit

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict
from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import ChannelKey, \
    BoolStr, SubchannelKey

from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.chipboard_ui_widget import Ui_Widget_Chipboard
from chipboard_configuration_software.gui.ui_files.qt_ui_modifications import EvenNumberValidator

logger = logging.getLogger(__name__)


class ChipboardController:
    def __init__(self, ui: Ui_Widget_Chipboard, config_handler: ConfigurationManager):
        self.ui = ui
        self.chipboard_config: ChipboardConfigurationDict = config_handler.current_chipboard_config
        self.config_handler = config_handler
        self.delay_sliders: List[QSlider] = []
        self.delay_texts: List[QLineEdit] = []
        self.delay_all_state = False

        self._connect_delay_signals()
        self._connect_mux_signals()

        self._update_ui()
        logger.info("CFD GUI signals connected!")

    def _update_ui(self, config: ChipboardConfigurationDict = None):

        if config is None:
            config = self.chipboard_config

        self._update_ui_delays(config)
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
        pass

    @Slot(str)
    def _on_delay_text_edited(self, channel, value):
        """Slot for delay text """
        logger.debug(f"delay {channel} text edited with value  {value}")
        try:
            slider_pos = int(value)
        except ValueError:
            slider_pos = 0

        self.delay_sliders[channel].blockSignals(True)
        self.delay_sliders[channel].setSliderPosition(slider_pos)
        self.delay_sliders[channel].blockSignals(False)

        channel = cast(ChannelKey, str(channel))
        self.chipboard_config["delay"][channel]["value"] = value

    @Slot(bool)
    def _on_delay_all_changed(self, state):
        """Slot for delay all """
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"delay all changed with value {state}")

        self.delay_all_state = state




    @Slot(int)
    def _on_delay_slider_changed(self, channel, value):
        """Slot for delay slider """
        logger.debug(f"delay {channel} slider changed with value {value}")

        if self.delay_all_state:

            for channel in range(16):
                self.delay_texts[channel].setText(str(value))
                channel = cast(ChannelKey, str(channel))
                self.chipboard_config["delay"][channel]["value"] = str(value)

        else:
            self.delay_texts[channel].setText(str(value))
            channel = cast(ChannelKey, str(channel))
            self.chipboard_config["delay"][channel]["value"] = str(value)

    def _connect_mux_signals(self):
        pass

    def _update_ui_delays(self, config: ChipboardConfigurationDict = None):

        if config is None:
            config = self.chipboard_config

        for channel in range(16):
            delay_value = config["delay"][cast(ChannelKey, str(channel))]["value"]

            self.delay_sliders[channel].setSliderPosition(int(delay_value))

    @Slot()
    def _on_reset_delays_clicked(self):
        """Slot for reset delays """
        logger.debug(f"reset delays clicked")
        last_config = self.config_handler.get_currently_loaded_chipboard_config()
        self._update_ui_delays(last_config)
