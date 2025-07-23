# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chipboard_ui_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget_Chipboard(object):
    def setupUi(self, Widget_Chipboard):
        if not Widget_Chipboard.objectName():
            Widget_Chipboard.setObjectName(u"Widget_Chipboard")
        Widget_Chipboard.resize(862, 727)
        self.gridLayout = QGridLayout(Widget_Chipboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Widget_Chipboard)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.pushButton = QPushButton(Widget_Chipboard)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 2)

        self.groupBox = QGroupBox(Widget_Chipboard)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.comboBox_pre_amp_mux = QComboBox(self.groupBox)
        self.comboBox_pre_amp_mux.addItem("")
        self.comboBox_pre_amp_mux.setObjectName(u"comboBox_pre_amp_mux")

        self.gridLayout_2.addWidget(self.comboBox_pre_amp_mux, 4, 3, 1, 1)

        self.comboBox_intx_mux = QComboBox(self.groupBox)
        self.comboBox_intx_mux.addItem("")
        self.comboBox_intx_mux.addItem("")
        self.comboBox_intx_mux.setObjectName(u"comboBox_intx_mux")

        self.gridLayout_2.addWidget(self.comboBox_intx_mux, 2, 3, 1, 1)

        self.comboBox_or_mux = QComboBox(self.groupBox)
        self.comboBox_or_mux.addItem("")
        self.comboBox_or_mux.addItem("")
        self.comboBox_or_mux.addItem("")
        self.comboBox_or_mux.addItem("")
        self.comboBox_or_mux.setObjectName(u"comboBox_or_mux")

        self.gridLayout_2.addWidget(self.comboBox_or_mux, 1, 3, 1, 1)

        self.comboBox_psd_cfd_mux = QComboBox(self.groupBox)
        self.comboBox_psd_cfd_mux.addItem("")
        self.comboBox_psd_cfd_mux.addItem("")
        self.comboBox_psd_cfd_mux.setObjectName(u"comboBox_psd_cfd_mux")

        self.gridLayout_2.addWidget(self.comboBox_psd_cfd_mux, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 4, 1)

        self.label_psd_auto_veto_dac_2 = QLabel(Widget_Chipboard)
        self.label_psd_auto_veto_dac_2.setObjectName(u"label_psd_auto_veto_dac_2")
        self.label_psd_auto_veto_dac_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_psd_auto_veto_dac_2, 1, 1, 1, 1)

        self.text_multiplicity_offset_dac = QLineEdit(Widget_Chipboard)
        self.text_multiplicity_offset_dac.setObjectName(u"text_multiplicity_offset_dac")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_multiplicity_offset_dac.sizePolicy().hasHeightForWidth())
        self.text_multiplicity_offset_dac.setSizePolicy(sizePolicy)
        self.text_multiplicity_offset_dac.setMinimumSize(QSize(21, 0))
        self.text_multiplicity_offset_dac.setMaximumSize(QSize(50, 16777215))
        self.text_multiplicity_offset_dac.setBaseSize(QSize(30, 0))
        self.text_multiplicity_offset_dac.setMaxLength(6)
        self.text_multiplicity_offset_dac.setCursorPosition(6)
        self.text_multiplicity_offset_dac.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_multiplicity_offset_dac.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.text_multiplicity_offset_dac, 1, 3, 1, 1)

        self.comboBox_chipboard_mode = QComboBox(Widget_Chipboard)
        self.comboBox_chipboard_mode.addItem("")
        self.comboBox_chipboard_mode.addItem("")
        self.comboBox_chipboard_mode.setObjectName(u"comboBox_chipboard_mode")

        self.gridLayout.addWidget(self.comboBox_chipboard_mode, 2, 2, 1, 1)

        self.groupBox_delays = QGroupBox(Widget_Chipboard)
        self.groupBox_delays.setObjectName(u"groupBox_delays")
        self.groupBox_delays.setMinimumSize(QSize(430, 451))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_delays)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontal_layout_delay_label = QHBoxLayout()
        self.horizontal_layout_delay_label.setObjectName(u"horizontal_layout_delay_label")
        self.horizontal_layout_delay_label.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_15 = QLabel(self.groupBox_delays)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_15.setFont(font)

        self.horizontal_layout_delay_label.addWidget(self.label_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_label.addItem(self.horizontalSpacer_2)

        self.label_21 = QLabel(self.groupBox_delays)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_label.addWidget(self.label_21)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_label.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_label)

        self.horizontal_layout_delay_ch_0 = QHBoxLayout()
        self.horizontal_layout_delay_ch_0.setObjectName(u"horizontal_layout_delay_ch_0")
        self.horizontal_layout_delay_ch_0.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_0 = QLabel(self.groupBox_delays)
        self.label_delay_ch_0.setObjectName(u"label_delay_ch_0")
        self.label_delay_ch_0.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_0.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_0.setMargin(0)

        self.horizontal_layout_delay_ch_0.addWidget(self.label_delay_ch_0)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_0.addItem(self.horizontalSpacer)

        self.slider_delay_ch_0 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_0.setObjectName(u"slider_delay_ch_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_0.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_0.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_0.setMaximum(62)
        self.slider_delay_ch_0.setSingleStep(2)
        self.slider_delay_ch_0.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_0.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_0.setTickInterval(2)

        self.horizontal_layout_delay_ch_0.addWidget(self.slider_delay_ch_0)

        self.horizontalSpacer_20 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_0.addItem(self.horizontalSpacer_20)

        self.text_delay_ch_0 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_0.setObjectName(u"text_delay_ch_0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_delay_ch_0.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_0.setSizePolicy(sizePolicy2)
        self.text_delay_ch_0.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_0.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_0.setMaxLength(5)
        self.text_delay_ch_0.setFrame(True)
        self.text_delay_ch_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_0.addWidget(self.text_delay_ch_0)

        self.label_delay_ns_ch_0 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_0.setObjectName(u"label_delay_ns_ch_0")

        self.horizontal_layout_delay_ch_0.addWidget(self.label_delay_ns_ch_0)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_0)

        self.horizontal_layout_delay_ch_1 = QHBoxLayout()
        self.horizontal_layout_delay_ch_1.setObjectName(u"horizontal_layout_delay_ch_1")
        self.horizontal_layout_delay_ch_1.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_1 = QLabel(self.groupBox_delays)
        self.label_delay_ch_1.setObjectName(u"label_delay_ch_1")
        self.label_delay_ch_1.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_1.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_1.setMargin(0)

        self.horizontal_layout_delay_ch_1.addWidget(self.label_delay_ch_1)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_1.addItem(self.horizontalSpacer_4)

        self.slider_delay_ch_1 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_1.setObjectName(u"slider_delay_ch_1")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_1.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_1.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_1.setMaximum(62)
        self.slider_delay_ch_1.setSingleStep(2)
        self.slider_delay_ch_1.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_1.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_1.setTickInterval(2)

        self.horizontal_layout_delay_ch_1.addWidget(self.slider_delay_ch_1)

        self.horizontalSpacer_31 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_1.addItem(self.horizontalSpacer_31)

        self.text_delay_ch_1 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_1.setObjectName(u"text_delay_ch_1")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_1.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_1.setSizePolicy(sizePolicy2)
        self.text_delay_ch_1.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_1.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_1.setMaxLength(5)
        self.text_delay_ch_1.setFrame(True)
        self.text_delay_ch_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_1.addWidget(self.text_delay_ch_1)

        self.label_delay_ns_ch_1 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_1.setObjectName(u"label_delay_ns_ch_1")

        self.horizontal_layout_delay_ch_1.addWidget(self.label_delay_ns_ch_1)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_1)

        self.horizontal_layout_delay_ch_2 = QHBoxLayout()
        self.horizontal_layout_delay_ch_2.setObjectName(u"horizontal_layout_delay_ch_2")
        self.horizontal_layout_delay_ch_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_2 = QLabel(self.groupBox_delays)
        self.label_delay_ch_2.setObjectName(u"label_delay_ch_2")
        self.label_delay_ch_2.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_2.setMargin(0)

        self.horizontal_layout_delay_ch_2.addWidget(self.label_delay_ch_2)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_2.addItem(self.horizontalSpacer_5)

        self.slider_delay_ch_2 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_2.setObjectName(u"slider_delay_ch_2")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_2.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_2.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_2.setMaximum(62)
        self.slider_delay_ch_2.setSingleStep(2)
        self.slider_delay_ch_2.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_2.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_2.setTickInterval(2)

        self.horizontal_layout_delay_ch_2.addWidget(self.slider_delay_ch_2)

        self.horizontalSpacer_30 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_2.addItem(self.horizontalSpacer_30)

        self.text_delay_ch_2 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_2.setObjectName(u"text_delay_ch_2")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_2.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_2.setSizePolicy(sizePolicy2)
        self.text_delay_ch_2.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_2.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_2.setMaxLength(5)
        self.text_delay_ch_2.setFrame(True)
        self.text_delay_ch_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_2.addWidget(self.text_delay_ch_2)

        self.label_delay_ns_ch_2 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_2.setObjectName(u"label_delay_ns_ch_2")

        self.horizontal_layout_delay_ch_2.addWidget(self.label_delay_ns_ch_2)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_2)

        self.horizontal_layout_delay_ch_3 = QHBoxLayout()
        self.horizontal_layout_delay_ch_3.setObjectName(u"horizontal_layout_delay_ch_3")
        self.horizontal_layout_delay_ch_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_3 = QLabel(self.groupBox_delays)
        self.label_delay_ch_3.setObjectName(u"label_delay_ch_3")
        self.label_delay_ch_3.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_3.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_3.setMargin(0)

        self.horizontal_layout_delay_ch_3.addWidget(self.label_delay_ch_3)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_3.addItem(self.horizontalSpacer_6)

        self.slider_delay_ch_3 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_3.setObjectName(u"slider_delay_ch_3")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_3.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_3.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_3.setMaximum(62)
        self.slider_delay_ch_3.setSingleStep(2)
        self.slider_delay_ch_3.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_3.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_3.setTickInterval(2)

        self.horizontal_layout_delay_ch_3.addWidget(self.slider_delay_ch_3)

        self.horizontalSpacer_29 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_3.addItem(self.horizontalSpacer_29)

        self.text_delay_ch_3 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_3.setObjectName(u"text_delay_ch_3")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_3.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_3.setSizePolicy(sizePolicy2)
        self.text_delay_ch_3.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_3.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_3.setMaxLength(5)
        self.text_delay_ch_3.setFrame(True)
        self.text_delay_ch_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_3.addWidget(self.text_delay_ch_3)

        self.label_delay_ns_ch_3 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_3.setObjectName(u"label_delay_ns_ch_3")

        self.horizontal_layout_delay_ch_3.addWidget(self.label_delay_ns_ch_3)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_3)

        self.horizontal_layout_delay_ch_4 = QHBoxLayout()
        self.horizontal_layout_delay_ch_4.setObjectName(u"horizontal_layout_delay_ch_4")
        self.horizontal_layout_delay_ch_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_4 = QLabel(self.groupBox_delays)
        self.label_delay_ch_4.setObjectName(u"label_delay_ch_4")
        self.label_delay_ch_4.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_4.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_4.setMargin(0)

        self.horizontal_layout_delay_ch_4.addWidget(self.label_delay_ch_4)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_4.addItem(self.horizontalSpacer_7)

        self.slider_delay_ch_4 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_4.setObjectName(u"slider_delay_ch_4")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_4.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_4.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_4.setMaximum(62)
        self.slider_delay_ch_4.setSingleStep(2)
        self.slider_delay_ch_4.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_4.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_4.setTickInterval(2)

        self.horizontal_layout_delay_ch_4.addWidget(self.slider_delay_ch_4)

        self.horizontalSpacer_28 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_4.addItem(self.horizontalSpacer_28)

        self.text_delay_ch_4 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_4.setObjectName(u"text_delay_ch_4")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_4.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_4.setSizePolicy(sizePolicy2)
        self.text_delay_ch_4.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_4.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_4.setMaxLength(5)
        self.text_delay_ch_4.setFrame(True)
        self.text_delay_ch_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_4.addWidget(self.text_delay_ch_4)

        self.label_delay_ns_ch_4 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_4.setObjectName(u"label_delay_ns_ch_4")

        self.horizontal_layout_delay_ch_4.addWidget(self.label_delay_ns_ch_4)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_4)

        self.horizontal_layout_delay_ch_5 = QHBoxLayout()
        self.horizontal_layout_delay_ch_5.setObjectName(u"horizontal_layout_delay_ch_5")
        self.horizontal_layout_delay_ch_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_5 = QLabel(self.groupBox_delays)
        self.label_delay_ch_5.setObjectName(u"label_delay_ch_5")
        self.label_delay_ch_5.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_5.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_5.setMargin(0)

        self.horizontal_layout_delay_ch_5.addWidget(self.label_delay_ch_5)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_5.addItem(self.horizontalSpacer_8)

        self.slider_delay_ch_5 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_5.setObjectName(u"slider_delay_ch_5")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_5.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_5.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_5.setMaximum(62)
        self.slider_delay_ch_5.setSingleStep(2)
        self.slider_delay_ch_5.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_5.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_5.setTickInterval(2)

        self.horizontal_layout_delay_ch_5.addWidget(self.slider_delay_ch_5)

        self.horizontalSpacer_27 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_5.addItem(self.horizontalSpacer_27)

        self.text_delay_ch_5 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_5.setObjectName(u"text_delay_ch_5")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_5.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_5.setSizePolicy(sizePolicy2)
        self.text_delay_ch_5.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_5.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_5.setMaxLength(5)
        self.text_delay_ch_5.setFrame(True)
        self.text_delay_ch_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_5.addWidget(self.text_delay_ch_5)

        self.label_delay_ns_ch_5 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_5.setObjectName(u"label_delay_ns_ch_5")

        self.horizontal_layout_delay_ch_5.addWidget(self.label_delay_ns_ch_5)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_5)

        self.horizontal_layout_delay_ch_6 = QHBoxLayout()
        self.horizontal_layout_delay_ch_6.setObjectName(u"horizontal_layout_delay_ch_6")
        self.horizontal_layout_delay_ch_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_6 = QLabel(self.groupBox_delays)
        self.label_delay_ch_6.setObjectName(u"label_delay_ch_6")
        self.label_delay_ch_6.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_6.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_6.setMargin(0)

        self.horizontal_layout_delay_ch_6.addWidget(self.label_delay_ch_6)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_6.addItem(self.horizontalSpacer_9)

        self.slider_delay_ch_6 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_6.setObjectName(u"slider_delay_ch_6")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_6.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_6.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_6.setMaximum(62)
        self.slider_delay_ch_6.setSingleStep(2)
        self.slider_delay_ch_6.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_6.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_6.setTickInterval(2)

        self.horizontal_layout_delay_ch_6.addWidget(self.slider_delay_ch_6)

        self.horizontalSpacer_26 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_6.addItem(self.horizontalSpacer_26)

        self.text_delay_ch_6 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_6.setObjectName(u"text_delay_ch_6")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_6.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_6.setSizePolicy(sizePolicy2)
        self.text_delay_ch_6.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_6.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_6.setMaxLength(5)
        self.text_delay_ch_6.setFrame(True)
        self.text_delay_ch_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_6.addWidget(self.text_delay_ch_6)

        self.label_delay_ns_ch_6 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_6.setObjectName(u"label_delay_ns_ch_6")

        self.horizontal_layout_delay_ch_6.addWidget(self.label_delay_ns_ch_6)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_6)

        self.horizontal_layout_delay_ch_7 = QHBoxLayout()
        self.horizontal_layout_delay_ch_7.setObjectName(u"horizontal_layout_delay_ch_7")
        self.horizontal_layout_delay_ch_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_7 = QLabel(self.groupBox_delays)
        self.label_delay_ch_7.setObjectName(u"label_delay_ch_7")
        self.label_delay_ch_7.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_7.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_7.setMargin(0)

        self.horizontal_layout_delay_ch_7.addWidget(self.label_delay_ch_7)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_7.addItem(self.horizontalSpacer_10)

        self.slider_delay_ch_7 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_7.setObjectName(u"slider_delay_ch_7")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_7.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_7.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_7.setMaximum(62)
        self.slider_delay_ch_7.setSingleStep(2)
        self.slider_delay_ch_7.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_7.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_7.setTickInterval(2)

        self.horizontal_layout_delay_ch_7.addWidget(self.slider_delay_ch_7)

        self.horizontalSpacer_25 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_7.addItem(self.horizontalSpacer_25)

        self.text_delay_ch_7 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_7.setObjectName(u"text_delay_ch_7")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_7.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_7.setSizePolicy(sizePolicy2)
        self.text_delay_ch_7.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_7.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_7.setMaxLength(5)
        self.text_delay_ch_7.setFrame(True)
        self.text_delay_ch_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_7.addWidget(self.text_delay_ch_7)

        self.label_delay_ns_ch_7 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_7.setObjectName(u"label_delay_ns_ch_7")

        self.horizontal_layout_delay_ch_7.addWidget(self.label_delay_ns_ch_7)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_7)

        self.horizontal_layout_delay_ch_8 = QHBoxLayout()
        self.horizontal_layout_delay_ch_8.setObjectName(u"horizontal_layout_delay_ch_8")
        self.horizontal_layout_delay_ch_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_8 = QLabel(self.groupBox_delays)
        self.label_delay_ch_8.setObjectName(u"label_delay_ch_8")
        self.label_delay_ch_8.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_8.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_8.setMargin(0)

        self.horizontal_layout_delay_ch_8.addWidget(self.label_delay_ch_8)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_8.addItem(self.horizontalSpacer_11)

        self.slider_delay_ch_8 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_8.setObjectName(u"slider_delay_ch_8")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_8.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_8.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_8.setMaximum(62)
        self.slider_delay_ch_8.setSingleStep(2)
        self.slider_delay_ch_8.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_8.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_8.setTickInterval(2)

        self.horizontal_layout_delay_ch_8.addWidget(self.slider_delay_ch_8)

        self.horizontalSpacer_24 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_8.addItem(self.horizontalSpacer_24)

        self.text_delay_ch_8 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_8.setObjectName(u"text_delay_ch_8")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_8.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_8.setSizePolicy(sizePolicy2)
        self.text_delay_ch_8.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_8.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_8.setMaxLength(5)
        self.text_delay_ch_8.setFrame(True)
        self.text_delay_ch_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_8.addWidget(self.text_delay_ch_8)

        self.label_delay_ns_ch_8 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_8.setObjectName(u"label_delay_ns_ch_8")

        self.horizontal_layout_delay_ch_8.addWidget(self.label_delay_ns_ch_8)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_8)

        self.horizontal_layout_delay_ch_9 = QHBoxLayout()
        self.horizontal_layout_delay_ch_9.setObjectName(u"horizontal_layout_delay_ch_9")
        self.horizontal_layout_delay_ch_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_9 = QLabel(self.groupBox_delays)
        self.label_delay_ch_9.setObjectName(u"label_delay_ch_9")
        self.label_delay_ch_9.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_9.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_9.setMargin(0)

        self.horizontal_layout_delay_ch_9.addWidget(self.label_delay_ch_9)

        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_9.addItem(self.horizontalSpacer_12)

        self.slider_delay_ch_9 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_9.setObjectName(u"slider_delay_ch_9")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_9.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_9.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_9.setMaximum(62)
        self.slider_delay_ch_9.setSingleStep(2)
        self.slider_delay_ch_9.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_9.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_9.setTickInterval(2)

        self.horizontal_layout_delay_ch_9.addWidget(self.slider_delay_ch_9)

        self.horizontalSpacer_23 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_9.addItem(self.horizontalSpacer_23)

        self.text_delay_ch_9 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_9.setObjectName(u"text_delay_ch_9")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_9.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_9.setSizePolicy(sizePolicy2)
        self.text_delay_ch_9.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_9.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_9.setMaxLength(5)
        self.text_delay_ch_9.setFrame(True)
        self.text_delay_ch_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_9.addWidget(self.text_delay_ch_9)

        self.label_delay_ns_ch_9 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_9.setObjectName(u"label_delay_ns_ch_9")

        self.horizontal_layout_delay_ch_9.addWidget(self.label_delay_ns_ch_9)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_9)

        self.horizontal_layout_delay_ch_10 = QHBoxLayout()
        self.horizontal_layout_delay_ch_10.setObjectName(u"horizontal_layout_delay_ch_10")
        self.horizontal_layout_delay_ch_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_10 = QLabel(self.groupBox_delays)
        self.label_delay_ch_10.setObjectName(u"label_delay_ch_10")
        self.label_delay_ch_10.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_10.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_10.setMargin(0)

        self.horizontal_layout_delay_ch_10.addWidget(self.label_delay_ch_10)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_10.addItem(self.horizontalSpacer_13)

        self.slider_delay_ch_10 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_10.setObjectName(u"slider_delay_ch_10")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_10.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_10.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_10.setMaximum(62)
        self.slider_delay_ch_10.setSingleStep(2)
        self.slider_delay_ch_10.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_10.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_10.setTickInterval(2)

        self.horizontal_layout_delay_ch_10.addWidget(self.slider_delay_ch_10)

        self.horizontalSpacer_34 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_10.addItem(self.horizontalSpacer_34)

        self.text_delay_ch_10 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_10.setObjectName(u"text_delay_ch_10")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_10.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_10.setSizePolicy(sizePolicy2)
        self.text_delay_ch_10.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_10.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_10.setMaxLength(5)
        self.text_delay_ch_10.setFrame(True)
        self.text_delay_ch_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_10.addWidget(self.text_delay_ch_10)

        self.label_delay_ns_ch_10 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_10.setObjectName(u"label_delay_ns_ch_10")

        self.horizontal_layout_delay_ch_10.addWidget(self.label_delay_ns_ch_10)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_10)

        self.horizontal_layout_delay_ch_11 = QHBoxLayout()
        self.horizontal_layout_delay_ch_11.setObjectName(u"horizontal_layout_delay_ch_11")
        self.horizontal_layout_delay_ch_11.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_11 = QLabel(self.groupBox_delays)
        self.label_delay_ch_11.setObjectName(u"label_delay_ch_11")
        self.label_delay_ch_11.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_11.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_11.setMargin(0)

        self.horizontal_layout_delay_ch_11.addWidget(self.label_delay_ch_11)

        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_11.addItem(self.horizontalSpacer_14)

        self.slider_delay_ch_11 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_11.setObjectName(u"slider_delay_ch_11")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_11.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_11.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_11.setMaximum(62)
        self.slider_delay_ch_11.setSingleStep(2)
        self.slider_delay_ch_11.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_11.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_11.setTickInterval(2)

        self.horizontal_layout_delay_ch_11.addWidget(self.slider_delay_ch_11)

        self.horizontalSpacer_32 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_11.addItem(self.horizontalSpacer_32)

        self.text_delay_ch_11 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_11.setObjectName(u"text_delay_ch_11")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_11.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_11.setSizePolicy(sizePolicy2)
        self.text_delay_ch_11.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_11.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_11.setMaxLength(5)
        self.text_delay_ch_11.setFrame(True)
        self.text_delay_ch_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_11.addWidget(self.text_delay_ch_11)

        self.label_delay_ns_ch_11 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_11.setObjectName(u"label_delay_ns_ch_11")

        self.horizontal_layout_delay_ch_11.addWidget(self.label_delay_ns_ch_11)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_11)

        self.horizontal_layout_delay_ch_12 = QHBoxLayout()
        self.horizontal_layout_delay_ch_12.setObjectName(u"horizontal_layout_delay_ch_12")
        self.horizontal_layout_delay_ch_12.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_12 = QLabel(self.groupBox_delays)
        self.label_delay_ch_12.setObjectName(u"label_delay_ch_12")
        self.label_delay_ch_12.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_12.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_12.setMargin(0)

        self.horizontal_layout_delay_ch_12.addWidget(self.label_delay_ch_12)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_12.addItem(self.horizontalSpacer_15)

        self.slider_delay_ch_12 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_12.setObjectName(u"slider_delay_ch_12")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_12.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_12.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_12.setMaximum(62)
        self.slider_delay_ch_12.setSingleStep(2)
        self.slider_delay_ch_12.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_12.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_12.setTickInterval(2)

        self.horizontal_layout_delay_ch_12.addWidget(self.slider_delay_ch_12)

        self.horizontalSpacer_33 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_12.addItem(self.horizontalSpacer_33)

        self.text_delay_ch_12 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_12.setObjectName(u"text_delay_ch_12")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_12.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_12.setSizePolicy(sizePolicy2)
        self.text_delay_ch_12.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_12.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_12.setMaxLength(5)
        self.text_delay_ch_12.setFrame(True)
        self.text_delay_ch_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_12.addWidget(self.text_delay_ch_12)

        self.label_delay_ns_ch_12 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_12.setObjectName(u"label_delay_ns_ch_12")

        self.horizontal_layout_delay_ch_12.addWidget(self.label_delay_ns_ch_12)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_12)

        self.horizontal_layout_delay_ch_13 = QHBoxLayout()
        self.horizontal_layout_delay_ch_13.setObjectName(u"horizontal_layout_delay_ch_13")
        self.horizontal_layout_delay_ch_13.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_13 = QLabel(self.groupBox_delays)
        self.label_delay_ch_13.setObjectName(u"label_delay_ch_13")
        self.label_delay_ch_13.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_13.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_13.setMargin(0)

        self.horizontal_layout_delay_ch_13.addWidget(self.label_delay_ch_13)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_13.addItem(self.horizontalSpacer_16)

        self.slider_delay_ch_13 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_13.setObjectName(u"slider_delay_ch_13")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_13.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_13.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_13.setMaximum(62)
        self.slider_delay_ch_13.setSingleStep(2)
        self.slider_delay_ch_13.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_13.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_13.setTickInterval(2)

        self.horizontal_layout_delay_ch_13.addWidget(self.slider_delay_ch_13)

        self.horizontalSpacer_35 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_13.addItem(self.horizontalSpacer_35)

        self.text_delay_ch_13 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_13.setObjectName(u"text_delay_ch_13")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_13.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_13.setSizePolicy(sizePolicy2)
        self.text_delay_ch_13.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_13.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_13.setMaxLength(5)
        self.text_delay_ch_13.setFrame(True)
        self.text_delay_ch_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_13.addWidget(self.text_delay_ch_13)

        self.label_delay_ns_ch_13 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_13.setObjectName(u"label_delay_ns_ch_13")

        self.horizontal_layout_delay_ch_13.addWidget(self.label_delay_ns_ch_13)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_13)

        self.horizontal_layout_delay_ch_14 = QHBoxLayout()
        self.horizontal_layout_delay_ch_14.setObjectName(u"horizontal_layout_delay_ch_14")
        self.horizontal_layout_delay_ch_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_14 = QLabel(self.groupBox_delays)
        self.label_delay_ch_14.setObjectName(u"label_delay_ch_14")
        self.label_delay_ch_14.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_14.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_14.setMargin(0)

        self.horizontal_layout_delay_ch_14.addWidget(self.label_delay_ch_14)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_14.addItem(self.horizontalSpacer_17)

        self.slider_delay_ch_14 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_14.setObjectName(u"slider_delay_ch_14")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_14.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_14.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_14.setMaximum(62)
        self.slider_delay_ch_14.setSingleStep(2)
        self.slider_delay_ch_14.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_14.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_14.setTickInterval(2)

        self.horizontal_layout_delay_ch_14.addWidget(self.slider_delay_ch_14)

        self.horizontalSpacer_22 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_14.addItem(self.horizontalSpacer_22)

        self.text_delay_ch_14 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_14.setObjectName(u"text_delay_ch_14")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_14.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_14.setSizePolicy(sizePolicy2)
        self.text_delay_ch_14.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_14.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_14.setMaxLength(5)
        self.text_delay_ch_14.setFrame(True)
        self.text_delay_ch_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_14.addWidget(self.text_delay_ch_14)

        self.label_delay_ns_ch_14 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_14.setObjectName(u"label_delay_ns_ch_14")

        self.horizontal_layout_delay_ch_14.addWidget(self.label_delay_ns_ch_14)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_14)

        self.horizontal_layout_delay_ch_15 = QHBoxLayout()
        self.horizontal_layout_delay_ch_15.setObjectName(u"horizontal_layout_delay_ch_15")
        self.horizontal_layout_delay_ch_15.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_delay_ch_15 = QLabel(self.groupBox_delays)
        self.label_delay_ch_15.setObjectName(u"label_delay_ch_15")
        self.label_delay_ch_15.setMinimumSize(QSize(49, 0))
        self.label_delay_ch_15.setFrameShape(QFrame.Shape.NoFrame)
        self.label_delay_ch_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_delay_ch_15.setMargin(0)

        self.horizontal_layout_delay_ch_15.addWidget(self.label_delay_ch_15)

        self.horizontalSpacer_18 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_15.addItem(self.horizontalSpacer_18)

        self.slider_delay_ch_15 = QSlider(self.groupBox_delays)
        self.slider_delay_ch_15.setObjectName(u"slider_delay_ch_15")
        sizePolicy1.setHeightForWidth(self.slider_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.slider_delay_ch_15.setSizePolicy(sizePolicy1)
        self.slider_delay_ch_15.setMinimumSize(QSize(250, 0))
        self.slider_delay_ch_15.setMaximum(62)
        self.slider_delay_ch_15.setSingleStep(2)
        self.slider_delay_ch_15.setOrientation(Qt.Orientation.Horizontal)
        self.slider_delay_ch_15.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_delay_ch_15.setTickInterval(2)

        self.horizontal_layout_delay_ch_15.addWidget(self.slider_delay_ch_15)

        self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_delay_ch_15.addItem(self.horizontalSpacer_21)

        self.text_delay_ch_15 = QLineEdit(self.groupBox_delays)
        self.text_delay_ch_15.setObjectName(u"text_delay_ch_15")
        sizePolicy2.setHeightForWidth(self.text_delay_ch_15.sizePolicy().hasHeightForWidth())
        self.text_delay_ch_15.setSizePolicy(sizePolicy2)
        self.text_delay_ch_15.setMinimumSize(QSize(21, 21))
        self.text_delay_ch_15.setMaximumSize(QSize(40, 16777215))
        self.text_delay_ch_15.setMaxLength(5)
        self.text_delay_ch_15.setFrame(True)
        self.text_delay_ch_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_layout_delay_ch_15.addWidget(self.text_delay_ch_15)

        self.label_delay_ns_ch_15 = QLabel(self.groupBox_delays)
        self.label_delay_ns_ch_15.setObjectName(u"label_delay_ns_ch_15")

        self.horizontal_layout_delay_ch_15.addWidget(self.label_delay_ns_ch_15)


        self.verticalLayout_3.addLayout(self.horizontal_layout_delay_ch_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
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

        self.horizontalLayout.addWidget(self.qb_delay_reset, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.qrb_control_all = QRadioButton(self.groupBox_delays)
        self.qrb_control_all.setObjectName(u"qrb_control_all")
        self.qrb_control_all.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.qrb_control_all)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox_delays, 0, 0, 1, 4)

        self.horizontalSlider_multiplicity_offset_dac = QSlider(Widget_Chipboard)
        self.horizontalSlider_multiplicity_offset_dac.setObjectName(u"horizontalSlider_multiplicity_offset_dac")
        self.horizontalSlider_multiplicity_offset_dac.setMaximum(1023)
        self.horizontalSlider_multiplicity_offset_dac.setSingleStep(10)
        self.horizontalSlider_multiplicity_offset_dac.setPageStep(128)
        self.horizontalSlider_multiplicity_offset_dac.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_multiplicity_offset_dac.setInvertedControls(False)
        self.horizontalSlider_multiplicity_offset_dac.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_multiplicity_offset_dac.setTickInterval(128)

        self.gridLayout.addWidget(self.horizontalSlider_multiplicity_offset_dac, 1, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_post_acq = QLabel(Widget_Chipboard)
        self.label_post_acq.setObjectName(u"label_post_acq")

        self.horizontalLayout_2.addWidget(self.label_post_acq)

        self.lineEdit_post_ack = QLineEdit(Widget_Chipboard)
        self.lineEdit_post_ack.setObjectName(u"lineEdit_post_ack")
        font1 = QFont()
        font1.setPointSize(13)
        self.lineEdit_post_ack.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lineEdit_post_ack)

        self.pushButton_post_acq = QPushButton(Widget_Chipboard)
        self.pushButton_post_acq.setObjectName(u"pushButton_post_acq")

        self.horizontalLayout_2.addWidget(self.pushButton_post_acq)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 3)


        self.retranslateUi(Widget_Chipboard)

        self.qb_delay_configure.setDefault(False)
        self.qb_delay_reset.setDefault(False)


        QMetaObject.connectSlotsByName(Widget_Chipboard)
    # setupUi

    def retranslateUi(self, Widget_Chipboard):
        Widget_Chipboard.setWindowTitle(QCoreApplication.translate("Widget_Chipboard", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget_Chipboard", u"Acquisition Mode", None))
        self.pushButton.setText(QCoreApplication.translate("Widget_Chipboard", u"Configure Chipboard Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget_Chipboard", u"Multiplexers", None))
        self.label_3.setText(QCoreApplication.translate("Widget_Chipboard", u"OR Output", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Widget_Chipboard", u"This is the CFD pulse generated by the PSD chips it is routed to backplane connector. ", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Widget_Chipboard", u"CFD OUT", None))
        self.label_4.setText(QCoreApplication.translate("Widget_Chipboard", u"INTX Output", None))
        self.label_6.setText(QCoreApplication.translate("Widget_Chipboard", u"Pre Amp MUX Output", None))
        self.comboBox_pre_amp_mux.setItemText(0, QCoreApplication.translate("Widget_Chipboard", u"Disabled", None))

        self.comboBox_intx_mux.setItemText(0, QCoreApplication.translate("Widget_Chipboard", u"PSD 0", None))
        self.comboBox_intx_mux.setItemText(1, QCoreApplication.translate("Widget_Chipboard", u"PSD 1", None))

        self.comboBox_or_mux.setItemText(0, QCoreApplication.translate("Widget_Chipboard", u"PSD 0", None))
        self.comboBox_or_mux.setItemText(1, QCoreApplication.translate("Widget_Chipboard", u"PSD 1", None))
        self.comboBox_or_mux.setItemText(2, QCoreApplication.translate("Widget_Chipboard", u"CFD", None))
        self.comboBox_or_mux.setItemText(3, QCoreApplication.translate("Widget_Chipboard", u"PSD 0 or PSD 1", None))

        self.comboBox_psd_cfd_mux.setItemText(0, QCoreApplication.translate("Widget_Chipboard", u"PSD 0", None))
        self.comboBox_psd_cfd_mux.setItemText(1, QCoreApplication.translate("Widget_Chipboard", u"PSD 1", None))

#if QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac_2.setToolTip(QCoreApplication.translate("Widget_Chipboard", u"<html><head/><body><p><span style=\" font-weight:700;\">Auto Veto Time: </span></p><p><br/></p><p>Configures the time at which the ASIC auto resets if the <span style=\" font-weight:700;\">Veto Reset(Take Event)</span> signal is not asserted.  </p><p>Inversely related to DAC voltage, not linear; Higher Voltage -&gt; Quicker reset.  </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_psd_auto_veto_dac_2.setText(QCoreApplication.translate("Widget_Chipboard", u"Multiplicity Offset", None))
        self.text_multiplicity_offset_dac.setInputMask(QCoreApplication.translate("Widget_Chipboard", u"0.00 V", None))
        self.text_multiplicity_offset_dac.setText(QCoreApplication.translate("Widget_Chipboard", u"0.0 V", None))
        self.comboBox_chipboard_mode.setItemText(0, QCoreApplication.translate("Widget_Chipboard", u"Disabled", None))
        self.comboBox_chipboard_mode.setItemText(1, QCoreApplication.translate("Widget_Chipboard", u"Enabled", None))

        self.groupBox_delays.setTitle(QCoreApplication.translate("Widget_Chipboard", u"Delays", None))
        self.label_15.setText(QCoreApplication.translate("Widget_Chipboard", u"Channel", None))
        self.label_21.setText(QCoreApplication.translate("Widget_Chipboard", u"Delay Setting", None))
        self.label_delay_ch_0.setText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.text_delay_ch_0.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_0.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_1.setText(QCoreApplication.translate("Widget_Chipboard", u"1", None))
        self.text_delay_ch_1.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_1.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_2.setText(QCoreApplication.translate("Widget_Chipboard", u"2", None))
        self.text_delay_ch_2.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_2.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_3.setText(QCoreApplication.translate("Widget_Chipboard", u"3", None))
        self.text_delay_ch_3.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_3.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_4.setText(QCoreApplication.translate("Widget_Chipboard", u"4", None))
        self.text_delay_ch_4.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_4.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_5.setText(QCoreApplication.translate("Widget_Chipboard", u"5", None))
        self.text_delay_ch_5.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_5.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_6.setText(QCoreApplication.translate("Widget_Chipboard", u"6", None))
        self.text_delay_ch_6.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_6.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_7.setText(QCoreApplication.translate("Widget_Chipboard", u"7", None))
        self.text_delay_ch_7.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_7.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_8.setText(QCoreApplication.translate("Widget_Chipboard", u"8", None))
        self.text_delay_ch_8.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_8.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_9.setText(QCoreApplication.translate("Widget_Chipboard", u"9", None))
        self.text_delay_ch_9.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_9.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_10.setText(QCoreApplication.translate("Widget_Chipboard", u"10", None))
        self.text_delay_ch_10.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_10.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_11.setText(QCoreApplication.translate("Widget_Chipboard", u"11", None))
        self.text_delay_ch_11.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_11.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_12.setText(QCoreApplication.translate("Widget_Chipboard", u"12", None))
        self.text_delay_ch_12.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_12.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_13.setText(QCoreApplication.translate("Widget_Chipboard", u"13", None))
        self.text_delay_ch_13.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_13.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_14.setText(QCoreApplication.translate("Widget_Chipboard", u"14", None))
        self.text_delay_ch_14.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_14.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.label_delay_ch_15.setText(QCoreApplication.translate("Widget_Chipboard", u"15", None))
        self.text_delay_ch_15.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"0", None))
        self.label_delay_ns_ch_15.setText(QCoreApplication.translate("Widget_Chipboard", u"ns", None))
        self.qb_delay_configure.setText(QCoreApplication.translate("Widget_Chipboard", u"Configure Delays", None))
        self.qb_delay_reset.setText(QCoreApplication.translate("Widget_Chipboard", u"Reset Delays", None))
        self.qrb_control_all.setText(QCoreApplication.translate("Widget_Chipboard", u"Control All Delays", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_multiplicity_offset_dac.setToolTip(QCoreApplication.translate("Widget_Chipboard", u"Voltage Slider for PSD Delay DAC A", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_post_acq.setToolTip(QCoreApplication.translate("Widget_Chipboard", u"<html><head/><body><p>This lets the user execute a data processing script after the data acquisition thread finishes acquisition. A new process will be executed of the program at the path specifed here. </p><p><span style=\" font-weight:700;\">$LAST_ACQ</span> can be used to pass the timestamped name of the last data acquisition. </p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_post_acq.setText(QCoreApplication.translate("Widget_Chipboard", u"Post Acquisition Script:", None))
        self.lineEdit_post_ack.setPlaceholderText(QCoreApplication.translate("Widget_Chipboard", u"/path/to/script $LAST_ACQ", None))
        self.pushButton_post_acq.setText(QCoreApplication.translate("Widget_Chipboard", u"Browse", None))
    # retranslateUi

