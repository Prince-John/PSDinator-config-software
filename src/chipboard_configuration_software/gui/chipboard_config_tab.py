import json
import sys

import configuration_helper
# import utilities
# import connection_helper

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRegularExpression

from ui_files.MainConfigWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ This is the class inheriting the Qt designer UI and adding functionality """

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()

    w.show()

    sys.exit(app.exec())
