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
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(659, 890)
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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 601, 581))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.enableDAC_05 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_05.setObjectName(u"enableDAC_05")

        self.gridLayout_2.addWidget(self.enableDAC_05, 7, 3, 1, 1)

        self.signBit_10 = QCheckBox(self.gridLayoutWidget)
        self.signBit_10.setObjectName(u"signBit_10")

        self.gridLayout_2.addWidget(self.signBit_10, 12, 4, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_2.addWidget(self.label_52, 3, 0, 1, 1)

        self.enableDAC_all = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_all.setObjectName(u"enableDAC_all")

        self.gridLayout_2.addWidget(self.enableDAC_all, 1, 3, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_2.addWidget(self.label_60, 7, 1, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_2.addWidget(self.label_56, 3, 1, 1, 1)

        self.enableDAC_03 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_03.setObjectName(u"enableDAC_03")

        self.gridLayout_2.addWidget(self.enableDAC_03, 5, 3, 1, 1)

        self.leadingEdgeDAC_15 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_15.setObjectName(u"leadingEdgeDAC_15")
        self.leadingEdgeDAC_15.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_15.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_15.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_15, 17, 2, 1, 1)

        self.leadingEdgeDAC_14 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_14.setObjectName(u"leadingEdgeDAC_14")
        self.leadingEdgeDAC_14.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_14.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_14.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_14, 16, 2, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 16, 0, 1, 1)

        self.enableDAC_00 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_00.setObjectName(u"enableDAC_00")

        self.gridLayout_2.addWidget(self.enableDAC_00, 2, 3, 1, 1)

        self.leadingEdgeDAC_05 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_05.setObjectName(u"leadingEdgeDAC_05")
        self.leadingEdgeDAC_05.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_05.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_05.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_05, 7, 2, 1, 1)

        self.signBit_06 = QCheckBox(self.gridLayoutWidget)
        self.signBit_06.setObjectName(u"signBit_06")

        self.gridLayout_2.addWidget(self.signBit_06, 8, 4, 1, 1)

        self.label_62 = QLabel(self.gridLayoutWidget)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_2.addWidget(self.label_62, 9, 1, 1, 1)

        self.enableDAC_02 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_02.setObjectName(u"enableDAC_02")

        self.gridLayout_2.addWidget(self.enableDAC_02, 4, 3, 1, 1)

        self.enableDAC_13 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_13.setObjectName(u"enableDAC_13")

        self.gridLayout_2.addWidget(self.enableDAC_13, 15, 3, 1, 1)

        self.enableDAC_07 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_07.setObjectName(u"enableDAC_07")

        self.gridLayout_2.addWidget(self.enableDAC_07, 9, 3, 1, 1)

        self.leadingEdgeDAC_13 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_13.setObjectName(u"leadingEdgeDAC_13")
        self.leadingEdgeDAC_13.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_13.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_13.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_13, 15, 2, 1, 1)

        self.signBit_02 = QCheckBox(self.gridLayoutWidget)
        self.signBit_02.setObjectName(u"signBit_02")

        self.gridLayout_2.addWidget(self.signBit_02, 4, 4, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_2.addWidget(self.label_58, 5, 1, 1, 1)

        self.leadingEdgeDAC_04 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_04.setObjectName(u"leadingEdgeDAC_04")
        self.leadingEdgeDAC_04.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_04.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_04.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_04, 6, 2, 1, 1)

        self.label_65 = QLabel(self.gridLayoutWidget)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_2.addWidget(self.label_65, 12, 1, 1, 1)

        self.enableDAC_12 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_12.setObjectName(u"enableDAC_12")

        self.gridLayout_2.addWidget(self.enableDAC_12, 14, 3, 1, 1)

        self.leadingEdgeDAC_07 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_07.setObjectName(u"leadingEdgeDAC_07")
        self.leadingEdgeDAC_07.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_07.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_07.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_07, 9, 2, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_63 = QLabel(self.gridLayoutWidget)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_2.addWidget(self.label_63, 10, 1, 1, 1)

        self.leadingEdgeDAC_10 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_10.setObjectName(u"leadingEdgeDAC_10")
        self.leadingEdgeDAC_10.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_10.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_10.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_10, 12, 2, 1, 1)

        self.signBit_07 = QCheckBox(self.gridLayoutWidget)
        self.signBit_07.setObjectName(u"signBit_07")

        self.gridLayout_2.addWidget(self.signBit_07, 9, 4, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_2.addWidget(self.label_66, 13, 1, 1, 1)

        self.enableDAC_10 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_10.setObjectName(u"enableDAC_10")

        self.gridLayout_2.addWidget(self.enableDAC_10, 12, 3, 1, 1)

        self.signBit_00 = QCheckBox(self.gridLayoutWidget)
        self.signBit_00.setObjectName(u"signBit_00")

        self.gridLayout_2.addWidget(self.signBit_00, 2, 4, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 14, 0, 1, 1)

        self.leadingEdgeDAC_06 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_06.setObjectName(u"leadingEdgeDAC_06")
        self.leadingEdgeDAC_06.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_06.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_06.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_06, 8, 2, 1, 1)

        self.leadingEdgeDAC_12 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_12.setObjectName(u"leadingEdgeDAC_12")
        self.leadingEdgeDAC_12.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_12.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_12.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_12, 14, 2, 1, 1)

        self.label_69 = QLabel(self.gridLayoutWidget)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_2.addWidget(self.label_69, 16, 1, 1, 1)

        self.enableDAC_01 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_01.setObjectName(u"enableDAC_01")

        self.gridLayout_2.addWidget(self.enableDAC_01, 3, 3, 1, 1)

        self.signBit_13 = QCheckBox(self.gridLayoutWidget)
        self.signBit_13.setObjectName(u"signBit_13")

        self.gridLayout_2.addWidget(self.signBit_13, 15, 4, 1, 1)

        self.enableDAC_11 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_11.setObjectName(u"enableDAC_11")

        self.gridLayout_2.addWidget(self.enableDAC_11, 13, 3, 1, 1)

        self.signBit_05 = QCheckBox(self.gridLayoutWidget)
        self.signBit_05.setObjectName(u"signBit_05")

        self.gridLayout_2.addWidget(self.signBit_05, 7, 4, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 15, 0, 1, 1)

        self.enableDAC_06 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_06.setObjectName(u"enableDAC_06")

        self.gridLayout_2.addWidget(self.enableDAC_06, 8, 3, 1, 1)

        self.signBit_15 = QCheckBox(self.gridLayoutWidget)
        self.signBit_15.setObjectName(u"signBit_15")

        self.gridLayout_2.addWidget(self.signBit_15, 17, 4, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_2.addWidget(self.label_57, 4, 1, 1, 1)

        self.leadingEdgeDAC_02 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_02.setObjectName(u"leadingEdgeDAC_02")
        self.leadingEdgeDAC_02.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_02.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_02.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_02, 4, 2, 1, 1)

        self.signBit_04 = QCheckBox(self.gridLayoutWidget)
        self.signBit_04.setObjectName(u"signBit_04")

        self.gridLayout_2.addWidget(self.signBit_04, 6, 4, 1, 1)

        self.signBit_14 = QCheckBox(self.gridLayoutWidget)
        self.signBit_14.setObjectName(u"signBit_14")

        self.gridLayout_2.addWidget(self.signBit_14, 16, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.leadingEdgeDAC_01 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_01.setObjectName(u"leadingEdgeDAC_01")
        self.leadingEdgeDAC_01.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_01.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_01.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_01, 3, 2, 1, 1)

        self.signBit_11 = QCheckBox(self.gridLayoutWidget)
        self.signBit_11.setObjectName(u"signBit_11")

        self.gridLayout_2.addWidget(self.signBit_11, 13, 4, 1, 1)

        self.enableDAC_15 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_15.setObjectName(u"enableDAC_15")

        self.gridLayout_2.addWidget(self.enableDAC_15, 17, 3, 1, 1)

        self.signBit_08 = QCheckBox(self.gridLayoutWidget)
        self.signBit_08.setObjectName(u"signBit_08")

        self.gridLayout_2.addWidget(self.signBit_08, 10, 4, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 1, 0, 1, 3)

        self.enableDAC_08 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_08.setObjectName(u"enableDAC_08")

        self.gridLayout_2.addWidget(self.enableDAC_08, 10, 3, 1, 1)

        self.leadingEdgeDAC_11 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_11.setObjectName(u"leadingEdgeDAC_11")
        self.leadingEdgeDAC_11.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_11.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_11.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_11, 13, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)

        self.enableDAC_04 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_04.setObjectName(u"enableDAC_04")

        self.gridLayout_2.addWidget(self.enableDAC_04, 6, 3, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 17, 0, 1, 1)

        self.leadingEdgeDAC_09 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_09.setObjectName(u"leadingEdgeDAC_09")
        self.leadingEdgeDAC_09.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_09.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_09.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_09, 11, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 6, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 13, 0, 1, 1)

        self.signBit_01 = QCheckBox(self.gridLayoutWidget)
        self.signBit_01.setObjectName(u"signBit_01")

        self.gridLayout_2.addWidget(self.signBit_01, 3, 4, 1, 1)

        self.label_68 = QLabel(self.gridLayoutWidget)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_2.addWidget(self.label_68, 15, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 5, 0, 1, 1)

        self.leadingEdgeDAC_08 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_08.setObjectName(u"leadingEdgeDAC_08")
        self.leadingEdgeDAC_08.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_08.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_08.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_08, 10, 2, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_2.addWidget(self.label_50, 7, 0, 1, 1)

        self.label_54 = QLabel(self.gridLayoutWidget)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_2.addWidget(self.label_54, 8, 0, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_2.addWidget(self.label_44, 10, 0, 1, 1)

        self.signBit_09 = QCheckBox(self.gridLayoutWidget)
        self.signBit_09.setObjectName(u"signBit_09")

        self.gridLayout_2.addWidget(self.signBit_09, 11, 4, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_2.addWidget(self.label_61, 8, 1, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_2.addWidget(self.label_48, 12, 0, 1, 1)

        self.signBit_03 = QCheckBox(self.gridLayoutWidget)
        self.signBit_03.setObjectName(u"signBit_03")

        self.gridLayout_2.addWidget(self.signBit_03, 5, 4, 1, 1)

        self.label_59 = QLabel(self.gridLayoutWidget)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_2.addWidget(self.label_59, 6, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 11, 0, 1, 1)

        self.enableDAC_14 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_14.setObjectName(u"enableDAC_14")

        self.gridLayout_2.addWidget(self.enableDAC_14, 16, 3, 1, 1)

        self.label_70 = QLabel(self.gridLayoutWidget)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_2.addWidget(self.label_70, 17, 1, 1, 1)

        self.leadingEdgeDAC_00 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_00.setObjectName(u"leadingEdgeDAC_00")
        self.leadingEdgeDAC_00.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_00.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_00.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_00, 2, 2, 1, 1)

        self.label_67 = QLabel(self.gridLayoutWidget)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_2.addWidget(self.label_67, 14, 1, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_2.addWidget(self.label_64, 11, 1, 1, 1)

        self.signBit_all = QCheckBox(self.gridLayoutWidget)
        self.signBit_all.setObjectName(u"signBit_all")

        self.gridLayout_2.addWidget(self.signBit_all, 1, 4, 1, 1)

        self.leadingEdgeDAC_03 = QLineEdit(self.gridLayoutWidget)
        self.leadingEdgeDAC_03.setObjectName(u"leadingEdgeDAC_03")
        self.leadingEdgeDAC_03.setMinimumSize(QSize(100, 0))
        self.leadingEdgeDAC_03.setInputMethodHints(Qt.ImhNone)
        self.leadingEdgeDAC_03.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.leadingEdgeDAC_03, 5, 2, 1, 1)

        self.signBit_12 = QCheckBox(self.gridLayoutWidget)
        self.signBit_12.setObjectName(u"signBit_12")

        self.gridLayout_2.addWidget(self.signBit_12, 14, 4, 1, 1)

        self.enableDAC_09 = QCheckBox(self.gridLayoutWidget)
        self.enableDAC_09.setObjectName(u"enableDAC_09")

        self.gridLayout_2.addWidget(self.enableDAC_09, 11, 3, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_5.addWidget(self.label)

        self.chipNumber_display = QLCDNumber(self.gridLayoutWidget)
        self.chipNumber_display.setObjectName(u"chipNumber_display")
        self.chipNumber_display.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chipNumber_display.sizePolicy().hasHeightForWidth())
        self.chipNumber_display.setSizePolicy(sizePolicy)
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
        self.chipNumber_display.setMode(QLCDNumber.Dec)
        self.chipNumber_display.setSegmentStyle(QLCDNumber.Flat)
        self.chipNumber_display.setProperty("value", 0.000000000000000)

        self.horizontalLayout_5.addWidget(self.chipNumber_display)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-20, 60, 731, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-50, 720, 781, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-90, 650, 781, 51))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 621, 44))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setTextFormat(Qt.MarkdownText)
        self.label_11.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.chipNumber = QComboBox(self.layoutWidget)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chipNumber.sizePolicy().hasHeightForWidth())
        self.chipNumber.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.chipNumber)

        self.detectI2CDevices = QPushButton(self.layoutWidget)
        self.detectI2CDevices.setObjectName(u"detectI2CDevices")
        self.detectI2CDevices.setFlat(False)

        self.horizontalLayout_2.addWidget(self.detectI2CDevices)

        self.editGlobalSettings = QPushButton(self.layoutWidget)
        self.editGlobalSettings.setObjectName(u"editGlobalSettings")

        self.horizontalLayout_2.addWidget(self.editGlobalSettings)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 750, 601, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.configureChip = QPushButton(self.layoutWidget1)
        self.configureChip.setObjectName(u"configureChip")

        self.horizontalLayout.addWidget(self.configureChip)

        self.pulseRST_L = QPushButton(self.layoutWidget1)
        self.pulseRST_L.setObjectName(u"pulseRST_L")

        self.horizontalLayout.addWidget(self.pulseRST_L)

        self.progressBar = QProgressBar(self.layoutWidget1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.progressBar)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 690, 601, 33))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_29.addWidget(self.label_2)

        self.testPoint = QComboBox(self.layoutWidget2)
        self.testPoint.addItem("")
        self.testPoint.addItem("")
        self.testPoint.addItem("")
        self.testPoint.addItem("")
        self.testPoint.addItem("")
        self.testPoint.setObjectName(u"testPoint")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.testPoint.sizePolicy().hasHeightForWidth())
        self.testPoint.setSizePolicy(sizePolicy3)

        self.horizontalLayout_29.addWidget(self.testPoint)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_29.addWidget(self.label_7)

        self.testPointChannel = QComboBox(self.layoutWidget2)
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.addItem("")
        self.testPointChannel.setObjectName(u"testPointChannel")

        self.horizontalLayout_29.addWidget(self.testPointChannel)

        self.negativePolarity = QCheckBox(self.layoutWidget2)
        self.negativePolarity.setObjectName(u"negativePolarity")

        self.horizontalLayout_29.addWidget(self.negativePolarity)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 659, 37))
        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_52.setBuddy(self.leadingEdgeDAC_01)
        self.label_46.setBuddy(self.leadingEdgeDAC_14)
        self.label_10.setBuddy(self.leadingEdgeDAC_02)
        self.label_40.setBuddy(self.leadingEdgeDAC_12)
        self.label_20.setBuddy(self.leadingEdgeDAC_13)
        self.label_3.setBuddy(self.leadingEdgeDAC_00)
        self.label_12.setBuddy(self.leadingEdgeDAC_07)
        self.label_18.setBuddy(self.leadingEdgeDAC_15)
        self.label_14.setBuddy(self.leadingEdgeDAC_04)
        self.label_16.setBuddy(self.leadingEdgeDAC_11)
        self.label_42.setBuddy(self.leadingEdgeDAC_03)
        self.label_50.setBuddy(self.leadingEdgeDAC_05)
        self.label_54.setBuddy(self.leadingEdgeDAC_06)
        self.label_44.setBuddy(self.leadingEdgeDAC_08)
        self.label_48.setBuddy(self.leadingEdgeDAC_10)
        self.label_22.setBuddy(self.leadingEdgeDAC_09)
        self.label_11.setBuddy(self.chipNumber)
        self.label_2.setBuddy(self.testPoint)
        self.label_7.setBuddy(self.testPointChannel)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.chipNumber, self.detectI2CDevices)
        QWidget.setTabOrder(self.detectI2CDevices, self.editGlobalSettings)
        QWidget.setTabOrder(self.editGlobalSettings, self.enableDAC_all)
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
        QWidget.setTabOrder(self.signBit_15, self.testPoint)
        QWidget.setTabOrder(self.testPoint, self.testPointChannel)
        QWidget.setTabOrder(self.testPointChannel, self.negativePolarity)
        QWidget.setTabOrder(self.negativePolarity, self.configureChip)
        QWidget.setTabOrder(self.configureChip, self.pulseRST_L)

        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menutest.addAction(self.actionload)
        self.menutest.addAction(self.actionSave)
        self.menutest.addAction(self.actionSavs_As)
        self.menuAbout.addAction(self.actionGithub_Repository)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionload.setText(QCoreApplication.translate("MainWindow", u"Load Configuration", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save ", None))
        self.actionSavs_As.setText(QCoreApplication.translate("MainWindow", u"Savs As", None))
        self.actionGithub_Repository.setText(QCoreApplication.translate("MainWindow", u"Github Repository", None))
        self.enableDAC_05.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_10.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.enableDAC_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.enableDAC_03.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_15.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_14.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Channel 14:", None))
        self.enableDAC_00.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_05.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_05.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_06.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.enableDAC_02.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_13.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.enableDAC_07.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_13.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_02.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_04.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_04.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.enableDAC_12.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_07.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_07.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_10.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_07.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.enableDAC_10.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_00.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Channel 12:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_06.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_06.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_12.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.enableDAC_01.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_13.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_11.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_05.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Channel 13:", None))
        self.enableDAC_06.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_15.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_02.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_02.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_04.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.signBit_14.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel 0:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_01.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_01.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_11.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_15.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.signBit_08.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_08.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_11.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Channel 7:", None))
        self.enableDAC_04.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Channel 15:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_09.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_09.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Channel 11:", None))
        self.signBit_01.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_08.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_08.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Channel 5:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Channel 6:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Channel 8:", None))
        self.signBit_09.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Channel 10:", None))
        self.signBit_03.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Channel 9:", None))
        self.enableDAC_14.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_00.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_00.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Leading Edge DAC", None))
        self.signBit_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
#if QT_CONFIG(tooltip)
        self.leadingEdgeDAC_03.setToolTip(QCoreApplication.translate("MainWindow", u"Enter value in Hex", None))
#endif // QT_CONFIG(tooltip)
        self.leadingEdgeDAC_03.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x00", None))
        self.signBit_12.setText(QCoreApplication.translate("MainWindow", u"Sign Bit", None))
        self.enableDAC_09.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"# Current chip is :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"**Select Chip Number:**", None))
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

        self.detectI2CDevices.setText(QCoreApplication.translate("MainWindow", u"Detect I2C Devices", None))
        self.editGlobalSettings.setText(QCoreApplication.translate("MainWindow", u"Edit Global Settings", None))
        self.configureChip.setText(QCoreApplication.translate("MainWindow", u"Configure Chip", None))
        self.pulseRST_L.setText(QCoreApplication.translate("MainWindow", u"Pulse RST_L", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Test Point", None))
        self.testPoint.setItemText(0, QCoreApplication.translate("MainWindow", u"AVSS", None))
        self.testPoint.setItemText(1, QCoreApplication.translate("MainWindow", u"Lockout Pulse", None))
        self.testPoint.setItemText(2, QCoreApplication.translate("MainWindow", u"Leading Edge Detector", None))
        self.testPoint.setItemText(3, QCoreApplication.translate("MainWindow", u"Zero Crossing Detector", None))
        self.testPoint.setItemText(4, QCoreApplication.translate("MainWindow", u"Oneshot Trigger", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Test Point Channel", None))
        self.testPointChannel.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.testPointChannel.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.testPointChannel.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.testPointChannel.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.testPointChannel.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.testPointChannel.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.testPointChannel.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.testPointChannel.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.testPointChannel.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.testPointChannel.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.testPointChannel.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.testPointChannel.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.testPointChannel.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.testPointChannel.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.testPointChannel.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.testPointChannel.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))

        self.negativePolarity.setText(QCoreApplication.translate("MainWindow", u"Negative Polarity", None))
        self.menutest.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

