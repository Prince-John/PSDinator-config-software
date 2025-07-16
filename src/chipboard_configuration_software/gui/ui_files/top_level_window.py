# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'top_level_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 902)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks|QMainWindow.DockOption.ForceTabbedDocks)
        self.actionSave_Configuration = QAction(MainWindow)
        self.actionSave_Configuration.setObjectName(u"actionSave_Configuration")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionReset_to_default = QAction(MainWindow)
        self.actionReset_to_default.setObjectName(u"actionReset_to_default")
        self.actionCFD_Settings = QAction(MainWindow)
        self.actionCFD_Settings.setObjectName(u"actionCFD_Settings")
        self.actionPSD_Settings = QAction(MainWindow)
        self.actionPSD_Settings.setObjectName(u"actionPSD_Settings")
        self.actionChipboard_Settings = QAction(MainWindow)
        self.actionChipboard_Settings.setObjectName(u"actionChipboard_Settings")
        self.actionGithub_Repo = QAction(MainWindow)
        self.actionGithub_Repo.setObjectName(u"actionGithub_Repo")
        self.actionChipboard_Firmware = QAction(MainWindow)
        self.actionChipboard_Firmware.setObjectName(u"actionChipboard_Firmware")
        self.actionCommand_Description = QAction(MainWindow)
        self.actionCommand_Description.setObjectName(u"actionCommand_Description")
        self.actionDebug_Console = QAction(MainWindow)
        self.actionDebug_Console.setObjectName(u"actionDebug_Console")
        self.actionDebug_Console.setCheckable(True)
        self.action_version = QAction(MainWindow)
        self.action_version.setObjectName(u"action_version")
        self.top_level = QWidget(MainWindow)
        self.top_level.setObjectName(u"top_level")
        self.verticalLayout = QVBoxLayout(self.top_level)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dock_area_placeholder = QWidget(self.top_level)
        self.dock_area_placeholder.setObjectName(u"dock_area_placeholder")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dock_area_placeholder.sizePolicy().hasHeightForWidth())
        self.dock_area_placeholder.setSizePolicy(sizePolicy)
        self.dock_area_placeholder.setMinimumSize(QSize(300, 300))
        self.Widget_closed_tabs_page = QWidget(self.dock_area_placeholder)
        self.Widget_closed_tabs_page.setObjectName(u"Widget_closed_tabs_page")
        self.Widget_closed_tabs_page.setGeometry(QRect(40, 140, 641, 251))
        self.gridLayout = QGridLayout(self.Widget_closed_tabs_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.Widget_closed_tabs_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.Widget_closed_tabs_page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.dock_area_placeholder)

        self.bottom_fixed_area = QWidget(self.top_level)
        self.bottom_fixed_area.setObjectName(u"bottom_fixed_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottom_fixed_area.sizePolicy().hasHeightForWidth())
        self.bottom_fixed_area.setSizePolicy(sizePolicy1)
        self.bottom_fixed_area.setMinimumSize(QSize(0, 45))
        self.bottom_fixed_area.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_bottom_configure = QHBoxLayout(self.bottom_fixed_area)
        self.horizontalLayout_bottom_configure.setObjectName(u"horizontalLayout_bottom_configure")
        self.pushButton_configure_chipboard = QPushButton(self.bottom_fixed_area)
        self.pushButton_configure_chipboard.setObjectName(u"pushButton_configure_chipboard")

        self.horizontalLayout_bottom_configure.addWidget(self.pushButton_configure_chipboard)

        self.line_2 = QFrame(self.bottom_fixed_area)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_bottom_configure.addWidget(self.line_2)

        self.progressBar = QProgressBar(self.bottom_fixed_area)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_bottom_configure.addWidget(self.progressBar)

        self.line = QFrame(self.bottom_fixed_area)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_bottom_configure.addWidget(self.line)

        self.pushButton_refresh_devices = QPushButton(self.bottom_fixed_area)
        self.pushButton_refresh_devices.setObjectName(u"pushButton_refresh_devices")

        self.horizontalLayout_bottom_configure.addWidget(self.pushButton_refresh_devices)

        self.label_3 = QLabel(self.bottom_fixed_area)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_bottom_configure.addWidget(self.label_3)

        self.comboBox_devices = QComboBox(self.bottom_fixed_area)
        self.comboBox_devices.setObjectName(u"comboBox_devices")
        self.comboBox_devices.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_bottom_configure.addWidget(self.comboBox_devices)


        self.verticalLayout.addWidget(self.bottom_fixed_area)

        MainWindow.setCentralWidget(self.top_level)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 928, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuWindows = QMenu(self.menubar)
        self.menuWindows.setObjectName(u"menuWindows")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave_Configuration)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionReset_to_default)
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.actionDebug_Console)
        self.menuAbout.addAction(self.action_version)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionGithub_Repo)
        self.menuAbout.addAction(self.actionChipboard_Firmware)
        self.menuAbout.addAction(self.actionCommand_Description)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PSDinator Configuration Software", None))
        self.actionSave_Configuration.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load ", None))
        self.actionReset_to_default.setText(QCoreApplication.translate("MainWindow", u"Reset to default", None))
        self.actionCFD_Settings.setText(QCoreApplication.translate("MainWindow", u"CFD Settings", None))
        self.actionPSD_Settings.setText(QCoreApplication.translate("MainWindow", u"PSD Settings", None))
        self.actionChipboard_Settings.setText(QCoreApplication.translate("MainWindow", u"Chipboard Settings", None))
        self.actionGithub_Repo.setText(QCoreApplication.translate("MainWindow", u"Github Repo", None))
        self.actionChipboard_Firmware.setText(QCoreApplication.translate("MainWindow", u"Chipboard Firmware Build Guide", None))
        self.actionCommand_Description.setText(QCoreApplication.translate("MainWindow", u"Command Description", None))
        self.actionDebug_Console.setText(QCoreApplication.translate("MainWindow", u"Debug Console", None))
        self.action_version.setText(QCoreApplication.translate("MainWindow", u"vX.X.X", None))
#if QT_CONFIG(tooltip)
        self.action_version.setToolTip(QCoreApplication.translate("MainWindow", u"Software Version", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"All configuration tabs have been closed. Open them from Menu bar -> Windows. ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WashU CFD-PSD Chipboard Configuration Utility", None))
        self.pushButton_configure_chipboard.setText(QCoreApplication.translate("MainWindow", u"Configure Chipboard", None))
        self.pushButton_refresh_devices.setText(QCoreApplication.translate("MainWindow", u"Refresh Devices", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Device:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuWindows.setTitle(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

