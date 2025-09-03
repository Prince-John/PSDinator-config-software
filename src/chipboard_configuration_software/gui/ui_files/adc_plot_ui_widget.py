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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_adc_plots(object):
    def setupUi(self, adc_plots):
        if not adc_plots.objectName():
            adc_plots.setObjectName(u"adc_plots")
        adc_plots.resize(897, 825)
        self.gridLayout = QGridLayout(adc_plots)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(adc_plots)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_event_count = QComboBox(adc_plots)
        self.comboBox_event_count.addItem("")
        self.comboBox_event_count.setObjectName(u"comboBox_event_count")

        self.horizontalLayout.addWidget(self.comboBox_event_count)

        self.label_4 = QLabel(adc_plots)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox_channel_selection = QComboBox(adc_plots)
        self.comboBox_channel_selection.addItem("")
        self.comboBox_channel_selection.setObjectName(u"comboBox_channel_selection")

        self.horizontalLayout.addWidget(self.comboBox_channel_selection)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.button_clear_all = QPushButton(adc_plots)
        self.button_clear_all.setObjectName(u"button_clear_all")

        self.gridLayout.addWidget(self.button_clear_all, 2, 0, 1, 1)

        self.button_save = QPushButton(adc_plots)
        self.button_save.setObjectName(u"button_save")

        self.gridLayout.addWidget(self.button_save, 2, 1, 1, 1)

        self.label_adc_hist = QLabel(adc_plots)
        self.label_adc_hist.setObjectName(u"label_adc_hist")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_adc_hist.setFont(font)

        self.gridLayout.addWidget(self.label_adc_hist, 0, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.adc_plot_layout_widget = GraphicsLayoutWidget(adc_plots)
        self.adc_plot_layout_widget.setObjectName(u"adc_plot_layout_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adc_plot_layout_widget.sizePolicy().hasHeightForWidth())
        self.adc_plot_layout_widget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.adc_plot_layout_widget)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 3)

        self.label_status_adc = QLabel(adc_plots)
        self.label_status_adc.setObjectName(u"label_status_adc")

        self.gridLayout.addWidget(self.label_status_adc, 2, 2, 1, 1)


        self.retranslateUi(adc_plots)

        QMetaObject.connectSlotsByName(adc_plots)
    # setupUi

    def retranslateUi(self, adc_plots):
        adc_plots.setWindowTitle(QCoreApplication.translate("adc_plots", u"Form", None))
        self.label.setText(QCoreApplication.translate("adc_plots", u"Histogram Max Count:", None))
        self.comboBox_event_count.setItemText(0, QCoreApplication.translate("adc_plots", u"2000", None))

        self.label_4.setText(QCoreApplication.translate("adc_plots", u"Channel Selection", None))
        self.comboBox_channel_selection.setItemText(0, QCoreApplication.translate("adc_plots", u"All", None))

        self.button_clear_all.setText(QCoreApplication.translate("adc_plots", u"Clear", None))
        self.button_save.setText(QCoreApplication.translate("adc_plots", u"Save Plots", None))
        self.label_adc_hist.setText(QCoreApplication.translate("adc_plots", u"ADC Histograms", None))
        self.label_status_adc.setText("")
    # retranslateUi

