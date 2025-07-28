import json
from functools import partial
from time import sleep
from typing import get_args, cast, List

from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtWidgets import QCheckBox, QComboBox, QSlider, QLineEdit, QWidget, QApplication
from serial import PortNotOpenError

from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import ChannelKey, \
    BoolStr, SubchannelKey
from chipboard_configuration_software.command_generator.commands.configuration_types.psd_config_types import \
    PSDConfigurationDict
from chipboard_configuration_software.command_generator.generate_command_string import generate_commands
from chipboard_configuration_software.gui.chipboard_configurator import threaded_configure_chipboard, \
    threaded_reset_chipboard
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.log_window import FailureDetailsDialog
from chipboard_configuration_software.gui.ui_files.psd_ui_widget import Ui_Widget_Psd
import logging

from chipboard_configuration_software.gui.utilities import set_checkbox_silently, configure_chipboard
from chipboard_configuration_software.uart_link.middleware import UartMiddleware, CommandRejectedError

logger = logging.getLogger(__name__)


class PsdController(QWidget):
    status_message = Signal(str)
    test_mode_flag = Signal()

    def __init__(self, parent_ui, ui: Ui_Widget_Psd, config_handler: ConfigurationManager, uart_link: UartMiddleware):
        """
             ui is an instance of Ui_DockWidget_psd (after setupUi has been called).
         """

        super().__init__()
        self.parent_ui = parent_ui
        self.uart_link = uart_link
        self.SUBCHANNELS: tuple[SubchannelKey, SubchannelKey, SubchannelKey] = ("a", "b", "c")
        self.ui = ui
        self.channel_enable_checkboxes: list[QCheckBox] = []
        self.gain_comboBoxes: list[QComboBox] = []
        self.delay_range_comboBoxes: list[QComboBox] = []
        self.width_range_comboBoxes: list[QComboBox] = []
        self.serial_register_comboBoxes: list[QComboBox] = []

        self.config_handler = config_handler
        self._connect_psd_offset_dac_signals()
        self._connect_psd_serial_register_signals()
        self._connect_octal_dac_signals()
        self._connect_test_mode_signals()
        self._connect_misc_signals()

        logger.info("PSD GUI signals connected!")

        self.update_ui()
        logger.info("PSD UI Updated!")

    @property
    def psd_config(self):
        return self.config_handler.current_chipboard_config["psd"]

    def _connect_signals(self):
        pass

    @staticmethod
    def __set_ui_triple_value(sliders: tuple[QSlider, QSlider, QSlider],
                              line_edits: tuple[QLineEdit, QLineEdit, QLineEdit],
                              values: tuple[int, int, int],
                              label: str = "triple"
                              ) -> None:
        """
        Generic function to update 3 sliders and line edits with given values.
        :param sliders: Tuple of 3 QSlider widgets (a, b, c)
        :param line_edits: Tuple of 3 QLineEdit widgets (a, b, c)
        :param values: Tuple of 3 integers to set on the sliders and line edits
        :param label: Optional label for logging/debugging
        """
        for slider, val in zip(sliders, values):
            slider.setSliderPosition(val)

        for line_edit, val in zip(line_edits, values):
            line_edit.setText(str(val))

        logger.debug(f"Set {label} UI to values {values[0]}, {values[1]}, {values[2]}")

    def _update_ui_psd_offset_dac(self, psd_config: PSDConfigurationDict = None) -> None:
        """
        Updates the PSD offset dac gui to settings present in current chipboard config state.

        :return: None
        """
        if psd_config is None:
            psd_config = self.psd_config

        channel_combobox_value = str(self.ui.comboBox_psd_offset_dac_channel_selection.currentIndex())
        assert channel_combobox_value in get_args(ChannelKey)

        current_offset_dac_channel = cast(ChannelKey, channel_combobox_value)

        psd_offset_dac_config = psd_config["channel_offset_dacs"][current_offset_dac_channel]

        values = (int(psd_offset_dac_config["a"]), int(psd_offset_dac_config["b"]), int(psd_offset_dac_config["c"]))

        sliders = (self.ui.verticalSlider_psd_single_channel_offset_dac_a,
                   self.ui.verticalSlider_psd_single_channel_offset_dac_b,
                   self.ui.verticalSlider_psd_single_channel_offset_dac_c)

        lines = (self.ui.lineEdit_psd_offset_dac_a,
                 self.ui.lineEdit_psd_offset_dac_b,
                 self.ui.lineEdit_psd_offset_dac_c)

        self.__set_ui_triple_value(sliders, lines, values, label="Offset DAC")

    def _connect_psd_offset_dac_signals(self):

        for i in range(16):
            self.ui.comboBox_psd_offset_dac_channel_selection.addItem(f"{i}")

        self.ui.comboBox_psd_offset_dac_channel_selection.currentIndexChanged.connect(
            self._on_psd_offset_dac_channel_selected)

        for subchannel in self.SUBCHANNELS:
            slider = getattr(self.ui, f"verticalSlider_psd_single_channel_offset_dac_{subchannel}")
            line = getattr(self.ui, f"lineEdit_psd_offset_dac_{subchannel}")

            # slider → lineEdit, tag with subchannel
            slider.valueChanged.connect(
                partial(self._on_psd_offset_subchannel_slider_valueChanged, subchannel)
            )

            # lineEdit → slider, tag with subchannel
            line.textEdited.connect(
                partial(self._on_psd_offset_subchannel_text_textEdited, subchannel)
            )

        self.ui.pushButton_psd_offset_dac_configure.pressed.connect(self._on_psd_offset_dac_configure)
        self.ui.pushButton_psd_offset_dac_reset.pressed.connect(self._on_psd_offset_dac_reset)
        logger.debug("PSD Offset DAC gui signals connected!")

    @Slot(str, int)
    def _on_psd_offset_subchannel_slider_valueChanged(self, subchannel: str, value: int):
        logger.debug(f"Offset Subchannel {subchannel} Slider Value Changed.")
        line = getattr(self.ui, f"lineEdit_psd_offset_dac_{subchannel}")
        line.setText(str(value))
        logger.debug(f"Offset Subchannel {subchannel} text auto set to {value}.")
        self._update_psd_offset_dac_state(subchannel, value)

    @Slot(str, str)
    def _on_psd_offset_subchannel_text_textEdited(self, subchannel: str, text: str):
        logger.debug(f"Offset Subchannel {subchannel} text edited.")
        try:
            value = int(text)
        except ValueError:
            value = 0
            logger.warning(f"Offset Subchannel text incorrect type, reset to zero!")
        value = max(-15, min(15, value))

        slider = getattr(self.ui, f"verticalSlider_psd_single_channel_offset_dac_{subchannel}")
        slider.setSliderPosition(value)
        logger.debug(f"Offset Subchannel {subchannel} slider auto set to {value}.")

    @Slot(int)
    def _on_psd_offset_dac_channel_selected(self, channel: int):
        logger.debug(f"Offset Dac channel Selection {channel}.")
        self._update_ui_psd_offset_dac()

    @Slot()
    def _on_psd_offset_dac_configure(self):
        logger.debug(f"Pressed offset_dac_configure.")

        channel_combobox_value = str(self.ui.comboBox_psd_offset_dac_channel_selection.currentIndex())
        assert channel_combobox_value in get_args(ChannelKey)

        current_offset_dac_channel = cast(ChannelKey, channel_combobox_value)

        current_a_value = self.ui.verticalSlider_psd_single_channel_offset_dac_a.value()
        current_b_value = self.ui.verticalSlider_psd_single_channel_offset_dac_b.value()
        current_c_value = self.ui.verticalSlider_psd_single_channel_offset_dac_c.value()

        psd_offset_dac_config = self.psd_config["channel_offset_dacs"][current_offset_dac_channel]

        psd_offset_dac_config["a"] = current_a_value
        psd_offset_dac_config["b"] = current_b_value
        psd_offset_dac_config["c"] = current_c_value

        logger.info(f"Updated psd offset dac settings for current config")

    @Slot()
    def _on_psd_offset_dac_reset(self):
        logger.debug(f"Pressed offset_dac_reset.")

        sliders = (self.ui.verticalSlider_psd_single_channel_offset_dac_a,
                   self.ui.verticalSlider_psd_single_channel_offset_dac_b,
                   self.ui.verticalSlider_psd_single_channel_offset_dac_c)

        lines = (self.ui.lineEdit_psd_offset_dac_a,
                 self.ui.lineEdit_psd_offset_dac_b,
                 self.ui.lineEdit_psd_offset_dac_c)

        values = (0, 0, 0)

        self.__set_ui_triple_value(sliders, lines, values, label="Offset DAC")

    def _update_psd_offset_dac_state(self, subchannel: str, value: int):
        channel_combobox_value = str(self.ui.comboBox_psd_offset_dac_channel_selection.currentIndex())
        if channel_combobox_value not in get_args(ChannelKey):
            logger.warning(f"Invalid channel selected: {channel_combobox_value}")
            return

        current_channel = cast(ChannelKey, channel_combobox_value)
        subchannel = cast(SubchannelKey, subchannel)
        self.psd_config["channel_offset_dacs"][current_channel][subchannel] = value
        logger.debug(f"Updated psd_config: channel {current_channel} subchannel {subchannel} = {value}")

    def _update_ui_psd_channel_enable_checkbox(self, psd_config: PSDConfigurationDict = None):

        if psd_config is None:
            psd_config = self.psd_config

        enable_states = psd_config["serial_register_settings"]["channel_enables"]

        for channel, state in enable_states.items():
            logger.debug(f"Enable checkbox {channel} ui updated to current config state {state}.")
            checkbox = self.channel_enable_checkboxes[int(channel)]
            set_checkbox_silently(checkbox, state)

        logger.info("Updated enable checkbox ui to current config state.")

    def _update_ui_psd_serial_register_comboBoxes(self, psd_config: PSDConfigurationDict = None):

        if psd_config is None:
            psd_config = self.psd_config

        current_gains = psd_config["serial_register_settings"]["gain"]
        current_delay_ranges = psd_config["serial_register_settings"]["delay_ranges"]
        current_width_ranges = psd_config["serial_register_settings"]["width_ranges"]

        for subchannel in self.SUBCHANNELS:
            gain_comboBox: QComboBox = getattr(self.ui, f"comboBox_psd_gain_{subchannel}")
            delay_range_comboBox: QComboBox = getattr(self.ui, f"comboBox_psd_delay_range_{subchannel}")
            width_range_comboBox: QComboBox = getattr(self.ui, f"comboBox_psd_width_range_{subchannel}")

            gain_comboBox.setCurrentText(str(current_gains[subchannel]))
            delay_range_comboBox.setCurrentText(current_delay_ranges[subchannel])
            width_range_comboBox.setCurrentText(current_width_ranges[subchannel])

        self.ui.comboBox_psd_vtc_range.setCurrentText(psd_config["serial_register_settings"]["vtc_range"])
        self.ui.comboBox_psd_bias.setCurrentText(psd_config["serial_register_settings"]["bias"])
        self.ui.comboBox_psd_polarity.setCurrentText(psd_config["serial_register_settings"]["polarity"])
        logger.debug(f"Updated Serial Config ComboBoxes!")

    def _connect_psd_serial_register_signals(self):

        # channel enable connections
        for channel in range(16):
            checkbox = getattr(self.ui, f'checkBox_psd_channel_enable_{channel}')
            checkbox.stateChanged.connect(partial(self._on_single_channel_enable_clicked, channel))
            self.channel_enable_checkboxes.append(checkbox)

        self.ui.checkBox_psd_channel_enable_all.stateChanged.connect(self._on_channel_enable_all_clicked)
        self.ui.checkBox_psd_channel_enable_0_7.stateChanged.connect(self._on_channel_enable_0_7_clicked)
        self.ui.checkBox_psd_channel_enable_8_15.stateChanged.connect(self._on_channel_enable_8_15_clicked)

        # ranges
        for subchannel in self.SUBCHANNELS:
            gain_comboBox = getattr(self.ui, f"comboBox_psd_gain_{subchannel}")
            delay_range_comboBox = getattr(self.ui, f"comboBox_psd_delay_range_{subchannel}")
            width_range_comboBox = getattr(self.ui, f"comboBox_psd_width_range_{subchannel}")

            gain_comboBox.currentTextChanged.connect(partial(self._on_gain_changed, subchannel))
            delay_range_comboBox.currentIndexChanged.connect(partial(self._on_delay_range_changed, subchannel))
            width_range_comboBox.currentIndexChanged.connect(partial(self._on_width_range_changed, subchannel))

        self.ui.comboBox_psd_vtc_range.currentTextChanged.connect(self._on_vtc_range_changed)

        # other connections
        self.ui.comboBox_psd_polarity.currentTextChanged.connect(self._on_polarity_changed)
        self.ui.comboBox_psd_bias.currentTextChanged.connect(self._on_bias_changed)

    @Slot(str)
    def _on_bias_changed(self, bias):
        logger.debug(f"Bias changed to {bias}")

        self.psd_config["serial_register_settings"]["bias"] = bias

    @Slot(str)
    def _on_polarity_changed(self, polarity):
        logger.debug(f"Polarity changed to {polarity}")

        self.psd_config["serial_register_settings"]["polarity"] = polarity

    @Slot(str)
    def _on_vtc_range_changed(self, vtc_range):
        logger.debug(f"VTC range changed to {vtc_range}")

        self.psd_config["serial_register_settings"]["vtc_range"] = vtc_range

    @Slot(str, str)
    def _on_gain_changed(self, subchannel: str, gain):
        logger.debug(f"Subchannel {subchannel} gain changed to {gain}")

        self.psd_config["serial_register_settings"]["gain"][subchannel] = gain

    @Slot(str, int)
    def _on_delay_range_changed(self, subchannel: SubchannelKey, delay_range):
        logger.debug(f"Subchannel {subchannel} delay range changed to {delay_range}")

        self.psd_config["serial_register_settings"]["delay_ranges"][subchannel] = delay_range

    @Slot(str, int)
    def _on_width_range_changed(self, subchannel: SubchannelKey, width_range):
        logger.debug(f"Subchannel {subchannel} width range changed to {width_range}")

        self.psd_config["serial_register_settings"]["width_ranges"][subchannel] = width_range

    @Slot(bool)
    def _on_channel_enable_all_clicked(self, state: bool):
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"Channel enable all checkbox set to {state}")

        for checkbox in self.channel_enable_checkboxes:
            checkbox.setChecked(state)

    @Slot(bool)
    def _on_channel_enable_0_7_clicked(self, state: bool):
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"Channel enable 0-7 checkbox set to {state}")

        for checkbox in self.channel_enable_checkboxes[0:8]:
            checkbox.setChecked(state)

    @Slot(bool)
    def _on_channel_enable_8_15_clicked(self, state: bool):
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"Channel enable 8-15 checkbox set to {state}")

        for checkbox in self.channel_enable_checkboxes[8:16]:
            checkbox.setChecked(state)

    @Slot(bool)
    def _on_single_channel_enable_clicked(self, channel: int, state):
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"Channel {channel} enable checkbox set to {state}")

        assert str(channel) in get_args(ChannelKey)
        channel_key = cast(ChannelKey, str(channel))

        self.psd_config["serial_register_settings"]["channel_enables"][channel_key] = cast(BoolStr, str(state))

        if not state:
            set_checkbox_silently(self.ui.checkBox_psd_channel_enable_all, "False")
            if channel < 8:
                set_checkbox_silently(self.ui.checkBox_psd_channel_enable_0_7, "False")
            else:
                set_checkbox_silently(self.ui.checkBox_psd_channel_enable_8_15, "False")

    def _connect_octal_dac_signals(self):

        for subchannel in self.SUBCHANNELS:
            delay_slider = getattr(self.ui, f"horizontalSlider_psd_delay_dac_{subchannel}")
            delay_line = getattr(self.ui, f"text_psd_delay_dac_{subchannel}")

            width_slider = getattr(self.ui, f"horizontalSlider_psd_width_dac_{subchannel}")
            width_line = getattr(self.ui, f"text_psd_width_dac_{subchannel}")

            reset_button = getattr(self.ui, f"pushButton_psd_reset_subchannel_{subchannel}")

            delay_slider.valueChanged.connect(partial(self._on_psd_delay_dac_slider_changed, subchannel))
            delay_line.textEdited.connect(partial(self._on_psd_delay_dac_text_edited, subchannel))

            width_slider.valueChanged.connect(partial(self._on_psd_width_dac_slider_changed, subchannel))
            width_line.textEdited.connect(partial(self._on_psd_width_dac_text_edited, subchannel))
            reset_button.pressed.connect(partial(self._on_psd_integrator_reset_clicked, subchannel))

        self.ui.text_psd_auto_veto_dac.textEdited.connect(self._on_psd_auto_veto_dac_text_edited)
        self.ui.horizontalSlider_psd_auto_veto_dac.valueChanged.connect(self._on_psd_auto_veto_dac_slider_changed)

        pass

    @Slot(int)
    def _on_psd_auto_veto_dac_slider_changed(self, value):
        """
        Wrapper for the `_on_octal_dac_slider_valueChanged` that updates the config dict
        """
        voltage = self._on_octal_dac_slider_valueChanged(f"text_psd_auto_veto_dac", value)
        self.psd_config["octal_dac_settings"]["auto_veto_time"] = voltage
        logger.debug(f"Updated config for auto veto voltage")
        pass

    @Slot(str)
    def _on_psd_auto_veto_dac_text_edited(self, value):
        """
        Wrapper for the `_on_octal_dac_text_textEdited()` that updates the config dict
        """
        voltage = self._on_octal_dac_text_textEdited(f"horizontalSlider_psd_auto_veto_dac", value)
        self.psd_config["octal_dac_settings"]["auto_veto_time"] = voltage
        logger.debug(f"Updated config for auto veto voltage")
        pass

    @Slot(int)
    def _on_psd_delay_dac_slider_changed(self, subchannel: SubchannelKey, value):
        """
        Wrapper for the `_on_octal_dac_slider_valueChanged` that updates the config dict
        """
        voltage = self._on_octal_dac_slider_valueChanged(f"text_psd_delay_dac_{subchannel}", value)
        self.psd_config["octal_dac_settings"]["delay_voltages"][subchannel] = voltage
        logger.debug(f"Updated config for delay voltage {subchannel}")
        pass

    @Slot(str)
    def _on_psd_delay_dac_text_edited(self, subchannel: SubchannelKey, value: str):
        """
        Wrapper for the `_on_octal_dac_text_textEdited()` that updates the config dict.
        """
        voltage = self._on_octal_dac_text_textEdited(f"horizontalSlider_psd_delay_dac_{subchannel}", value)
        self.psd_config["octal_dac_settings"]["delay_voltages"][subchannel] = voltage
        logger.debug(f"Updated config for delay voltage {subchannel}")
        pass

    @Slot(int)
    def _on_psd_width_dac_slider_changed(self, subchannel: SubchannelKey, value):
        """
        Wrapper for the `_on_octal_dac_slider_valueChanged` that updates the config dict
        """
        voltage = self._on_octal_dac_slider_valueChanged(f"text_psd_width_dac_{subchannel}", value)
        self.psd_config["octal_dac_settings"]["width_voltages"][subchannel] = voltage
        logger.debug(f"Updated config for width voltage {subchannel}")
        pass

    @Slot(str)
    def _on_psd_width_dac_text_edited(self, subchannel: SubchannelKey, value: str):
        """
        Wrapper for the `_on_octal_dac_text_textEdited()` that updates the config dict.
        """
        voltage = self._on_octal_dac_text_textEdited(f"horizontalSlider_psd_width_dac_{subchannel}", value)
        self.psd_config["octal_dac_settings"]["width_voltages"][subchannel] = voltage
        logger.debug(f"Updated config for width voltage {subchannel}")
        pass

    @Slot(int)
    def _on_octal_dac_slider_valueChanged(self, text_object_name: str, value: int) -> str:
        logger.debug(f"{text_object_name} Slider Value Changed to {value}")
        line = getattr(self.ui, text_object_name)

        voltage = (value / 1023) * 5.0

        line.setText(f"{voltage:0.2f} V")
        logger.debug(f"{text_object_name} text auto set to {voltage:0.2f} V")

        return str(voltage)

    @Slot(str)
    def _on_octal_dac_text_textEdited(self, object_name: str, text: str):
        logger.debug(f"{object_name} text edited to {text}.")

        """
        value in X.XX V format
        strip ''V
        typecast to float
        
        """
        text = text.strip(' V')

        try:
            value = float(text)

        except ValueError:
            value = 0
            logger.warning(f"Text input incorrect type, reset to zero!")

        if value < 0:
            logger.info("DAC voltage must be between 0.0 V-5.0 V")
            value = 0
        elif value > 5:
            logger.info("DAC voltage must be between 0.0 V-5.0 V")
            value = 5.0

        value = int((value / 5.0) * 1023)

        slider = getattr(self.ui, object_name)
        slider.blockSignals(True)
        slider.setSliderPosition(value)
        slider.blockSignals(False)
        logger.debug(f"{object_name} slider auto set to {value}.")
        return text

    def _update_ui_psd_single_integrator(self, subchannel: SubchannelKey, psd_config: PSDConfigurationDict = None):

        if psd_config is None:
            psd_config = self.psd_config

        delay = psd_config["octal_dac_settings"]["delay_voltages"][subchannel]
        width = psd_config["octal_dac_settings"]["width_voltages"][subchannel]
        gain = psd_config["serial_register_settings"]["gain"][subchannel]
        delay_range = psd_config["serial_register_settings"]["delay_ranges"][subchannel]
        width_range = psd_config["serial_register_settings"]["width_ranges"][subchannel]

        delay_slider = getattr(self.ui, f"horizontalSlider_psd_delay_dac_{subchannel}")
        width_slider = getattr(self.ui, f"horizontalSlider_psd_width_dac_{subchannel}")
        gain_comboBox = getattr(self.ui, f"comboBox_psd_gain_{subchannel}")
        delay_range_comboBox = getattr(self.ui, f"comboBox_psd_delay_range_{subchannel}")
        width_range_comboBox = getattr(self.ui, f"comboBox_psd_width_range_{subchannel}")

        delay_slider.setSliderPosition(int((float(delay) / 5.0) * 1023))
        width_slider.setSliderPosition(int((float(width) / 5.0) * 1023))

        gain_comboBox.setCurrentText(gain)
        delay_range_comboBox.setCurrentText(str(delay_range))
        width_range_comboBox.setCurrentText(str(width_range))

    def _update_ui_psd_integrators(self, psd_config=None):

        if psd_config is None:
            psd_config = self.psd_config

        for subchannel in self.SUBCHANNELS:
            self._update_ui_psd_single_integrator(subchannel, psd_config)

        auto_veto_position = (int((float(psd_config["octal_dac_settings"]["auto_veto_time"]) / 5.0) * 1023))
        self.ui.horizontalSlider_psd_auto_veto_dac.setSliderPosition(auto_veto_position)

        logger.info("Updated UI for integrators!")

    @Slot()
    def _on_psd_integrator_reset_clicked(self, subchannel):
        last_psd_config = self.config_handler.get_currently_loaded_chipboard_config("psd")
        self._update_ui_psd_single_integrator(subchannel, last_psd_config)

        pass

    def _connect_test_mode_signals(self):
        for i in range(16):
            self.ui.comboBox_psd_test_mode_channel_selection.addItem(f"{i}")

        self.ui.comboBox_psd_test_mode.currentTextChanged.connect(self._on_test_mode_status_changed)
        self.ui.comboBox_psd_test_mode_channel_selection.currentIndexChanged.connect(self._on_test_channel_changed)
        self.ui.comboBox_psd_test_mode_subchannel_selection.currentTextChanged.connect(self._on_test_subchannel_changed)

        logger.debug("PSD test mode signals connected")
        pass

    @Slot(str)
    def _on_test_mode_status_changed(self, value):
        logger.debug(f"PSD test mode status changed {value}")
        self.psd_config["test_mode"]["status"] = value

    @Slot(int)
    def _on_test_channel_changed(self, channel):
        """Slot for test_channel """
        logger.debug(f"test_channel changed with value {channel}")
        self.psd_config["test_mode"]["channel"] = channel

    @Slot(str)
    def _on_test_subchannel_changed(self, subchannel):
        """Slot for test subchannel """
        logger.debug(f"test subchannel changed with value {subchannel}")
        self.psd_config["test_mode"]["subchannel"] = subchannel

    @Slot()
    def _on_test_mode_reset_clicked(self):
        """
        DEPRECATED- DO not use.
        Slot for test mode reset

        """
        logger.debug(f"test mode reset clicked")
        last_psd_config = self.config_handler.get_currently_loaded_chipboard_config("psd")
        self._update_ui_psd_test_mode(last_psd_config)

    def _update_ui_psd_test_mode(self, psd_config=None):

        if psd_config is None:
            psd_config = self.psd_config

        status = psd_config["test_mode"]["status"].capitalize()
        channel = psd_config["test_mode"]["channel"]
        subchannel = psd_config["test_mode"]["subchannel"].capitalize()

        self.ui.comboBox_psd_test_mode.setCurrentText(status)
        self.ui.comboBox_psd_test_mode_channel_selection.setCurrentText(str(channel))
        self.ui.comboBox_psd_test_mode_subchannel_selection.setCurrentText(subchannel)

    def _connect_misc_signals(self):

        self.ui.comboBox_psd_trigger_mode.currentTextChanged.connect(self._on_trigger_mode_changed)
        self.ui.checkBox_psd_global_enable.stateChanged.connect(self._on_psd_global_enable_changed)
        self.ui.pushButton_real_time_config.clicked.connect(self._on_real_time_config_clicked)
        self.ui.pushButton_configure_psd.pressed.connect(self._on_configure_psd_clicked)
        self.ui.pushButton_reset_psd.pressed.connect(self._on_reset_psd_clicked)
        self.ui.pushButton_psd_digital_reset.pressed.connect(self._on_digital_reset_psd_clicked)
        self.ui.pushButton_psd_force_reset.pressed.connect(self._on_force_reset_psd_clicked)

    @Slot(bool)
    def _on_real_time_config_clicked(self, state):
        """Slot for real time config """
        logger.info(f"real time config clicked with value {state}")

        if state:

            self.parent_ui.configuration_thread, self.parent_ui.configuration_worker = threaded_configure_chipboard(
                self.parent_ui,
                config_handler=self.config_handler,
                uart_link=self.uart_link
            )

            # TODO Error handle if configuration is not successful.
            self.parent_ui.configuration_thread.finished.connect(self.__start_real_time_config)
            self.parent_ui.configuration_thread.start()

        else:
            self.parent_ui.real_time_configurator.disable()

    def __start_real_time_config(self):
        """
        Helper to start the polled real time configurator after the bulk configuration thread has finished.

        :return: None.
        """
        logger.info(f"real time config started")
        self.parent_ui.real_time_configurator.enable()

    @Slot(bool)
    def _on_psd_global_enable_changed(self, state):
        """Slot for psd global enable """
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"psd global enable changed with value {state}")

        self.psd_config["global_enable"] = cast(BoolStr, str(state))

    @Slot(str)
    def _on_trigger_mode_changed(self, value):
        """Slot for trigger mode """
        logger.debug(f"trigger mode changed with value {value}")

        self.psd_config["trigger_mode"] = value

    @Slot()
    def _on_reset_gui_clicked(self):
        """Slot for reset gui button """
        logger.debug(f"reset gui clicked")
        last_psd_config = self.config_handler.get_currently_loaded_chipboard_config("psd")
        self.update_ui(last_psd_config)

    def _update_ui_psd_misc(self, psd_config=None):

        if psd_config is None:
            psd_config = self.psd_config
        set_checkbox_silently(self.ui.checkBox_psd_global_enable, psd_config["global_enable"])
        self.ui.comboBox_psd_trigger_mode.setCurrentText(psd_config["trigger_mode"])

    def update_ui(self, psd_config=None):

        if psd_config is None:
            psd_config = self.psd_config

        self._update_ui_psd_test_mode(psd_config)
        self._update_ui_psd_serial_register_comboBoxes(psd_config)
        self._update_ui_psd_channel_enable_checkbox(psd_config)
        self._update_ui_psd_integrators(psd_config)
        self._update_ui_psd_offset_dac(psd_config)
        self._update_ui_psd_misc(psd_config)
        pass

    @Slot()
    def _on_configure_psd_clicked(self):
        """Slot for configure psd """
        logger.debug(f"configure psd clicked")

        self.configure_psd()

    @Slot()
    def _on_reset_psd_clicked(self):
        """Slot for reset psd """
        logger.debug(f"reset psd clicked")
        self.parent_ui.reset_thread, self.parent_ui.reset_worker = threaded_reset_chipboard(self.parent_ui,
                                                                                            self.uart_link,
                                                                                            component="psd")
        self.parent_ui.reset_thread.start()

    @Slot()
    def _on_digital_reset_psd_clicked(self):
        """Slot for digital reset psd """
        logger.debug(f"digital reset psd clicked ")
        self.parent_ui.reset_thread, self.parent_ui.reset_worker = threaded_reset_chipboard(self.parent_ui,
                                                                                            self.uart_link,
                                                                                            component="psd",
                                                                                            reset_type="digital")
        self.parent_ui.reset_thread.start()

    @Slot()
    def _on_force_reset_psd_clicked(self):
        """Slot for force reset psd """
        logger.debug(f"force reset psd clicked")
        self.parent_ui.reset_thread, self.parent_ui.reset_worker = threaded_reset_chipboard(self.parent_ui,
                                                                                            self.uart_link,
                                                                                            component="psd",
                                                                                            reset_type="force")
        self.parent_ui.reset_thread.start()

    def show_failure_details(self, failures):
        dialog = FailureDetailsDialog(failures, parent=self)
        dialog.exec()

    def configure_psd(self):
        self.parent_ui.configuration_thread, self.parent_ui.configuration_worker = threaded_configure_chipboard(
            parent_ui=self.parent_ui,
            config_handler=self.config_handler,
            uart_link=self.uart_link,
            component="psd")
        self.parent_ui.configuration_thread.start()
