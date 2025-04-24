# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainConfigWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1105, 993)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionload = QAction(MainWindow)
        self.actionload.setObjectName(u"actionload")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSavs_As = QAction(MainWindow)
        self.actionSavs_As.setObjectName(u"actionSavs_As")
        self.actionGithub_Repository = QAction(MainWindow)
        self.actionGithub_Repository.setObjectName(u"actionGithub_Repository")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_chipboard_selection = QHBoxLayout()
        self.horizontalLayout_chipboard_selection.setObjectName(u"horizontalLayout_chipboard_selection")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.PlainText)

        self.horizontalLayout_chipboard_selection.addWidget(self.label)

        self.chipNumber_display = QLCDNumber(self.centralwidget)
        self.chipNumber_display.setObjectName(u"chipNumber_display")
        self.chipNumber_display.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chipNumber_display.sizePolicy().hasHeightForWidth())
        self.chipNumber_display.setSizePolicy(sizePolicy2)
        self.chipNumber_display.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(22)
        self.chipNumber_display.setFont(font)
        self.chipNumber_display.setLayoutDirection(Qt.LeftToRight)
        self.chipNumber_display.setAutoFillBackground(False)
        self.chipNumber_display.setLineWidth(1)
        self.chipNumber_display.setSmallDecimalPoint(False)
        self.chipNumber_display.setDigitCount(2)
        self.chipNumber_display.setMode(QLCDNumber.Hex)
        self.chipNumber_display.setSegmentStyle(QLCDNumber.Outline)
        self.chipNumber_display.setProperty("value", 0.000000000000000)

        self.horizontalLayout_chipboard_selection.addWidget(self.chipNumber_display)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.chipNumber = QComboBox(self.centralwidget)
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.addItem("")
        self.chipNumber.setObjectName(u"chipNumber")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.chipNumber.sizePolicy().hasHeightForWidth())
        self.chipNumber.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.chipNumber)


        self.horizontalLayout_chipboard_selection.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_chipboard_selection)

        self.tabWidgets = QTabWidget(self.centralwidget)
        self.tabWidgets.setObjectName(u"tabWidgets")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidgets.sizePolicy().hasHeightForWidth())
        self.tabWidgets.setSizePolicy(sizePolicy5)
        self.tabWidgets.setTabPosition(QTabWidget.North)
        self.tabWidgets.setTabShape(QTabWidget.Rounded)
        self.tabWidgets.setElideMode(Qt.ElideLeft)
        self.tabWidgets.setMovable(True)
        self.cfd_tab = QWidget()
        self.cfd_tab.setObjectName(u"cfd_tab")
        self.gridLayout_6 = QGridLayout(self.cfd_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_cfd_global_settings = QGroupBox(self.cfd_tab)
        self.groupBox_cfd_global_settings.setObjectName(u"groupBox_cfd_global_settings")
        self.groupBox_cfd_global_settings.setEnabled(True)
        self.groupBox_cfd_global_settings.setMinimumSize(QSize(241, 321))
        self.groupBox_cfd_global_settings.setFlat(False)
        self.groupBox_cfd_global_settings.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_cfd_global_settings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_cfd_global_settings)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.nowlinMode = QComboBox(self.groupBox_cfd_global_settings)
        self.nowlinMode.addItem("")
        self.nowlinMode.addItem("")
        self.nowlinMode.setObjectName(u"nowlinMode")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.nowlinMode.sizePolicy().hasHeightForWidth())
        self.nowlinMode.setSizePolicy(sizePolicy7)

        self.horizontalLayout_3.addWidget(self.nowlinMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_cfd_global_settings)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.nowlinDelay = QComboBox(self.groupBox_cfd_global_settings)
        self.nowlinDelay.addItem("")
        self.nowlinDelay.addItem("")
        self.nowlinDelay.setObjectName(u"nowlinDelay")
        sizePolicy7.setHeightForWidth(self.nowlinDelay.sizePolicy().hasHeightForWidth())
        self.nowlinDelay.setSizePolicy(sizePolicy7)

        self.horizontalLayout_4.addWidget(self.nowlinDelay)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_cfd_global_settings)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.LockoutDAC = QLineEdit(self.groupBox_cfd_global_settings)
        self.LockoutDAC.setObjectName(u"LockoutDAC")
        sizePolicy7.setHeightForWidth(self.LockoutDAC.sizePolicy().hasHeightForWidth())
        self.LockoutDAC.setSizePolicy(sizePolicy7)

        self.horizontalLayout_6.addWidget(self.LockoutDAC)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.groupBox_cfd_global_settings)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lockoutMode = QComboBox(self.groupBox_cfd_global_settings)
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.setObjectName(u"lockoutMode")
        sizePolicy7.setHeightForWidth(self.lockoutMode.sizePolicy().hasHeightForWidth())
        self.lockoutMode.setSizePolicy(sizePolicy7)

        self.horizontalLayout_7.addWidget(self.lockoutMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.groupBox_cfd_global_settings)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.CFDPulseWidth = QComboBox(self.groupBox_cfd_global_settings)
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.setObjectName(u"CFDPulseWidth")

        self.horizontalLayout_8.addWidget(self.CFDPulseWidth)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.groupBox_cfd_global_settings)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.AgndTrim = QComboBox(self.groupBox_cfd_global_settings)
        self.AgndTrim.addItem("")
        self.AgndTrim.setObjectName(u"AgndTrim")

        self.horizontalLayout_9.addWidget(self.AgndTrim)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.negativePolarity = QCheckBox(self.groupBox_cfd_global_settings)
        self.negativePolarity.setObjectName(u"negativePolarity")

        self.verticalLayout_2.addWidget(self.negativePolarity)

        self.globalMode = QCheckBox(self.groupBox_cfd_global_settings)
        self.globalMode.setObjectName(u"globalMode")

        self.verticalLayout_2.addWidget(self.globalMode)

        self.LEOutEnable = QCheckBox(self.groupBox_cfd_global_settings)
        self.LEOutEnable.setObjectName(u"LEOutEnable")

        self.verticalLayout_2.addWidget(self.LEOutEnable)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.globalEnable = QCheckBox(self.groupBox_cfd_global_settings)
        self.globalEnable.setObjectName(u"globalEnable")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.globalEnable.setFont(font1)

        self.gridLayout_4.addWidget(self.globalEnable, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_cfd_global_settings, 0, 0, 1, 2)

        self.groupBox_cfd_individual_ch_settings = QGroupBox(self.cfd_tab)
        self.groupBox_cfd_individual_ch_settings.setObjectName(u"groupBox_cfd_individual_ch_settings")
        self.groupBox_cfd_individual_ch_settings.setMinimumSize(QSize(421, 371))
        self.gridLayout_5 = QGridLayout(self.groupBox_cfd_individual_ch_settings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.leadingEdgeDAC_15 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_15.setObjectName(u"leadingEdgeDAC_15")
        self.leadingEdgeDAC_15.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_15.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_15.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_15, 16, 1, 1, 1)

        self.signBit_13 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_13.setObjectName(u"signBit_13")
        sizePolicy7.setHeightForWidth(self.signBit_13.sizePolicy().hasHeightForWidth())
        self.signBit_13.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_13, 14, 3, 1, 1)

        self.enableDAC_01 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_01.setObjectName(u"enableDAC_01")
        sizePolicy7.setHeightForWidth(self.enableDAC_01.sizePolicy().hasHeightForWidth())
        self.enableDAC_01.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_01, 2, 2, 1, 1)

        self.leadingEdgeDAC_13 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_13.setObjectName(u"leadingEdgeDAC_13")
        self.leadingEdgeDAC_13.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_13.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_13.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_13, 14, 1, 1, 1)

        self.leadingEdgeDAC_14 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_14.setObjectName(u"leadingEdgeDAC_14")
        self.leadingEdgeDAC_14.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_14.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_14.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_14, 15, 1, 1, 1)

        self.enableDAC_08 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_08.setObjectName(u"enableDAC_08")
        sizePolicy7.setHeightForWidth(self.enableDAC_08.sizePolicy().hasHeightForWidth())
        self.enableDAC_08.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_08, 9, 2, 1, 1)

        self.label_channel_header = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_channel_header.setObjectName(u"label_channel_header")

        self.gridLayout_2.addWidget(self.label_channel_header, 0, 0, 1, 1)

        self.signBit_all = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_all.setObjectName(u"signBit_all")

        self.gridLayout_2.addWidget(self.signBit_all, 0, 3, 1, 1)

        self.label_leading_edge_dac_header = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_leading_edge_dac_header.setObjectName(u"label_leading_edge_dac_header")

        self.gridLayout_2.addWidget(self.label_leading_edge_dac_header, 0, 1, 1, 1)

        self.leadingEdgeDAC_05 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_05.setObjectName(u"leadingEdgeDAC_05")
        self.leadingEdgeDAC_05.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_05.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_05.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_05, 6, 1, 1, 1)

        self.enableDAC_05 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_05.setObjectName(u"enableDAC_05")
        sizePolicy7.setHeightForWidth(self.enableDAC_05.sizePolicy().hasHeightForWidth())
        self.enableDAC_05.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_05, 6, 2, 1, 1)

        self.enableDAC_02 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_02.setObjectName(u"enableDAC_02")
        sizePolicy7.setHeightForWidth(self.enableDAC_02.sizePolicy().hasHeightForWidth())
        self.enableDAC_02.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_02, 3, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 12, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 15, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)

        self.enableDAC_10 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_10.setObjectName(u"enableDAC_10")
        sizePolicy7.setHeightForWidth(self.enableDAC_10.sizePolicy().hasHeightForWidth())
        self.enableDAC_10.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_10, 11, 2, 1, 1)

        self.signBit_02 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_02.setObjectName(u"signBit_02")
        sizePolicy7.setHeightForWidth(self.signBit_02.sizePolicy().hasHeightForWidth())
        self.signBit_02.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_02, 3, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 14, 0, 1, 1)

        self.leadingEdgeDAC_09 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_09.setObjectName(u"leadingEdgeDAC_09")
        self.leadingEdgeDAC_09.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_09.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_09.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_09, 10, 1, 1, 1)

        self.signBit_06 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_06.setObjectName(u"signBit_06")
        sizePolicy7.setHeightForWidth(self.signBit_06.sizePolicy().hasHeightForWidth())
        self.signBit_06.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_06, 7, 3, 1, 1)

        self.enableDAC_04 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_04.setObjectName(u"enableDAC_04")
        sizePolicy7.setHeightForWidth(self.enableDAC_04.sizePolicy().hasHeightForWidth())
        self.enableDAC_04.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_04, 5, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.leadingEdgeDAC_02 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_02.setObjectName(u"leadingEdgeDAC_02")
        self.leadingEdgeDAC_02.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_02.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_02.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_02, 3, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_2.addWidget(self.label_48, 11, 0, 1, 1)

        self.signBit_11 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_11.setObjectName(u"signBit_11")
        sizePolicy7.setHeightForWidth(self.signBit_11.sizePolicy().hasHeightForWidth())
        self.signBit_11.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_11, 12, 3, 1, 1)

        self.label_42 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 4, 0, 1, 1)

        self.enableDAC_00 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_00.setObjectName(u"enableDAC_00")
        sizePolicy7.setHeightForWidth(self.enableDAC_00.sizePolicy().hasHeightForWidth())
        self.enableDAC_00.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_00, 1, 2, 1, 1)

        self.signBit_09 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_09.setObjectName(u"signBit_09")
        sizePolicy7.setHeightForWidth(self.signBit_09.sizePolicy().hasHeightForWidth())
        self.signBit_09.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_09, 10, 3, 1, 1)

        self.signBit_01 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_01.setObjectName(u"signBit_01")
        sizePolicy7.setHeightForWidth(self.signBit_01.sizePolicy().hasHeightForWidth())
        self.signBit_01.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_01, 2, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.signBit_10 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_10.setObjectName(u"signBit_10")
        sizePolicy7.setHeightForWidth(self.signBit_10.sizePolicy().hasHeightForWidth())
        self.signBit_10.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_10, 11, 3, 1, 1)

        self.enableDAC_12 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_12.setObjectName(u"enableDAC_12")
        sizePolicy7.setHeightForWidth(self.enableDAC_12.sizePolicy().hasHeightForWidth())
        self.enableDAC_12.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_12, 13, 2, 1, 1)

        self.enableDAC_15 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_15.setObjectName(u"enableDAC_15")
        sizePolicy7.setHeightForWidth(self.enableDAC_15.sizePolicy().hasHeightForWidth())
        self.enableDAC_15.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_15, 16, 2, 1, 1)

        self.signBit_00 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_00.setObjectName(u"signBit_00")
        sizePolicy7.setHeightForWidth(self.signBit_00.sizePolicy().hasHeightForWidth())
        self.signBit_00.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_00, 1, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 16, 0, 1, 1)

        self.signBit_08 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_08.setObjectName(u"signBit_08")
        sizePolicy7.setHeightForWidth(self.signBit_08.sizePolicy().hasHeightForWidth())
        self.signBit_08.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_08, 9, 3, 1, 1)

        self.enableDAC_all = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_all.setObjectName(u"enableDAC_all")

        self.gridLayout_2.addWidget(self.enableDAC_all, 0, 2, 1, 1)

        self.label_54 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_2.addWidget(self.label_54, 7, 0, 1, 1)

        self.label_40 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 13, 0, 1, 1)

        self.enableDAC_11 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_11.setObjectName(u"enableDAC_11")
        sizePolicy7.setHeightForWidth(self.enableDAC_11.sizePolicy().hasHeightForWidth())
        self.enableDAC_11.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_11, 12, 2, 1, 1)

        self.signBit_15 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_15.setObjectName(u"signBit_15")
        sizePolicy7.setHeightForWidth(self.signBit_15.sizePolicy().hasHeightForWidth())
        self.signBit_15.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_15, 16, 3, 1, 1)

        self.enableDAC_13 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_13.setObjectName(u"enableDAC_13")
        sizePolicy7.setHeightForWidth(self.enableDAC_13.sizePolicy().hasHeightForWidth())
        self.enableDAC_13.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_13, 14, 2, 1, 1)

        self.enableDAC_07 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_07.setObjectName(u"enableDAC_07")
        sizePolicy7.setHeightForWidth(self.enableDAC_07.sizePolicy().hasHeightForWidth())
        self.enableDAC_07.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_07, 8, 2, 1, 1)

        self.enableDAC_09 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_09.setObjectName(u"enableDAC_09")
        sizePolicy7.setHeightForWidth(self.enableDAC_09.sizePolicy().hasHeightForWidth())
        self.enableDAC_09.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_09, 10, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 10, 0, 1, 1)

        self.label_50 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_2.addWidget(self.label_50, 6, 0, 1, 1)

        self.leadingEdgeDAC_11 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_11.setObjectName(u"leadingEdgeDAC_11")
        self.leadingEdgeDAC_11.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_11.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_11.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_11, 12, 1, 1, 1)

        self.signBit_07 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_07.setObjectName(u"signBit_07")
        sizePolicy7.setHeightForWidth(self.signBit_07.sizePolicy().hasHeightForWidth())
        self.signBit_07.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_07, 8, 3, 1, 1)

        self.leadingEdgeDAC_06 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_06.setObjectName(u"leadingEdgeDAC_06")
        self.leadingEdgeDAC_06.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_06.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_06.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_06, 7, 1, 1, 1)

        self.signBit_04 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_04.setObjectName(u"signBit_04")
        sizePolicy7.setHeightForWidth(self.signBit_04.sizePolicy().hasHeightForWidth())
        self.signBit_04.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_04, 5, 3, 1, 1)

        self.leadingEdgeDAC_07 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_07.setObjectName(u"leadingEdgeDAC_07")
        self.leadingEdgeDAC_07.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_07.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_07.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_07, 8, 1, 1, 1)

        self.enableDAC_03 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_03.setObjectName(u"enableDAC_03")
        sizePolicy7.setHeightForWidth(self.enableDAC_03.sizePolicy().hasHeightForWidth())
        self.enableDAC_03.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_03, 4, 2, 1, 1)

        self.label_44 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_2.addWidget(self.label_44, 9, 0, 1, 1)

        self.leadingEdgeDAC_01 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_01.setObjectName(u"leadingEdgeDAC_01")
        self.leadingEdgeDAC_01.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_01.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_01.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_01, 2, 1, 1, 1)

        self.signBit_05 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_05.setObjectName(u"signBit_05")

        self.gridLayout_2.addWidget(self.signBit_05, 6, 3, 1, 1)

        self.leadingEdgeDAC_12 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_12.setObjectName(u"leadingEdgeDAC_12")
        self.leadingEdgeDAC_12.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_12.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_12.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_12, 13, 1, 1, 1)

        self.signBit_14 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_14.setObjectName(u"signBit_14")
        sizePolicy7.setHeightForWidth(self.signBit_14.sizePolicy().hasHeightForWidth())
        self.signBit_14.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_14, 15, 3, 1, 1)

        self.enableDAC_06 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_06.setObjectName(u"enableDAC_06")
        sizePolicy7.setHeightForWidth(self.enableDAC_06.sizePolicy().hasHeightForWidth())
        self.enableDAC_06.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_06, 7, 2, 1, 1)

        self.leadingEdgeDAC_03 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_03.setObjectName(u"leadingEdgeDAC_03")
        self.leadingEdgeDAC_03.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_03.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_03.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_03, 4, 1, 1, 1)

        self.enableDAC_14 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.enableDAC_14.setObjectName(u"enableDAC_14")
        sizePolicy7.setHeightForWidth(self.enableDAC_14.sizePolicy().hasHeightForWidth())
        self.enableDAC_14.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.enableDAC_14, 15, 2, 1, 1)

        self.leadingEdgeDAC_00 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_00.setObjectName(u"leadingEdgeDAC_00")
        self.leadingEdgeDAC_00.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_00.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_00.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_00, 1, 1, 1, 1)

        self.signBit_03 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_03.setObjectName(u"signBit_03")
        sizePolicy7.setHeightForWidth(self.signBit_03.sizePolicy().hasHeightForWidth())
        self.signBit_03.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_03, 4, 3, 1, 1)

        self.leadingEdgeDAC_04 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_04.setObjectName(u"leadingEdgeDAC_04")
        self.leadingEdgeDAC_04.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_04.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_04.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_04, 5, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 8, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox_cfd_individual_ch_settings)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_2.addWidget(self.label_52, 2, 0, 1, 1)

        self.signBit_12 = QCheckBox(self.groupBox_cfd_individual_ch_settings)
        self.signBit_12.setObjectName(u"signBit_12")
        sizePolicy7.setHeightForWidth(self.signBit_12.sizePolicy().hasHeightForWidth())
        self.signBit_12.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.signBit_12, 13, 3, 1, 1)

        self.leadingEdgeDAC_08 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_08.setObjectName(u"leadingEdgeDAC_08")
        self.leadingEdgeDAC_08.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_08.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_08.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_08, 9, 1, 1, 1)

        self.leadingEdgeDAC_10 = QLineEdit(self.groupBox_cfd_individual_ch_settings)
        self.leadingEdgeDAC_10.setObjectName(u"leadingEdgeDAC_10")
        self.leadingEdgeDAC_10.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_10.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_10.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_10, 11, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_cfd_individual_ch_settings, 0, 2, 1, 1)

        self.pulseRST_L = QPushButton(self.cfd_tab)
        self.pulseRST_L.setObjectName(u"pulseRST_L")

        self.gridLayout_6.addWidget(self.pulseRST_L, 1, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.line_3 = QFrame(self.cfd_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_3)

        self.label_2 = QLabel(self.cfd_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_29.addWidget(self.label_2)

        self.qcb_cfd_testPoint = QComboBox(self.cfd_tab)
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.setObjectName(u"qcb_cfd_testPoint")
        sizePolicy7.setHeightForWidth(self.qcb_cfd_testPoint.sizePolicy().hasHeightForWidth())
        self.qcb_cfd_testPoint.setSizePolicy(sizePolicy7)

        self.horizontalLayout_29.addWidget(self.qcb_cfd_testPoint)

        self.label_7 = QLabel(self.cfd_tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_29.addWidget(self.label_7)

        self.qcb_cfd_testPointChannel = QComboBox(self.cfd_tab)
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.addItem("")
        self.qcb_cfd_testPointChannel.setObjectName(u"qcb_cfd_testPointChannel")

        self.horizontalLayout_29.addWidget(self.qcb_cfd_testPointChannel)


        self.gridLayout_6.addLayout(self.horizontalLayout_29, 1, 1, 2, 2)

        self.configureChip_2 = QPushButton(self.cfd_tab)
        self.configureChip_2.setObjectName(u"configureChip_2")

        self.gridLayout_6.addWidget(self.configureChip_2, 2, 0, 1, 1)

        self.tabWidgets.addTab(self.cfd_tab, "")
        self.psd_tab = QWidget()
        self.psd_tab.setObjectName(u"psd_tab")
        self.horizontalLayout_45 = QHBoxLayout(self.psd_tab)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.gridLayout_psd = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout_psd.setSpacing(-1)
#endif
        self.gridLayout_psd.setObjectName(u"gridLayout_psd")
        self.gridLayout_psd.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.pushButton_reset_psd = QPushButton(self.psd_tab)
        self.pushButton_reset_psd.setObjectName(u"pushButton_reset_psd")

        self.gridLayout_psd.addWidget(self.pushButton_reset_psd, 3, 1, 1, 1)

        self.checkBox_psd_global_enable = QCheckBox(self.psd_tab)
        self.checkBox_psd_global_enable.setObjectName(u"checkBox_psd_global_enable")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.checkBox_psd_global_enable.setFont(font2)

        self.gridLayout_psd.addWidget(self.checkBox_psd_global_enable, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.psd_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.groupBox_2.setMinimumSize(QSize(251, 251))
        self.groupBox_2.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_47.addWidget(self.label_33)

        self.comboBox_psd_offset_dac_channel_selection = QComboBox(self.groupBox_2)
        self.comboBox_psd_offset_dac_channel_selection.setObjectName(u"comboBox_psd_offset_dac_channel_selection")

        self.horizontalLayout_47.addWidget(self.comboBox_psd_offset_dac_channel_selection)


        self.verticalLayout_17.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setBold(True)
        self.label_30.setFont(font3)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_30)

        self.verticalSlider_psd_single_channel_offset_dac_a = QSlider(self.groupBox_2)
        self.verticalSlider_psd_single_channel_offset_dac_a.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_a")
        self.verticalSlider_psd_single_channel_offset_dac_a.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_a.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_a.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_a.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_a.setOrientation(Qt.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_a.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_a.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTickPosition(QSlider.TicksAbove)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTickInterval(5)

        self.verticalLayout_14.addWidget(self.verticalSlider_psd_single_channel_offset_dac_a, 0, Qt.AlignHCenter)

        self.text_psd_offset_dac_a = QLineEdit(self.groupBox_2)
        self.text_psd_offset_dac_a.setObjectName(u"text_psd_offset_dac_a")

        self.verticalLayout_14.addWidget(self.text_psd_offset_dac_a, 0, Qt.AlignHCenter)


        self.horizontalLayout_48.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_31)

        self.verticalSlider_psd_single_channel_offset_dac_b = QSlider(self.groupBox_2)
        self.verticalSlider_psd_single_channel_offset_dac_b.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_b")
        self.verticalSlider_psd_single_channel_offset_dac_b.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_b.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_b.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_b.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_b.setOrientation(Qt.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_b.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_b.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTickPosition(QSlider.TicksAbove)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTickInterval(5)

        self.verticalLayout_15.addWidget(self.verticalSlider_psd_single_channel_offset_dac_b, 0, Qt.AlignHCenter)

        self.text_psd_offset_dac_b = QLineEdit(self.groupBox_2)
        self.text_psd_offset_dac_b.setObjectName(u"text_psd_offset_dac_b")

        self.verticalLayout_15.addWidget(self.text_psd_offset_dac_b, 0, Qt.AlignHCenter)


        self.horizontalLayout_48.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_32)

        self.verticalSlider_psd_single_channel_offset_dac_c = QSlider(self.groupBox_2)
        self.verticalSlider_psd_single_channel_offset_dac_c.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_c")
        self.verticalSlider_psd_single_channel_offset_dac_c.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_c.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_c.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_c.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_c.setOrientation(Qt.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_c.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_c.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTickPosition(QSlider.TicksAbove)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTickInterval(5)

        self.verticalLayout_16.addWidget(self.verticalSlider_psd_single_channel_offset_dac_c, 0, Qt.AlignHCenter)

        self.text_psd_offset_dac_c = QLineEdit(self.groupBox_2)
        self.text_psd_offset_dac_c.setObjectName(u"text_psd_offset_dac_c")

        self.verticalLayout_16.addWidget(self.text_psd_offset_dac_c, 0, Qt.AlignHCenter)


        self.horizontalLayout_48.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_psd_single_channel_configure = QPushButton(self.groupBox_2)
        self.pushButton_psd_single_channel_configure.setObjectName(u"pushButton_psd_single_channel_configure")
        self.pushButton_psd_single_channel_configure.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_46.addWidget(self.pushButton_psd_single_channel_configure)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_46.addWidget(self.pushButton)


        self.verticalLayout_17.addLayout(self.horizontalLayout_46)


        self.gridLayout_psd.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.pushButton_configure_psd = QPushButton(self.psd_tab)
        self.pushButton_configure_psd.setObjectName(u"pushButton_configure_psd")

        self.gridLayout_psd.addWidget(self.pushButton_configure_psd, 3, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_psd_polarity = QLabel(self.psd_tab)
        self.label_psd_polarity.setObjectName(u"label_psd_polarity")

        self.horizontalLayout_10.addWidget(self.label_psd_polarity)

        self.comboBox_psd_polarity = QComboBox(self.psd_tab)
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.setObjectName(u"comboBox_psd_polarity")

        self.horizontalLayout_10.addWidget(self.comboBox_psd_polarity)


        self.verticalLayout_18.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_psd_bias = QLabel(self.psd_tab)
        self.label_psd_bias.setObjectName(u"label_psd_bias")

        self.horizontalLayout_11.addWidget(self.label_psd_bias)

        self.comboBox_psd_bias = QComboBox(self.psd_tab)
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.setObjectName(u"comboBox_psd_bias")

        self.horizontalLayout_11.addWidget(self.comboBox_psd_bias)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_psd_trigger_mode = QLabel(self.psd_tab)
        self.label_psd_trigger_mode.setObjectName(u"label_psd_trigger_mode")

        self.horizontalLayout_49.addWidget(self.label_psd_trigger_mode)

        self.comboBox_psd_trigger_mode = QComboBox(self.psd_tab)
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.setObjectName(u"comboBox_psd_trigger_mode")

        self.horizontalLayout_49.addWidget(self.comboBox_psd_trigger_mode)


        self.verticalLayout_18.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_35 = QLabel(self.psd_tab)
        self.label_35.setObjectName(u"label_35")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        self.label_35.setFont(font4)

        self.horizontalLayout_50.addWidget(self.label_35)

        self.comboBox_psd_vtc_range = QComboBox(self.psd_tab)
        self.comboBox_psd_vtc_range.addItem("")
        self.comboBox_psd_vtc_range.addItem("")
        self.comboBox_psd_vtc_range.setObjectName(u"comboBox_psd_vtc_range")

        self.horizontalLayout_50.addWidget(self.comboBox_psd_vtc_range)


        self.verticalLayout_18.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_psd_auto_veto_dac = QLabel(self.psd_tab)
        self.label_psd_auto_veto_dac.setObjectName(u"label_psd_auto_veto_dac")

        self.horizontalLayout_51.addWidget(self.label_psd_auto_veto_dac)

        self.horizontalSlider_psd_auto_veto_dac = QSlider(self.psd_tab)
        self.horizontalSlider_psd_auto_veto_dac.setObjectName(u"horizontalSlider_psd_auto_veto_dac")
        self.horizontalSlider_psd_auto_veto_dac.setMaximum(1023)
        self.horizontalSlider_psd_auto_veto_dac.setSingleStep(10)
        self.horizontalSlider_psd_auto_veto_dac.setPageStep(128)
        self.horizontalSlider_psd_auto_veto_dac.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_auto_veto_dac.setInvertedControls(False)
        self.horizontalSlider_psd_auto_veto_dac.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_auto_veto_dac.setTickInterval(128)

        self.horizontalLayout_51.addWidget(self.horizontalSlider_psd_auto_veto_dac)

        self.horizontalSpacer_48 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_48)

        self.text_psd_auto_veto_dac = QLineEdit(self.psd_tab)
        self.text_psd_auto_veto_dac.setObjectName(u"text_psd_auto_veto_dac")
        sizePolicy7.setHeightForWidth(self.text_psd_auto_veto_dac.sizePolicy().hasHeightForWidth())
        self.text_psd_auto_veto_dac.setSizePolicy(sizePolicy7)
        self.text_psd_auto_veto_dac.setMinimumSize(QSize(21, 0))
        self.text_psd_auto_veto_dac.setMaximumSize(QSize(50, 16777215))
        self.text_psd_auto_veto_dac.setBaseSize(QSize(30, 0))
        self.text_psd_auto_veto_dac.setMaxLength(6)
        self.text_psd_auto_veto_dac.setCursorPosition(6)
        self.text_psd_auto_veto_dac.setAlignment(Qt.AlignCenter)
        self.text_psd_auto_veto_dac.setClearButtonEnabled(False)

        self.horizontalLayout_51.addWidget(self.text_psd_auto_veto_dac)


        self.verticalLayout_18.addLayout(self.horizontalLayout_51)

        self.groupBox_psd_test_mode = QGroupBox(self.psd_tab)
        self.groupBox_psd_test_mode.setObjectName(u"groupBox_psd_test_mode")
        self.groupBox_psd_test_mode.setMinimumSize(QSize(188, 0))
        self.formLayout = QFormLayout(self.groupBox_psd_test_mode)
        self.formLayout.setObjectName(u"formLayout")
        self.label_36 = QLabel(self.groupBox_psd_test_mode)
        self.label_36.setObjectName(u"label_36")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_36)

        self.comboBox_psd_test_mode = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode.addItem("")
        self.comboBox_psd_test_mode.addItem("")
        self.comboBox_psd_test_mode.setObjectName(u"comboBox_psd_test_mode")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_psd_test_mode)

        self.label_37 = QLabel(self.groupBox_psd_test_mode)
        self.label_37.setObjectName(u"label_37")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_37)

        self.comboBox_psd_test_mode_channel_selection = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode_channel_selection.setObjectName(u"comboBox_psd_test_mode_channel_selection")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_psd_test_mode_channel_selection)

        self.label_38 = QLabel(self.groupBox_psd_test_mode)
        self.label_38.setObjectName(u"label_38")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_38)

        self.comboBox_psd_test_mode_subchannel_selection = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.setObjectName(u"comboBox_psd_test_mode_subchannel_selection")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_psd_test_mode_subchannel_selection)

        self.pushButton_psd_test_mode_configure = QPushButton(self.groupBox_psd_test_mode)
        self.pushButton_psd_test_mode_configure.setObjectName(u"pushButton_psd_test_mode_configure")
        self.pushButton_psd_test_mode_configure.setMinimumSize(QSize(75, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.pushButton_psd_test_mode_configure)

        self.pushButton_psd_test_mode_reset = QPushButton(self.groupBox_psd_test_mode)
        self.pushButton_psd_test_mode_reset.setObjectName(u"pushButton_psd_test_mode_reset")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_psd_test_mode_reset)


        self.verticalLayout_18.addWidget(self.groupBox_psd_test_mode)


        self.gridLayout_psd.addLayout(self.verticalLayout_18, 1, 0, 1, 1)

        self.verticalGroupBox = QGroupBox(self.psd_tab)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMinimumSize(QSize(125, 0))
        self.verticalGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalGroupBox.setFlat(False)
        self.verticalGroupBox.setCheckable(False)
        self.gridLayout_7 = QGridLayout(self.verticalGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.checkBox_psd_channel_enable_10 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_10.setObjectName(u"checkBox_psd_channel_enable_10")
        self.checkBox_psd_channel_enable_10.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_10, 12, 1, 1, 2)

        self.checkBox_psd_channel_enable_12 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_12.setObjectName(u"checkBox_psd_channel_enable_12")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_12, 14, 1, 1, 2)

        self.checkBox_psd_channel_enable_0_7 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_0_7.setObjectName(u"checkBox_psd_channel_enable_0_7")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_0_7, 1, 0, 1, 1)

        self.checkBox_psd_channel_enable_14 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_14.setObjectName(u"checkBox_psd_channel_enable_14")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_14, 16, 1, 1, 2)

        self.checkBox_psd_channel_enable_11 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_11.setObjectName(u"checkBox_psd_channel_enable_11")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_11, 13, 1, 1, 2)

        self.checkBox_psd_channel_enable_15 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_15.setObjectName(u"checkBox_psd_channel_enable_15")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_15, 17, 1, 1, 2)

        self.checkBox_psd_channel_enable_4 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_4.setObjectName(u"checkBox_psd_channel_enable_4")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_4, 6, 1, 1, 2)

        self.checkBox_psd_channel_enable_5 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_5.setObjectName(u"checkBox_psd_channel_enable_5")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_5, 7, 1, 1, 2)

        self.checkBox_psd_channel_enable_3 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_3.setObjectName(u"checkBox_psd_channel_enable_3")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_3, 5, 1, 1, 2)

        self.checkBox_psd_channel_enable_0 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_0.setObjectName(u"checkBox_psd_channel_enable_0")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_0, 1, 1, 1, 1)

        self.checkBox_psd_channel_enable_2 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_2.setObjectName(u"checkBox_psd_channel_enable_2")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_2, 4, 1, 1, 2)

        self.checkBox_psd_channel_enable_13 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_13.setObjectName(u"checkBox_psd_channel_enable_13")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_13, 15, 1, 1, 2)

        self.checkBox_psd_channel_enable_9 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_9.setObjectName(u"checkBox_psd_channel_enable_9")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_9, 11, 1, 1, 2)

        self.label_34 = QLabel(self.verticalGroupBox)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.gridLayout_7.addWidget(self.label_34, 0, 0, 1, 1)

        self.checkBox_psd_channel_enable_7 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_7.setObjectName(u"checkBox_psd_channel_enable_7")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_7, 9, 1, 1, 2)

        self.checkBox_psd_channel_enable_all = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_all.setObjectName(u"checkBox_psd_channel_enable_all")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_all, 0, 1, 1, 2)

        self.checkBox_psd_channel_enable_8 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_8.setObjectName(u"checkBox_psd_channel_enable_8")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_8, 10, 1, 1, 2)

        self.checkBox_psd_channel_enable_6 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_6.setObjectName(u"checkBox_psd_channel_enable_6")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_6, 8, 1, 1, 2)

        self.checkBox_psd_channel_enable_8_15 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_8_15.setObjectName(u"checkBox_psd_channel_enable_8_15")
        self.checkBox_psd_channel_enable_8_15.setMaximumSize(QSize(68, 16777215))

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_8_15, 10, 0, 1, 1)

        self.checkBox_psd_channel_enable_1 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_1.setObjectName(u"checkBox_psd_channel_enable_1")

        self.gridLayout_7.addWidget(self.checkBox_psd_channel_enable_1, 3, 1, 1, 2)


        self.gridLayout_psd.addWidget(self.verticalGroupBox, 0, 2, 2, 1)

        self.horizontalGroupBox_5 = QGroupBox(self.psd_tab)
        self.horizontalGroupBox_5.setObjectName(u"horizontalGroupBox_5")
        self.horizontalGroupBox_5.setMinimumSize(QSize(831, 251))
        self.gridLayout_8 = QGridLayout(self.horizontalGroupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(-1)
        self.gridLayout_8.setVerticalSpacing(0)
        self.groupBox_subchannel_A = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_A.setObjectName(u"groupBox_subchannel_A")
        self.groupBox_subchannel_A.setMinimumSize(QSize(270, 225))
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_subchannel_A)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_17 = QLabel(self.groupBox_subchannel_A)
        self.label_17.setObjectName(u"label_17")
        font5 = QFont()
        font5.setPointSize(36)
        font5.setBold(True)
        self.label_17.setFont(font5)

        self.horizontalLayout_30.addWidget(self.label_17)

        self.label_psd_gain_a = QLabel(self.groupBox_subchannel_A)
        self.label_psd_gain_a.setObjectName(u"label_psd_gain_a")

        self.horizontalLayout_30.addWidget(self.label_psd_gain_a)

        self.comboBox_psd_gain_a = QComboBox(self.groupBox_subchannel_A)
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.addItem("")
        self.comboBox_psd_gain_a.setObjectName(u"comboBox_psd_gain_a")
        self.comboBox_psd_gain_a.setMinimumSize(QSize(72, 0))

        self.horizontalLayout_30.addWidget(self.comboBox_psd_gain_a)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_38)

        self.pushButton_psd_reset_subchannel_a = QPushButton(self.groupBox_subchannel_A)
        self.pushButton_psd_reset_subchannel_a.setObjectName(u"pushButton_psd_reset_subchannel_a")

        self.horizontalLayout_30.addWidget(self.pushButton_psd_reset_subchannel_a)


        self.verticalLayout_7.addLayout(self.horizontalLayout_30)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_19 = QLabel(self.groupBox_subchannel_A)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label_19)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)

        self.label_psd_delay_range_a = QLabel(self.groupBox_subchannel_A)
        self.label_psd_delay_range_a.setObjectName(u"label_psd_delay_range_a")
        self.label_psd_delay_range_a.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_delay_range_a.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_psd_delay_range_a)

        self.comboBox_psd_delay_range_a = QComboBox(self.groupBox_subchannel_A)
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.setObjectName(u"comboBox_psd_delay_range_a")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_delay_range_a.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_a.setSizePolicy(sizePolicy4)
        self.comboBox_psd_delay_range_a.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_delay_range_a.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_31.addWidget(self.comboBox_psd_delay_range_a)


        self.verticalLayout_5.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSlider_psd_delay_dac_a = QSlider(self.groupBox_subchannel_A)
        self.horizontalSlider_psd_delay_dac_a.setObjectName(u"horizontalSlider_psd_delay_dac_a")
        self.horizontalSlider_psd_delay_dac_a.setMaximum(1023)
        self.horizontalSlider_psd_delay_dac_a.setSingleStep(10)
        self.horizontalSlider_psd_delay_dac_a.setPageStep(128)
        self.horizontalSlider_psd_delay_dac_a.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_delay_dac_a.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_a.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_delay_dac_a.setTickInterval(128)

        self.horizontalLayout_33.addWidget(self.horizontalSlider_psd_delay_dac_a)

        self.text_psd_delay_dac_a = QLineEdit(self.groupBox_subchannel_A)
        self.text_psd_delay_dac_a.setObjectName(u"text_psd_delay_dac_a")
        sizePolicy7.setHeightForWidth(self.text_psd_delay_dac_a.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_a.setSizePolicy(sizePolicy7)
        self.text_psd_delay_dac_a.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_a.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_a.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_a.setMaxLength(6)
        self.text_psd_delay_dac_a.setCursorPosition(6)
        self.text_psd_delay_dac_a.setAlignment(Qt.AlignCenter)
        self.text_psd_delay_dac_a.setClearButtonEnabled(False)

        self.horizontalLayout_33.addWidget(self.text_psd_delay_dac_a)


        self.verticalLayout_5.addLayout(self.horizontalLayout_33)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_23 = QLabel(self.groupBox_subchannel_A)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_23)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_37)

        self.label_psd_width_range_a = QLabel(self.groupBox_subchannel_A)
        self.label_psd_width_range_a.setObjectName(u"label_psd_width_range_a")
        self.label_psd_width_range_a.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_width_range_a.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_psd_width_range_a)

        self.comboBox_psd_width_range_a = QComboBox(self.groupBox_subchannel_A)
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.setObjectName(u"comboBox_psd_width_range_a")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_width_range_a.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_a.setSizePolicy(sizePolicy4)
        self.comboBox_psd_width_range_a.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_width_range_a.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_34.addWidget(self.comboBox_psd_width_range_a)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSlider_psd_width_dac_a = QSlider(self.groupBox_subchannel_A)
        self.horizontalSlider_psd_width_dac_a.setObjectName(u"horizontalSlider_psd_width_dac_a")
        self.horizontalSlider_psd_width_dac_a.setMaximum(1023)
        self.horizontalSlider_psd_width_dac_a.setSingleStep(10)
        self.horizontalSlider_psd_width_dac_a.setPageStep(128)
        self.horizontalSlider_psd_width_dac_a.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_width_dac_a.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_a.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_width_dac_a.setTickInterval(128)

        self.horizontalLayout_35.addWidget(self.horizontalSlider_psd_width_dac_a)

        self.text_psd_width_dac_a = QLineEdit(self.groupBox_subchannel_A)
        self.text_psd_width_dac_a.setObjectName(u"text_psd_width_dac_a")
        sizePolicy7.setHeightForWidth(self.text_psd_width_dac_a.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_a.setSizePolicy(sizePolicy7)
        self.text_psd_width_dac_a.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_a.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_a.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_a.setMaxLength(6)
        self.text_psd_width_dac_a.setCursorPosition(6)
        self.text_psd_width_dac_a.setAlignment(Qt.AlignCenter)
        self.text_psd_width_dac_a.setClearButtonEnabled(False)

        self.horizontalLayout_35.addWidget(self.text_psd_width_dac_a)


        self.verticalLayout_6.addLayout(self.horizontalLayout_35)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_8.addWidget(self.groupBox_subchannel_A, 0, 0, 1, 1)

        self.groupBox_subchannel_B = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_B.setObjectName(u"groupBox_subchannel_B")
        self.groupBox_subchannel_B.setMinimumSize(QSize(270, 225))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_subchannel_B)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_24 = QLabel(self.groupBox_subchannel_B)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.horizontalLayout_32.addWidget(self.label_24)

        self.label_psd_gain_a_2 = QLabel(self.groupBox_subchannel_B)
        self.label_psd_gain_a_2.setObjectName(u"label_psd_gain_a_2")

        self.horizontalLayout_32.addWidget(self.label_psd_gain_a_2)

        self.comboBox_psd_gain_b = QComboBox(self.groupBox_subchannel_B)
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.addItem("")
        self.comboBox_psd_gain_b.setObjectName(u"comboBox_psd_gain_b")
        self.comboBox_psd_gain_b.setMinimumSize(QSize(72, 0))

        self.horizontalLayout_32.addWidget(self.comboBox_psd_gain_b)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_39)

        self.pushButton_psd_reset_subchannel_b = QPushButton(self.groupBox_subchannel_B)
        self.pushButton_psd_reset_subchannel_b.setObjectName(u"pushButton_psd_reset_subchannel_b")

        self.horizontalLayout_32.addWidget(self.pushButton_psd_reset_subchannel_b)


        self.verticalLayout_8.addLayout(self.horizontalLayout_32)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_25 = QLabel(self.groupBox_subchannel_B)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_25)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_40)

        self.label_psd_delay_range_b = QLabel(self.groupBox_subchannel_B)
        self.label_psd_delay_range_b.setObjectName(u"label_psd_delay_range_b")
        self.label_psd_delay_range_b.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_delay_range_b.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_psd_delay_range_b)

        self.comboBox_psd_delay_range_b = QComboBox(self.groupBox_subchannel_B)
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.setObjectName(u"comboBox_psd_delay_range_b")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_delay_range_b.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_b.setSizePolicy(sizePolicy4)
        self.comboBox_psd_delay_range_b.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_delay_range_b.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_36.addWidget(self.comboBox_psd_delay_range_b)


        self.verticalLayout_9.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSlider_psd_delay_dac_b = QSlider(self.groupBox_subchannel_B)
        self.horizontalSlider_psd_delay_dac_b.setObjectName(u"horizontalSlider_psd_delay_dac_b")
        self.horizontalSlider_psd_delay_dac_b.setMaximum(1023)
        self.horizontalSlider_psd_delay_dac_b.setSingleStep(10)
        self.horizontalSlider_psd_delay_dac_b.setPageStep(128)
        self.horizontalSlider_psd_delay_dac_b.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_delay_dac_b.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_b.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_delay_dac_b.setTickInterval(128)

        self.horizontalLayout_37.addWidget(self.horizontalSlider_psd_delay_dac_b)

        self.text_psd_delay_dac_b = QLineEdit(self.groupBox_subchannel_B)
        self.text_psd_delay_dac_b.setObjectName(u"text_psd_delay_dac_b")
        sizePolicy7.setHeightForWidth(self.text_psd_delay_dac_b.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_b.setSizePolicy(sizePolicy7)
        self.text_psd_delay_dac_b.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_b.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_b.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_b.setMaxLength(6)
        self.text_psd_delay_dac_b.setCursorPosition(6)
        self.text_psd_delay_dac_b.setAlignment(Qt.AlignCenter)
        self.text_psd_delay_dac_b.setClearButtonEnabled(False)

        self.horizontalLayout_37.addWidget(self.text_psd_delay_dac_b)


        self.verticalLayout_9.addLayout(self.horizontalLayout_37)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_26 = QLabel(self.groupBox_subchannel_B)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.horizontalLayout_38.addWidget(self.label_26)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_41)

        self.label_psd_width_range_b = QLabel(self.groupBox_subchannel_B)
        self.label_psd_width_range_b.setObjectName(u"label_psd_width_range_b")
        self.label_psd_width_range_b.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_width_range_b.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_psd_width_range_b)

        self.comboBox_psd_width_range_b = QComboBox(self.groupBox_subchannel_B)
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.setObjectName(u"comboBox_psd_width_range_b")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_width_range_b.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_b.setSizePolicy(sizePolicy4)
        self.comboBox_psd_width_range_b.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_width_range_b.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_38.addWidget(self.comboBox_psd_width_range_b)


        self.verticalLayout_10.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSlider_psd_width_dac_b = QSlider(self.groupBox_subchannel_B)
        self.horizontalSlider_psd_width_dac_b.setObjectName(u"horizontalSlider_psd_width_dac_b")
        self.horizontalSlider_psd_width_dac_b.setMaximum(1023)
        self.horizontalSlider_psd_width_dac_b.setSingleStep(10)
        self.horizontalSlider_psd_width_dac_b.setPageStep(128)
        self.horizontalSlider_psd_width_dac_b.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_width_dac_b.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_b.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_width_dac_b.setTickInterval(128)

        self.horizontalLayout_39.addWidget(self.horizontalSlider_psd_width_dac_b)

        self.text_psd_width_dac_b = QLineEdit(self.groupBox_subchannel_B)
        self.text_psd_width_dac_b.setObjectName(u"text_psd_width_dac_b")
        sizePolicy7.setHeightForWidth(self.text_psd_width_dac_b.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_b.setSizePolicy(sizePolicy7)
        self.text_psd_width_dac_b.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_b.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_b.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_b.setMaxLength(6)
        self.text_psd_width_dac_b.setCursorPosition(6)
        self.text_psd_width_dac_b.setAlignment(Qt.AlignCenter)
        self.text_psd_width_dac_b.setClearButtonEnabled(False)

        self.horizontalLayout_39.addWidget(self.text_psd_width_dac_b)


        self.verticalLayout_10.addLayout(self.horizontalLayout_39)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)


        self.gridLayout_8.addWidget(self.groupBox_subchannel_B, 0, 1, 1, 1)

        self.groupBox_subchannel_C = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_C.setObjectName(u"groupBox_subchannel_C")
        self.groupBox_subchannel_C.setMinimumSize(QSize(270, 225))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_subchannel_C)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_27 = QLabel(self.groupBox_subchannel_C)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.horizontalLayout_40.addWidget(self.label_27)

        self.label_psd_gain_a_3 = QLabel(self.groupBox_subchannel_C)
        self.label_psd_gain_a_3.setObjectName(u"label_psd_gain_a_3")

        self.horizontalLayout_40.addWidget(self.label_psd_gain_a_3)

        self.comboBox_psd_gain_c = QComboBox(self.groupBox_subchannel_C)
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.addItem("")
        self.comboBox_psd_gain_c.setObjectName(u"comboBox_psd_gain_c")
        self.comboBox_psd_gain_c.setMinimumSize(QSize(72, 0))

        self.horizontalLayout_40.addWidget(self.comboBox_psd_gain_c)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_42)

        self.pushButton_psd_reset_subchannel_c = QPushButton(self.groupBox_subchannel_C)
        self.pushButton_psd_reset_subchannel_c.setObjectName(u"pushButton_psd_reset_subchannel_c")

        self.horizontalLayout_40.addWidget(self.pushButton_psd_reset_subchannel_c)


        self.verticalLayout_11.addLayout(self.horizontalLayout_40)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_28 = QLabel(self.groupBox_subchannel_C)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.horizontalLayout_41.addWidget(self.label_28)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_43)

        self.label_psd_delay_range_c = QLabel(self.groupBox_subchannel_C)
        self.label_psd_delay_range_c.setObjectName(u"label_psd_delay_range_c")
        self.label_psd_delay_range_c.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_delay_range_c.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_psd_delay_range_c)

        self.comboBox_psd_delay_range_c = QComboBox(self.groupBox_subchannel_C)
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.setObjectName(u"comboBox_psd_delay_range_c")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_delay_range_c.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_c.setSizePolicy(sizePolicy4)
        self.comboBox_psd_delay_range_c.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_delay_range_c.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_41.addWidget(self.comboBox_psd_delay_range_c)


        self.verticalLayout_12.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSlider_psd_delay_dac_c = QSlider(self.groupBox_subchannel_C)
        self.horizontalSlider_psd_delay_dac_c.setObjectName(u"horizontalSlider_psd_delay_dac_c")
        self.horizontalSlider_psd_delay_dac_c.setMaximum(1023)
        self.horizontalSlider_psd_delay_dac_c.setSingleStep(10)
        self.horizontalSlider_psd_delay_dac_c.setPageStep(128)
        self.horizontalSlider_psd_delay_dac_c.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_delay_dac_c.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_c.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_delay_dac_c.setTickInterval(128)

        self.horizontalLayout_42.addWidget(self.horizontalSlider_psd_delay_dac_c)

        self.text_psd_delay_dac_c = QLineEdit(self.groupBox_subchannel_C)
        self.text_psd_delay_dac_c.setObjectName(u"text_psd_delay_dac_c")
        sizePolicy7.setHeightForWidth(self.text_psd_delay_dac_c.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_c.setSizePolicy(sizePolicy7)
        self.text_psd_delay_dac_c.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_c.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_c.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_c.setMaxLength(6)
        self.text_psd_delay_dac_c.setCursorPosition(6)
        self.text_psd_delay_dac_c.setAlignment(Qt.AlignCenter)
        self.text_psd_delay_dac_c.setClearButtonEnabled(False)

        self.horizontalLayout_42.addWidget(self.text_psd_delay_dac_c)


        self.verticalLayout_12.addLayout(self.horizontalLayout_42)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_29 = QLabel(self.groupBox_subchannel_C)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.horizontalLayout_43.addWidget(self.label_29)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_44)

        self.label_psd_width_range_c = QLabel(self.groupBox_subchannel_C)
        self.label_psd_width_range_c.setObjectName(u"label_psd_width_range_c")
        self.label_psd_width_range_c.setLayoutDirection(Qt.RightToLeft)
        self.label_psd_width_range_c.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_psd_width_range_c)

        self.comboBox_psd_width_range_c = QComboBox(self.groupBox_subchannel_C)
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.setObjectName(u"comboBox_psd_width_range_c")
        sizePolicy4.setHeightForWidth(self.comboBox_psd_width_range_c.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_c.setSizePolicy(sizePolicy4)
        self.comboBox_psd_width_range_c.setMinimumSize(QSize(10, 0))
        self.comboBox_psd_width_range_c.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_43.addWidget(self.comboBox_psd_width_range_c)


        self.verticalLayout_13.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSlider_psd_width_dac_c = QSlider(self.groupBox_subchannel_C)
        self.horizontalSlider_psd_width_dac_c.setObjectName(u"horizontalSlider_psd_width_dac_c")
        self.horizontalSlider_psd_width_dac_c.setMaximum(1023)
        self.horizontalSlider_psd_width_dac_c.setSingleStep(10)
        self.horizontalSlider_psd_width_dac_c.setPageStep(128)
        self.horizontalSlider_psd_width_dac_c.setOrientation(Qt.Horizontal)
        self.horizontalSlider_psd_width_dac_c.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_c.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_psd_width_dac_c.setTickInterval(128)

        self.horizontalLayout_44.addWidget(self.horizontalSlider_psd_width_dac_c)

        self.text_psd_width_dac_c = QLineEdit(self.groupBox_subchannel_C)
        self.text_psd_width_dac_c.setObjectName(u"text_psd_width_dac_c")
        sizePolicy7.setHeightForWidth(self.text_psd_width_dac_c.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_c.setSizePolicy(sizePolicy7)
        self.text_psd_width_dac_c.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_c.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_c.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_c.setMaxLength(6)
        self.text_psd_width_dac_c.setCursorPosition(6)
        self.text_psd_width_dac_c.setAlignment(Qt.AlignCenter)
        self.text_psd_width_dac_c.setClearButtonEnabled(False)

        self.horizontalLayout_44.addWidget(self.text_psd_width_dac_c)


        self.verticalLayout_13.addLayout(self.horizontalLayout_44)


        self.verticalLayout_11.addLayout(self.verticalLayout_13)


        self.gridLayout_8.addWidget(self.groupBox_subchannel_C, 0, 2, 1, 1)


        self.gridLayout_psd.addWidget(self.horizontalGroupBox_5, 2, 0, 1, 3)


        self.horizontalLayout_45.addLayout(self.gridLayout_psd)

        self.tabWidgets.addTab(self.psd_tab, "")
        self.chipboard_tab = QWidget()
        self.chipboard_tab.setObjectName(u"chipboard_tab")
        self.gridLayout_3 = QGridLayout(self.chipboard_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_signalRouting = QGroupBox(self.chipboard_tab)
        self.groupBox_signalRouting.setObjectName(u"groupBox_signalRouting")
        self.groupBox_signalRouting.setMinimumSize(QSize(50, 0))

        self.gridLayout_3.addWidget(self.groupBox_signalRouting, 1, 0, 1, 1)

        self.groupBox_muxs = QGroupBox(self.chipboard_tab)
        self.groupBox_muxs.setObjectName(u"groupBox_muxs")

        self.gridLayout_3.addWidget(self.groupBox_muxs, 4, 0, 1, 1)

        self.groupBox_delays = QGroupBox(self.chipboard_tab)
        self.groupBox_delays.setObjectName(u"groupBox_delays")
        self.groupBox_delays.setMinimumSize(QSize(430, 451))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_delays)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontal_layout_delay_label = QHBoxLayout()
        self.horizontal_layout_delay_label.setObjectName(u"horizontal_layout_delay_label")
        self.horizontal_layout_delay_label.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_15 = QLabel(self.groupBox_delays)
        self.label_15.setObjectName(u"label_15")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_15.setFont(font6)

        self.horizontal_layout_delay_label.addWidget(self.label_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_delay_label.addItem(self.horizontalSpacer_2)

        self.label_21 = QLabel(self.groupBox_delays)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_label.addWidget(self.label_21)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_delay_label.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_label)

        self.horizontal_layout_delay_ch_0 = QHBoxLayout()
        self.horizontal_layout_delay_ch_0.setObjectName(u"horizontal_layout_delay_ch_0")
        self.horizontal_layout_delay_ch_0.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_0 = QLabel(self.groupBox_delays)
        self.label_delay_ch_0.setObjectName(u"label_delay_ch_0")
        self.label_delay_ch_0.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_0.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_0.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_0.setMargin(0)

        self.horizontal_layout_delay_ch_0.addWidget(self.label_delay_ch_0)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_0.addItem(self.horizontalSpacer)

        self.slider_delay_ch_0 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_0.setObjectName(u"slider_delay_ch_0")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_0.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_0.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_0.setMaximum(62)
        self.slider_delay_ch_0.setSingleStep(2)
        self.slider_delay_ch_0.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_0.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_0.setTickInterval(2)

        self.horizontal_layout_delay_ch_0.addWidget(self.slider_delay_ch_0)

        self.horizontalSpacer_20 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_0.addItem(self.horizontalSpacer_20)

        self.text_delay_ch_0 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_0.setObjectName(u"text_delay_ch_0")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.text_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_0.setSizePolicy(sizePolicy9)
        self.text_delay_ch_0.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_0.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_0.setMaxLength(5)
        self.text_delay_ch_0.setFrame(True)
        self.text_delay_ch_0.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_0.addWidget(self.text_delay_ch_0)

        self.label_delay_ns_ch_0 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_0.setObjectName(u"label_delay_ns_ch_0")

        self.horizontal_layout_delay_ch_0.addWidget(self.label_delay_ns_ch_0)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_0)

        self.horizontal_layout_delay_ch_1 = QHBoxLayout()
        self.horizontal_layout_delay_ch_1.setObjectName(u"horizontal_layout_delay_ch_1")
        self.horizontal_layout_delay_ch_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_1 = QLabel(self.groupBox_delays)
        self.label_delay_ch_1.setObjectName(u"label_delay_ch_1")
        self.label_delay_ch_1.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_1.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_1.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_1.setMargin(0)

        self.horizontal_layout_delay_ch_1.addWidget(self.label_delay_ch_1)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_1.addItem(self.horizontalSpacer_4)

        self.slider_delay_ch_1 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_1.setObjectName(u"slider_delay_ch_1")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_1.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_1.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_1.setMaximum(62)
        self.slider_delay_ch_1.setSingleStep(2)
        self.slider_delay_ch_1.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_1.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_1.setTickInterval(2)

        self.horizontal_layout_delay_ch_1.addWidget(self.slider_delay_ch_1)

        self.horizontalSpacer_31 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_1.addItem(self.horizontalSpacer_31)

        self.text_delay_ch_1 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_1.setObjectName(u"text_delay_ch_1")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_1.setSizePolicy(sizePolicy9)
        self.text_delay_ch_1.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_1.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_1.setMaxLength(5)
        self.text_delay_ch_1.setFrame(True)
        self.text_delay_ch_1.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_1.addWidget(self.text_delay_ch_1)

        self.label_delay_ns_ch_1 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_1.setObjectName(u"label_delay_ns_ch_1")

        self.horizontal_layout_delay_ch_1.addWidget(self.label_delay_ns_ch_1)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_1)

        self.horizontal_layout_delay_ch_2 = QHBoxLayout()
        self.horizontal_layout_delay_ch_2.setObjectName(u"horizontal_layout_delay_ch_2")
        self.horizontal_layout_delay_ch_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_2 = QLabel(self.groupBox_delays)
        self.label_delay_ch_2.setObjectName(u"label_delay_ch_2")
        self.label_delay_ch_2.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_2.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_2.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_2.setMargin(0)

        self.horizontal_layout_delay_ch_2.addWidget(self.label_delay_ch_2)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_2.addItem(self.horizontalSpacer_5)

        self.slider_delay_ch_2 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_2.setObjectName(u"slider_delay_ch_2")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_2.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_2.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_2.setMaximum(62)
        self.slider_delay_ch_2.setSingleStep(2)
        self.slider_delay_ch_2.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_2.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_2.setTickInterval(2)

        self.horizontal_layout_delay_ch_2.addWidget(self.slider_delay_ch_2)

        self.horizontalSpacer_30 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_2.addItem(self.horizontalSpacer_30)

        self.text_delay_ch_2 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_2.setObjectName(u"text_delay_ch_2")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_2.setSizePolicy(sizePolicy9)
        self.text_delay_ch_2.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_2.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_2.setMaxLength(5)
        self.text_delay_ch_2.setFrame(True)
        self.text_delay_ch_2.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_2.addWidget(self.text_delay_ch_2)

        self.label_delay_ns_ch_2 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_2.setObjectName(u"label_delay_ns_ch_2")

        self.horizontal_layout_delay_ch_2.addWidget(self.label_delay_ns_ch_2)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_2)

        self.horizontal_layout_delay_ch_3 = QHBoxLayout()
        self.horizontal_layout_delay_ch_3.setObjectName(u"horizontal_layout_delay_ch_3")
        self.horizontal_layout_delay_ch_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_3 = QLabel(self.groupBox_delays)
        self.label_delay_ch_3.setObjectName(u"label_delay_ch_3")
        self.label_delay_ch_3.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_3.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_3.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_3.setMargin(0)

        self.horizontal_layout_delay_ch_3.addWidget(self.label_delay_ch_3)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_3.addItem(self.horizontalSpacer_6)

        self.slider_delay_ch_3 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_3.setObjectName(u"slider_delay_ch_3")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_3.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_3.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_3.setMaximum(62)
        self.slider_delay_ch_3.setSingleStep(2)
        self.slider_delay_ch_3.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_3.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_3.setTickInterval(2)

        self.horizontal_layout_delay_ch_3.addWidget(self.slider_delay_ch_3)

        self.horizontalSpacer_29 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_3.addItem(self.horizontalSpacer_29)

        self.text_delay_ch_3 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_3.setObjectName(u"text_delay_ch_3")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_3.setSizePolicy(sizePolicy9)
        self.text_delay_ch_3.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_3.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_3.setMaxLength(5)
        self.text_delay_ch_3.setFrame(True)
        self.text_delay_ch_3.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_3.addWidget(self.text_delay_ch_3)

        self.label_delay_ns_ch_3 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_3.setObjectName(u"label_delay_ns_ch_3")

        self.horizontal_layout_delay_ch_3.addWidget(self.label_delay_ns_ch_3)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_3)

        self.horizontal_layout_delay_ch_4 = QHBoxLayout()
        self.horizontal_layout_delay_ch_4.setObjectName(u"horizontal_layout_delay_ch_4")
        self.horizontal_layout_delay_ch_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_4 = QLabel(self.groupBox_delays)
        self.label_delay_ch_4.setObjectName(u"label_delay_ch_4")
        self.label_delay_ch_4.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_4.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_4.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_4.setMargin(0)

        self.horizontal_layout_delay_ch_4.addWidget(self.label_delay_ch_4)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_4.addItem(self.horizontalSpacer_7)

        self.slider_delay_ch_4 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_4.setObjectName(u"slider_delay_ch_4")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_4.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_4.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_4.setMaximum(62)
        self.slider_delay_ch_4.setSingleStep(2)
        self.slider_delay_ch_4.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_4.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_4.setTickInterval(2)

        self.horizontal_layout_delay_ch_4.addWidget(self.slider_delay_ch_4)

        self.horizontalSpacer_28 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_4.addItem(self.horizontalSpacer_28)

        self.text_delay_ch_4 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_4.setObjectName(u"text_delay_ch_4")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_4.setSizePolicy(sizePolicy9)
        self.text_delay_ch_4.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_4.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_4.setMaxLength(5)
        self.text_delay_ch_4.setFrame(True)
        self.text_delay_ch_4.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_4.addWidget(self.text_delay_ch_4)

        self.label_delay_ns_ch_4 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_4.setObjectName(u"label_delay_ns_ch_4")

        self.horizontal_layout_delay_ch_4.addWidget(self.label_delay_ns_ch_4)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_4)

        self.horizontal_layout_delay_ch_5 = QHBoxLayout()
        self.horizontal_layout_delay_ch_5.setObjectName(u"horizontal_layout_delay_ch_5")
        self.horizontal_layout_delay_ch_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_5 = QLabel(self.groupBox_delays)
        self.label_delay_ch_5.setObjectName(u"label_delay_ch_5")
        self.label_delay_ch_5.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_5.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_5.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_5.setMargin(0)

        self.horizontal_layout_delay_ch_5.addWidget(self.label_delay_ch_5)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_5.addItem(self.horizontalSpacer_8)

        self.slider_delay_ch_5 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_5.setObjectName(u"slider_delay_ch_5")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_5.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_5.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_5.setMaximum(62)
        self.slider_delay_ch_5.setSingleStep(2)
        self.slider_delay_ch_5.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_5.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_5.setTickInterval(2)

        self.horizontal_layout_delay_ch_5.addWidget(self.slider_delay_ch_5)

        self.horizontalSpacer_27 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_5.addItem(self.horizontalSpacer_27)

        self.text_delay_ch_5 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_5.setObjectName(u"text_delay_ch_5")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_5.setSizePolicy(sizePolicy9)
        self.text_delay_ch_5.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_5.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_5.setMaxLength(5)
        self.text_delay_ch_5.setFrame(True)
        self.text_delay_ch_5.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_5.addWidget(self.text_delay_ch_5)

        self.label_delay_ns_ch_5 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_5.setObjectName(u"label_delay_ns_ch_5")

        self.horizontal_layout_delay_ch_5.addWidget(self.label_delay_ns_ch_5)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_5)

        self.horizontal_layout_delay_ch_6 = QHBoxLayout()
        self.horizontal_layout_delay_ch_6.setObjectName(u"horizontal_layout_delay_ch_6")
        self.horizontal_layout_delay_ch_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_6 = QLabel(self.groupBox_delays)
        self.label_delay_ch_6.setObjectName(u"label_delay_ch_6")
        self.label_delay_ch_6.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_6.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_6.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_6.setMargin(0)

        self.horizontal_layout_delay_ch_6.addWidget(self.label_delay_ch_6)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_6.addItem(self.horizontalSpacer_9)

        self.slider_delay_ch_6 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_6.setObjectName(u"slider_delay_ch_6")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_6.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_6.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_6.setMaximum(62)
        self.slider_delay_ch_6.setSingleStep(2)
        self.slider_delay_ch_6.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_6.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_6.setTickInterval(2)

        self.horizontal_layout_delay_ch_6.addWidget(self.slider_delay_ch_6)

        self.horizontalSpacer_26 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_6.addItem(self.horizontalSpacer_26)

        self.text_delay_ch_6 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_6.setObjectName(u"text_delay_ch_6")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_6.setSizePolicy(sizePolicy9)
        self.text_delay_ch_6.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_6.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_6.setMaxLength(5)
        self.text_delay_ch_6.setFrame(True)
        self.text_delay_ch_6.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_6.addWidget(self.text_delay_ch_6)

        self.label_delay_ns_ch_6 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_6.setObjectName(u"label_delay_ns_ch_6")

        self.horizontal_layout_delay_ch_6.addWidget(self.label_delay_ns_ch_6)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_6)

        self.horizontal_layout_delay_ch_7 = QHBoxLayout()
        self.horizontal_layout_delay_ch_7.setObjectName(u"horizontal_layout_delay_ch_7")
        self.horizontal_layout_delay_ch_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_7 = QLabel(self.groupBox_delays)
        self.label_delay_ch_7.setObjectName(u"label_delay_ch_7")
        self.label_delay_ch_7.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_7.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_7.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_7.setMargin(0)

        self.horizontal_layout_delay_ch_7.addWidget(self.label_delay_ch_7)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_7.addItem(self.horizontalSpacer_10)

        self.slider_delay_ch_7 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_7.setObjectName(u"slider_delay_ch_7")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_7.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_7.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_7.setMaximum(62)
        self.slider_delay_ch_7.setSingleStep(2)
        self.slider_delay_ch_7.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_7.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_7.setTickInterval(2)

        self.horizontal_layout_delay_ch_7.addWidget(self.slider_delay_ch_7)

        self.horizontalSpacer_25 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_7.addItem(self.horizontalSpacer_25)

        self.text_delay_ch_7 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_7.setObjectName(u"text_delay_ch_7")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_7.setSizePolicy(sizePolicy9)
        self.text_delay_ch_7.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_7.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_7.setMaxLength(5)
        self.text_delay_ch_7.setFrame(True)
        self.text_delay_ch_7.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_7.addWidget(self.text_delay_ch_7)

        self.label_delay_ns_ch_7 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_7.setObjectName(u"label_delay_ns_ch_7")

        self.horizontal_layout_delay_ch_7.addWidget(self.label_delay_ns_ch_7)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_7)

        self.horizontal_layout_delay_ch_8 = QHBoxLayout()
        self.horizontal_layout_delay_ch_8.setObjectName(u"horizontal_layout_delay_ch_8")
        self.horizontal_layout_delay_ch_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_8 = QLabel(self.groupBox_delays)
        self.label_delay_ch_8.setObjectName(u"label_delay_ch_8")
        self.label_delay_ch_8.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_8.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_8.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_8.setMargin(0)

        self.horizontal_layout_delay_ch_8.addWidget(self.label_delay_ch_8)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_8.addItem(self.horizontalSpacer_11)

        self.slider_delay_ch_8 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_8.setObjectName(u"slider_delay_ch_8")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_8.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_8.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_8.setMaximum(62)
        self.slider_delay_ch_8.setSingleStep(2)
        self.slider_delay_ch_8.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_8.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_8.setTickInterval(2)

        self.horizontal_layout_delay_ch_8.addWidget(self.slider_delay_ch_8)

        self.horizontalSpacer_24 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_8.addItem(self.horizontalSpacer_24)

        self.text_delay_ch_8 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_8.setObjectName(u"text_delay_ch_8")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_8.setSizePolicy(sizePolicy9)
        self.text_delay_ch_8.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_8.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_8.setMaxLength(5)
        self.text_delay_ch_8.setFrame(True)
        self.text_delay_ch_8.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_8.addWidget(self.text_delay_ch_8)

        self.label_delay_ns_ch_8 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_8.setObjectName(u"label_delay_ns_ch_8")

        self.horizontal_layout_delay_ch_8.addWidget(self.label_delay_ns_ch_8)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_8)

        self.horizontal_layout_delay_ch_9 = QHBoxLayout()
        self.horizontal_layout_delay_ch_9.setObjectName(u"horizontal_layout_delay_ch_9")
        self.horizontal_layout_delay_ch_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_9 = QLabel(self.groupBox_delays)
        self.label_delay_ch_9.setObjectName(u"label_delay_ch_9")
        self.label_delay_ch_9.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_9.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_9.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_9.setMargin(0)

        self.horizontal_layout_delay_ch_9.addWidget(self.label_delay_ch_9)

        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_9.addItem(self.horizontalSpacer_12)

        self.slider_delay_ch_9 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_9.setObjectName(u"slider_delay_ch_9")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_9.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_9.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_9.setMaximum(62)
        self.slider_delay_ch_9.setSingleStep(2)
        self.slider_delay_ch_9.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_9.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_9.setTickInterval(2)

        self.horizontal_layout_delay_ch_9.addWidget(self.slider_delay_ch_9)

        self.horizontalSpacer_23 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_9.addItem(self.horizontalSpacer_23)

        self.text_delay_ch_9 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_9.setObjectName(u"text_delay_ch_9")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_9.setSizePolicy(sizePolicy9)
        self.text_delay_ch_9.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_9.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_9.setMaxLength(5)
        self.text_delay_ch_9.setFrame(True)
        self.text_delay_ch_9.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_9.addWidget(self.text_delay_ch_9)

        self.label_delay_ns_ch_9 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_9.setObjectName(u"label_delay_ns_ch_9")

        self.horizontal_layout_delay_ch_9.addWidget(self.label_delay_ns_ch_9)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_9)

        self.horizontal_layout_delay_ch_10 = QHBoxLayout()
        self.horizontal_layout_delay_ch_10.setObjectName(u"horizontal_layout_delay_ch_10")
        self.horizontal_layout_delay_ch_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_10 = QLabel(self.groupBox_delays)
        self.label_delay_ch_10.setObjectName(u"label_delay_ch_10")
        self.label_delay_ch_10.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_10.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_10.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_10.setMargin(0)

        self.horizontal_layout_delay_ch_10.addWidget(self.label_delay_ch_10)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_10.addItem(self.horizontalSpacer_13)

        self.slider_delay_ch_10 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_10.setObjectName(u"slider_delay_ch_10")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_10.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_10.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_10.setMaximum(62)
        self.slider_delay_ch_10.setSingleStep(2)
        self.slider_delay_ch_10.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_10.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_10.setTickInterval(2)

        self.horizontal_layout_delay_ch_10.addWidget(self.slider_delay_ch_10)

        self.horizontalSpacer_34 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_10.addItem(self.horizontalSpacer_34)

        self.text_delay_ch_10 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_10.setObjectName(u"text_delay_ch_10")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_10.setSizePolicy(sizePolicy9)
        self.text_delay_ch_10.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_10.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_10.setMaxLength(5)
        self.text_delay_ch_10.setFrame(True)
        self.text_delay_ch_10.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_10.addWidget(self.text_delay_ch_10)

        self.label_delay_ns_ch_10 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_10.setObjectName(u"label_delay_ns_ch_10")

        self.horizontal_layout_delay_ch_10.addWidget(self.label_delay_ns_ch_10)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_10)

        self.horizontal_layout_delay_ch_11 = QHBoxLayout()
        self.horizontal_layout_delay_ch_11.setObjectName(u"horizontal_layout_delay_ch_11")
        self.horizontal_layout_delay_ch_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_11 = QLabel(self.groupBox_delays)
        self.label_delay_ch_11.setObjectName(u"label_delay_ch_11")
        self.label_delay_ch_11.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_11.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_11.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_11.setMargin(0)

        self.horizontal_layout_delay_ch_11.addWidget(self.label_delay_ch_11)

        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_11.addItem(self.horizontalSpacer_14)

        self.slider_delay_ch_11 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_11.setObjectName(u"slider_delay_ch_11")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_11.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_11.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_11.setMaximum(62)
        self.slider_delay_ch_11.setSingleStep(2)
        self.slider_delay_ch_11.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_11.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_11.setTickInterval(2)

        self.horizontal_layout_delay_ch_11.addWidget(self.slider_delay_ch_11)

        self.horizontalSpacer_32 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_11.addItem(self.horizontalSpacer_32)

        self.text_delay_ch_11 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_11.setObjectName(u"text_delay_ch_11")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_11.setSizePolicy(sizePolicy9)
        self.text_delay_ch_11.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_11.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_11.setMaxLength(5)
        self.text_delay_ch_11.setFrame(True)
        self.text_delay_ch_11.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_11.addWidget(self.text_delay_ch_11)

        self.label_delay_ns_ch_11 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_11.setObjectName(u"label_delay_ns_ch_11")

        self.horizontal_layout_delay_ch_11.addWidget(self.label_delay_ns_ch_11)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_11)

        self.horizontal_layout_delay_ch_12 = QHBoxLayout()
        self.horizontal_layout_delay_ch_12.setObjectName(u"horizontal_layout_delay_ch_12")
        self.horizontal_layout_delay_ch_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_12 = QLabel(self.groupBox_delays)
        self.label_delay_ch_12.setObjectName(u"label_delay_ch_12")
        self.label_delay_ch_12.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_12.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_12.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_12.setMargin(0)

        self.horizontal_layout_delay_ch_12.addWidget(self.label_delay_ch_12)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_12.addItem(self.horizontalSpacer_15)

        self.slider_delay_ch_12 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_12.setObjectName(u"slider_delay_ch_12")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_12.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_12.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_12.setMaximum(62)
        self.slider_delay_ch_12.setSingleStep(2)
        self.slider_delay_ch_12.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_12.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_12.setTickInterval(2)

        self.horizontal_layout_delay_ch_12.addWidget(self.slider_delay_ch_12)

        self.horizontalSpacer_33 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_12.addItem(self.horizontalSpacer_33)

        self.text_delay_ch_12 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_12.setObjectName(u"text_delay_ch_12")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_12.setSizePolicy(sizePolicy9)
        self.text_delay_ch_12.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_12.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_12.setMaxLength(5)
        self.text_delay_ch_12.setFrame(True)
        self.text_delay_ch_12.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_12.addWidget(self.text_delay_ch_12)

        self.label_delay_ns_ch_12 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_12.setObjectName(u"label_delay_ns_ch_12")

        self.horizontal_layout_delay_ch_12.addWidget(self.label_delay_ns_ch_12)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_12)

        self.horizontal_layout_delay_ch_13 = QHBoxLayout()
        self.horizontal_layout_delay_ch_13.setObjectName(u"horizontal_layout_delay_ch_13")
        self.horizontal_layout_delay_ch_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_13 = QLabel(self.groupBox_delays)
        self.label_delay_ch_13.setObjectName(u"label_delay_ch_13")
        self.label_delay_ch_13.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_13.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_13.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_13.setMargin(0)

        self.horizontal_layout_delay_ch_13.addWidget(self.label_delay_ch_13)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_13.addItem(self.horizontalSpacer_16)

        self.slider_delay_ch_13 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_13.setObjectName(u"slider_delay_ch_13")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_13.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_13.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_13.setMaximum(62)
        self.slider_delay_ch_13.setSingleStep(2)
        self.slider_delay_ch_13.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_13.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_13.setTickInterval(2)

        self.horizontal_layout_delay_ch_13.addWidget(self.slider_delay_ch_13)

        self.horizontalSpacer_35 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_13.addItem(self.horizontalSpacer_35)

        self.text_delay_ch_13 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_13.setObjectName(u"text_delay_ch_13")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_13.setSizePolicy(sizePolicy9)
        self.text_delay_ch_13.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_13.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_13.setMaxLength(5)
        self.text_delay_ch_13.setFrame(True)
        self.text_delay_ch_13.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_13.addWidget(self.text_delay_ch_13)

        self.label_delay_ns_ch_13 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_13.setObjectName(u"label_delay_ns_ch_13")

        self.horizontal_layout_delay_ch_13.addWidget(self.label_delay_ns_ch_13)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_13)

        self.horizontal_layout_delay_ch_14 = QHBoxLayout()
        self.horizontal_layout_delay_ch_14.setObjectName(u"horizontal_layout_delay_ch_14")
        self.horizontal_layout_delay_ch_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_14 = QLabel(self.groupBox_delays)
        self.label_delay_ch_14.setObjectName(u"label_delay_ch_14")
        self.label_delay_ch_14.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_14.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_14.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_14.setMargin(0)

        self.horizontal_layout_delay_ch_14.addWidget(self.label_delay_ch_14)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_14.addItem(self.horizontalSpacer_17)

        self.slider_delay_ch_14 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_14.setObjectName(u"slider_delay_ch_14")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_14.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_14.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_14.setMaximum(62)
        self.slider_delay_ch_14.setSingleStep(2)
        self.slider_delay_ch_14.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_14.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_14.setTickInterval(2)

        self.horizontal_layout_delay_ch_14.addWidget(self.slider_delay_ch_14)

        self.horizontalSpacer_22 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_14.addItem(self.horizontalSpacer_22)

        self.text_delay_ch_14 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_14.setObjectName(u"text_delay_ch_14")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_14.setSizePolicy(sizePolicy9)
        self.text_delay_ch_14.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_14.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_14.setMaxLength(5)
        self.text_delay_ch_14.setFrame(True)
        self.text_delay_ch_14.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_14.addWidget(self.text_delay_ch_14)

        self.label_delay_ns_ch_14 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_14.setObjectName(u"label_delay_ns_ch_14")

        self.horizontal_layout_delay_ch_14.addWidget(self.label_delay_ns_ch_14)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_14)

        self.horizontal_layout_delay_ch_15 = QHBoxLayout()
        self.horizontal_layout_delay_ch_15.setObjectName(u"horizontal_layout_delay_ch_15")
        self.horizontal_layout_delay_ch_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delay_ch_15 = QLabel(self.groupBox_delays)
        self.label_delay_ch_15.setObjectName(u"label_delay_ch_15")
        self.label_delay_ch_15.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_15.setFrameShape(QFrame.NoFrame)
        self.label_delay_ch_15.setAlignment(Qt.AlignCenter)
        self.label_delay_ch_15.setMargin(0)

        self.horizontal_layout_delay_ch_15.addWidget(self.label_delay_ch_15)

        self.horizontalSpacer_18 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_15.addItem(self.horizontalSpacer_18)

        self.slider_delay_ch_15 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_15.setObjectName(u"slider_delay_ch_15")
        sizePolicy8.setHeightForWidth(self.slider_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_15.setSizePolicy(sizePolicy8)
        self.slider_delay_ch_15.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_15.setMaximum(62)
        self.slider_delay_ch_15.setSingleStep(2)
        self.slider_delay_ch_15.setOrientation(Qt.Horizontal)
        self.slider_delay_ch_15.setTickPosition(QSlider.TicksAbove)
        self.slider_delay_ch_15.setTickInterval(2)

        self.horizontal_layout_delay_ch_15.addWidget(self.slider_delay_ch_15)

        self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontal_layout_delay_ch_15.addItem(self.horizontalSpacer_21)

        self.text_delay_ch_15 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_15.setObjectName(u"text_delay_ch_15")
        sizePolicy9.setHeightForWidth(self.text_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_15.setSizePolicy(sizePolicy9)
        self.text_delay_ch_15.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_15.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_15.setMaxLength(5)
        self.text_delay_ch_15.setFrame(True)
        self.text_delay_ch_15.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_delay_ch_15.addWidget(self.text_delay_ch_15)

        self.label_delay_ns_ch_15 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_15.setObjectName(u"label_delay_ns_ch_15")

        self.horizontal_layout_delay_ch_15.addWidget(self.label_delay_ns_ch_15)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.qb_delay_configure = QPushButton(self.groupBox_delays)
        self.qb_delay_configure.setObjectName(u"qb_delay_configure")
        self.qb_delay_configure.setMinimumSize(QSize(0, 32))
        self.qb_delay_configure.setCheckable(False)
        self.qb_delay_configure.setChecked(False)
        self.qb_delay_configure.setFlat(False)

        self.horizontalLayout.addWidget(self.qb_delay_configure)

        self.qb_delay_reset = QPushButton(self.groupBox_delays)
        self.qb_delay_reset.setObjectName(u"qb_delay_reset")
        self.qb_delay_reset.setMinimumSize(QSize(0, 32))
        self.qb_delay_reset.setCheckable(False)
        self.qb_delay_reset.setChecked(False)
        self.qb_delay_reset.setFlat(False)

        self.horizontalLayout.addWidget(self.qb_delay_reset, 0, Qt.AlignVCenter)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.qrb_control_all = QRadioButton(self.groupBox_delays)
        self.qrb_control_all.setObjectName(u"qrb_control_all")
        self.qrb_control_all.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.qrb_control_all)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_3.addWidget(self.groupBox_delays, 0, 0, 1, 1)

        self.groupBox_dacOverride = QGroupBox(self.chipboard_tab)
        self.groupBox_dacOverride.setObjectName(u"groupBox_dacOverride")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.groupBox_dacOverride.sizePolicy().hasHeightForWidth())
        self.groupBox_dacOverride.setSizePolicy(sizePolicy10)
        self.groupBox_dacOverride.setMinimumSize(QSize(251, 241))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_dacOverride)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_octalDac_ch_0 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_0.setObjectName(u"verticalLayout_octalDac_ch_0")
        self.label_octalDac_ch_0 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_0.setObjectName(u"label_octalDac_ch_0")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_0.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_0.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_0.setFont(font3)
        self.label_octalDac_ch_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_0.addWidget(self.label_octalDac_ch_0)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slider_octalDac_ch_0 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_0.setObjectName(u"slider_octalDac_ch_0")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_0.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_0.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_0.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_0.setMaximum(1023)
        self.slider_octalDac_ch_0.setSingleStep(10)
        self.slider_octalDac_ch_0.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_0.setInvertedAppearance(False)
        self.slider_octalDac_ch_0.setInvertedControls(False)
        self.slider_octalDac_ch_0.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_0.setTickInterval(80)

        self.horizontalLayout_12.addWidget(self.slider_octalDac_ch_0)


        self.verticalLayout_octalDac_ch_0.addLayout(self.horizontalLayout_12)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_0.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.text_octalDac_ch_0 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_0.setObjectName(u"text_octalDac_ch_0")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_0.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_0.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_0.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_0.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_0.setMaxLength(6)
        self.text_octalDac_ch_0.setCursorPosition(6)
        self.text_octalDac_ch_0.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_0.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.text_octalDac_ch_0)


        self.verticalLayout_octalDac_ch_0.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_0)

        self.verticalLayout_octalDac_ch_1 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_1.setObjectName(u"verticalLayout_octalDac_ch_1")
        self.label_octalDac_ch_1 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_1.setObjectName(u"label_octalDac_ch_1")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_1.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_1.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_1.setFont(font3)
        self.label_octalDac_ch_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_1.addWidget(self.label_octalDac_ch_1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.slider_octalDac_ch_1 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_1.setObjectName(u"slider_octalDac_ch_1")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_1.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_1.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_1.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_1.setMaximum(1023)
        self.slider_octalDac_ch_1.setSingleStep(10)
        self.slider_octalDac_ch_1.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_1.setInvertedAppearance(False)
        self.slider_octalDac_ch_1.setInvertedControls(False)
        self.slider_octalDac_ch_1.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_1.setTickInterval(80)

        self.horizontalLayout_13.addWidget(self.slider_octalDac_ch_1)


        self.verticalLayout_octalDac_ch_1.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_1.addItem(self.verticalSpacer_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.text_octalDac_ch_1 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_1.setObjectName(u"text_octalDac_ch_1")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_1.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_1.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_1.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_1.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_1.setCursorPosition(6)
        self.text_octalDac_ch_1.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_1.setClearButtonEnabled(False)

        self.horizontalLayout_14.addWidget(self.text_octalDac_ch_1)


        self.verticalLayout_octalDac_ch_1.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_1)

        self.verticalLayout_octalDac_ch_2 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_2.setObjectName(u"verticalLayout_octalDac_ch_2")
        self.label_octalDac_ch_2 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_2.setObjectName(u"label_octalDac_ch_2")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_2.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_2.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_2.setFont(font3)
        self.label_octalDac_ch_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_2.addWidget(self.label_octalDac_ch_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.slider_octalDac_ch_2 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_2.setObjectName(u"slider_octalDac_ch_2")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_2.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_2.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_2.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_2.setMaximum(1023)
        self.slider_octalDac_ch_2.setSingleStep(10)
        self.slider_octalDac_ch_2.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_2.setInvertedAppearance(False)
        self.slider_octalDac_ch_2.setInvertedControls(False)
        self.slider_octalDac_ch_2.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_2.setTickInterval(80)

        self.horizontalLayout_15.addWidget(self.slider_octalDac_ch_2)


        self.verticalLayout_octalDac_ch_2.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.text_octalDac_ch_2 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_2.setObjectName(u"text_octalDac_ch_2")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_2.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_2.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_2.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_2.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_2.setMaxLength(6)
        self.text_octalDac_ch_2.setFrame(True)
        self.text_octalDac_ch_2.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_2.setClearButtonEnabled(False)

        self.horizontalLayout_16.addWidget(self.text_octalDac_ch_2)


        self.verticalLayout_octalDac_ch_2.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_2)

        self.verticalLayout_octalDac_ch_3 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_3.setObjectName(u"verticalLayout_octalDac_ch_3")
        self.label_octalDac_ch_3 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_3.setObjectName(u"label_octalDac_ch_3")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_3.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_3.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_3.setFont(font3)
        self.label_octalDac_ch_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_3.addWidget(self.label_octalDac_ch_3)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.slider_octalDac_ch_3 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_3.setObjectName(u"slider_octalDac_ch_3")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_3.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_3.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_3.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_3.setMaximum(1023)
        self.slider_octalDac_ch_3.setSingleStep(10)
        self.slider_octalDac_ch_3.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_3.setInvertedAppearance(False)
        self.slider_octalDac_ch_3.setInvertedControls(False)
        self.slider_octalDac_ch_3.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_3.setTickInterval(80)

        self.horizontalLayout_17.addWidget(self.slider_octalDac_ch_3)


        self.verticalLayout_octalDac_ch_3.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.text_octalDac_ch_3 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_3.setObjectName(u"text_octalDac_ch_3")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_3.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_3.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_3.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_3.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_3.setMaxLength(6)
        self.text_octalDac_ch_3.setCursorPosition(6)
        self.text_octalDac_ch_3.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_3.setClearButtonEnabled(False)

        self.horizontalLayout_18.addWidget(self.text_octalDac_ch_3)


        self.verticalLayout_octalDac_ch_3.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_3)

        self.verticalLayout_octalDac_ch_4 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_4.setObjectName(u"verticalLayout_octalDac_ch_4")
        self.label_octalDac_ch_4 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_4.setObjectName(u"label_octalDac_ch_4")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_4.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_4.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_4.setFont(font3)
        self.label_octalDac_ch_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_4.addWidget(self.label_octalDac_ch_4)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.slider_octalDac_ch_4 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_4.setObjectName(u"slider_octalDac_ch_4")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_4.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_4.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_4.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_4.setMaximum(1023)
        self.slider_octalDac_ch_4.setSingleStep(10)
        self.slider_octalDac_ch_4.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_4.setInvertedAppearance(False)
        self.slider_octalDac_ch_4.setInvertedControls(False)
        self.slider_octalDac_ch_4.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_4.setTickInterval(80)

        self.horizontalLayout_19.addWidget(self.slider_octalDac_ch_4)


        self.verticalLayout_octalDac_ch_4.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_4.addItem(self.verticalSpacer_5)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.text_octalDac_ch_4 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_4.setObjectName(u"text_octalDac_ch_4")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_4.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_4.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_4.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_4.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_4.setCursorPosition(0)
        self.text_octalDac_ch_4.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_4.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.text_octalDac_ch_4)


        self.verticalLayout_octalDac_ch_4.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_4)

        self.verticalLayout_octalDac_ch_5 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_5.setObjectName(u"verticalLayout_octalDac_ch_5")
        self.label_octalDac_ch_5 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_5.setObjectName(u"label_octalDac_ch_5")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_5.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_5.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_5.setFont(font3)
        self.label_octalDac_ch_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_5.addWidget(self.label_octalDac_ch_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.slider_octalDac_ch_5 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_5.setObjectName(u"slider_octalDac_ch_5")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_5.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_5.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_5.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_5.setMaximum(1023)
        self.slider_octalDac_ch_5.setSingleStep(10)
        self.slider_octalDac_ch_5.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_5.setInvertedAppearance(False)
        self.slider_octalDac_ch_5.setInvertedControls(False)
        self.slider_octalDac_ch_5.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_5.setTickInterval(80)

        self.horizontalLayout_21.addWidget(self.slider_octalDac_ch_5)


        self.verticalLayout_octalDac_ch_5.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_5.addItem(self.verticalSpacer_6)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.text_octalDac_ch_5 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_5.setObjectName(u"text_octalDac_ch_5")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_5.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_5.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_5.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_5.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_5.setCursorPosition(0)
        self.text_octalDac_ch_5.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_5.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.text_octalDac_ch_5)


        self.verticalLayout_octalDac_ch_5.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_5)

        self.verticalLayout_octalDac_ch_6 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_6.setObjectName(u"verticalLayout_octalDac_ch_6")
        self.label_octalDac_ch_6 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_6.setObjectName(u"label_octalDac_ch_6")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_6.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_6.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_6.setFont(font3)
        self.label_octalDac_ch_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_6.addWidget(self.label_octalDac_ch_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.slider_octalDac_ch_6 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_6.setObjectName(u"slider_octalDac_ch_6")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_6.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_6.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_6.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_6.setMaximum(1023)
        self.slider_octalDac_ch_6.setSingleStep(10)
        self.slider_octalDac_ch_6.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_6.setInvertedAppearance(False)
        self.slider_octalDac_ch_6.setInvertedControls(False)
        self.slider_octalDac_ch_6.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_6.setTickInterval(80)

        self.horizontalLayout_23.addWidget(self.slider_octalDac_ch_6)


        self.verticalLayout_octalDac_ch_6.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_6.addItem(self.verticalSpacer_7)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.text_octalDac_ch_6 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_6.setObjectName(u"text_octalDac_ch_6")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_6.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_6.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_6.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_6.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_6.setMaxLength(6)
        self.text_octalDac_ch_6.setCursorPosition(0)
        self.text_octalDac_ch_6.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_6.setClearButtonEnabled(False)

        self.horizontalLayout_24.addWidget(self.text_octalDac_ch_6)


        self.verticalLayout_octalDac_ch_6.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_6)

        self.verticalLayout_octalDac_ch_7 = QVBoxLayout()
        self.verticalLayout_octalDac_ch_7.setObjectName(u"verticalLayout_octalDac_ch_7")
        self.label_octalDac_ch_7 = QLabel(self.groupBox_dacOverride)
        self.label_octalDac_ch_7.setObjectName(u"label_octalDac_ch_7")
        sizePolicy11.setHeightForWidth(self.label_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_7.setSizePolicy(sizePolicy11)
        self.label_octalDac_ch_7.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_7.setFont(font3)
        self.label_octalDac_ch_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_7.addWidget(self.label_octalDac_ch_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.slider_octalDac_ch_7 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_7.setObjectName(u"slider_octalDac_ch_7")
        sizePolicy12.setHeightForWidth(self.slider_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_7.setSizePolicy(sizePolicy12)
        self.slider_octalDac_ch_7.setMinimumSize(QSize(0, 90))
        self.slider_octalDac_ch_7.setLayoutDirection(Qt.LeftToRight)
        self.slider_octalDac_ch_7.setMaximum(1023)
        self.slider_octalDac_ch_7.setSingleStep(10)
        self.slider_octalDac_ch_7.setOrientation(Qt.Vertical)
        self.slider_octalDac_ch_7.setInvertedAppearance(False)
        self.slider_octalDac_ch_7.setInvertedControls(False)
        self.slider_octalDac_ch_7.setTickPosition(QSlider.TicksAbove)
        self.slider_octalDac_ch_7.setTickInterval(80)

        self.horizontalLayout_25.addWidget(self.slider_octalDac_ch_7)


        self.verticalLayout_octalDac_ch_7.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_octalDac_ch_7.addItem(self.verticalSpacer_8)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.text_octalDac_ch_7 = QLineEdit(self.groupBox_dacOverride)
        self.text_octalDac_ch_7.setObjectName(u"text_octalDac_ch_7")
        sizePolicy7.setHeightForWidth(self.text_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_7.setSizePolicy(sizePolicy7)
        self.text_octalDac_ch_7.setMinimumSize(QSize(21, 0))
        self.text_octalDac_ch_7.setMaximumSize(QSize(50, 16777215))
        self.text_octalDac_ch_7.setBaseSize(QSize(30, 0))
        self.text_octalDac_ch_7.setCursorPosition(0)
        self.text_octalDac_ch_7.setAlignment(Qt.AlignCenter)
        self.text_octalDac_ch_7.setClearButtonEnabled(False)

        self.horizontalLayout_26.addWidget(self.text_octalDac_ch_7)


        self.verticalLayout_octalDac_ch_7.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_27.addLayout(self.verticalLayout_octalDac_ch_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setSizeConstraint(QLayout.SetNoConstraint)
        self.qb_octalDAC_configure = QPushButton(self.groupBox_dacOverride)
        self.qb_octalDAC_configure.setObjectName(u"qb_octalDAC_configure")

        self.horizontalLayout_28.addWidget(self.qb_octalDAC_configure)

        self.qb_octalDAC_reset = QPushButton(self.groupBox_dacOverride)
        self.qb_octalDAC_reset.setObjectName(u"qb_octalDAC_reset")

        self.horizontalLayout_28.addWidget(self.qb_octalDAC_reset)

        self.qb_octalDAC_updateConfig = QPushButton(self.groupBox_dacOverride)
        self.qb_octalDAC_updateConfig.setObjectName(u"qb_octalDAC_updateConfig")

        self.horizontalLayout_28.addWidget(self.qb_octalDAC_updateConfig)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)


        self.gridLayout_3.addWidget(self.groupBox_dacOverride, 0, 2, 1, 1)

        self.groupBox_misc = QGroupBox(self.chipboard_tab)
        self.groupBox_misc.setObjectName(u"groupBox_misc")

        self.gridLayout_3.addWidget(self.groupBox_misc, 1, 2, 1, 1)

        self.tabWidgets.addTab(self.chipboard_tab, "")

        self.verticalLayout.addWidget(self.tabWidgets)

        self.horizontalLayout_bottom_configure = QHBoxLayout()
        self.horizontalLayout_bottom_configure.setObjectName(u"horizontalLayout_bottom_configure")
        self.configureChip = QPushButton(self.centralwidget)
        self.configureChip.setObjectName(u"configureChip")

        self.horizontalLayout_bottom_configure.addWidget(self.configureChip)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_bottom_configure.addWidget(self.line_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_bottom_configure.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_bottom_configure)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1105, 24))
        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
#if QT_CONFIG(shortcut)
        self.label_11.setBuddy(self.chipNumber)
        self.label_16.setBuddy(self.leadingEdgeDAC_11)
        self.label_46.setBuddy(self.leadingEdgeDAC_14)
        self.label_14.setBuddy(self.leadingEdgeDAC_04)
        self.label_20.setBuddy(self.leadingEdgeDAC_13)
        self.label_3.setBuddy(self.leadingEdgeDAC_00)
        self.label_48.setBuddy(self.leadingEdgeDAC_10)
        self.label_42.setBuddy(self.leadingEdgeDAC_03)
        self.label_10.setBuddy(self.leadingEdgeDAC_02)
        self.label_18.setBuddy(self.leadingEdgeDAC_15)
        self.label_54.setBuddy(self.leadingEdgeDAC_06)
        self.label_40.setBuddy(self.leadingEdgeDAC_12)
        self.label_22.setBuddy(self.leadingEdgeDAC_09)
        self.label_50.setBuddy(self.leadingEdgeDAC_05)
        self.label_44.setBuddy(self.leadingEdgeDAC_08)
        self.label_12.setBuddy(self.leadingEdgeDAC_07)
        self.label_52.setBuddy(self.leadingEdgeDAC_01)
        self.label_2.setBuddy(self.qcb_cfd_testPoint)
        self.label_7.setBuddy(self.qcb_cfd_testPointChannel)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.enableDAC_all, self.signBit_all)
        QWidget.setTabOrder(self.signBit_all, self.leadingEdgeDAC_00)
        QWidget.setTabOrder(self.leadingEdgeDAC_00, self.leadingEdgeDAC_01)
        QWidget.setTabOrder(self.leadingEdgeDAC_01, self.leadingEdgeDAC_02)
        QWidget.setTabOrder(self.leadingEdgeDAC_02, self.leadingEdgeDAC_03)
        QWidget.setTabOrder(self.leadingEdgeDAC_03, self.leadingEdgeDAC_04)
        QWidget.setTabOrder(self.leadingEdgeDAC_04, self.leadingEdgeDAC_05)
        QWidget.setTabOrder(self.leadingEdgeDAC_05, self.leadingEdgeDAC_06)
        QWidget.setTabOrder(self.leadingEdgeDAC_06, self.leadingEdgeDAC_07)
        QWidget.setTabOrder(self.leadingEdgeDAC_07, self.leadingEdgeDAC_08)
        QWidget.setTabOrder(self.leadingEdgeDAC_08, self.leadingEdgeDAC_09)
        QWidget.setTabOrder(self.leadingEdgeDAC_09, self.leadingEdgeDAC_10)
        QWidget.setTabOrder(self.leadingEdgeDAC_10, self.leadingEdgeDAC_11)
        QWidget.setTabOrder(self.leadingEdgeDAC_11, self.leadingEdgeDAC_12)
        QWidget.setTabOrder(self.leadingEdgeDAC_12, self.leadingEdgeDAC_13)
        QWidget.setTabOrder(self.leadingEdgeDAC_13, self.leadingEdgeDAC_14)
        QWidget.setTabOrder(self.leadingEdgeDAC_14, self.leadingEdgeDAC_15)
        QWidget.setTabOrder(self.leadingEdgeDAC_15, self.enableDAC_00)
        QWidget.setTabOrder(self.enableDAC_00, self.signBit_00)
        QWidget.setTabOrder(self.signBit_00, self.enableDAC_01)
        QWidget.setTabOrder(self.enableDAC_01, self.signBit_01)
        QWidget.setTabOrder(self.signBit_01, self.enableDAC_02)
        QWidget.setTabOrder(self.enableDAC_02, self.signBit_02)
        QWidget.setTabOrder(self.signBit_02, self.enableDAC_03)
        QWidget.setTabOrder(self.enableDAC_03, self.signBit_03)
        QWidget.setTabOrder(self.signBit_03, self.enableDAC_04)
        QWidget.setTabOrder(self.enableDAC_04, self.signBit_04)
        QWidget.setTabOrder(self.signBit_04, self.enableDAC_05)
        QWidget.setTabOrder(self.enableDAC_05, self.signBit_05)
        QWidget.setTabOrder(self.signBit_05, self.enableDAC_06)
        QWidget.setTabOrder(self.enableDAC_06, self.signBit_06)
        QWidget.setTabOrder(self.signBit_06, self.enableDAC_07)
        QWidget.setTabOrder(self.enableDAC_07, self.signBit_07)
        QWidget.setTabOrder(self.signBit_07, self.enableDAC_08)
        QWidget.setTabOrder(self.enableDAC_08, self.signBit_08)
        QWidget.setTabOrder(self.signBit_08, self.enableDAC_09)
        QWidget.setTabOrder(self.enableDAC_09, self.signBit_09)
        QWidget.setTabOrder(self.signBit_09, self.enableDAC_10)
        QWidget.setTabOrder(self.enableDAC_10, self.signBit_10)
        QWidget.setTabOrder(self.signBit_10, self.enableDAC_11)
        QWidget.setTabOrder(self.enableDAC_11, self.signBit_11)
        QWidget.setTabOrder(self.signBit_11, self.enableDAC_12)
        QWidget.setTabOrder(self.enableDAC_12, self.signBit_12)
        QWidget.setTabOrder(self.signBit_12, self.enableDAC_13)
        QWidget.setTabOrder(self.enableDAC_13, self.signBit_13)
        QWidget.setTabOrder(self.signBit_13, self.enableDAC_14)
        QWidget.setTabOrder(self.enableDAC_14, self.signBit_14)
        QWidget.setTabOrder(self.signBit_14, self.enableDAC_15)
        QWidget.setTabOrder(self.enableDAC_15, self.signBit_15)
        QWidget.setTabOrder(self.signBit_15, self.qcb_cfd_testPoint)
        QWidget.setTabOrder(self.qcb_cfd_testPoint, self.qcb_cfd_testPointChannel)
        QWidget.setTabOrder(self.qcb_cfd_testPointChannel, self.configureChip)

        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menutest.addAction(self.actionload)
        self.menutest.addAction(self.actionSave)
        self.menutest.addAction(self.actionSavs_As)
        self.menuAbout.addAction(self.actionGithub_Repository)

        self.retranslateUi(MainWindow)

        self.tabWidgets.setCurrentIndex(1)
        self.qb_delay_configure.setDefault(False)
        self.qb_delay_reset.setDefault(False)
        self.qb_octalDAC_reset.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PSDinator Configuration GUI", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.actionload.setText(QCoreApplication.translate("MainWindow", u"Load Configuration", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save ", None))
        self.actionSavs_As.setText(QCoreApplication.translate("MainWindow", u"Savs As", None))
        self.actionGithub_Repository.setText(QCoreApplication.translate("MainWindow", u"Github Repository", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"# Current chipboard is :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"**Select Chipboard Number:**", None))
        self.chipNumber.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.chipNumber.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.chipNumber.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.chipNumber.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.chipNumber.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.chipNumber.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.chipNumber.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.chipNumber.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.chipNumber.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.chipNumber.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.chipNumber.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.chipNumber.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.chipNumber.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.chipNumber.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.chipNumber.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.chipNumber.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.chipNumber.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.chipNumber.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.chipNumber.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.chipNumber.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.chipNumber.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))
        self.chipNumber.setItemText(21, QCoreApplication.translate("MainWindow", u"21", None))
        self.chipNumber.setItemText(22, QCoreApplication.translate("MainWindow", u"22", None))
        self.chipNumber.setItemText(23, QCoreApplication.translate("MainWindow", u"23", None))
        self.chipNumber.setItemText(24, QCoreApplication.translate("MainWindow", u"24", None))
        self.chipNumber.setItemText(25, QCoreApplication.translate("MainWindow", u"25", None))
        self.chipNumber.setItemText(26, QCoreApplication.translate("MainWindow", u"26", None))
        self.chipNumber.setItemText(27, QCoreApplication.translate("MainWindow", u"27", None))
        self.chipNumber.setItemText(28, QCoreApplication.translate("MainWindow", u"28", None))
        self.chipNumber.setItemText(29, QCoreApplication.translate("MainWindow", u"29", None))
        self.chipNumber.setItemText(30, QCoreApplication.translate("MainWindow", u"30", None))
        self.chipNumber.setItemText(31, QCoreApplication.translate("MainWindow", u"31", None))

        self.groupBox_cfd_global_settings.setTitle(QCoreApplication.translate("MainWindow", u"CFD Global Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nowlin Mode", None))
        self.nowlinMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Short", None))
        self.nowlinMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Long", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nowlin Delay (ns)", None))
        self.nowlinDelay.setItemText(0, QCoreApplication.translate("MainWindow", u"Short", None))
        self.nowlinDelay.setItemText(1, QCoreApplication.translate("MainWindow", u"Long", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lockout DAC", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Lockout Mode", None))
        self.lockoutMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Short", None))
        self.lockoutMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Long", None))
        self.lockoutMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Disabled", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CFD Pulse Width (ns)", None))
        self.CFDPulseWidth.setItemText(0, QCoreApplication.translate("MainWindow", u"50", None))
        self.CFDPulseWidth.setItemText(1, QCoreApplication.translate("MainWindow", u"100", None))
        self.CFDPulseWidth.setItemText(2, QCoreApplication.translate("MainWindow", u"200", None))
        self.CFDPulseWidth.setItemText(3, QCoreApplication.translate("MainWindow", u"500", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"AGND Trim", None))
        self.AgndTrim.setItemText(0, QCoreApplication.translate("MainWindow", u"1.77", None))

        self.negativePolarity.setText(QCoreApplication.translate("MainWindow", u"Negative Polarity", None))
        self.globalMode.setText(QCoreApplication.translate("MainWindow", u"Global Mode", None))
        self.LEOutEnable.setText(QCoreApplication.translate("MainWindow", u"LE Out Enable", None))
        self.globalEnable.setText(QCoreApplication.translate("MainWindow", u"CFD Global Enable", None))
        self.groupBox_cfd_individual_ch_settings.setTitle(QCoreApplication.translate("MainWindow", u"CFD individual channel threshold settings", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_15.setText("")
        self.leadingEdgeDAC_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_13.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_01.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_13.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_14.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.enableDAC_08.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_channel_header.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.signBit_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_leading_edge_dac_header.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC(5 bit value)", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_05.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_05.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.enableDAC_05.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_02.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Channel 11:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Channel 14:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.enableDAC_10.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_02.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Channel 13:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_09.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_09.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_06.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_04.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel 0:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_02.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_02.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Channel 10:", None))
        self.signBit_11.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
        self.enableDAC_00.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_09.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.signBit_01.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.signBit_10.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_12.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_15.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_00.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Channel 15:", None))
        self.signBit_08.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Channel 6:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Channel 12:", None))
        self.enableDAC_11.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_15.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_13.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_07.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_09.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Channel 9:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Channel 5:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_07.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_06.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_06.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_04.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_07.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_07.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.enableDAC_03.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Channel 8:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_01.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_01.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_05.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_14.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_06.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_03.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_03.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.enableDAC_14.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_00.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_00.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_03.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_04.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_04.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Channel 7:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.signBit_12.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_08.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_08.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
