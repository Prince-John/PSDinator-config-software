# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cfd_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSlider, QWidget)

from chipboard_configuration_software.gui.ui_files.qt_ui_modifications import ClickableLineEdit

class Ui_DockWidget_cfd(object):
    def setupUi(self, DockWidget_cfd):
        if not DockWidget_cfd.objectName():
            DockWidget_cfd.setObjectName(u"DockWidget_cfd")
        DockWidget_cfd.resize(565, 583)
        DockWidget_cfd.setFloating(False)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 4, 0, 1, 1)

        self.cfd_pushButton = QPushButton(self.dockWidgetContents)
        self.cfd_pushButton.setObjectName(u"cfd_pushButton")

        self.gridLayout_4.addWidget(self.cfd_pushButton, 4, 2, 1, 1)

        self.line = QFrame(self.dockWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 3)

        self.groupBox_cfd_global_settings = QGroupBox(self.dockWidgetContents)
        self.groupBox_cfd_global_settings.setObjectName(u"groupBox_cfd_global_settings")
        self.groupBox_cfd_global_settings.setEnabled(True)
        self.groupBox_cfd_global_settings.setMinimumSize(QSize(241, 321))
        self.groupBox_cfd_global_settings.setFlat(True)
        self.groupBox_cfd_global_settings.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_cfd_global_settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_cfd_global_settings)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.checkBox_le_out_enable = QCheckBox(self.groupBox_cfd_global_settings)
        self.checkBox_le_out_enable.setObjectName(u"checkBox_le_out_enable")

        self.gridLayout_3.addWidget(self.checkBox_le_out_enable, 9, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_cfd_global_settings)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)

        self.comboBox_lockout_dac = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_lockout_dac.setObjectName(u"comboBox_lockout_dac")

        self.gridLayout_3.addWidget(self.comboBox_lockout_dac, 4, 1, 1, 1)

        self.checkBox_negative_polarity = QCheckBox(self.groupBox_cfd_global_settings)
        self.checkBox_negative_polarity.setObjectName(u"checkBox_negative_polarity")

        self.gridLayout_3.addWidget(self.checkBox_negative_polarity, 7, 0, 1, 1)

        self.comboBox_cfd_pulse_width = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_cfd_pulse_width.addItem("")
        self.comboBox_cfd_pulse_width.addItem("")
        self.comboBox_cfd_pulse_width.addItem("")
        self.comboBox_cfd_pulse_width.addItem("")
        self.comboBox_cfd_pulse_width.setObjectName(u"comboBox_cfd_pulse_width")

        self.gridLayout_3.addWidget(self.comboBox_cfd_pulse_width, 5, 1, 1, 1)

        self.comboBox_nowlin_delay = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_nowlin_delay.setObjectName(u"comboBox_nowlin_delay")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_nowlin_delay.sizePolicy().hasHeightForWidth())
        self.comboBox_nowlin_delay.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.comboBox_nowlin_delay, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_cfd_global_settings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_cfd_global_settings)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.comboBox_lockout_mode = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_lockout_mode.addItem("")
        self.comboBox_lockout_mode.addItem("")
        self.comboBox_lockout_mode.addItem("")
        self.comboBox_lockout_mode.setObjectName(u"comboBox_lockout_mode")
        sizePolicy1.setHeightForWidth(self.comboBox_lockout_mode.sizePolicy().hasHeightForWidth())
        self.comboBox_lockout_mode.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.comboBox_lockout_mode, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_cfd_global_settings)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.comboBox_agnd_trim = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.addItem("")
        self.comboBox_agnd_trim.setObjectName(u"comboBox_agnd_trim")

        self.gridLayout_3.addWidget(self.comboBox_agnd_trim, 6, 1, 1, 1)

        self.checkBox_cfd_global_enable = QCheckBox(self.groupBox_cfd_global_settings)
        self.checkBox_cfd_global_enable.setObjectName(u"checkBox_cfd_global_enable")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.checkBox_cfd_global_enable.setFont(font)

        self.gridLayout_3.addWidget(self.checkBox_cfd_global_enable, 0, 0, 1, 2)

        self.comboBox_nowlin_mode = QComboBox(self.groupBox_cfd_global_settings)
        self.comboBox_nowlin_mode.addItem("")
        self.comboBox_nowlin_mode.addItem("")
        self.comboBox_nowlin_mode.setObjectName(u"comboBox_nowlin_mode")
        sizePolicy1.setHeightForWidth(self.comboBox_nowlin_mode.sizePolicy().hasHeightForWidth())
        self.comboBox_nowlin_mode.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.comboBox_nowlin_mode, 1, 1, 1, 1)

        self.checkBox_global_mode = QCheckBox(self.groupBox_cfd_global_settings)
        self.checkBox_global_mode.setObjectName(u"checkBox_global_mode")

        self.gridLayout_3.addWidget(self.checkBox_global_mode, 7, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_cfd_global_settings)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_cfd_global_settings, 0, 0, 1, 1)

        self.pushButton_cfd_reset_gui = QPushButton(self.dockWidgetContents)
        self.pushButton_cfd_reset_gui.setObjectName(u"pushButton_cfd_reset_gui")

        self.gridLayout_4.addWidget(self.pushButton_cfd_reset_gui, 4, 1, 1, 1)

        self.groupBox_test_cfd = QGroupBox(self.dockWidgetContents)
        self.groupBox_test_cfd.setObjectName(u"groupBox_test_cfd")
        self.groupBox_test_cfd.setMinimumSize(QSize(283, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox_test_cfd)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_test_cfd)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 2)

        self.comboBox_cfd_test_point = QComboBox(self.groupBox_test_cfd)
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.addItem("")
        self.comboBox_cfd_test_point.setObjectName(u"comboBox_cfd_test_point")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_cfd_test_point.sizePolicy().hasHeightForWidth())
        self.comboBox_cfd_test_point.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.comboBox_cfd_test_point, 0, 1, 1, 2)

        self.comboBox_cfd_test_point_channel = QComboBox(self.groupBox_test_cfd)
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.addItem("")
        self.comboBox_cfd_test_point_channel.setObjectName(u"comboBox_cfd_test_point_channel")

        self.gridLayout_2.addWidget(self.comboBox_cfd_test_point_channel, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_test_cfd)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_test_cfd, 1, 0, 1, 1)

        self.verticalGroupBox = QGroupBox(self.dockWidgetContents)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMinimumSize(QSize(240, 0))
        self.verticalGroupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalGroupBox.setFlat(False)
        self.verticalGroupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.verticalGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.lineEdit_cfd_le_dac_2 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_2.setObjectName(u"lineEdit_cfd_le_dac_2")
        self.lineEdit_cfd_le_dac_2.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_2, 4, 2, 1, 1, Qt.AlignHCenter)

        self.label_34 = QLabel(self.verticalGroupBox)
        self.label_34.setObjectName(u"label_34")
        font1 = QFont()
        font1.setBold(True)
        self.label_34.setFont(font1)

        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 2, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_8_15 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_8_15.setObjectName(u"checkBox_cfd_channel_enable_8_15")
        self.checkBox_cfd_channel_enable_8_15.setMaximumSize(QSize(68, 16777215))

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_8_15, 10, 0, 1, 1)

        self.checkBox_cfd_channel_enable_0_7 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_0_7.setObjectName(u"checkBox_cfd_channel_enable_0_7")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_0_7, 2, 0, 1, 1)

        self.lineEdit_cfd_le_dac_3 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_3.setObjectName(u"lineEdit_cfd_le_dac_3")
        self.lineEdit_cfd_le_dac_3.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_3, 5, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_all = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_all.setObjectName(u"checkBox_cfd_channel_enable_all")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_all, 1, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_12 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_12.setObjectName(u"lineEdit_cfd_le_dac_12")
        self.lineEdit_cfd_le_dac_12.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_12, 14, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_15 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_15.setObjectName(u"lineEdit_cfd_le_dac_15")
        self.lineEdit_cfd_le_dac_15.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_15, 17, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_4 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_4.setObjectName(u"lineEdit_cfd_le_dac_4")
        self.lineEdit_cfd_le_dac_4.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_4, 6, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_5 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_5.setObjectName(u"lineEdit_cfd_le_dac_5")
        self.lineEdit_cfd_le_dac_5.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_5, 7, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_4 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_4.setObjectName(u"checkBox_cfd_channel_enable_4")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_4, 6, 1, 1, 1)

        self.verticalSlider_cfd_leading_edge_dac_value = QSlider(self.verticalGroupBox)
        self.verticalSlider_cfd_leading_edge_dac_value.setObjectName(u"verticalSlider_cfd_leading_edge_dac_value")
        self.verticalSlider_cfd_leading_edge_dac_value.setMinimum(-31)
        self.verticalSlider_cfd_leading_edge_dac_value.setMaximum(31)
        self.verticalSlider_cfd_leading_edge_dac_value.setOrientation(Qt.Vertical)
        self.verticalSlider_cfd_leading_edge_dac_value.setInvertedControls(False)
        self.verticalSlider_cfd_leading_edge_dac_value.setTickPosition(QSlider.TicksBelow)
        self.verticalSlider_cfd_leading_edge_dac_value.setTickInterval(4)

        self.gridLayout.addWidget(self.verticalSlider_cfd_leading_edge_dac_value, 3, 3, 14, 1)

        self.checkBox_cfd_channel_enable_14 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_14.setObjectName(u"checkBox_cfd_channel_enable_14")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_14, 16, 1, 1, 1)

        self.checkBox_cfd_channel_enable_6 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_6.setObjectName(u"checkBox_cfd_channel_enable_6")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_6, 8, 1, 1, 1)

        self.checkBox_cfd_channel_enable_8 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_8.setObjectName(u"checkBox_cfd_channel_enable_8")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_8, 10, 1, 1, 1)

        self.lineEdit_cfd_le_dac_11 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_11.setObjectName(u"lineEdit_cfd_le_dac_11")
        self.lineEdit_cfd_le_dac_11.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_11, 13, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_10 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_10.setObjectName(u"lineEdit_cfd_le_dac_10")
        self.lineEdit_cfd_le_dac_10.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_10, 12, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_13 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_13.setObjectName(u"checkBox_cfd_channel_enable_13")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_13, 15, 1, 1, 1)

        self.checkBox_cfd_channel_enable_2 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_2.setObjectName(u"checkBox_cfd_channel_enable_2")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_2, 4, 1, 1, 1)

        self.label_35 = QLabel(self.verticalGroupBox)
        self.label_35.setObjectName(u"label_35")
        sizePolicy2.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy2)
        self.label_35.setFont(font1)
        self.label_35.setWordWrap(False)

        self.gridLayout.addWidget(self.label_35, 0, 2, 1, 2)

        self.checkBox_cfd_channel_enable_15 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_15.setObjectName(u"checkBox_cfd_channel_enable_15")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_15, 17, 1, 1, 1)

        self.lineEdit_cfd_le_dac_1 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_1.setObjectName(u"lineEdit_cfd_le_dac_1")
        self.lineEdit_cfd_le_dac_1.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_1, 3, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_9 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_9.setObjectName(u"lineEdit_cfd_le_dac_9")
        self.lineEdit_cfd_le_dac_9.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_9, 11, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_9 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_9.setObjectName(u"checkBox_cfd_channel_enable_9")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_9, 11, 1, 1, 1)

        self.lineEdit_cfd_le_dac_0 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_0.setObjectName(u"lineEdit_cfd_le_dac_0")
        self.lineEdit_cfd_le_dac_0.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_0, 2, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_11 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_11.setObjectName(u"checkBox_cfd_channel_enable_11")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_11, 13, 1, 1, 1)

        self.checkBox_cfd_channel_enable_3 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_3.setObjectName(u"checkBox_cfd_channel_enable_3")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_3, 5, 1, 1, 1)

        self.lineEdit_cfd_le_dac_8 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_8.setObjectName(u"lineEdit_cfd_le_dac_8")
        self.lineEdit_cfd_le_dac_8.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_8, 10, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_12 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_12.setObjectName(u"checkBox_cfd_channel_enable_12")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_12, 14, 1, 1, 1)

        self.checkBox_cfd_channel_enable_0 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_0.setObjectName(u"checkBox_cfd_channel_enable_0")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_0, 2, 1, 1, 1)

        self.checkBox_cfd_channel_enable_7 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_7.setObjectName(u"checkBox_cfd_channel_enable_7")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_7, 9, 1, 1, 1)

        self.checkBox_cfd_channel_enable_10 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_10.setObjectName(u"checkBox_cfd_channel_enable_10")
        self.checkBox_cfd_channel_enable_10.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_10, 12, 1, 1, 1)

        self.lineEdit_cfd_le_dac_6 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_6.setObjectName(u"lineEdit_cfd_le_dac_6")
        self.lineEdit_cfd_le_dac_6.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_6, 8, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_14 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_14.setObjectName(u"lineEdit_cfd_le_dac_14")
        self.lineEdit_cfd_le_dac_14.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_14, 16, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_cfd_le_dac_7 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_7.setObjectName(u"lineEdit_cfd_le_dac_7")
        self.lineEdit_cfd_le_dac_7.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_7, 9, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_1 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_1.setObjectName(u"checkBox_cfd_channel_enable_1")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_1, 3, 1, 1, 1)

        self.lineEdit_cfd_le_dac_13 = ClickableLineEdit(self.verticalGroupBox)
        self.lineEdit_cfd_le_dac_13.setObjectName(u"lineEdit_cfd_le_dac_13")
        self.lineEdit_cfd_le_dac_13.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_cfd_le_dac_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cfd_le_dac_13, 15, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_cfd_channel_enable_5 = QCheckBox(self.verticalGroupBox)
        self.checkBox_cfd_channel_enable_5.setObjectName(u"checkBox_cfd_channel_enable_5")

        self.gridLayout.addWidget(self.checkBox_cfd_channel_enable_5, 7, 1, 1, 1)


        self.gridLayout_4.addWidget(self.verticalGroupBox, 0, 1, 2, 3)

        DockWidget_cfd.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_cfd)

        QMetaObject.connectSlotsByName(DockWidget_cfd)
    # setupUi

    def retranslateUi(self, DockWidget_cfd):
        DockWidget_cfd.setWindowTitle(QCoreApplication.translate("DockWidget_cfd", u"CFD Settings", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget_cfd", u"Configure CFD", None))
        self.cfd_pushButton.setText(QCoreApplication.translate("DockWidget_cfd", u"Reset CFD", None))
        self.groupBox_cfd_global_settings.setTitle(QCoreApplication.translate("DockWidget_cfd", u"CFD Global Settings", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget_cfd", u"Nowlin Mode", None))
        self.checkBox_le_out_enable.setText(QCoreApplication.translate("DockWidget_cfd", u"LE Out Enable", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget_cfd", u"AGND Trim", None))
        self.checkBox_negative_polarity.setText(QCoreApplication.translate("DockWidget_cfd", u"Negative Polarity", None))
        self.comboBox_cfd_pulse_width.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"50", None))
        self.comboBox_cfd_pulse_width.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"100", None))
        self.comboBox_cfd_pulse_width.setItemText(2, QCoreApplication.translate("DockWidget_cfd", u"200", None))
        self.comboBox_cfd_pulse_width.setItemText(3, QCoreApplication.translate("DockWidget_cfd", u"500", None))

        self.label_6.setText(QCoreApplication.translate("DockWidget_cfd", u"Lockout DAC", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget_cfd", u"Lockout Mode", None))
        self.comboBox_lockout_mode.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"Short", None))
        self.comboBox_lockout_mode.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"Long", None))
        self.comboBox_lockout_mode.setItemText(2, QCoreApplication.translate("DockWidget_cfd", u"Disabled", None))

        self.label_9.setText(QCoreApplication.translate("DockWidget_cfd", u"CFD Pulse Width", None))
        self.comboBox_agnd_trim.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"1.36 V", None))
        self.comboBox_agnd_trim.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"1.43 V", None))
        self.comboBox_agnd_trim.setItemText(2, QCoreApplication.translate("DockWidget_cfd", u"1.49 V", None))
        self.comboBox_agnd_trim.setItemText(3, QCoreApplication.translate("DockWidget_cfd", u"1.56 V", None))
        self.comboBox_agnd_trim.setItemText(4, QCoreApplication.translate("DockWidget_cfd", u"1.63 V", None))
        self.comboBox_agnd_trim.setItemText(5, QCoreApplication.translate("DockWidget_cfd", u"1.69 V", None))
        self.comboBox_agnd_trim.setItemText(6, QCoreApplication.translate("DockWidget_cfd", u"1.77 V", None))
        self.comboBox_agnd_trim.setItemText(7, QCoreApplication.translate("DockWidget_cfd", u"1.84 V", None))

        self.checkBox_cfd_global_enable.setText(QCoreApplication.translate("DockWidget_cfd", u"CFD Global Enable", None))
        self.comboBox_nowlin_mode.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"Short", None))
        self.comboBox_nowlin_mode.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"Long", None))

        self.checkBox_global_mode.setText(QCoreApplication.translate("DockWidget_cfd", u"Global Mode", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget_cfd", u"Nowlin Delay (ns)", None))
        self.pushButton_cfd_reset_gui.setText(QCoreApplication.translate("DockWidget_cfd", u"Reset CFD GUI", None))
        self.groupBox_test_cfd.setTitle(QCoreApplication.translate("DockWidget_cfd", u"CFD Test Settings", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget_cfd", u"Test Point Channel", None))
        self.comboBox_cfd_test_point.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"AVSS", None))
        self.comboBox_cfd_test_point.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"lockout pulse", None))
        self.comboBox_cfd_test_point.setItemText(2, QCoreApplication.translate("DockWidget_cfd", u"leading edge detector pulse", None))
        self.comboBox_cfd_test_point.setItemText(3, QCoreApplication.translate("DockWidget_cfd", u"zero crossing detector pulse", None))
        self.comboBox_cfd_test_point.setItemText(4, QCoreApplication.translate("DockWidget_cfd", u"oneshot input", None))
        self.comboBox_cfd_test_point.setItemText(5, QCoreApplication.translate("DockWidget_cfd", u"oneshot pulse", None))

        self.comboBox_cfd_test_point_channel.setItemText(0, QCoreApplication.translate("DockWidget_cfd", u"0", None))
        self.comboBox_cfd_test_point_channel.setItemText(1, QCoreApplication.translate("DockWidget_cfd", u"1", None))
        self.comboBox_cfd_test_point_channel.setItemText(2, QCoreApplication.translate("DockWidget_cfd", u"2", None))
        self.comboBox_cfd_test_point_channel.setItemText(3, QCoreApplication.translate("DockWidget_cfd", u"3", None))
        self.comboBox_cfd_test_point_channel.setItemText(4, QCoreApplication.translate("DockWidget_cfd", u"4", None))
        self.comboBox_cfd_test_point_channel.setItemText(5, QCoreApplication.translate("DockWidget_cfd", u"5", None))
        self.comboBox_cfd_test_point_channel.setItemText(6, QCoreApplication.translate("DockWidget_cfd", u"6", None))
        self.comboBox_cfd_test_point_channel.setItemText(7, QCoreApplication.translate("DockWidget_cfd", u"7", None))
        self.comboBox_cfd_test_point_channel.setItemText(8, QCoreApplication.translate("DockWidget_cfd", u"8", None))
        self.comboBox_cfd_test_point_channel.setItemText(9, QCoreApplication.translate("DockWidget_cfd", u"9", None))
        self.comboBox_cfd_test_point_channel.setItemText(10, QCoreApplication.translate("DockWidget_cfd", u"10", None))
        self.comboBox_cfd_test_point_channel.setItemText(11, QCoreApplication.translate("DockWidget_cfd", u"11", None))
        self.comboBox_cfd_test_point_channel.setItemText(12, QCoreApplication.translate("DockWidget_cfd", u"12", None))
        self.comboBox_cfd_test_point_channel.setItemText(13, QCoreApplication.translate("DockWidget_cfd", u"13", None))
        self.comboBox_cfd_test_point_channel.setItemText(14, QCoreApplication.translate("DockWidget_cfd", u"14", None))
        self.comboBox_cfd_test_point_channel.setItemText(15, QCoreApplication.translate("DockWidget_cfd", u"15", None))

        self.label_2.setText(QCoreApplication.translate("DockWidget_cfd", u"Test Point", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("DockWidget_cfd", u"Channel Enable ", None))
        self.label_34.setText(QCoreApplication.translate("DockWidget_cfd", u"Enable", None))
        self.checkBox_cfd_channel_enable_8_15.setText(QCoreApplication.translate("DockWidget_cfd", u"8-15", None))
        self.checkBox_cfd_channel_enable_0_7.setText(QCoreApplication.translate("DockWidget_cfd", u"0-7", None))
        self.checkBox_cfd_channel_enable_all.setText(QCoreApplication.translate("DockWidget_cfd", u"All", None))
        self.checkBox_cfd_channel_enable_4.setText(QCoreApplication.translate("DockWidget_cfd", u"4", None))
        self.checkBox_cfd_channel_enable_14.setText(QCoreApplication.translate("DockWidget_cfd", u"14", None))
        self.checkBox_cfd_channel_enable_6.setText(QCoreApplication.translate("DockWidget_cfd", u"6", None))
        self.checkBox_cfd_channel_enable_8.setText(QCoreApplication.translate("DockWidget_cfd", u"8", None))
        self.checkBox_cfd_channel_enable_13.setText(QCoreApplication.translate("DockWidget_cfd", u"13", None))
        self.checkBox_cfd_channel_enable_2.setText(QCoreApplication.translate("DockWidget_cfd", u"2", None))
        self.label_35.setText(QCoreApplication.translate("DockWidget_cfd", u"Leading Edge DAC", None))
        self.checkBox_cfd_channel_enable_15.setText(QCoreApplication.translate("DockWidget_cfd", u"15", None))
        self.checkBox_cfd_channel_enable_9.setText(QCoreApplication.translate("DockWidget_cfd", u"9", None))
        self.checkBox_cfd_channel_enable_11.setText(QCoreApplication.translate("DockWidget_cfd", u"11", None))
        self.checkBox_cfd_channel_enable_3.setText(QCoreApplication.translate("DockWidget_cfd", u"3", None))
        self.checkBox_cfd_channel_enable_12.setText(QCoreApplication.translate("DockWidget_cfd", u"12", None))
        self.checkBox_cfd_channel_enable_0.setText(QCoreApplication.translate("DockWidget_cfd", u"0", None))
        self.checkBox_cfd_channel_enable_7.setText(QCoreApplication.translate("DockWidget_cfd", u"7", None))
        self.checkBox_cfd_channel_enable_10.setText(QCoreApplication.translate("DockWidget_cfd", u"10", None))
        self.checkBox_cfd_channel_enable_1.setText(QCoreApplication.translate("DockWidget_cfd", u"1", None))
        self.checkBox_cfd_channel_enable_5.setText(QCoreApplication.translate("DockWidget_cfd", u"5", None))
    # retranslateUi

