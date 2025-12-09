"""
plot_manager.py — container widget that manages all loaded plots.

Creates a tab for each plot class discovered by plot_loader.
Each tab contains an instance of that plot class.
"""

from PySide6.QtWidgets import QTabWidget

from visualizer_app.core.plot_loader import load_plot_classes


class PlotManager(QTabWidget):
    """
    Holds plot modules as tabs.
    Responsible for creating, storing, and updating plot instances.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Discover user plot modules
        self.plot_classes = load_plot_classes()

        # Instantiate each class & add a tab for it
        self.plots = []
        for plot_cls in self.plot_classes:
            try:
                plot_obj = plot_cls()
            except Exception as e:
                print(f"[PlotManager] Failed to instantiate {plot_cls.__name__}: {e}")
                continue

            self.addTab(plot_obj, plot_obj.name)
            self.plots.append(plot_obj)

    def update_all_plots(self, data_dict: dict):
        """
        Send updated histogram data to all plot instances.
        Called every time the decode thread emits new data.

        Parameters
        ----------
        data_dict : dict[int → dict[str → (counts, bins)]]
        """
        for plot in self.plots:
            try:
                plot.update_plot(data_dict)
            except Exception as e:
                print(f"[PlotManager] Plot '{plot.name}' update failed: {e}")