#if QT_CONFIG(tooltip)
        self.pulseRST_L.setToolTip(QCoreApplication.translate("MainWindow", u"Applies a reset signal to the CFD chip, pulses RST_L", None))
#endif // QT_CONFIG(tooltip)
        self.pulseRST_L.setText(QCoreApplication.translate("MainWindow", u"Reset CFD ASIC", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Test Point", None))
        self.qcb_cfd_testPoint.setItemText(0, QCoreApplication.translate("MainWindow", u"AVSS", None))
        self.qcb_cfd_testPoint.setItemText(1, QCoreApplication.translate("MainWindow", u"Lockout Pulse", None))
        self.qcb_cfd_testPoint.setItemText(2, QCoreApplication.translate("MainWindow", u"Leading Edge Detector", None))
        self.qcb_cfd_testPoint.setItemText(3, QCoreApplication.translate("MainWindow", u"Zero Crossing Detector", None))
        self.qcb_cfd_testPoint.setItemText(4, QCoreApplication.translate("MainWindow", u"Oneshot Trigger", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Test Point Channel", None))
        self.qcb_cfd_testPointChannel.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.qcb_cfd_testPointChannel.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.qcb_cfd_testPointChannel.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.qcb_cfd_testPointChannel.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.qcb_cfd_testPointChannel.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.qcb_cfd_testPointChannel.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.qcb_cfd_testPointChannel.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.qcb_cfd_testPointChannel.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.qcb_cfd_testPointChannel.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.qcb_cfd_testPointChannel.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.qcb_cfd_testPointChannel.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.qcb_cfd_testPointChannel.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.qcb_cfd_testPointChannel.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.qcb_cfd_testPointChannel.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.qcb_cfd_testPointChannel.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.qcb_cfd_testPointChannel.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))

        self.configureChip_2.setText(QCoreApplication.translate("MainWindow", u"Configure Only CFD Chip", None))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.cfd_tab), QCoreApplication.translate("MainWindow", u"CFD", None))
        self.pushButton_reset_psd.setText(QCoreApplication.translate("MainWindow", u"Reset PSD", None))
        self.checkBox_psd_global_enable.setText(QCoreApplication.translate("MainWindow", u"PSD Global Enable ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Offset DAC Config", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_psd_single_channel_configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_configure_psd.setText(QCoreApplication.translate("MainWindow", u"Configure PSD", None))
        self.label_psd_polarity.setText(QCoreApplication.translate("MainWindow", u"Polarity", None))
        self.comboBox_psd_polarity.setItemText(0, QCoreApplication.translate("MainWindow", u"positive", None))
        self.comboBox_psd_polarity.setItemText(1, QCoreApplication.translate("MainWindow", u"negative", None))

        self.label_psd_bias.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.comboBox_psd_bias.setItemText(0, QCoreApplication.translate("MainWindow", u"high", None))
        self.comboBox_psd_bias.setItemText(1, QCoreApplication.translate("MainWindow", u"low", None))

        self.label_psd_trigger_mode.setText(QCoreApplication.translate("MainWindow", u"Trigger Mode", None))
        self.comboBox_psd_trigger_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_psd_trigger_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_trigger_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"VTC Range", None))
        self.comboBox_psd_vtc_range.setItemText(0, QCoreApplication.translate("MainWindow", u"250 ns", None))
        self.comboBox_psd_vtc_range.setItemText(1, QCoreApplication.translate("MainWindow", u"2 us", None))

