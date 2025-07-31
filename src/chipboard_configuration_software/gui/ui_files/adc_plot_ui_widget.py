# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adc_plot_ui_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_adc_plots(object):
    def setupUi(self, adc_plots):
        if not adc_plots.objectName():
            adc_plots.setObjectName(u"adc_plots")
        adc_plots.resize(862, 790)
        self.gridLayout = QGridLayout(adc_plots)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_adc_hist = QLabel(adc_plots)
        self.label_adc_hist.setObjectName(u"label_adc_hist")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_adc_hist.setFont(font)

        self.gridLayout.addWidget(self.label_adc_hist, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(adc_plots)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_test_mode_channel = QLabel(adc_plots)
        self.label_test_mode_channel.setObjectName(u"label_test_mode_channel")

        self.horizontalLayout.addWidget(self.label_test_mode_channel)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.adc_a_widget = PlotWidget(adc_plots)
        self.adc_a_widget.setObjectName(u"adc_a_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adc_a_widget.sizePolicy().hasHeightForWidth())
        self.adc_a_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.adc_a_widget)

        self.label = QLabel(adc_plots)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.adc_b_widget = PlotWidget(adc_plots)
        self.adc_b_widget.setObjectName(u"adc_b_widget")
        sizePolicy.setHeightForWidth(self.adc_b_widget.sizePolicy().hasHeightForWidth())
        self.adc_b_widget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.adc_b_widget)

        self.label_2 = QLabel(adc_plots)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.adc_c_widget = PlotWidget(adc_plots)
        self.adc_c_widget.setObjectName(u"adc_c_widget")
        sizePolicy.setHeightForWidth(self.adc_c_widget.sizePolicy().hasHeightForWidth())
        self.adc_c_widget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.adc_c_widget)

        self.label_3 = QLabel(adc_plots)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 3)

        self.button_clear_all = QPushButton(adc_plots)
        self.button_clear_all.setObjectName(u"button_clear_all")

        self.gridLayout.addWidget(self.button_clear_all, 4, 0, 1, 1)

        self.button_save = QPushButton(adc_plots)
        self.button_save.setObjectName(u"button_save")

        self.gridLayout.addWidget(self.button_save, 4, 1, 1, 1)


        self.retranslateUi(adc_plots)

        QMetaObject.connectSlotsByName(adc_plots)
    # setupUi

    def retranslateUi(self, adc_plots):
        adc_plots.setWindowTitle(QCoreApplication.translate("adc_plots", u"Form", None))
        self.label_adc_hist.setText(QCoreApplication.translate("adc_plots", u"ADC Histograms", None))
        self.label_4.setText(QCoreApplication.translate("adc_plots", u"Test Mode Channel:", None))
        self.label_test_mode_channel.setText("")
        self.label.setText(QCoreApplication.translate("adc_plots", u"A", None))
        self.label_2.setText(QCoreApplication.translate("adc_plots", u"B", None))
        self.label_3.setText(QCoreApplication.translate("adc_plots", u"C", None))
        self.button_clear_all.setText(QCoreApplication.translate("adc_plots", u"Clear", None))
        self.button_save.setText(QCoreApplication.translate("adc_plots", u"Save", None))
    # retranslateUi

