from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit

from PySide6.QtGui import QValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ClickableLineEdit(QLineEdit):
    focused = Signal()
    clicked = Signal()

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.focused.emit()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()


class EvenNumberValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.min_value = 0
        self.max_value = 62

    def validate(self, input_str, pos):
        if input_str == '':
            return QValidator.Intermediate, input_str, pos  # allow typing

        try:
            value = int(input_str)
        except ValueError:
            return QValidator.Invalid, input_str, pos

        if self.min_value <= value <= self.max_value and value % 2 == 0:
            return QValidator.Acceptable, input_str, pos
        elif 0 <= value <= self.max_value:
            return QValidator.Intermediate, input_str, pos  # still typing
        else:
            return QValidator.Invalid, input_str, pos

    def fixup(self, input_str):
        try:
            value = int(input_str)
            # Round to nearest even number within range
            if value < self.min_value:
                return str(self.min_value)
            if value > self.max_value:
                return str(self.max_value)
            if value % 2 != 0:
                value -= 1  # move down to nearest even
            return str(value)
        except ValueError:
            return str(self.min_value)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