#if QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Auto Veto Time: </span></p><p><br/></p><p>Configures the time at which the ASIC auto resets if the <span style=\" font-weight:700;\">Veto Reset(Take Event)</span> signal is not asserted.  </p><p>Inversely related to DAC voltage, not linear; Higher Voltage -&gt; Quicker reset.  </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac.setText(QCoreApplication.translate("MainWindow", u"Auto Veto DAC voltage", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_auto_veto_dac.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_auto_veto_dac.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_auto_veto_dac.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.groupBox_psd_test_mode.setTitle(QCoreApplication.translate("MainWindow", u"PSD Test Mode", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.comboBox_psd_test_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"On", None))
        self.comboBox_psd_test_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Off", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Test Channel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Test Sub Channel", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))

        self.pushButton_psd_test_mode_configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.pushButton_psd_test_mode_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Channel Enable ", None))
        self.checkBox_psd_channel_enable_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.checkBox_psd_channel_enable_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.checkBox_psd_channel_enable_0_7.setText(QCoreApplication.translate("MainWindow", u"0-7", None))
        self.checkBox_psd_channel_enable_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.checkBox_psd_channel_enable_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.checkBox_psd_channel_enable_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.checkBox_psd_channel_enable_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.checkBox_psd_channel_enable_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.checkBox_psd_channel_enable_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.checkBox_psd_channel_enable_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBox_psd_channel_enable_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.checkBox_psd_channel_enable_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.checkBox_psd_channel_enable_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.checkBox_psd_channel_enable_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.checkBox_psd_channel_enable_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.checkBox_psd_channel_enable_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.checkBox_psd_channel_enable_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.checkBox_psd_channel_enable_8_15.setText(QCoreApplication.translate("MainWindow", u"8-15", None))
        self.checkBox_psd_channel_enable_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.horizontalGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Integrator Gates", None))
        self.groupBox_subchannel_A.setTitle(QCoreApplication.translate("MainWindow", u"Subchannel A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_psd_gain_a.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.comboBox_psd_gain_a.setItemText(0, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox_psd_gain_a.setItemText(1, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox_psd_gain_a.setItemText(2, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_psd_gain_a.setItemText(3, QCoreApplication.translate("MainWindow", u"5000", None))
        self.comboBox_psd_gain_a.setItemText(4, QCoreApplication.translate("MainWindow", u"10000", None))
        self.comboBox_psd_gain_a.setItemText(5, QCoreApplication.translate("MainWindow", u"20000", None))
        self.comboBox_psd_gain_a.setItemText(6, QCoreApplication.translate("MainWindow", u"50000", None))
        self.comboBox_psd_gain_a.setItemText(7, QCoreApplication.translate("MainWindow", u"100000", None))

        self.pushButton_psd_reset_subchannel_a.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.label_psd_delay_range_a.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_delay_range_a.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_delay_range_a.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_delay_range_a.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_delay_range_a.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_a.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_a.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_delay_dac_a.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_psd_width_range_a.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_width_range_a.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_width_range_a.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_width_range_a.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_width_range_a.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_a.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_a.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_width_dac_a.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.groupBox_subchannel_B.setTitle(QCoreApplication.translate("MainWindow", u"Subchannel B", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_psd_gain_a_2.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.comboBox_psd_gain_b.setItemText(0, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox_psd_gain_b.setItemText(1, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox_psd_gain_b.setItemText(2, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_psd_gain_b.setItemText(3, QCoreApplication.translate("MainWindow", u"5000", None))
        self.comboBox_psd_gain_b.setItemText(4, QCoreApplication.translate("MainWindow", u"10000", None))
        self.comboBox_psd_gain_b.setItemText(5, QCoreApplication.translate("MainWindow", u"20000", None))
        self.comboBox_psd_gain_b.setItemText(6, QCoreApplication.translate("MainWindow", u"50000", None))
        self.comboBox_psd_gain_b.setItemText(7, QCoreApplication.translate("MainWindow", u"100000", None))

        self.pushButton_psd_reset_subchannel_b.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.label_psd_delay_range_b.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_delay_range_b.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_delay_range_b.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_delay_range_b.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_delay_range_b.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_b.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_b.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_delay_dac_b.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_psd_width_range_b.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_width_range_b.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_width_range_b.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_width_range_b.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_width_range_b.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_b.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_b.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_width_dac_b.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.groupBox_subchannel_C.setTitle(QCoreApplication.translate("MainWindow", u"Subchannel B", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_psd_gain_a_3.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.comboBox_psd_gain_c.setItemText(0, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox_psd_gain_c.setItemText(1, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox_psd_gain_c.setItemText(2, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_psd_gain_c.setItemText(3, QCoreApplication.translate("MainWindow", u"5000", None))
        self.comboBox_psd_gain_c.setItemText(4, QCoreApplication.translate("MainWindow", u"10000", None))
        self.comboBox_psd_gain_c.setItemText(5, QCoreApplication.translate("MainWindow", u"20000", None))
        self.comboBox_psd_gain_c.setItemText(6, QCoreApplication.translate("MainWindow", u"50000", None))
        self.comboBox_psd_gain_c.setItemText(7, QCoreApplication.translate("MainWindow", u"100000", None))

        self.pushButton_psd_reset_subchannel_c.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.label_psd_delay_range_c.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_delay_range_c.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_delay_range_c.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_delay_range_c.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_delay_range_c.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_c.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_c.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_delay_dac_c.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_psd_width_range_c.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.comboBox_psd_width_range_c.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_psd_width_range_c.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_psd_width_range_c.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_psd_width_range_c.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_c.setToolTip(QCoreApplication.translate("MainWindow", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_c.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_psd_width_dac_c.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.psd_tab), QCoreApplication.translate("MainWindow", u"PSD", None))
#if QT_CONFIG(tooltip)
        self.tabWidgets.setTabToolTip(self.tabWidgets.indexOf(self.psd_tab), QCoreApplication.translate("MainWindow", u"Configuration settings for the PSD Chips", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_signalRouting.setTitle(QCoreApplication.translate("MainWindow", u"Signal Routing", None))
        self.groupBox_muxs.setTitle(QCoreApplication.translate("MainWindow", u"Multiplexer", None))
        self.groupBox_delays.setTitle(QCoreApplication.translate("MainWindow", u"Delays", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Delay Setting", None))
        self.label_delay_ch_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.text_delay_ch_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_0.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.text_delay_ch_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_1.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.text_delay_ch_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_2.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.text_delay_ch_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_3.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.text_delay_ch_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_4.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.text_delay_ch_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_5.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.text_delay_ch_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_6.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.text_delay_ch_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_7.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.text_delay_ch_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_8.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.text_delay_ch_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_9.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.text_delay_ch_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_10.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.text_delay_ch_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_11.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.text_delay_ch_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_12.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.text_delay_ch_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_13.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.text_delay_ch_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_14.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.label_delay_ch_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.text_delay_ch_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_delay_ns_ch_15.setText(QCoreApplication.translate("MainWindow", u"ns", None))
        self.qb_delay_configure.setText(QCoreApplication.translate("MainWindow", u"Configure Delays", None))
        self.qb_delay_reset.setText(QCoreApplication.translate("MainWindow", u"Reset Delays", None))
        self.qrb_control_all.setText(QCoreApplication.translate("MainWindow", u"Control All Delays", None))
        self.groupBox_dacOverride.setTitle(QCoreApplication.translate("MainWindow", u"Octal DAC Overide", None))
        self.label_octalDac_ch_0.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.text_octalDac_ch_0.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_0.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_1.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.text_octalDac_ch_1.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_1.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.text_octalDac_ch_2.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_2.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.text_octalDac_ch_2.setPlaceholderText("")
        self.label_octalDac_ch_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.text_octalDac_ch_3.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_3.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.text_octalDac_ch_4.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_4.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.text_octalDac_ch_5.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_5.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_6.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.text_octalDac_ch_6.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_6.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.label_octalDac_ch_7.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.text_octalDac_ch_7.setInputMask(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.text_octalDac_ch_7.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
#if QT_CONFIG(tooltip)
        self.qb_octalDAC_configure.setToolTip(QCoreApplication.translate("MainWindow", u"Configure Octal DACs to values shown above", None))
#endif // QT_CONFIG(tooltip)
        self.qb_octalDAC_configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
#if QT_CONFIG(tooltip)
        self.qb_octalDAC_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset Octal DACs to values from currently loaded configuration", None))
#endif // QT_CONFIG(tooltip)
        self.qb_octalDAC_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.qb_octalDAC_updateConfig.setToolTip(QCoreApplication.translate("MainWindow", u"Update chipboard configuration to the overide settings. ", None))
#endif // QT_CONFIG(tooltip)
        self.qb_octalDAC_updateConfig.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.groupBox_misc.setTitle(QCoreApplication.translate("MainWindow", u"Misc. ", None))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.chipboard_tab), QCoreApplication.translate("MainWindow", u"Chipboard Settings", None))
        self.configureChip.setText(QCoreApplication.translate("MainWindow", u"Configure Chipboard", None))
        self.menutest.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

