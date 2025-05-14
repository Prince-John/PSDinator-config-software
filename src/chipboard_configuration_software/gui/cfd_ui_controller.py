import logging
from functools import partial
from typing import get_args, cast

from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QCheckBox, QLineEdit, QWidget

from chipboard_configuration_software.command_generator.commands.configuration_types.cfd_config_types import \
    CFDConfigurationDict, NowlinMode, NowlinDelay, LockoutMode
from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import ChannelKey, \
    BoolStr
from chipboard_configuration_software.gui.chipboard_configurator import threaded_configure_chipboard
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.cfd_ui_widget import Ui_Widget_Cfd
from chipboard_configuration_software.gui.ui_files.qt_ui_modifications import ClickableLineEdit
from chipboard_configuration_software.gui.utilities import set_checkbox_silently
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

logger = logging.getLogger(__name__)


def validate_cfd_le_dac_value(value) -> int:
    try:
        value = int(value)
    except ValueError:
        logger.info("Incorrect cfd leading edge dac value")
        value = 0

    value = min(value, 31)
    value = max(value, -31)

    return value


class CfdController(QWidget):
    status_message = Signal(str)

    def __init__(self, parent_ui, ui: Ui_Widget_Cfd, config_handler: ConfigurationManager, uart_link: UartMiddleware):
        super().__init__()

        self.parent_ui = parent_ui
        self.ui = ui
        self.config_handler = config_handler
        self.uart_link = uart_link
        self.channel_enable_checkboxes: list[QCheckBox] = []
        self.leading_edge_dac_text: list[QLineEdit | ClickableLineEdit] = []
        self.current_leading_edge_dac_slider_channel: ChannelKey = "0"

        self._connect_cfd_common_settings_signals()
        self._connect_cfd_test_signals()
        self._connect_cfd_individual_channel_setting_signals()
        self._connect_cfd_misc_signals()
        self.update_ui()
        logger.info("CFD GUI signals connected!")

    @property
    def cfd_config(self):
        return self.config_handler.current_chipboard_config["cfd"]

    def _connect_cfd_common_settings_signals(self):
        self.ui.comboBox_nowlin_mode.currentTextChanged.connect(self._on_nowlin_mode_changed)
        self.ui.comboBox_nowlin_delay.currentTextChanged.connect(self._on_nowlin_delay_changed)
        self.ui.comboBox_lockout_mode.currentTextChanged.connect(self._on_lockout_mode_changed)
        self.ui.comboBox_lockout_dac.currentIndexChanged.connect(self._on_lockout_dac_changed)
        self.ui.comboBox_cfd_pulse_width.currentTextChanged.connect(self._on_cfd_pulse_width_changed)
        self.ui.comboBox_agnd_trim.currentTextChanged.connect(self._on_agnd_trim_changed)
        self.ui.checkBox_negative_polarity.stateChanged.connect(self._on_negative_polarity_checkbox_clicked)
        self.ui.checkBox_le_out_enable.setDisabled(True)
        self.ui.checkBox_global_mode.stateChanged.connect(self._on_global_mode_clicked)

        logger.debug("Connected CFD common settings signals!")
        pass

    def _update_ui_cfd_common_settings(self, cfd_config: CFDConfigurationDict = None):

        if cfd_config is None:
            cfd_config = self.cfd_config

        set_checkbox_silently(self.ui.checkBox_cfd_global_enable, cfd_config["global_enable"])

        nowlin_mode = cfd_config["common_settings"]["nowlin_mode"]
        nowlin_delay = cfd_config["common_settings"]["nowlin_delay"]
        lockout_mode = cfd_config["common_settings"]["lockout_mode"]
        lockout_dac = cfd_config["common_settings"]["lockout_DAC"]
        cfd_pulse_width = cfd_config["common_settings"]["cfd_pulse_width"]
        agnd_trim = cfd_config["common_settings"]["agnd_trim"]
        negative_polarity = cfd_config["common_settings"]["negative_polarity"]
        global_mode = cfd_config["common_settings"]["global_Mode"]

        self.ui.comboBox_nowlin_mode.setCurrentText(nowlin_mode.capitalize())
        self._update_nowlin_delay_comboBox(nowlin_mode)
        self.ui.comboBox_nowlin_delay.setCurrentText(nowlin_delay)
        self.ui.comboBox_lockout_mode.setCurrentText(lockout_mode.capitalize())
        self._update_lockout_dac_comboBox(lockout_mode)
        self.ui.comboBox_lockout_dac.setCurrentIndex(int(lockout_dac) - 1)
        self.ui.comboBox_cfd_pulse_width.setCurrentText(cfd_pulse_width)
        self.ui.comboBox_agnd_trim.setCurrentText(agnd_trim)

        set_checkbox_silently(self.ui.checkBox_negative_polarity, negative_polarity)
        set_checkbox_silently(self.ui.checkBox_global_mode, global_mode)

    def _update_nowlin_delay_comboBox(self, mode: NowlinMode = "short"):
        mode = cast(NowlinMode, mode.lower())
        nowlin_delay_map = {"short": ["1 ns",
                                      "2 ns",
                                      "3 ns",
                                      "4 ns",
                                      "5 ns",
                                      "6 ns",
                                      "7 ns",
                                      "8 ns",
                                      "9 ns",
                                      "10 ns",
                                      "11 ns",
                                      "12 ns",
                                      "13 ns",
                                      "14 ns",
                                      "15 ns",
                                      "16 ns"],
                            "long": ["12 ns",
                                     "24 ns",
                                     "36 ns",
                                     "48 ns",
                                     "60 ns",
                                     "72 ns",
                                     "84 ns",
                                     "96 ns",
                                     "108 ns",
                                     "120 ns",
                                     "132 ns",
                                     "144 ns",
                                     "156 ns",
                                     "168 ns",
                                     "180 ns",
                                     "192 ns"]
                            }

        self.ui.comboBox_nowlin_delay.clear()
        self.ui.comboBox_nowlin_delay.addItems(nowlin_delay_map[mode])
        logger.debug(f"Updated nowlin delay for nowlin mode {mode} ")

    @Slot(str)
    def _on_nowlin_mode_changed(self, mode: str):
        """Slot for nowlin mode """
        logger.debug(f"nowlin mode changed with value {mode}")
        mode = cast(NowlinMode, mode.lower())
        self.cfd_config["common_settings"]["nowlin_mode"] = mode
        self._update_nowlin_delay_comboBox(mode)

    @Slot(str)
    def _on_nowlin_delay_changed(self, delay: NowlinDelay):
        """Slot for nowlin delay """
        logger.debug(f"nowlin delay changed with value {delay}")
        self.cfd_config["common_settings"]["nowlin_delay"] = delay

    def _update_lockout_dac_comboBox(self, mode: LockoutMode = "short"):
        lock_out_dac_map = {"short": ["110 ns",
                                      '220 ns',
                                      "330 ns", '440 ns', '550 ns', '660 ns', '770 ns', '880 ns', '990 ns', '1.1 us',
                                      '1.2 us', '1.3 us', '1.4 us', '1.5 us', '1.6 us', '1.8 us', '1.9 us', '2.0 us',
                                      '2.1 us', '2.2 us', '2.3 us', '2.4 us', '2.5 us', '2.6 us', '2.8 us', '2.9 us',
                                      '3.0 us', '3.1 us', '3.2 us', '3.3 us', '3.4 us'],
                            "long": ["535 ns",
                                     '1.1 us',
                                     '1.6 us',
                                     '2.1 us', '2.7 us', '3.2 us', '3.7 us', '4.3 us', '4.8 us', '5.3 us', '5.9 us',
                                     '6.4 us', '7.0 us', '7.5 us', '8.0 us', '8.6 us', '9.1 us', '9.6 us', '10.2 us',
                                     '10.7 us', '11.2 us', '11.8 us', '12.3 us', '12.8 us', '13.4 us', '13.9 us',
                                     '14.4 us', '15.0 us', '15.5 us', '16.1 us', '16.6 us'],
                            "disabled": []
                            }

        self.ui.comboBox_lockout_dac.clear()
        if mode == "disabled":
            self.ui.comboBox_lockout_dac.setDisabled(True)
        else:
            self.ui.comboBox_lockout_dac.setEnabled(True)

        self.ui.comboBox_lockout_dac.addItems(lock_out_dac_map[mode])
        logger.debug(f"Updated lockout delay for lockout mode {mode} ")

    @Slot(str)
    def _on_lockout_mode_changed(self, mode):
        """Slot for lockout mode """
        logger.debug(f"lockout mode changed with value {mode}")

        mode = cast(LockoutMode, mode.lower())
        self.cfd_config["common_settings"]["lockout_mode"] = mode
        self._update_lockout_dac_comboBox(mode)

    @Slot(int)
    def _on_lockout_dac_changed(self, value):
        """Slot for lockout dac """
        logger.debug(f"lockout dac changed to index {value}")

        self.cfd_config["common_settings"]["lockout_DAC"] = str(value + 1)

    @Slot(str)
    def _on_cfd_pulse_width_changed(self, value):
        """Slot for cfd pulse width """
        logger.debug(f"cfd pulse width changed with value {value}")

        self.cfd_config["common_settings"]["cfd_pulse_width"] = value

    @Slot(str)
    def _on_agnd_trim_changed(self, value):
        """Slot for agnd trim """
        logger.debug(f"agnd trim changed with value {value}")

        self.cfd_config["common_settings"]["agnd_trim"] = value

    @Slot(bool)
    def _on_negative_polarity_checkbox_clicked(self, state):
        """Slot for negative polarity checkbox """
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"negative polarity checkbox clicked with value {state}")

        self.cfd_config["common_settings"]["negative_polarity"] = cast(BoolStr, str(state))

    @Slot(bool)
    def _on_global_mode_clicked(self, state):
        """Slot for global mode """
        state = state == Qt.CheckState.Checked.value
        logger.debug(f"global mode clicked with value {state}")

        self.cfd_config["common_settings"]["global_Mode"] = cast(BoolStr, str(state))

    @Slot(bool)
    def _on_cfd_global_enable_clicked(self, state):
        """Slot for cfd global enable """
        logger.debug(f"cfd global enable clicked with value {state}")

        state = state == Qt.CheckState.Checked.value
        logger.debug(f"global mode clicked with value {state}")

        self.cfd_config["global_enable"] = cast(BoolStr, str(state))

    def _connect_cfd_test_signals(self):

        self.ui.comboBox_cfd_test_point.currentTextChanged.connect(self._on_cfd_test_point_changed)
        self.ui.comboBox_cfd_test_point_channel.currentTextChanged.connect(self._on_cfd_test_point_channel_changed)

        logger.debug("CFD Test signals connected!")

    @Slot(str)
    def _on_cfd_test_point_changed(self, value):
        """Slot for cfd test point """
        logger.debug(f"cfd test point changed with value {value}")

        self.cfd_config["common_settings"]["test_point"] = value

    @Slot(str)
    def _on_cfd_test_point_channel_changed(self, channel):
        """Slot for cfd test point channel """
        logger.debug(f"cfd test point channel changed with value {channel}")

        self.cfd_config["common_settings"]["test_point_channel"] = channel

    def _update_ui_cfd_test_settings(self, cfd_config: CFDConfigurationDict = None):
        if cfd_config is None:
            cfd_config = self.cfd_config

        self.ui.comboBox_cfd_test_point.setCurrentText(cfd_config["common_settings"]["test_point"])
        self.ui.comboBox_cfd_test_point_channel.setCurrentText(cfd_config["common_settings"]["test_point_channel"])

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

        self.cfd_config["individual_channel_settings"][channel_key]["enable"] = cast(BoolStr, str(state))

        if not state:
            set_checkbox_silently(self.ui.checkBox_cfd_channel_enable_all, "False")
            if channel < 8:
                set_checkbox_silently(self.ui.checkBox_cfd_channel_enable_0_7, "False")
            else:
                set_checkbox_silently(self.ui.checkBox_cfd_channel_enable_8_15, "False")

    def _connect_cfd_individual_channel_setting_signals(self):

        le_dac_validator = QIntValidator(-31, 31)

        for channel in range(16):
            checkbox = getattr(self.ui, f'checkBox_cfd_channel_enable_{channel}')
            line = getattr(self.ui, f'lineEdit_cfd_le_dac_{channel}')

            checkbox.stateChanged.connect(partial(self._on_single_channel_enable_clicked, channel))
            line.setValidator(le_dac_validator)
            line.textEdited.connect(partial(self._on_leading_edge_dac_edited, channel))
            # line.clicked.connect(partial(self._on_leading_edge_dac_focused, channel))
            line.focused.connect(partial(self._on_leading_edge_dac_focused, channel))

            self.channel_enable_checkboxes.append(checkbox)
            self.leading_edge_dac_text.append(line)

        self.ui.verticalSlider_cfd_leading_edge_dac_value.valueChanged.connect(self._on_leading_edge_dac_slider_changed)
        self.ui.checkBox_cfd_channel_enable_all.stateChanged.connect(self._on_channel_enable_all_clicked)
        self.ui.checkBox_cfd_channel_enable_0_7.stateChanged.connect(self._on_channel_enable_0_7_clicked)
        self.ui.checkBox_cfd_channel_enable_8_15.stateChanged.connect(self._on_channel_enable_8_15_clicked)

    @Slot(int)
    def _on_leading_edge_dac_slider_changed(self, value):
        """Slot for leading edge dac slider """
        logger.debug(f"leading edge dac slider clicked with value {value}")
        self.leading_edge_dac_text[int(self.current_leading_edge_dac_slider_channel)].setText(str(value))

    @Slot(str)
    def _on_leading_edge_dac_edited(self, channel, value):
        """Slot for leading edge dac """
        logger.debug(f"leading edge dac {channel} edited with value {value}")

        channel = cast(ChannelKey, str(channel))

        value = validate_cfd_le_dac_value(value)

        self.cfd_config["individual_channel_settings"][channel]["leading_edge_DAC_value"] = value
        self.current_leading_edge_dac_slider_channel = channel

        self._update_cfd_leading_edge_dac_slider()

    @Slot()
    def _on_leading_edge_dac_focused(self, channel):
        """Slot for leading edge dac """
        logger.debug(f"leading edge dac {channel} focused")
        channel = cast(ChannelKey, str(channel))

        self.current_leading_edge_dac_slider_channel = channel

        self._update_cfd_leading_edge_dac_slider()

    def _update_cfd_leading_edge_dac_slider(self, cfd_config: CFDConfigurationDict = None):

        if cfd_config is None:
            cfd_config = self.cfd_config

        value = cfd_config["individual_channel_settings"][self.current_leading_edge_dac_slider_channel][
            "leading_edge_DAC_value"]
        self.ui.verticalSlider_cfd_leading_edge_dac_value.blockSignals(True)
        self.ui.verticalSlider_cfd_leading_edge_dac_value.setSliderPosition(int(value))
        self.ui.verticalSlider_cfd_leading_edge_dac_value.blockSignals(False)

    def _update_ui_individual_channel_settings(self, cfd_config: CFDConfigurationDict = None):

        if cfd_config is None:
            cfd_config = self.cfd_config

        for channel in range(16):
            text_value = cfd_config["individual_channel_settings"][cast(ChannelKey, str(channel))][
                "leading_edge_DAC_value"]
            enable_state = cfd_config["individual_channel_settings"][cast(ChannelKey, str(channel))]["enable"]

            self.leading_edge_dac_text[channel].setText(text_value)
            set_checkbox_silently(self.channel_enable_checkboxes[channel], enable_state)

    @Slot()
    def _on_cfd_reset_gui_clicked(self):
        """Slot for cfd reset gui """
        logger.debug(f"cfd reset gui clicked")

        last_cfd_config = self.config_handler.get_currently_loaded_chipboard_config("cfd")

        self.update_ui(last_cfd_config)

    def update_ui(self, cfd_config: CFDConfigurationDict = None):

        if cfd_config is None:
            cfd_config = self.cfd_config

        self._update_ui_cfd_common_settings(cfd_config)
        self._update_ui_cfd_test_settings(cfd_config)
        self._update_ui_individual_channel_settings(cfd_config)

    def _connect_cfd_misc_signals(self):
        self.ui.pushButton_cfd_configure.pressed.connect(self._on_cfd_configure_clicked)
        self.ui.pushButton_cfd_reset.pressed.connect(self._on_cfd_reset_clicked)
        self.ui.pushButton_cfd_reset_gui.pressed.connect(self._on_cfd_reset_gui_clicked)

    def configure_cfd(self):

        self.parent_ui.configuration_thread, self.parent_ui.configuration_worker = threaded_configure_chipboard(
            parent_ui=self.parent_ui,
            config_handler=self.config_handler,
            uart_link=self.uart_link,
            component="cfd")
        self.parent_ui.configuration_thread.start()

    @Slot()
    def _on_cfd_configure_clicked(self):
        """Slot for cfd configure """
        logger.debug(f"cfd configure clicked")
        self.configure_cfd()

    @Slot()
    def _on_cfd_reset_clicked(self):
        """Slot for cfd reset """
        # TODO: Implement this.
        logger.debug(f"cfd reset clicked. Functionality not yet implemented. #TODO")
