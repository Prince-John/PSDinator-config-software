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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1398, 829)
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
        self.tabWidgets.setTabPosition(QTabWidget.North)
        self.tabWidgets.setTabShape(QTabWidget.Rounded)
        self.tabWidgets.setElideMode(Qt.ElideLeft)
        self.tabWidgets.setMovable(True)
        self.cfd_tab = QWidget()
        self.cfd_tab.setObjectName(u"cfd_tab")
        self.layoutWidget = QWidget(self.cfd_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 580, 461, 41))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_3)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_29.addWidget(self.label_2)

        self.qcb_cfd_testPoint = QComboBox(self.layoutWidget)
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.addItem("")
        self.qcb_cfd_testPoint.setObjectName(u"qcb_cfd_testPoint")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.qcb_cfd_testPoint.sizePolicy().hasHeightForWidth())
        self.qcb_cfd_testPoint.setSizePolicy(sizePolicy5)

        self.horizontalLayout_29.addWidget(self.qcb_cfd_testPoint)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_29.addWidget(self.label_7)

        self.qcb_cfd_testPointChannel = QComboBox(self.layoutWidget)
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

        self.pulseRST_L = QPushButton(self.cfd_tab)
        self.pulseRST_L.setObjectName(u"pulseRST_L")
        self.pulseRST_L.setGeometry(QRect(20, 550, 131, 32))
        self.groupBox_cfd_global_settings = QGroupBox(self.cfd_tab)
        self.groupBox_cfd_global_settings.setObjectName(u"groupBox_cfd_global_settings")
        self.groupBox_cfd_global_settings.setEnabled(True)
        self.groupBox_cfd_global_settings.setGeometry(QRect(10, 20, 241, 491))
        self.groupBox_cfd_global_settings.setFlat(False)
        self.groupBox_cfd_global_settings.setCheckable(False)
        self.layoutWidget_2 = QWidget(self.groupBox_cfd_global_settings)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 30, 224, 441))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.nowlinMode = QComboBox(self.layoutWidget_2)
        self.nowlinMode.addItem("")
        self.nowlinMode.addItem("")
        self.nowlinMode.setObjectName(u"nowlinMode")
        sizePolicy5.setHeightForWidth(self.nowlinMode.sizePolicy().hasHeightForWidth())
        self.nowlinMode.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.nowlinMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.nowlinDelay = QComboBox(self.layoutWidget_2)
        self.nowlinDelay.addItem("")
        self.nowlinDelay.addItem("")
        self.nowlinDelay.setObjectName(u"nowlinDelay")
        sizePolicy5.setHeightForWidth(self.nowlinDelay.sizePolicy().hasHeightForWidth())
        self.nowlinDelay.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.nowlinDelay)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.LockoutDAC = QLineEdit(self.layoutWidget_2)
        self.LockoutDAC.setObjectName(u"LockoutDAC")
        sizePolicy5.setHeightForWidth(self.LockoutDAC.sizePolicy().hasHeightForWidth())
        self.LockoutDAC.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.LockoutDAC)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lockoutMode = QComboBox(self.layoutWidget_2)
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.setObjectName(u"lockoutMode")
        sizePolicy5.setHeightForWidth(self.lockoutMode.sizePolicy().hasHeightForWidth())
        self.lockoutMode.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.lockoutMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.CFDPulseWidth = QComboBox(self.layoutWidget_2)
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.setObjectName(u"CFDPulseWidth")

        self.horizontalLayout_8.addWidget(self.CFDPulseWidth)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.AgndTrim = QComboBox(self.layoutWidget_2)
        self.AgndTrim.addItem("")
        self.AgndTrim.setObjectName(u"AgndTrim")

        self.horizontalLayout_9.addWidget(self.AgndTrim)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.negativePolarity = QCheckBox(self.layoutWidget_2)
        self.negativePolarity.setObjectName(u"negativePolarity")

        self.verticalLayout_2.addWidget(self.negativePolarity)

        self.globalMode = QCheckBox(self.layoutWidget_2)
        self.globalMode.setObjectName(u"globalMode")

        self.verticalLayout_2.addWidget(self.globalMode)

        self.LEOutEnable = QCheckBox(self.layoutWidget_2)
        self.LEOutEnable.setObjectName(u"LEOutEnable")

        self.verticalLayout_2.addWidget(self.LEOutEnable)

        self.globalEnable = QCheckBox(self.layoutWidget_2)
        self.globalEnable.setObjectName(u"globalEnable")

        self.verticalLayout_2.addWidget(self.globalEnable)

        self.groupBox_cfd_individual_ch_settings = QGroupBox(self.cfd_tab)
        self.groupBox_cfd_individual_ch_settings.setObjectName(u"groupBox_cfd_individual_ch_settings")
        self.groupBox_cfd_individual_ch_settings.setGeometry(QRect(330, 10, 401, 551))
        self.gridLayoutWidget = QWidget(self.groupBox_cfd_individual_ch_settings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 30, 401, 521))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.leadingEdgeDAC_15 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_15.setObjectName(u"leadingEdgeDAC_15")
        self.leadingEdgeDAC_15.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_15.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_15.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_15, 16, 1, 1, 1)

        self.signBit_13 = QCheckBox(self.gridLayoutWidget)
        self.signBit_13.setObjectName(u"signBit_13")
        sizePolicy5.setHeightForWidth(self.signBit_13.sizePolicy().hasHeightForWidth())
        self.signBit_13.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_13, 14, 3, 1, 1)

        self.enableDAC_01 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_01.setObjectName(u"enableDAC_01")
        sizePolicy5.setHeightForWidth(self.enableDAC_01.sizePolicy().hasHeightForWidth())
        self.enableDAC_01.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_01, 2, 2, 1, 1)

        self.leadingEdgeDAC_13 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_13.setObjectName(u"leadingEdgeDAC_13")
        self.leadingEdgeDAC_13.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_13.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_13.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_13, 14, 1, 1, 1)

        self.leadingEdgeDAC_14 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_14.setObjectName(u"leadingEdgeDAC_14")
        self.leadingEdgeDAC_14.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_14.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_14.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_14, 15, 1, 1, 1)

        self.enableDAC_08 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_08.setObjectName(u"enableDAC_08")
        sizePolicy5.setHeightForWidth(self.enableDAC_08.sizePolicy().hasHeightForWidth())
        self.enableDAC_08.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_08, 9, 2, 1, 1)

        self.label_channel_header = QLabel(self.gridLayoutWidget)
        self.label_channel_header.setObjectName(u"label_channel_header")

        self.gridLayout_2.addWidget(self.label_channel_header, 0, 0, 1, 1)

        self.signBit_all = QCheckBox(self.gridLayoutWidget)
        self.signBit_all.setObjectName(u"signBit_all")

        self.gridLayout_2.addWidget(self.signBit_all, 0, 3, 1, 1)

        self.label_leading_edge_dac_header = QLabel(self.gridLayoutWidget)
        self.label_leading_edge_dac_header.setObjectName(u"label_leading_edge_dac_header")

        self.gridLayout_2.addWidget(self.label_leading_edge_dac_header, 0, 1, 1, 1)

        self.leadingEdgeDAC_05 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_05.setObjectName(u"leadingEdgeDAC_05")
        self.leadingEdgeDAC_05.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_05.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_05.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_05, 6, 1, 1, 1)

        self.enableDAC_05 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_05.setObjectName(u"enableDAC_05")
        sizePolicy5.setHeightForWidth(self.enableDAC_05.sizePolicy().hasHeightForWidth())
        self.enableDAC_05.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_05, 6, 2, 1, 1)

        self.enableDAC_02 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_02.setObjectName(u"enableDAC_02")
        sizePolicy5.setHeightForWidth(self.enableDAC_02.sizePolicy().hasHeightForWidth())
        self.enableDAC_02.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_02, 3, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 12, 0, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 15, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)

        self.enableDAC_10 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_10.setObjectName(u"enableDAC_10")
        sizePolicy5.setHeightForWidth(self.enableDAC_10.sizePolicy().hasHeightForWidth())
        self.enableDAC_10.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_10, 11, 2, 1, 1)

        self.signBit_02 = QCheckBox(self.gridLayoutWidget)
        self.signBit_02.setObjectName(u"signBit_02")
        sizePolicy5.setHeightForWidth(self.signBit_02.sizePolicy().hasHeightForWidth())
        self.signBit_02.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_02, 3, 3, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 14, 0, 1, 1)

        self.leadingEdgeDAC_09 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_09.setObjectName(u"leadingEdgeDAC_09")
        self.leadingEdgeDAC_09.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_09.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_09.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_09, 10, 1, 1, 1)

        self.signBit_06 = QCheckBox(self.gridLayoutWidget)
        self.signBit_06.setObjectName(u"signBit_06")
        sizePolicy5.setHeightForWidth(self.signBit_06.sizePolicy().hasHeightForWidth())
        self.signBit_06.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_06, 7, 3, 1, 1)

        self.enableDAC_04 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_04.setObjectName(u"enableDAC_04")
        sizePolicy5.setHeightForWidth(self.enableDAC_04.sizePolicy().hasHeightForWidth())
        self.enableDAC_04.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_04, 5, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.leadingEdgeDAC_02 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_02.setObjectName(u"leadingEdgeDAC_02")
        self.leadingEdgeDAC_02.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_02.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_02.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_02, 3, 1, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_2.addWidget(self.label_48, 11, 0, 1, 1)

        self.signBit_11 = QCheckBox(self.gridLayoutWidget)
        self.signBit_11.setObjectName(u"signBit_11")
        sizePolicy5.setHeightForWidth(self.signBit_11.sizePolicy().hasHeightForWidth())
        self.signBit_11.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_11, 12, 3, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 4, 0, 1, 1)

        self.enableDAC_00 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_00.setObjectName(u"enableDAC_00")
        sizePolicy5.setHeightForWidth(self.enableDAC_00.sizePolicy().hasHeightForWidth())
        self.enableDAC_00.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_00, 1, 2, 1, 1)

        self.signBit_09 = QCheckBox(self.gridLayoutWidget)
        self.signBit_09.setObjectName(u"signBit_09")
        sizePolicy5.setHeightForWidth(self.signBit_09.sizePolicy().hasHeightForWidth())
        self.signBit_09.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_09, 10, 3, 1, 1)

        self.signBit_01 = QCheckBox(self.gridLayoutWidget)
        self.signBit_01.setObjectName(u"signBit_01")
        sizePolicy5.setHeightForWidth(self.signBit_01.sizePolicy().hasHeightForWidth())
        self.signBit_01.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_01, 2, 3, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.signBit_10 = QCheckBox(self.gridLayoutWidget)
        self.signBit_10.setObjectName(u"signBit_10")
        sizePolicy5.setHeightForWidth(self.signBit_10.sizePolicy().hasHeightForWidth())
        self.signBit_10.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_10, 11, 3, 1, 1)

        self.enableDAC_12 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_12.setObjectName(u"enableDAC_12")
        sizePolicy5.setHeightForWidth(self.enableDAC_12.sizePolicy().hasHeightForWidth())
        self.enableDAC_12.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_12, 13, 2, 1, 1)

        self.enableDAC_15 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_15.setObjectName(u"enableDAC_15")
        sizePolicy5.setHeightForWidth(self.enableDAC_15.sizePolicy().hasHeightForWidth())
        self.enableDAC_15.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_15, 16, 2, 1, 1)

        self.signBit_00 = QCheckBox(self.gridLayoutWidget)
        self.signBit_00.setObjectName(u"signBit_00")
        sizePolicy5.setHeightForWidth(self.signBit_00.sizePolicy().hasHeightForWidth())
        self.signBit_00.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_00, 1, 3, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 16, 0, 1, 1)

        self.signBit_08 = QCheckBox(self.gridLayoutWidget)
        self.signBit_08.setObjectName(u"signBit_08")
        sizePolicy5.setHeightForWidth(self.signBit_08.sizePolicy().hasHeightForWidth())
        self.signBit_08.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_08, 9, 3, 1, 1)

        self.enableDAC_all = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_all.setObjectName(u"enableDAC_all")

        self.gridLayout_2.addWidget(self.enableDAC_all, 0, 2, 1, 1)

        self.label_54 = QLabel(self.gridLayoutWidget)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_2.addWidget(self.label_54, 7, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 13, 0, 1, 1)

        self.enableDAC_11 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_11.setObjectName(u"enableDAC_11")
        sizePolicy5.setHeightForWidth(self.enableDAC_11.sizePolicy().hasHeightForWidth())
        self.enableDAC_11.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_11, 12, 2, 1, 1)

        self.signBit_15 = QCheckBox(self.gridLayoutWidget)
        self.signBit_15.setObjectName(u"signBit_15")
        sizePolicy5.setHeightForWidth(self.signBit_15.sizePolicy().hasHeightForWidth())
        self.signBit_15.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_15, 16, 3, 1, 1)

        self.enableDAC_13 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_13.setObjectName(u"enableDAC_13")
        sizePolicy5.setHeightForWidth(self.enableDAC_13.sizePolicy().hasHeightForWidth())
        self.enableDAC_13.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_13, 14, 2, 1, 1)

        self.enableDAC_07 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_07.setObjectName(u"enableDAC_07")
        sizePolicy5.setHeightForWidth(self.enableDAC_07.sizePolicy().hasHeightForWidth())
        self.enableDAC_07.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_07, 8, 2, 1, 1)

        self.enableDAC_09 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_09.setObjectName(u"enableDAC_09")
        sizePolicy5.setHeightForWidth(self.enableDAC_09.sizePolicy().hasHeightForWidth())
        self.enableDAC_09.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_09, 10, 2, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 10, 0, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_2.addWidget(self.label_50, 6, 0, 1, 1)

        self.leadingEdgeDAC_11 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_11.setObjectName(u"leadingEdgeDAC_11")
        self.leadingEdgeDAC_11.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_11.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_11.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_11, 12, 1, 1, 1)

        self.signBit_07 = QCheckBox(self.gridLayoutWidget)
        self.signBit_07.setObjectName(u"signBit_07")
        sizePolicy5.setHeightForWidth(self.signBit_07.sizePolicy().hasHeightForWidth())
        self.signBit_07.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_07, 8, 3, 1, 1)

        self.leadingEdgeDAC_06 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_06.setObjectName(u"leadingEdgeDAC_06")
        self.leadingEdgeDAC_06.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_06.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_06.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_06, 7, 1, 1, 1)

        self.signBit_04 = QCheckBox(self.gridLayoutWidget)
        self.signBit_04.setObjectName(u"signBit_04")
        sizePolicy5.setHeightForWidth(self.signBit_04.sizePolicy().hasHeightForWidth())
        self.signBit_04.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_04, 5, 3, 1, 1)

        self.leadingEdgeDAC_07 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_07.setObjectName(u"leadingEdgeDAC_07")
        self.leadingEdgeDAC_07.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_07.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_07.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_07, 8, 1, 1, 1)

        self.enableDAC_03 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_03.setObjectName(u"enableDAC_03")
        sizePolicy5.setHeightForWidth(self.enableDAC_03.sizePolicy().hasHeightForWidth())
        self.enableDAC_03.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_03, 4, 2, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_2.addWidget(self.label_44, 9, 0, 1, 1)

        self.leadingEdgeDAC_01 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_01.setObjectName(u"leadingEdgeDAC_01")
        self.leadingEdgeDAC_01.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_01.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_01.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_01, 2, 1, 1, 1)

        self.signBit_05 = QCheckBox(self.gridLayoutWidget)
        self.signBit_05.setObjectName(u"signBit_05")

        self.gridLayout_2.addWidget(self.signBit_05, 6, 3, 1, 1)

        self.leadingEdgeDAC_12 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_12.setObjectName(u"leadingEdgeDAC_12")
        self.leadingEdgeDAC_12.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_12.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_12.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_12, 13, 1, 1, 1)

        self.signBit_14 = QCheckBox(self.gridLayoutWidget)
        self.signBit_14.setObjectName(u"signBit_14")
        sizePolicy5.setHeightForWidth(self.signBit_14.sizePolicy().hasHeightForWidth())
        self.signBit_14.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_14, 15, 3, 1, 1)

        self.enableDAC_06 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_06.setObjectName(u"enableDAC_06")
        sizePolicy5.setHeightForWidth(self.enableDAC_06.sizePolicy().hasHeightForWidth())
        self.enableDAC_06.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_06, 7, 2, 1, 1)

        self.leadingEdgeDAC_03 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_03.setObjectName(u"leadingEdgeDAC_03")
        self.leadingEdgeDAC_03.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_03.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_03.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_03, 4, 1, 1, 1)

        self.enableDAC_14 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_14.setObjectName(u"enableDAC_14")
        sizePolicy5.setHeightForWidth(self.enableDAC_14.sizePolicy().hasHeightForWidth())
        self.enableDAC_14.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.enableDAC_14, 15, 2, 1, 1)

        self.leadingEdgeDAC_00 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_00.setObjectName(u"leadingEdgeDAC_00")
        self.leadingEdgeDAC_00.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_00.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_00.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_00, 1, 1, 1, 1)

        self.signBit_03 = QCheckBox(self.gridLayoutWidget)
        self.signBit_03.setObjectName(u"signBit_03")
        sizePolicy5.setHeightForWidth(self.signBit_03.sizePolicy().hasHeightForWidth())
        self.signBit_03.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_03, 4, 3, 1, 1)

        self.leadingEdgeDAC_04 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_04.setObjectName(u"leadingEdgeDAC_04")
        self.leadingEdgeDAC_04.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_04.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_04.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_04, 5, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 8, 0, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_2.addWidget(self.label_52, 2, 0, 1, 1)

        self.signBit_12 = QCheckBox(self.gridLayoutWidget)
        self.signBit_12.setObjectName(u"signBit_12")
        sizePolicy5.setHeightForWidth(self.signBit_12.sizePolicy().hasHeightForWidth())
        self.signBit_12.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.signBit_12, 13, 3, 1, 1)

        self.leadingEdgeDAC_08 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_08.setObjectName(u"leadingEdgeDAC_08")
        self.leadingEdgeDAC_08.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_08.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_08.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_08, 9, 1, 1, 1)

        self.leadingEdgeDAC_10 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_10.setObjectName(u"leadingEdgeDAC_10")
        self.leadingEdgeDAC_10.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_10.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_10.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_10, 11, 1, 1, 1)

        self.configureChip_2 = QPushButton(self.cfd_tab)
        self.configureChip_2.setObjectName(u"configureChip_2")
        self.configureChip_2.setGeometry(QRect(20, 590, 171, 32))
        self.tabWidgets.addTab(self.cfd_tab, "")
        self.psd_tab = QWidget()
        self.psd_tab.setObjectName(u"psd_tab")
        self.horizontalLayoutWidget = QWidget(self.psd_tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 60, 154, 32))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_psd_polarity = QLabel(self.horizontalLayoutWidget)
        self.label_psd_polarity.setObjectName(u"label_psd_polarity")

        self.horizontalLayout_10.addWidget(self.label_psd_polarity)

        self.comboBox_psd_polarity = QComboBox(self.horizontalLayoutWidget)
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.setObjectName(u"comboBox_psd_polarity")

        self.horizontalLayout_10.addWidget(self.comboBox_psd_polarity)

        self.horizontalLayoutWidget_2 = QWidget(self.psd_tab)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(80, 100, 121, 32))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_psd_bias = QLabel(self.horizontalLayoutWidget_2)
        self.label_psd_bias.setObjectName(u"label_psd_bias")

        self.horizontalLayout_11.addWidget(self.label_psd_bias)

        self.comboBox_psd_bias = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.setObjectName(u"comboBox_psd_bias")

        self.horizontalLayout_11.addWidget(self.comboBox_psd_bias)

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
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_15.setFont(font1)

        self.horizontal_layout_delay_label.addWidget(self.label_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_delay_label.addItem(self.horizontalSpacer_2)

        self.label_21 = QLabel(self.groupBox_delays)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_0.setSizePolicy(sizePolicy7)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.text_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_0.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_1.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_1.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_2.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_2.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_3.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_3.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_4.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_4.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_5.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_5.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_6.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_6.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_7.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_7.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_8.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_8.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_9.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_9.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_10.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_10.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_11.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_11.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_12.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_12.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_13.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_13.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_14.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_14.setSizePolicy(sizePolicy8)
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
        sizePolicy7.setHeightForWidth(self.slider_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_15.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.text_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_15.setSizePolicy(sizePolicy8)
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
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.groupBox_dacOverride.sizePolicy().hasHeightForWidth())
        self.groupBox_dacOverride.setSizePolicy(sizePolicy9)
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
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_0.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_0.setMinimumSize(QSize(21, 0))
        font2 = QFont()
        font2.setBold(True)
        self.label_octalDac_ch_0.setFont(font2)
        self.label_octalDac_ch_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_0.addWidget(self.label_octalDac_ch_0)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slider_octalDac_ch_0 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_0.setObjectName(u"slider_octalDac_ch_0")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_0.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_0.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_0.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_1.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_1.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_1.setFont(font2)
        self.label_octalDac_ch_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_1.addWidget(self.label_octalDac_ch_1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.slider_octalDac_ch_1 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_1.setObjectName(u"slider_octalDac_ch_1")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_1.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_1.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_1.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_2.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_2.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_2.setFont(font2)
        self.label_octalDac_ch_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_2.addWidget(self.label_octalDac_ch_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.slider_octalDac_ch_2 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_2.setObjectName(u"slider_octalDac_ch_2")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_2.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_2.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_2.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_3.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_3.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_3.setFont(font2)
        self.label_octalDac_ch_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_3.addWidget(self.label_octalDac_ch_3)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.slider_octalDac_ch_3 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_3.setObjectName(u"slider_octalDac_ch_3")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_3.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_3.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_3.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_4.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_4.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_4.setFont(font2)
        self.label_octalDac_ch_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_4.addWidget(self.label_octalDac_ch_4)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.slider_octalDac_ch_4 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_4.setObjectName(u"slider_octalDac_ch_4")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_4.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_4.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_4.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_5.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_5.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_5.setFont(font2)
        self.label_octalDac_ch_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_5.addWidget(self.label_octalDac_ch_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.slider_octalDac_ch_5 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_5.setObjectName(u"slider_octalDac_ch_5")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_5.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_5.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_5.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_6.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_6.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_6.setFont(font2)
        self.label_octalDac_ch_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_6.addWidget(self.label_octalDac_ch_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.slider_octalDac_ch_6 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_6.setObjectName(u"slider_octalDac_ch_6")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_6.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_6.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_6.setSizePolicy(sizePolicy5)
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
        sizePolicy10.setHeightForWidth(self.label_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.label_octalDac_ch_7.setSizePolicy(sizePolicy10)
        self.label_octalDac_ch_7.setMinimumSize(QSize(21, 0))
        self.label_octalDac_ch_7.setFont(font2)
        self.label_octalDac_ch_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_octalDac_ch_7.addWidget(self.label_octalDac_ch_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.slider_octalDac_ch_7 = QSlider(self.groupBox_dacOverride)
        self.slider_octalDac_ch_7.setObjectName(u"slider_octalDac_ch_7")
        sizePolicy11.setHeightForWidth(self.slider_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.slider_octalDac_ch_7.setSizePolicy(sizePolicy11)
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
        sizePolicy5.setHeightForWidth(self.text_octalDac_ch_7.sizePolicy().hasHeightForWidth())
        self.text_octalDac_ch_7.setSizePolicy(sizePolicy5)
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
        self.menubar.setGeometry(QRect(0, 0, 1398, 24))
        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
#if QT_CONFIG(shortcut)
        self.label_11.setBuddy(self.chipNumber)
        self.label_2.setBuddy(self.qcb_cfd_testPoint)
        self.label_7.setBuddy(self.qcb_cfd_testPointChannel)
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

        self.tabWidgets.setCurrentIndex(2)
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

#if QT_CONFIG(tooltip)
        self.pulseRST_L.setToolTip(QCoreApplication.translate("MainWindow", u"Applies a reset signal to the CFD chip, pulses RST_L", None))
#endif // QT_CONFIG(tooltip)
        self.pulseRST_L.setText(QCoreApplication.translate("MainWindow", u"Reset CFD ASIC", None))
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
        self.globalEnable.setText(QCoreApplication.translate("MainWindow", u"Global Enable", None))
        self.groupBox_cfd_individual_ch_settings.setTitle(QCoreApplication.translate("MainWindow", u"CFD individual channel threshold settings", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter value in Hex(Max 5 bits 0x1F)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
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
        self.configureChip_2.setText(QCoreApplication.translate("MainWindow", u"Configure Only CFD Chip", None))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.cfd_tab), QCoreApplication.translate("MainWindow", u"CFD", None))
        self.label_psd_polarity.setText(QCoreApplication.translate("MainWindow", u"Polarity", None))
        self.comboBox_psd_polarity.setItemText(0, QCoreApplication.translate("MainWindow", u"positive", None))
        self.comboBox_psd_polarity.setItemText(1, QCoreApplication.translate("MainWindow", u"negative", None))

        self.label_psd_bias.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.comboBox_psd_bias.setItemText(0, QCoreApplication.translate("MainWindow", u"high", None))
        self.comboBox_psd_bias.setItemText(1, QCoreApplication.translate("MainWindow", u"low", None))

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

