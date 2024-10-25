# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GlobalSettingsWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 358)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 260, 281, 61))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.externalAgndEnable = QCheckBox(self.layoutWidget)
        self.externalAgndEnable.setObjectName(u"externalAgndEnable")

        self.gridLayout.addWidget(self.externalAgndEnable, 3, 2, 1, 1)

        self.globalMode = QCheckBox(self.layoutWidget)
        self.globalMode.setObjectName(u"globalMode")

        self.gridLayout.addWidget(self.globalMode, 3, 1, 1, 1)

        self.LEOutEnable = QCheckBox(self.layoutWidget)
        self.LEOutEnable.setObjectName(u"LEOutEnable")

        self.gridLayout.addWidget(self.LEOutEnable, 2, 2, 1, 1)

        self.globalEnable = QCheckBox(self.layoutWidget)
        self.globalEnable.setObjectName(u"globalEnable")

        self.gridLayout.addWidget(self.globalEnable, 2, 1, 1, 1)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 20, 231, 235))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.nowlinMode = QComboBox(self.layoutWidget1)
        self.nowlinMode.addItem("")
        self.nowlinMode.addItem("")
        self.nowlinMode.setObjectName(u"nowlinMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nowlinMode.sizePolicy().hasHeightForWidth())
        self.nowlinMode.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nowlinMode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.nowlinDelay = QComboBox(self.layoutWidget1)
        self.nowlinDelay.addItem("")
        self.nowlinDelay.addItem("")
        self.nowlinDelay.setObjectName(u"nowlinDelay")
        sizePolicy1.setHeightForWidth(self.nowlinDelay.sizePolicy().hasHeightForWidth())
        self.nowlinDelay.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.nowlinDelay)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.LockoutDAC = QLineEdit(self.layoutWidget1)
        self.LockoutDAC.setObjectName(u"LockoutDAC")
        sizePolicy1.setHeightForWidth(self.LockoutDAC.sizePolicy().hasHeightForWidth())
        self.LockoutDAC.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.LockoutDAC)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lockoutMode = QComboBox(self.layoutWidget1)
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.addItem("")
        self.lockoutMode.setObjectName(u"lockoutMode")
        sizePolicy1.setHeightForWidth(self.lockoutMode.sizePolicy().hasHeightForWidth())
        self.lockoutMode.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lockoutMode)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.CFDPulseWidth = QComboBox(self.layoutWidget1)
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.addItem("")
        self.CFDPulseWidth.setObjectName(u"CFDPulseWidth")

        self.horizontalLayout_6.addWidget(self.CFDPulseWidth)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.AgndTrim = QComboBox(self.layoutWidget1)
        self.AgndTrim.addItem("")
        self.AgndTrim.setObjectName(u"AgndTrim")

        self.horizontalLayout_3.addWidget(self.AgndTrim)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.externalAgndEnable.setText(QCoreApplication.translate("Dialog", u"External AGND Enable", None))
        self.globalMode.setText(QCoreApplication.translate("Dialog", u"Global Mode", None))
        self.LEOutEnable.setText(QCoreApplication.translate("Dialog", u"LE Out Enable", None))
        self.globalEnable.setText(QCoreApplication.translate("Dialog", u"Global Enable", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nowlin Mode", None))
        self.nowlinMode.setItemText(0, QCoreApplication.translate("Dialog", u"Short", None))
        self.nowlinMode.setItemText(1, QCoreApplication.translate("Dialog", u"Long", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nowlin Delay (ns)", None))
        self.nowlinDelay.setItemText(0, QCoreApplication.translate("Dialog", u"Short", None))
        self.nowlinDelay.setItemText(1, QCoreApplication.translate("Dialog", u"Long", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Lockout DAC", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Lockout Mode", None))
        self.lockoutMode.setItemText(0, QCoreApplication.translate("Dialog", u"Short", None))
        self.lockoutMode.setItemText(1, QCoreApplication.translate("Dialog", u"Long", None))
        self.lockoutMode.setItemText(2, QCoreApplication.translate("Dialog", u"Disabled", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"CFD Pulse Width (ns)", None))
        self.CFDPulseWidth.setItemText(0, QCoreApplication.translate("Dialog", u"50", None))
        self.CFDPulseWidth.setItemText(1, QCoreApplication.translate("Dialog", u"100", None))
        self.CFDPulseWidth.setItemText(2, QCoreApplication.translate("Dialog", u"200", None))
        self.CFDPulseWidth.setItemText(3, QCoreApplication.translate("Dialog", u"500", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"AGND Trim", None))
        self.AgndTrim.setItemText(0, QCoreApplication.translate("Dialog", u"1.77", None))

    # retranslateUi

