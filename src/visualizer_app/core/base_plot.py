from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg


class BasePlot(QWidget):
    """
    Base class for visualization plugin modules.

    Subclasses may override:
        - name (string)
        - _create_main_widget()  ← to replace the PlotWidget entirely
        - setup()
        - update_plot(data)
    """

    name = "Unnamed Plot"

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        # Subclass may override this to provide a replacement widget
        self.main_widget = self._create_main_widget()

        layout.addWidget(self.main_widget)

        # If using PlotWidget, make plot_item available
        if isinstance(self.main_widget, pg.PlotWidget):
            self.plot_widget = self.main_widget
            self.plot_item = self.plot_widget.getPlotItem()
        else:
            self.plot_widget = None
            self.plot_item = None

        self.items = {}

        self.setup()

    # ------------------------------------------------------------------
    # Hooks for subclasses
    # ------------------------------------------------------------------

    def _create_main_widget(self):
        """
        Default: return a PlotWidget.
        Subclasses may override (e.g. DockArea)
        """
        return pg.PlotWidget()

    def setup(self):
        """Subclass sets up curves, axes, items, etc."""
        pass

    def update_plot(self, data_dict: dict):
        """Subclass updates visuals using histogram data."""
        pass
