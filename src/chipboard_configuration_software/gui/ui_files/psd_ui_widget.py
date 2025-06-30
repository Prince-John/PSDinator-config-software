# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'psd_ui_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)

class Ui_Widget_Psd(object):
    def setupUi(self, Widget_Psd):
        if not Widget_Psd.objectName():
            Widget_Psd.setObjectName(u"Widget_Psd")
        Widget_Psd.setWindowModality(Qt.WindowModality.WindowModal)
        Widget_Psd.resize(855, 759)
        self.horizontalLayout_2 = QHBoxLayout(Widget_Psd)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(-1)
        self.gridLayout_3.setVerticalSpacing(6)
        self.splitter = QSplitter(Widget_Psd)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_psd_auto_veto_dac_2 = QLabel(self.splitter)
        self.label_psd_auto_veto_dac_2.setObjectName(u"label_psd_auto_veto_dac_2")
        self.label_psd_auto_veto_dac_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.label_psd_auto_veto_dac_2)
        self.horizontalSlider_psd_auto_veto_dac = QSlider(self.splitter)
        self.horizontalSlider_psd_auto_veto_dac.setObjectName(u"horizontalSlider_psd_auto_veto_dac")
        self.horizontalSlider_psd_auto_veto_dac.setMaximum(1023)
        self.horizontalSlider_psd_auto_veto_dac.setSingleStep(10)
        self.horizontalSlider_psd_auto_veto_dac.setPageStep(128)
        self.horizontalSlider_psd_auto_veto_dac.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_auto_veto_dac.setInvertedControls(False)
        self.horizontalSlider_psd_auto_veto_dac.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_auto_veto_dac.setTickInterval(128)
        self.splitter.addWidget(self.horizontalSlider_psd_auto_veto_dac)
        self.text_psd_auto_veto_dac = QLineEdit(self.splitter)
        self.text_psd_auto_veto_dac.setObjectName(u"text_psd_auto_veto_dac")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_psd_auto_veto_dac.sizePolicy().hasHeightForWidth())
        self.text_psd_auto_veto_dac.setSizePolicy(sizePolicy)
        self.text_psd_auto_veto_dac.setMinimumSize(QSize(21, 0))
        self.text_psd_auto_veto_dac.setMaximumSize(QSize(50, 16777215))
        self.text_psd_auto_veto_dac.setBaseSize(QSize(30, 0))
        self.text_psd_auto_veto_dac.setMaxLength(6)
        self.text_psd_auto_veto_dac.setCursorPosition(6)
        self.text_psd_auto_veto_dac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_psd_auto_veto_dac.setClearButtonEnabled(False)
        self.splitter.addWidget(self.text_psd_auto_veto_dac)

        self.gridLayout_3.addWidget(self.splitter, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 3, 1, 1)

        self.verticalGroupBox = QGroupBox(Widget_Psd)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy1)
        self.verticalGroupBox.setMinimumSize(QSize(125, 341))
        self.verticalGroupBox.setBaseSize(QSize(0, 400))
        self.verticalGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalGroupBox.setFlat(False)
        self.verticalGroupBox.setCheckable(False)
        self.gridLayout_7 = QGridLayout(self.verticalGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.checkBox_psd_channel_enable_10 = QCheckBox(self.verticalGroupBox)
        self.checkBox_psd_channel_enable_10.setObjectName(u"checkBox_psd_channel_enable_10")
        self.checkBox_psd_channel_enable_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

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
        font = QFont()
        font.setBold(True)
        self.label_34.setFont(font)

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


        self.gridLayout_3.addWidget(self.verticalGroupBox, 0, 1, 7, 2)

        self.line_12 = QFrame(Widget_Psd)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_12, 8, 0, 1, 4)

        self.horizontalGroupBox_5 = QGroupBox(Widget_Psd)
        self.horizontalGroupBox_5.setObjectName(u"horizontalGroupBox_5")
        sizePolicy1.setHeightForWidth(self.horizontalGroupBox_5.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_5.setSizePolicy(sizePolicy1)
        self.horizontalGroupBox_5.setMinimumSize(QSize(821, 251))
        self.horizontalGroupBox_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalGroupBox_5.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.horizontalGroupBox_5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 12)
        self.line_10 = QFrame(self.horizontalGroupBox_5)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_10, 0, 3, 1, 1)

        self.groupBox_subchannel_B = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_B.setObjectName(u"groupBox_subchannel_B")
        self.groupBox_subchannel_B.setMinimumSize(QSize(270, 160))
        self.groupBox_subchannel_B.setFlat(True)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_subchannel_B)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_24 = QLabel(self.groupBox_subchannel_B)
        self.label_24.setObjectName(u"label_24")
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label_24.setFont(font1)

        self.horizontalLayout_32.addWidget(self.label_24)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_39)

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
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_25.setFont(font2)

        self.horizontalLayout_36.addWidget(self.label_25)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_40)

        self.label_psd_delay_range_b = QLabel(self.groupBox_subchannel_B)
        self.label_psd_delay_range_b.setObjectName(u"label_psd_delay_range_b")
        self.label_psd_delay_range_b.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_delay_range_b.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_psd_delay_range_b)

        self.comboBox_psd_delay_range_b = QComboBox(self.groupBox_subchannel_B)
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.addItem("")
        self.comboBox_psd_delay_range_b.setObjectName(u"comboBox_psd_delay_range_b")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_psd_delay_range_b.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_b.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_delay_dac_b.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_delay_dac_b.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_b.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_delay_dac_b.setTickInterval(128)

        self.horizontalLayout_37.addWidget(self.horizontalSlider_psd_delay_dac_b)

        self.text_psd_delay_dac_b = QLineEdit(self.groupBox_subchannel_B)
        self.text_psd_delay_dac_b.setObjectName(u"text_psd_delay_dac_b")
        sizePolicy.setHeightForWidth(self.text_psd_delay_dac_b.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_b.setSizePolicy(sizePolicy)
        self.text_psd_delay_dac_b.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_b.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_b.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_b.setMaxLength(6)
        self.text_psd_delay_dac_b.setCursorPosition(6)
        self.text_psd_delay_dac_b.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_26.setFont(font2)

        self.horizontalLayout_38.addWidget(self.label_26)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_41)

        self.label_psd_width_range_b = QLabel(self.groupBox_subchannel_B)
        self.label_psd_width_range_b.setObjectName(u"label_psd_width_range_b")
        self.label_psd_width_range_b.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_width_range_b.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_psd_width_range_b)

        self.comboBox_psd_width_range_b = QComboBox(self.groupBox_subchannel_B)
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.addItem("")
        self.comboBox_psd_width_range_b.setObjectName(u"comboBox_psd_width_range_b")
        sizePolicy2.setHeightForWidth(self.comboBox_psd_width_range_b.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_b.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_width_dac_b.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_width_dac_b.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_b.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_width_dac_b.setTickInterval(128)

        self.horizontalLayout_39.addWidget(self.horizontalSlider_psd_width_dac_b)

        self.text_psd_width_dac_b = QLineEdit(self.groupBox_subchannel_B)
        self.text_psd_width_dac_b.setObjectName(u"text_psd_width_dac_b")
        sizePolicy.setHeightForWidth(self.text_psd_width_dac_b.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_b.setSizePolicy(sizePolicy)
        self.text_psd_width_dac_b.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_b.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_b.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_b.setMaxLength(6)
        self.text_psd_width_dac_b.setCursorPosition(6)
        self.text_psd_width_dac_b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_psd_width_dac_b.setClearButtonEnabled(False)

        self.horizontalLayout_39.addWidget(self.text_psd_width_dac_b)


        self.verticalLayout_10.addLayout(self.horizontalLayout_39)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)


        self.gridLayout_2.addWidget(self.groupBox_subchannel_B, 0, 6, 1, 1)

        self.line_11 = QFrame(self.horizontalGroupBox_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_11, 0, 8, 1, 1)

        self.groupBox_subchannel_A = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_A.setObjectName(u"groupBox_subchannel_A")
        self.groupBox_subchannel_A.setMinimumSize(QSize(270, 160))
        self.groupBox_subchannel_A.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_subchannel_A)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_17 = QLabel(self.groupBox_subchannel_A)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_17)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_38)

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
        self.label_19.setFont(font2)

        self.horizontalLayout_31.addWidget(self.label_19)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)

        self.label_psd_delay_range_a = QLabel(self.groupBox_subchannel_A)
        self.label_psd_delay_range_a.setObjectName(u"label_psd_delay_range_a")
        self.label_psd_delay_range_a.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_delay_range_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_psd_delay_range_a)

        self.comboBox_psd_delay_range_a = QComboBox(self.groupBox_subchannel_A)
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.addItem("")
        self.comboBox_psd_delay_range_a.setObjectName(u"comboBox_psd_delay_range_a")
        sizePolicy2.setHeightForWidth(self.comboBox_psd_delay_range_a.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_a.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_delay_dac_a.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_delay_dac_a.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_a.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_delay_dac_a.setTickInterval(128)

        self.horizontalLayout_33.addWidget(self.horizontalSlider_psd_delay_dac_a)

        self.text_psd_delay_dac_a = QLineEdit(self.groupBox_subchannel_A)
        self.text_psd_delay_dac_a.setObjectName(u"text_psd_delay_dac_a")
        sizePolicy.setHeightForWidth(self.text_psd_delay_dac_a.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_a.setSizePolicy(sizePolicy)
        self.text_psd_delay_dac_a.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_a.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_a.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_a.setMaxLength(6)
        self.text_psd_delay_dac_a.setCursorPosition(6)
        self.text_psd_delay_dac_a.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_23.setFont(font2)

        self.horizontalLayout_34.addWidget(self.label_23)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_37)

        self.label_psd_width_range_a = QLabel(self.groupBox_subchannel_A)
        self.label_psd_width_range_a.setObjectName(u"label_psd_width_range_a")
        self.label_psd_width_range_a.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_width_range_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_psd_width_range_a)

        self.comboBox_psd_width_range_a = QComboBox(self.groupBox_subchannel_A)
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.addItem("")
        self.comboBox_psd_width_range_a.setObjectName(u"comboBox_psd_width_range_a")
        sizePolicy2.setHeightForWidth(self.comboBox_psd_width_range_a.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_a.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_width_dac_a.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_width_dac_a.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_a.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_width_dac_a.setTickInterval(128)

        self.horizontalLayout_35.addWidget(self.horizontalSlider_psd_width_dac_a)

        self.text_psd_width_dac_a = QLineEdit(self.groupBox_subchannel_A)
        self.text_psd_width_dac_a.setObjectName(u"text_psd_width_dac_a")
        sizePolicy.setHeightForWidth(self.text_psd_width_dac_a.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_a.setSizePolicy(sizePolicy)
        self.text_psd_width_dac_a.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_a.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_a.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_a.setMaxLength(6)
        self.text_psd_width_dac_a.setCursorPosition(6)
        self.text_psd_width_dac_a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_psd_width_dac_a.setClearButtonEnabled(False)

        self.horizontalLayout_35.addWidget(self.text_psd_width_dac_a)


        self.verticalLayout_6.addLayout(self.horizontalLayout_35)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_2.addWidget(self.groupBox_subchannel_A, 0, 1, 1, 1)

        self.groupBox_subchannel_C = QGroupBox(self.horizontalGroupBox_5)
        self.groupBox_subchannel_C.setObjectName(u"groupBox_subchannel_C")
        self.groupBox_subchannel_C.setMinimumSize(QSize(270, 160))
        self.groupBox_subchannel_C.setFlat(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_subchannel_C)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_27 = QLabel(self.groupBox_subchannel_C)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.horizontalLayout_40.addWidget(self.label_27)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_42)

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
        self.label_28.setFont(font2)

        self.horizontalLayout_41.addWidget(self.label_28)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_43)

        self.label_psd_delay_range_c = QLabel(self.groupBox_subchannel_C)
        self.label_psd_delay_range_c.setObjectName(u"label_psd_delay_range_c")
        self.label_psd_delay_range_c.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_delay_range_c.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_psd_delay_range_c)

        self.comboBox_psd_delay_range_c = QComboBox(self.groupBox_subchannel_C)
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.addItem("")
        self.comboBox_psd_delay_range_c.setObjectName(u"comboBox_psd_delay_range_c")
        sizePolicy2.setHeightForWidth(self.comboBox_psd_delay_range_c.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_delay_range_c.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_delay_dac_c.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_delay_dac_c.setInvertedControls(False)
        self.horizontalSlider_psd_delay_dac_c.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_delay_dac_c.setTickInterval(128)

        self.horizontalLayout_42.addWidget(self.horizontalSlider_psd_delay_dac_c)

        self.text_psd_delay_dac_c = QLineEdit(self.groupBox_subchannel_C)
        self.text_psd_delay_dac_c.setObjectName(u"text_psd_delay_dac_c")
        sizePolicy.setHeightForWidth(self.text_psd_delay_dac_c.sizePolicy().hasHeightForWidth())
        self.text_psd_delay_dac_c.setSizePolicy(sizePolicy)
        self.text_psd_delay_dac_c.setMinimumSize(QSize(21, 0))
        self.text_psd_delay_dac_c.setMaximumSize(QSize(50, 16777215))
        self.text_psd_delay_dac_c.setBaseSize(QSize(30, 0))
        self.text_psd_delay_dac_c.setMaxLength(6)
        self.text_psd_delay_dac_c.setCursorPosition(6)
        self.text_psd_delay_dac_c.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_29.setFont(font2)

        self.horizontalLayout_43.addWidget(self.label_29)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_44)

        self.label_psd_width_range_c = QLabel(self.groupBox_subchannel_C)
        self.label_psd_width_range_c.setObjectName(u"label_psd_width_range_c")
        self.label_psd_width_range_c.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_psd_width_range_c.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_psd_width_range_c)

        self.comboBox_psd_width_range_c = QComboBox(self.groupBox_subchannel_C)
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.addItem("")
        self.comboBox_psd_width_range_c.setObjectName(u"comboBox_psd_width_range_c")
        sizePolicy2.setHeightForWidth(self.comboBox_psd_width_range_c.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_width_range_c.setSizePolicy(sizePolicy2)
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
        self.horizontalSlider_psd_width_dac_c.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_psd_width_dac_c.setInvertedControls(False)
        self.horizontalSlider_psd_width_dac_c.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_psd_width_dac_c.setTickInterval(128)

        self.horizontalLayout_44.addWidget(self.horizontalSlider_psd_width_dac_c)

        self.text_psd_width_dac_c = QLineEdit(self.groupBox_subchannel_C)
        self.text_psd_width_dac_c.setObjectName(u"text_psd_width_dac_c")
        sizePolicy.setHeightForWidth(self.text_psd_width_dac_c.sizePolicy().hasHeightForWidth())
        self.text_psd_width_dac_c.setSizePolicy(sizePolicy)
        self.text_psd_width_dac_c.setMinimumSize(QSize(21, 0))
        self.text_psd_width_dac_c.setMaximumSize(QSize(50, 16777215))
        self.text_psd_width_dac_c.setBaseSize(QSize(30, 0))
        self.text_psd_width_dac_c.setMaxLength(6)
        self.text_psd_width_dac_c.setCursorPosition(6)
        self.text_psd_width_dac_c.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_psd_width_dac_c.setClearButtonEnabled(False)

        self.horizontalLayout_44.addWidget(self.text_psd_width_dac_c)


        self.verticalLayout_13.addLayout(self.horizontalLayout_44)


        self.verticalLayout_11.addLayout(self.verticalLayout_13)


        self.gridLayout_2.addWidget(self.groupBox_subchannel_C, 0, 9, 1, 1)


        self.gridLayout_3.addWidget(self.horizontalGroupBox_5, 7, 0, 1, 4)

        self.groupBox = QGroupBox(Widget_Psd)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setBaseSize(QSize(0, 120))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(-1, 12, -1, 12)
        self.label_psd_polarity = QLabel(self.groupBox)
        self.label_psd_polarity.setObjectName(u"label_psd_polarity")

        self.gridLayout_4.addWidget(self.label_psd_polarity, 0, 0, 1, 1)

        self.comboBox_psd_polarity = QComboBox(self.groupBox)
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.addItem("")
        self.comboBox_psd_polarity.setObjectName(u"comboBox_psd_polarity")

        self.gridLayout_4.addWidget(self.comboBox_psd_polarity, 0, 1, 1, 1)

        self.label_psd_bias_2 = QLabel(self.groupBox)
        self.label_psd_bias_2.setObjectName(u"label_psd_bias_2")

        self.gridLayout_4.addWidget(self.label_psd_bias_2, 1, 0, 1, 1)

        self.comboBox_psd_bias = QComboBox(self.groupBox)
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.addItem("")
        self.comboBox_psd_bias.setObjectName(u"comboBox_psd_bias")

        self.gridLayout_4.addWidget(self.comboBox_psd_bias, 1, 1, 1, 1)

        self.label_psd_trigger_mode = QLabel(self.groupBox)
        self.label_psd_trigger_mode.setObjectName(u"label_psd_trigger_mode")

        self.gridLayout_4.addWidget(self.label_psd_trigger_mode, 2, 0, 1, 1)

        self.comboBox_psd_trigger_mode = QComboBox(self.groupBox)
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.addItem("")
        self.comboBox_psd_trigger_mode.setObjectName(u"comboBox_psd_trigger_mode")

        self.gridLayout_4.addWidget(self.comboBox_psd_trigger_mode, 2, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox)
        self.label_35.setObjectName(u"label_35")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_35.setFont(font3)

        self.gridLayout_4.addWidget(self.label_35, 3, 0, 1, 1)

        self.comboBox_psd_vtc_range = QComboBox(self.groupBox)
        self.comboBox_psd_vtc_range.addItem("")
        self.comboBox_psd_vtc_range.addItem("")
        self.comboBox_psd_vtc_range.setObjectName(u"comboBox_psd_vtc_range")

        self.gridLayout_4.addWidget(self.comboBox_psd_vtc_range, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 3, 1, 1)

        self.pushButton_configure_psd = QPushButton(Widget_Psd)
        self.pushButton_configure_psd.setObjectName(u"pushButton_configure_psd")

        self.gridLayout_3.addWidget(self.pushButton_configure_psd, 9, 0, 1, 1)

        self.pushButton_reset_psd_ui = QPushButton(Widget_Psd)
        self.pushButton_reset_psd_ui.setObjectName(u"pushButton_reset_psd_ui")

        self.gridLayout_3.addWidget(self.pushButton_reset_psd_ui, 6, 3, 1, 1)

        self.groupBox_psd_test_mode = QGroupBox(Widget_Psd)
        self.groupBox_psd_test_mode.setObjectName(u"groupBox_psd_test_mode")
        sizePolicy1.setHeightForWidth(self.groupBox_psd_test_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_psd_test_mode.setSizePolicy(sizePolicy1)
        self.groupBox_psd_test_mode.setMinimumSize(QSize(0, 0))
        self.groupBox_psd_test_mode.setBaseSize(QSize(201, 0))
        self.gridLayout_5 = QGridLayout(self.groupBox_psd_test_mode)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(5)
        self.comboBox_psd_test_mode_channel_selection = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode_channel_selection.setObjectName(u"comboBox_psd_test_mode_channel_selection")
        sizePolicy1.setHeightForWidth(self.comboBox_psd_test_mode_channel_selection.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_test_mode_channel_selection.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.comboBox_psd_test_mode_channel_selection, 1, 1, 1, 2)

        self.label_37 = QLabel(self.groupBox_psd_test_mode)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_5.addWidget(self.label_37, 1, 0, 1, 1)

        self.comboBox_psd_test_mode = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode.addItem("")
        self.comboBox_psd_test_mode.addItem("")
        self.comboBox_psd_test_mode.setObjectName(u"comboBox_psd_test_mode")
        sizePolicy1.setHeightForWidth(self.comboBox_psd_test_mode.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_test_mode.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.comboBox_psd_test_mode, 0, 1, 1, 2)

        self.label_36 = QLabel(self.groupBox_psd_test_mode)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_38 = QLabel(self.groupBox_psd_test_mode)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_5.addWidget(self.label_38, 2, 0, 1, 1)

        self.comboBox_psd_test_mode_subchannel_selection = QComboBox(self.groupBox_psd_test_mode)
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.addItem("")
        self.comboBox_psd_test_mode_subchannel_selection.setObjectName(u"comboBox_psd_test_mode_subchannel_selection")
        sizePolicy1.setHeightForWidth(self.comboBox_psd_test_mode_subchannel_selection.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_test_mode_subchannel_selection.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.comboBox_psd_test_mode_subchannel_selection, 2, 1, 2, 2)

        self.pushButton_psd_test_mode_reset = QPushButton(self.groupBox_psd_test_mode)
        self.pushButton_psd_test_mode_reset.setObjectName(u"pushButton_psd_test_mode_reset")

        self.gridLayout_5.addWidget(self.pushButton_psd_test_mode_reset, 4, 1, 1, 1)

        self.pushButton_psd_test_mode_configure = QPushButton(self.groupBox_psd_test_mode)
        self.pushButton_psd_test_mode_configure.setObjectName(u"pushButton_psd_test_mode_configure")
        self.pushButton_psd_test_mode_configure.setMinimumSize(QSize(75, 0))

        self.gridLayout_5.addWidget(self.pushButton_psd_test_mode_configure, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_psd_test_mode, 0, 3, 1, 1)

        self.checkBox_psd_global_enable = QCheckBox(Widget_Psd)
        self.checkBox_psd_global_enable.setObjectName(u"checkBox_psd_global_enable")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.checkBox_psd_global_enable.setFont(font4)

        self.gridLayout_3.addWidget(self.checkBox_psd_global_enable, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_reset_all_dacs = QPushButton(Widget_Psd)
        self.pushButton_reset_all_dacs.setObjectName(u"pushButton_reset_all_dacs")

        self.gridLayout_3.addWidget(self.pushButton_reset_all_dacs, 5, 3, 1, 1)

        self.pushButton_continous_octal_dac_update = QPushButton(Widget_Psd)
        self.pushButton_continous_octal_dac_update.setObjectName(u"pushButton_continous_octal_dac_update")
        self.pushButton_continous_octal_dac_update.setCheckable(True)

        self.gridLayout_3.addWidget(self.pushButton_continous_octal_dac_update, 4, 3, 1, 1)

        self.groupBox_psd_offset_dac = QGroupBox(Widget_Psd)
        self.groupBox_psd_offset_dac.setObjectName(u"groupBox_psd_offset_dac")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_psd_offset_dac.sizePolicy().hasHeightForWidth())
        self.groupBox_psd_offset_dac.setSizePolicy(sizePolicy3)
        self.groupBox_psd_offset_dac.setMinimumSize(QSize(180, 270))
        self.groupBox_psd_offset_dac.setMaximumSize(QSize(3500, 16777215))
        self.groupBox_psd_offset_dac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_psd_offset_dac)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_33 = QLabel(self.groupBox_psd_offset_dac)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_47.addWidget(self.label_33, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_2)

        self.comboBox_psd_offset_dac_channel_selection = QComboBox(self.groupBox_psd_offset_dac)
        self.comboBox_psd_offset_dac_channel_selection.setObjectName(u"comboBox_psd_offset_dac_channel_selection")
        sizePolicy.setHeightForWidth(self.comboBox_psd_offset_dac_channel_selection.sizePolicy().hasHeightForWidth())
        self.comboBox_psd_offset_dac_channel_selection.setSizePolicy(sizePolicy)
        self.comboBox_psd_offset_dac_channel_selection.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_47.addWidget(self.comboBox_psd_offset_dac_channel_selection, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_17.addLayout(self.horizontalLayout_47)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_6 = QFrame(self.groupBox_psd_offset_dac)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 0, 2, 1, 2)

        self.verticalSlider_psd_single_channel_offset_dac_b = QSlider(self.groupBox_psd_offset_dac)
        self.verticalSlider_psd_single_channel_offset_dac_b.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_b")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalSlider_psd_single_channel_offset_dac_b.sizePolicy().hasHeightForWidth())
        self.verticalSlider_psd_single_channel_offset_dac_b.setSizePolicy(sizePolicy4)
        self.verticalSlider_psd_single_channel_offset_dac_b.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_b.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_b.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_b.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_b.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_b.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_b.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.verticalSlider_psd_single_channel_offset_dac_b.setTickInterval(5)

        self.gridLayout.addWidget(self.verticalSlider_psd_single_channel_offset_dac_b, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(self.groupBox_psd_offset_dac)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 4, 1)

        self.line_2 = QFrame(self.groupBox_psd_offset_dac)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 3, 4, 1)

        self.verticalSlider_psd_single_channel_offset_dac_a = QSlider(self.groupBox_psd_offset_dac)
        self.verticalSlider_psd_single_channel_offset_dac_a.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_a")
        sizePolicy4.setHeightForWidth(self.verticalSlider_psd_single_channel_offset_dac_a.sizePolicy().hasHeightForWidth())
        self.verticalSlider_psd_single_channel_offset_dac_a.setSizePolicy(sizePolicy4)
        self.verticalSlider_psd_single_channel_offset_dac_a.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_a.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_a.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_a.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_a.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_a.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_a.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.verticalSlider_psd_single_channel_offset_dac_a.setTickInterval(5)

        self.gridLayout.addWidget(self.verticalSlider_psd_single_channel_offset_dac_a, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_5 = QFrame(self.groupBox_psd_offset_dac)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 2, 4, 1, 1)

        self.label_30 = QLabel(self.groupBox_psd_offset_dac)
        self.label_30.setObjectName(u"label_30")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy5)
        self.label_30.setFont(font)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_30, 1, 0, 1, 1)

        self.lineEdit_psd_offset_dac_c = QLineEdit(self.groupBox_psd_offset_dac)
        self.lineEdit_psd_offset_dac_c.setObjectName(u"lineEdit_psd_offset_dac_c")
        self.lineEdit_psd_offset_dac_c.setMaximumSize(QSize(42, 16777215))
        self.lineEdit_psd_offset_dac_c.setFrame(True)
        self.lineEdit_psd_offset_dac_c.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_psd_offset_dac_c.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_psd_offset_dac_c, 4, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_psd_offset_dac_b = QLineEdit(self.groupBox_psd_offset_dac)
        self.lineEdit_psd_offset_dac_b.setObjectName(u"lineEdit_psd_offset_dac_b")
        self.lineEdit_psd_offset_dac_b.setMaximumSize(QSize(42, 16777215))
        self.lineEdit_psd_offset_dac_b.setFrame(True)
        self.lineEdit_psd_offset_dac_b.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_psd_offset_dac_b, 4, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_9 = QFrame(self.groupBox_psd_offset_dac)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 0, 4, 1, 1)

        self.line_7 = QFrame(self.groupBox_psd_offset_dac)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 0, 1, 1, 1)

        self.verticalSlider_psd_single_channel_offset_dac_c = QSlider(self.groupBox_psd_offset_dac)
        self.verticalSlider_psd_single_channel_offset_dac_c.setObjectName(u"verticalSlider_psd_single_channel_offset_dac_c")
        sizePolicy4.setHeightForWidth(self.verticalSlider_psd_single_channel_offset_dac_c.sizePolicy().hasHeightForWidth())
        self.verticalSlider_psd_single_channel_offset_dac_c.setSizePolicy(sizePolicy4)
        self.verticalSlider_psd_single_channel_offset_dac_c.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalSlider_psd_single_channel_offset_dac_c.setMinimum(-15)
        self.verticalSlider_psd_single_channel_offset_dac_c.setMaximum(15)
        self.verticalSlider_psd_single_channel_offset_dac_c.setSingleStep(0)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTracking(True)
        self.verticalSlider_psd_single_channel_offset_dac_c.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_psd_single_channel_offset_dac_c.setInvertedAppearance(False)
        self.verticalSlider_psd_single_channel_offset_dac_c.setInvertedControls(False)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.verticalSlider_psd_single_channel_offset_dac_c.setTickInterval(5)

        self.gridLayout.addWidget(self.verticalSlider_psd_single_channel_offset_dac_c, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_8 = QFrame(self.groupBox_psd_offset_dac)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_8, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_psd_offset_dac)
        self.label_32.setObjectName(u"label_32")
        sizePolicy5.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy5)
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_32, 1, 4, 1, 1)

        self.line_4 = QFrame(self.groupBox_psd_offset_dac)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 2, 0, 1, 1)

        self.lineEdit_psd_offset_dac_a = QLineEdit(self.groupBox_psd_offset_dac)
        self.lineEdit_psd_offset_dac_a.setObjectName(u"lineEdit_psd_offset_dac_a")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_psd_offset_dac_a.sizePolicy().hasHeightForWidth())
        self.lineEdit_psd_offset_dac_a.setSizePolicy(sizePolicy6)
        self.lineEdit_psd_offset_dac_a.setMaximumSize(QSize(42, 16777215))
        self.lineEdit_psd_offset_dac_a.setFrame(True)
        self.lineEdit_psd_offset_dac_a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_psd_offset_dac_a.setDragEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_psd_offset_dac_a, 4, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.line_3 = QFrame(self.groupBox_psd_offset_dac)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_psd_offset_dac)
        self.label_31.setObjectName(u"label_31")
        sizePolicy5.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy5)
        self.label_31.setFont(font)
        self.label_31.setTabletTracking(False)
        self.label_31.setScaledContents(False)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 5, 2, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.pushButton_psd_offset_dac_configure = QPushButton(self.groupBox_psd_offset_dac)
        self.pushButton_psd_offset_dac_configure.setObjectName(u"pushButton_psd_offset_dac_configure")
        self.pushButton_psd_offset_dac_configure.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_46.addWidget(self.pushButton_psd_offset_dac_configure)

        self.pushButton_psd_offset_dac_reset = QPushButton(self.groupBox_psd_offset_dac)
        self.pushButton_psd_offset_dac_reset.setObjectName(u"pushButton_psd_offset_dac_reset")

        self.horizontalLayout_46.addWidget(self.pushButton_psd_offset_dac_reset)


        self.verticalLayout_17.addLayout(self.horizontalLayout_46)


        self.gridLayout_3.addWidget(self.groupBox_psd_offset_dac, 0, 0, 6, 1)

        self.pushButton_reset_psd = QPushButton(Widget_Psd)
        self.pushButton_reset_psd.setObjectName(u"pushButton_reset_psd")

        self.gridLayout_3.addWidget(self.pushButton_reset_psd, 9, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_psd_force_reset = QPushButton(Widget_Psd)
        self.pushButton_psd_force_reset.setObjectName(u"pushButton_psd_force_reset")

        self.horizontalLayout.addWidget(self.pushButton_psd_force_reset)

        self.pushButton_psd_digital_reset = QPushButton(Widget_Psd)
        self.pushButton_psd_digital_reset.setObjectName(u"pushButton_psd_digital_reset")

        self.horizontalLayout.addWidget(self.pushButton_psd_digital_reset)


        self.gridLayout_3.addLayout(self.horizontalLayout, 9, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        QWidget.setTabOrder(self.pushButton_configure_psd, self.pushButton_reset_psd)
        QWidget.setTabOrder(self.pushButton_reset_psd, self.checkBox_psd_global_enable)
        QWidget.setTabOrder(self.checkBox_psd_global_enable, self.checkBox_psd_channel_enable_all)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_all, self.checkBox_psd_channel_enable_0_7)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_0_7, self.checkBox_psd_channel_enable_0)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_0, self.checkBox_psd_channel_enable_1)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_1, self.checkBox_psd_channel_enable_2)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_2, self.checkBox_psd_channel_enable_3)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_3, self.checkBox_psd_channel_enable_4)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_4, self.checkBox_psd_channel_enable_5)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_5, self.checkBox_psd_channel_enable_6)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_6, self.checkBox_psd_channel_enable_7)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_7, self.checkBox_psd_channel_enable_8_15)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_8_15, self.checkBox_psd_channel_enable_8)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_8, self.checkBox_psd_channel_enable_9)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_9, self.checkBox_psd_channel_enable_10)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_10, self.checkBox_psd_channel_enable_11)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_11, self.checkBox_psd_channel_enable_12)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_12, self.checkBox_psd_channel_enable_13)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_13, self.checkBox_psd_channel_enable_14)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_14, self.checkBox_psd_channel_enable_15)
        QWidget.setTabOrder(self.checkBox_psd_channel_enable_15, self.horizontalSlider_psd_delay_dac_a)
        QWidget.setTabOrder(self.horizontalSlider_psd_delay_dac_a, self.horizontalSlider_psd_width_dac_a)
        QWidget.setTabOrder(self.horizontalSlider_psd_width_dac_a, self.pushButton_psd_reset_subchannel_a)
        QWidget.setTabOrder(self.pushButton_psd_reset_subchannel_a, self.comboBox_psd_gain_a)
        QWidget.setTabOrder(self.comboBox_psd_gain_a, self.horizontalSlider_psd_delay_dac_b)
        QWidget.setTabOrder(self.horizontalSlider_psd_delay_dac_b, self.horizontalSlider_psd_width_dac_b)
        QWidget.setTabOrder(self.horizontalSlider_psd_width_dac_b, self.pushButton_psd_reset_subchannel_b)
        QWidget.setTabOrder(self.pushButton_psd_reset_subchannel_b, self.comboBox_psd_gain_b)
        QWidget.setTabOrder(self.comboBox_psd_gain_b, self.horizontalSlider_psd_delay_dac_c)
        QWidget.setTabOrder(self.horizontalSlider_psd_delay_dac_c, self.horizontalSlider_psd_width_dac_c)
        QWidget.setTabOrder(self.horizontalSlider_psd_width_dac_c, self.pushButton_psd_reset_subchannel_c)
        QWidget.setTabOrder(self.pushButton_psd_reset_subchannel_c, self.comboBox_psd_gain_c)
        QWidget.setTabOrder(self.comboBox_psd_gain_c, self.comboBox_psd_delay_range_a)
        QWidget.setTabOrder(self.comboBox_psd_delay_range_a, self.comboBox_psd_delay_range_b)
        QWidget.setTabOrder(self.comboBox_psd_delay_range_b, self.comboBox_psd_delay_range_c)
        QWidget.setTabOrder(self.comboBox_psd_delay_range_c, self.comboBox_psd_polarity)
        QWidget.setTabOrder(self.comboBox_psd_polarity, self.lineEdit_psd_offset_dac_a)
        QWidget.setTabOrder(self.lineEdit_psd_offset_dac_a, self.comboBox_psd_bias)
        QWidget.setTabOrder(self.comboBox_psd_bias, self.comboBox_psd_trigger_mode)
        QWidget.setTabOrder(self.comboBox_psd_trigger_mode, self.comboBox_psd_vtc_range)
        QWidget.setTabOrder(self.comboBox_psd_vtc_range, self.verticalSlider_psd_single_channel_offset_dac_a)
        QWidget.setTabOrder(self.verticalSlider_psd_single_channel_offset_dac_a, self.verticalSlider_psd_single_channel_offset_dac_b)
        QWidget.setTabOrder(self.verticalSlider_psd_single_channel_offset_dac_b, self.verticalSlider_psd_single_channel_offset_dac_c)
        QWidget.setTabOrder(self.verticalSlider_psd_single_channel_offset_dac_c, self.pushButton_psd_offset_dac_configure)
        QWidget.setTabOrder(self.pushButton_psd_offset_dac_configure, self.pushButton_psd_offset_dac_reset)
        QWidget.setTabOrder(self.pushButton_psd_offset_dac_reset, self.pushButton_continous_octal_dac_update)
        QWidget.setTabOrder(self.pushButton_continous_octal_dac_update, self.pushButton_reset_all_dacs)
        QWidget.setTabOrder(self.pushButton_reset_all_dacs, self.pushButton_reset_psd_ui)
        QWidget.setTabOrder(self.pushButton_reset_psd_ui, self.comboBox_psd_width_range_c)
        QWidget.setTabOrder(self.comboBox_psd_width_range_c, self.lineEdit_psd_offset_dac_b)
        QWidget.setTabOrder(self.lineEdit_psd_offset_dac_b, self.text_psd_width_dac_c)
        QWidget.setTabOrder(self.text_psd_width_dac_c, self.pushButton_psd_test_mode_configure)
        QWidget.setTabOrder(self.pushButton_psd_test_mode_configure, self.pushButton_psd_test_mode_reset)
        QWidget.setTabOrder(self.pushButton_psd_test_mode_reset, self.text_psd_auto_veto_dac)
        QWidget.setTabOrder(self.text_psd_auto_veto_dac, self.comboBox_psd_test_mode_channel_selection)
        QWidget.setTabOrder(self.comboBox_psd_test_mode_channel_selection, self.text_psd_delay_dac_b)
        QWidget.setTabOrder(self.text_psd_delay_dac_b, self.comboBox_psd_width_range_b)
        QWidget.setTabOrder(self.comboBox_psd_width_range_b, self.comboBox_psd_test_mode_subchannel_selection)
        QWidget.setTabOrder(self.comboBox_psd_test_mode_subchannel_selection, self.text_psd_width_dac_b)
        QWidget.setTabOrder(self.text_psd_width_dac_b, self.comboBox_psd_test_mode)
        QWidget.setTabOrder(self.comboBox_psd_test_mode, self.comboBox_psd_offset_dac_channel_selection)
        QWidget.setTabOrder(self.comboBox_psd_offset_dac_channel_selection, self.horizontalSlider_psd_auto_veto_dac)
        QWidget.setTabOrder(self.horizontalSlider_psd_auto_veto_dac, self.text_psd_delay_dac_c)
        QWidget.setTabOrder(self.text_psd_delay_dac_c, self.text_psd_delay_dac_a)
        QWidget.setTabOrder(self.text_psd_delay_dac_a, self.comboBox_psd_width_range_a)
        QWidget.setTabOrder(self.comboBox_psd_width_range_a, self.lineEdit_psd_offset_dac_c)
        QWidget.setTabOrder(self.lineEdit_psd_offset_dac_c, self.text_psd_width_dac_a)

        self.retranslateUi(Widget_Psd)

        QMetaObject.connectSlotsByName(Widget_Psd)
    # setupUi

    def retranslateUi(self, Widget_Psd):
        Widget_Psd.setWindowTitle(QCoreApplication.translate("Widget_Psd", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac_2.setToolTip(QCoreApplication.translate("Widget_Psd", u"<html><head/><body><p><span style=\" font-weight:700;\">Auto Veto Time: </span></p><p><br/></p><p>Configures the time at which the ASIC auto resets if the <span style=\" font-weight:700;\">Veto Reset(Take Event)</span> signal is not asserted.  </p><p>Inversely related to DAC voltage, not linear; Higher Voltage -&gt; Quicker reset.  </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac_2.setText(QCoreApplication.translate("Widget_Psd", u"Auto Veto DAC voltage", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_auto_veto_dac.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_auto_veto_dac.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_auto_veto_dac.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("Widget_Psd", u"Channel Enable ", None))
        self.checkBox_psd_channel_enable_10.setText(QCoreApplication.translate("Widget_Psd", u"10", None))
        self.checkBox_psd_channel_enable_12.setText(QCoreApplication.translate("Widget_Psd", u"12", None))
        self.checkBox_psd_channel_enable_0_7.setText(QCoreApplication.translate("Widget_Psd", u"0-7", None))
        self.checkBox_psd_channel_enable_14.setText(QCoreApplication.translate("Widget_Psd", u"14", None))
        self.checkBox_psd_channel_enable_11.setText(QCoreApplication.translate("Widget_Psd", u"11", None))
        self.checkBox_psd_channel_enable_15.setText(QCoreApplication.translate("Widget_Psd", u"15", None))
        self.checkBox_psd_channel_enable_4.setText(QCoreApplication.translate("Widget_Psd", u"4", None))
        self.checkBox_psd_channel_enable_5.setText(QCoreApplication.translate("Widget_Psd", u"5", None))
        self.checkBox_psd_channel_enable_3.setText(QCoreApplication.translate("Widget_Psd", u"3", None))
        self.checkBox_psd_channel_enable_0.setText(QCoreApplication.translate("Widget_Psd", u"0", None))
        self.checkBox_psd_channel_enable_2.setText(QCoreApplication.translate("Widget_Psd", u"2", None))
        self.checkBox_psd_channel_enable_13.setText(QCoreApplication.translate("Widget_Psd", u"13", None))
        self.checkBox_psd_channel_enable_9.setText(QCoreApplication.translate("Widget_Psd", u"9", None))
        self.label_34.setText(QCoreApplication.translate("Widget_Psd", u"Enable", None))
        self.checkBox_psd_channel_enable_7.setText(QCoreApplication.translate("Widget_Psd", u"7", None))
        self.checkBox_psd_channel_enable_all.setText(QCoreApplication.translate("Widget_Psd", u"All", None))
        self.checkBox_psd_channel_enable_8.setText(QCoreApplication.translate("Widget_Psd", u"8", None))
        self.checkBox_psd_channel_enable_6.setText(QCoreApplication.translate("Widget_Psd", u"6", None))
        self.checkBox_psd_channel_enable_8_15.setText(QCoreApplication.translate("Widget_Psd", u"8-15", None))
        self.checkBox_psd_channel_enable_1.setText(QCoreApplication.translate("Widget_Psd", u"1", None))
        self.horizontalGroupBox_5.setTitle(QCoreApplication.translate("Widget_Psd", u"Integrator Gates", None))
        self.groupBox_subchannel_B.setTitle("")
        self.label_24.setText(QCoreApplication.translate("Widget_Psd", u"B", None))
        self.label_psd_gain_a_2.setText(QCoreApplication.translate("Widget_Psd", u"Gain", None))
        self.comboBox_psd_gain_b.setItemText(0, QCoreApplication.translate("Widget_Psd", u"500", None))
        self.comboBox_psd_gain_b.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1000", None))
        self.comboBox_psd_gain_b.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2000", None))
        self.comboBox_psd_gain_b.setItemText(3, QCoreApplication.translate("Widget_Psd", u"5000", None))
        self.comboBox_psd_gain_b.setItemText(4, QCoreApplication.translate("Widget_Psd", u"10000", None))
        self.comboBox_psd_gain_b.setItemText(5, QCoreApplication.translate("Widget_Psd", u"20000", None))
        self.comboBox_psd_gain_b.setItemText(6, QCoreApplication.translate("Widget_Psd", u"50000", None))
        self.comboBox_psd_gain_b.setItemText(7, QCoreApplication.translate("Widget_Psd", u"100000", None))

        self.pushButton_psd_reset_subchannel_b.setText(QCoreApplication.translate("Widget_Psd", u"Reset", None))
        self.label_25.setText(QCoreApplication.translate("Widget_Psd", u"Delay", None))
        self.label_psd_delay_range_b.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_delay_range_b.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_delay_range_b.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_delay_range_b.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_delay_range_b.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_b.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_b.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_delay_dac_b.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.label_26.setText(QCoreApplication.translate("Widget_Psd", u"Width", None))
        self.label_psd_width_range_b.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_width_range_b.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_width_range_b.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_width_range_b.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_width_range_b.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_b.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_b.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_width_dac_b.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.groupBox_subchannel_A.setTitle("")
        self.label_17.setText(QCoreApplication.translate("Widget_Psd", u"A", None))
        self.label_psd_gain_a.setText(QCoreApplication.translate("Widget_Psd", u"Gain", None))
        self.comboBox_psd_gain_a.setItemText(0, QCoreApplication.translate("Widget_Psd", u"500", None))
        self.comboBox_psd_gain_a.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1000", None))
        self.comboBox_psd_gain_a.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2000", None))
        self.comboBox_psd_gain_a.setItemText(3, QCoreApplication.translate("Widget_Psd", u"5000", None))
        self.comboBox_psd_gain_a.setItemText(4, QCoreApplication.translate("Widget_Psd", u"10000", None))
        self.comboBox_psd_gain_a.setItemText(5, QCoreApplication.translate("Widget_Psd", u"20000", None))
        self.comboBox_psd_gain_a.setItemText(6, QCoreApplication.translate("Widget_Psd", u"50000", None))
        self.comboBox_psd_gain_a.setItemText(7, QCoreApplication.translate("Widget_Psd", u"100000", None))

        self.pushButton_psd_reset_subchannel_a.setText(QCoreApplication.translate("Widget_Psd", u"Reset", None))
        self.label_19.setText(QCoreApplication.translate("Widget_Psd", u"Delay", None))
        self.label_psd_delay_range_a.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_delay_range_a.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_delay_range_a.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_delay_range_a.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_delay_range_a.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_a.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_a.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_delay_dac_a.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.label_23.setText(QCoreApplication.translate("Widget_Psd", u"Width", None))
        self.label_psd_width_range_a.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_width_range_a.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_width_range_a.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_width_range_a.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_width_range_a.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_a.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_a.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_width_dac_a.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.groupBox_subchannel_C.setTitle("")
        self.label_27.setText(QCoreApplication.translate("Widget_Psd", u"C", None))
        self.label_psd_gain_a_3.setText(QCoreApplication.translate("Widget_Psd", u"Gain", None))
        self.comboBox_psd_gain_c.setItemText(0, QCoreApplication.translate("Widget_Psd", u"500", None))
        self.comboBox_psd_gain_c.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1000", None))
        self.comboBox_psd_gain_c.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2000", None))
        self.comboBox_psd_gain_c.setItemText(3, QCoreApplication.translate("Widget_Psd", u"5000", None))
        self.comboBox_psd_gain_c.setItemText(4, QCoreApplication.translate("Widget_Psd", u"10000", None))
        self.comboBox_psd_gain_c.setItemText(5, QCoreApplication.translate("Widget_Psd", u"20000", None))
        self.comboBox_psd_gain_c.setItemText(6, QCoreApplication.translate("Widget_Psd", u"50000", None))
        self.comboBox_psd_gain_c.setItemText(7, QCoreApplication.translate("Widget_Psd", u"100000", None))

        self.pushButton_psd_reset_subchannel_c.setText(QCoreApplication.translate("Widget_Psd", u"Reset", None))
        self.label_28.setText(QCoreApplication.translate("Widget_Psd", u"Delay", None))
        self.label_psd_delay_range_c.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_delay_range_c.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_delay_range_c.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_delay_range_c.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_delay_range_c.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_delay_dac_c.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_delay_dac_c.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_delay_dac_c.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.label_29.setText(QCoreApplication.translate("Widget_Psd", u"Width", None))
        self.label_psd_width_range_c.setText(QCoreApplication.translate("Widget_Psd", u"Range", None))
        self.comboBox_psd_width_range_c.setItemText(0, QCoreApplication.translate("Widget_Psd", u"0", None))
        self.comboBox_psd_width_range_c.setItemText(1, QCoreApplication.translate("Widget_Psd", u"1", None))
        self.comboBox_psd_width_range_c.setItemText(2, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_width_range_c.setItemText(3, QCoreApplication.translate("Widget_Psd", u"3", None))

#if QT_CONFIG(tooltip)
        self.horizontalSlider_psd_width_dac_c.setToolTip(QCoreApplication.translate("Widget_Psd", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
        self.text_psd_width_dac_c.setInputMask(QCoreApplication.translate("Widget_Psd", u"0.00 V", None))
        self.text_psd_width_dac_c.setText(QCoreApplication.translate("Widget_Psd", u"0.0 V", None))
        self.label_psd_polarity.setText(QCoreApplication.translate("Widget_Psd", u"Polarity", None))
        self.comboBox_psd_polarity.setItemText(0, QCoreApplication.translate("Widget_Psd", u"positive", None))
        self.comboBox_psd_polarity.setItemText(1, QCoreApplication.translate("Widget_Psd", u"negative", None))

        self.label_psd_bias_2.setText(QCoreApplication.translate("Widget_Psd", u"Bias", None))
        self.comboBox_psd_bias.setItemText(0, QCoreApplication.translate("Widget_Psd", u"high", None))
        self.comboBox_psd_bias.setItemText(1, QCoreApplication.translate("Widget_Psd", u"low", None))

        self.label_psd_trigger_mode.setText(QCoreApplication.translate("Widget_Psd", u"Trigger Mode", None))
        self.comboBox_psd_trigger_mode.setItemText(0, QCoreApplication.translate("Widget_Psd", u"3", None))
        self.comboBox_psd_trigger_mode.setItemText(1, QCoreApplication.translate("Widget_Psd", u"2", None))
        self.comboBox_psd_trigger_mode.setItemText(2, QCoreApplication.translate("Widget_Psd", u"1", None))

        self.label_35.setText(QCoreApplication.translate("Widget_Psd", u"VTC Range", None))
        self.comboBox_psd_vtc_range.setItemText(0, QCoreApplication.translate("Widget_Psd", u"250 ns", None))
        self.comboBox_psd_vtc_range.setItemText(1, QCoreApplication.translate("Widget_Psd", u"2 us", None))

        self.pushButton_configure_psd.setText(QCoreApplication.translate("Widget_Psd", u"Configure PSD", None))
        self.pushButton_reset_psd_ui.setText(QCoreApplication.translate("Widget_Psd", u"Reset PSD GUI to last configured state", None))
        self.groupBox_psd_test_mode.setTitle(QCoreApplication.translate("Widget_Psd", u"PSD Test Mode", None))
        self.label_37.setText(QCoreApplication.translate("Widget_Psd", u"Test Channel", None))
        self.comboBox_psd_test_mode.setItemText(0, QCoreApplication.translate("Widget_Psd", u"On", None))
        self.comboBox_psd_test_mode.setItemText(1, QCoreApplication.translate("Widget_Psd", u"Off", None))

        self.label_36.setText(QCoreApplication.translate("Widget_Psd", u"Status", None))
        self.label_38.setText(QCoreApplication.translate("Widget_Psd", u"Test Sub Channel", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(0, QCoreApplication.translate("Widget_Psd", u"A", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(1, QCoreApplication.translate("Widget_Psd", u"B", None))
        self.comboBox_psd_test_mode_subchannel_selection.setItemText(2, QCoreApplication.translate("Widget_Psd", u"C", None))

        self.pushButton_psd_test_mode_reset.setText(QCoreApplication.translate("Widget_Psd", u"Reset", None))
        self.pushButton_psd_test_mode_configure.setText(QCoreApplication.translate("Widget_Psd", u"Configure", None))
        self.checkBox_psd_global_enable.setText(QCoreApplication.translate("Widget_Psd", u"PSD Global Enable ", None))
        self.pushButton_reset_all_dacs.setText(QCoreApplication.translate("Widget_Psd", u"Reset DACs", None))
        self.pushButton_continous_octal_dac_update.setText(QCoreApplication.translate("Widget_Psd", u"Continous Octal Dac Update", None))
        self.groupBox_psd_offset_dac.setTitle(QCoreApplication.translate("Widget_Psd", u"Offset DAC Config", None))
        self.label_33.setText(QCoreApplication.translate("Widget_Psd", u"Channel", None))
        self.label_30.setText(QCoreApplication.translate("Widget_Psd", u"A", None))
        self.label_32.setText(QCoreApplication.translate("Widget_Psd", u"C", None))
        self.label_31.setText(QCoreApplication.translate("Widget_Psd", u"B", None))
        self.pushButton_psd_offset_dac_configure.setText(QCoreApplication.translate("Widget_Psd", u"Configure", None))
        self.pushButton_psd_offset_dac_reset.setText(QCoreApplication.translate("Widget_Psd", u"Reset", None))
        self.pushButton_reset_psd.setText(QCoreApplication.translate("Widget_Psd", u"Reset PSD", None))
        self.pushButton_psd_force_reset.setText(QCoreApplication.translate("Widget_Psd", u"Force Reset", None))
        self.pushButton_psd_digital_reset.setText(QCoreApplication.translate("Widget_Psd", u"Digital Reset", None))
    # retranslateUi

