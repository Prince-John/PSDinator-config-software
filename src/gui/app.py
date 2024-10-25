import json
import sys

import configuration_helper
# import utilities
# import connection_helper

import PySide6.QtCore
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QRegularExpression, SIGNAL

from src.gui import utilities
from ui_files.MainConfigWindow import Ui_MainWindow
from ui_files.GlobalSettingsWindow import Ui_Dialog


# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)


def on_detectI2CDevices_clicked():
    print("detectI2CDevices Clicked.")
    pass


def change_item_selection(comboBox, text):
    index = comboBox.findText(text, Qt.MatchFixedString)
    if index >= 0:
        comboBox.setCurrentIndex(index)
    else:
        raise ValueError("Text passed does not match any comboBox options")


class GlobalSettingsWindow(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, configuration_manager):
        super(GlobalSettingsWindow, self).__init__()
        self.setupUi(self)
        self.configuration_manager = configuration_manager

        # CheckBox Connections

        self.externalAgndEnable.stateChanged.connect(self.on_externalAgndEnable_clicked)
        self.globalMode.stateChanged.connect(self.on_globalMode_clicked)
        self.LEOutEnable.stateChanged.connect(self.on_LEOutEnable_clicked)
        self.globalEnable.stateChanged.connect(self.on_globalEnable_clicked)

        # ComboBox Connections

        self.nowlinMode.currentTextChanged.connect(self.on_nowlinMode_clicked)
        self.nowlinDelay.currentTextChanged.connect(self.on_nowlinDelay_clicked)
        self.lockoutMode.currentTextChanged.connect(self.on_lockoutMode_clicked)
        self.CFDPulseWidth.currentTextChanged.connect(self.on_CFDPulseWidth_clicked)
        self.AgndTrim.currentTextChanged.connect(self.on_AgndTrim_clicked)

    # Checkbox slot function declarations

    def on_externalAgndEnable_clicked(self):
        print("externalAgndEnable State Changed.")

        pass

    def on_globalMode_clicked(self):
        print("globalMode State Changed.")
        pass

    def on_LEOutEnable_clicked(self):
        print("LEOutEnable State Changed.")
        pass

    def on_globalEnable_clicked(self):
        print("globalEnable State Changed.")
        pass

    # ComboBox slot function declarations

    def on_nowlinMode_clicked(self, text):
        print("nowlinMode selection changed to {0}".format(text))
        pass

    def on_nowlinDelay_clicked(self, text):
        print("nowlinDelay selection changed to {0}".format(text))
        pass

    def on_lockoutMode_clicked(self, text):
        print("lockoutMode selection changed to {0}".format(text))
        pass

    def on_CFDPulseWidth_clicked(self, text):
        print("CFDPulseWidth selection changed to {0}".format(text))
        pass

    def on_AgndTrim_clicked(self, text):
        print("AgndTrim selection changed to {0}".format(text))
        pass

    def update_current_gui(self):
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ This is the class inheriting the Qt designer UI and adding functionality """

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.configuration_manager = configuration_helper.ConfigurationManager()
        self.current_config_path = configuration_helper.tempfile_path

        # Button Connections

        self.detectI2CDevices.clicked.connect(on_detectI2CDevices_clicked)
        self.editGlobalSettings.clicked.connect(self.on_editGlobalSettings_clicked)
        self.configureChip.clicked.connect(self.on_configureChip_clicked)
        self.pulseRST_L.clicked.connect(self.on_pulseRST_L_clicked)

        # CheckBox Connections

        self.enable_DAC_checkboxes = self.get_checkboxes(r"enableDAC_\d\d")
        self.signBit_checkboxes = self.get_checkboxes(r"signBit_\d\d")
        self.DAC_value_inputs = self.get_line_edits(r"leadingEdgeDAC_\d\d")

        self.enableDAC_05.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_10.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_all.stateChanged.connect(self.on_enableDAC_all_clicked)
        self.enableDAC_03.stateChanged.connect(self.on_enableDAC_clicked)
        self.enableDAC_00.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_06.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_02.stateChanged.connect(self.on_enableDAC_clicked)
        self.enableDAC_13.stateChanged.connect(self.on_enableDAC_clicked)
        self.enableDAC_07.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_02.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_12.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_07.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_10.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_00.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_01.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_13.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_11.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_05.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_06.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_15.stateChanged.connect(self.on_signBit_clicked)
        self.signBit_04.stateChanged.connect(self.on_signBit_clicked)
        self.signBit_14.stateChanged.connect(self.on_signBit_clicked)
        self.signBit_11.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_15.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_08.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_08.stateChanged.connect(self.on_enableDAC_clicked)
        self.enableDAC_04.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_01.stateChanged.connect(self.on_signBit_clicked)
        self.signBit_09.stateChanged.connect(self.on_signBit_clicked)
        self.signBit_03.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_14.stateChanged.connect(self.on_enableDAC_clicked)
        self.signBit_all.stateChanged.connect(self.on_signBit_all_clicked)
        self.signBit_12.stateChanged.connect(self.on_signBit_clicked)
        self.enableDAC_09.stateChanged.connect(self.on_enableDAC_clicked)

        self.negativePolarity.stateChanged.connect(self.on_negativePolarity_clicked)

        # ComboBox Connections

        self.chipNumber.currentTextChanged.connect(self.on_chipNumber_clicked)
        self.testPoint.currentTextChanged.connect(self.on_testPoint_clicked)
        self.testPointChannel.currentTextChanged.connect(self.on_testPointChannel_clicked)

        # Update GUI
        self.update_current_gui()

        # Initializing Global settings window

        self.global_settings_window = GlobalSettingsWindow(self.configuration_manager)

    def get_checkboxes(self, expression):
        """ This function returns a list of checkbox objects matching a regEx that were
        created using the QtDesigner generated UI """
        check_boxes = self.findChildren(QtWidgets.QCheckBox, QRegularExpression(expression))
        return sorted(check_boxes, key=lambda check_box: check_box.objectName())

    def get_line_edits(self, expression):
        """ This function returns a list of checkbox objects matching a regEx that were
        created using the QtDesigner generated UI """
        line_edits = self.findChildren(QtWidgets.QLineEdit, QRegularExpression(expression))
        return sorted(line_edits, key=lambda line_edit: line_edit.objectName())

    # Button slot function declarations

    def on_editGlobalSettings_clicked(self):
        print("editGlobalSettings Clicked.")
        self.global_settings_window.show()
        pass

    def on_configureChip_clicked(self):
        print("configureChip Clicked.")
        pass

    def on_pulseRST_L_clicked(self):
        print("pulseRST Clicked.")
        pass

    def on_enableDAC_all_clicked(self, state):

        print("{0} State Changed.".format("enableDAC_all"))

        for checkbox in self.enable_DAC_checkboxes:
            checkbox.setChecked(state == Qt.CheckState.Checked.value)

    def on_signBit_all_clicked(self, state):

        print("{0} State Changed.".format("signBit_all"))

        for checkbox in self.signBit_checkboxes:
            checkbox.setChecked(state == Qt.CheckState.Checked.value)

        pass

    def on_enableDAC_clicked(self, state):
        check_box = self.sender()
        print("{0} State Changed.".format(str(check_box.objectName())))

        channel = utilities.get_channel(check_box)
        key = "enable"
        value = (state == Qt.CheckState.Checked.value)

        self.configuration_manager.modify_DAC_value(channel, key, value)
        self.unset_all_checkbox(state, self.enableDAC_all)

    def on_signBit_clicked(self, state):
        check_box = self.sender()
        print("{0} State Changed.".format(str(check_box.objectName())))

        channel = utilities.get_channel(check_box)
        key = "sign_bit"
        value = (state == Qt.CheckState.Checked.value)

        self.configuration_manager.modify_DAC_value(channel, key, value)
        self.unset_all_checkbox(state, self.signBit_all)

    def on_negativePolarity_clicked(self, state):
        print("negativePolarity State Changed.")

        self.configuration_manager.current_chip_config["negative_polarity"] = str(state == Qt.CheckState.Checked.value)

        pass

    def unset_all_checkbox(self, state, checkbox_all):

        if state == Qt.CheckState.Unchecked.value:
            # This is to prevent the loop of unchecking all checkboxes
            checkbox_all.blockSignals(True)
            checkbox_all.setChecked(False)
            checkbox_all.blockSignals(False)

        pass

    # ComboBox slot function declarations

    def on_chipNumber_clicked(self, text):
        print("chipNumber selection changed to {0}".format(text))
        self.configuration_manager.set_current_chip(int(text))
        self.chipNumber_display.display(text)
        self.update_current_gui()

    def on_testPoint_clicked(self, text):
        print("testPoint selection changed to {0}".format(text))

        self.configuration_manager.current_chip_config["test_point"] = text

    def on_testPointChannel_clicked(self, text):
        print("testPointChannel selection changed to {0}".format(text))

        self.configuration_manager.current_chip_config["test_point_channel"] = text

    def update_current_gui(self):

        current_enable_values = self.configuration_manager.get_DAC_values("enable")
        current_sign_values = self.configuration_manager.get_DAC_values("sign_bit")
        current_DAC_values = self.configuration_manager.get_DAC_values("leading_edge_DAC_value")
        print(json.dumps(self.configuration_manager.current_chip_config, indent=4))
        # update checkboxes
        for index, checkbox in enumerate(self.signBit_checkboxes):
            checkbox.setChecked(current_sign_values[index])
        for index, checkbox in enumerate(self.enable_DAC_checkboxes):
            checkbox.setChecked(current_enable_values[index])

        # update DAC values
        for index, DAC_value in enumerate(self.DAC_value_inputs):
            # Setting to default hints if value is uninitialized
            if current_DAC_values[index] is None:
                DAC_value.setPlaceholderText("0x00")
            else:
                DAC_value.setText(current_DAC_values[index])

        # update test point
        self.negativePolarity.setChecked(self.configuration_manager.current_chip_config["negative_polarity"] == 'True')

        change_item_selection(self.testPoint, self.configuration_manager.current_chip_config["test_point"])
        change_item_selection(self.testPointChannel,
                              self.configuration_manager.current_chip_config["test_point_channel"])

    def closeEvent(self, event):
        """ overloads the default PyQt function to save file config on exit"""
        print("Saving the current configuration state to {0}".format(self.current_config_path))
        configuration_helper.write_config(self.current_config_path, self.configuration_manager.configuration)
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()

    w.show()

    sys.exit(app.exec())
