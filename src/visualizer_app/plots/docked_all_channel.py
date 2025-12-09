import numpy as np
import pyqtgraph as pg
from pyqtgraph.dockarea import DockArea, Dock

from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QComboBox,
    QVBoxLayout, QPushButton
)
from PySide6 import QtGui

from visualizer_app.core.base_plot import BasePlot


FONT_SIZE = 14
TITLE_SIZE = 20
TICK_FONT = QtGui.QFont("Helvetica", 12)


class ADCDockHistogramView(BasePlot):
    name = "ADC Histogram"

    # ---------------------------------------------------------
    # Create QWidget containing controls + dock area
    # ---------------------------------------------------------
    def _create_main_widget(self):
        container = QWidget()
        layout = QVBoxLayout(container)

        # ===== Top Control Bar =====
        ctrl = QHBoxLayout()

        # Channel filter combo
        self.filter_label = QLabel("Channel Filter:")
        self.filter_label.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        self.filter_combo = QComboBox()
        self.filter_combo.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        self.filter_combo.addItem("All")
        for ch in range(16):
            self.filter_combo.addItem(str(ch))
        ctrl.addWidget(self.filter_label)
        ctrl.addWidget(self.filter_combo)

        # Share X-axis toggle
        self.share_axes_btn = QPushButton("Share X-Axis")
        self.share_axes_btn.setCheckable(True)
        self.share_axes_btn.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(self.share_axes_btn)

        # Clear histograms
        self.clear_btn = QPushButton("Clear Histograms")
        self.clear_btn.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(self.clear_btn)

        # Log scale toggle
        self.log_btn = QPushButton("Log Scale")
        self.log_btn.setCheckable(True)
        self.log_btn.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(self.log_btn)

        ctrl.addStretch()
        layout.addLayout(ctrl)

        # ===== DockArea =====
        self.area = DockArea()
        layout.addWidget(self.area)

        return container

    # ---------------------------------------------------------
    # Setup docked histograms
    # ---------------------------------------------------------
    def setup(self):
        # Docks
        self.dock_A = Dock("Subchannel A", size=(500, 400))
        self.dock_B = Dock("Subchannel B", size=(500, 400))
        self.dock_C = Dock("Subchannel C", size=(500, 400))
        self.dock_T = Dock("TVC",          size=(500, 500))

        self.area.addDock(self.dock_A, 'top')
        self.area.addDock(self.dock_B, 'bottom', self.dock_A)
        self.area.addDock(self.dock_C, 'bottom', self.dock_B)
        self.area.addDock(self.dock_T, 'bottom', self.dock_C)

        # Maps for A/B/C/T
        self.labels = ["A", "B", "C", "T"]
        self.docks = {
            "A": self.dock_A,
            "B": self.dock_B,
            "C": self.dock_C,
            "T": self.dock_T,
        }

        self.plots = {}
        self.curves = {"A": {}, "B": {}, "C": {}, "T": {}}

        # Cache of original linear histogram data (for reversible log)
        self.original_y = {
            "A": {},
            "B": {},
            "C": {},
            "T": {}
        }

        self.legends = {}

        # Build each dock's PlotWidget
        for label in self.labels:
            pw = pg.PlotWidget()
            pw.setTitle(f"ADC {label}", size=f"{TITLE_SIZE}pt")
            pw.setLabel("bottom", "ADC Value", size=f"{FONT_SIZE}pt")
            pw.setLabel("left", "Counts",     size=f"{FONT_SIZE}pt")
            pw.enableAutoRange("y", True)
            pw.enableAutoRange("x", True)
            pw.setMouseEnabled(x=True, y=False)
            pw.setDownsampling(mode="peak")

            # Increase tick fonts
            pw.getAxis("bottom").setStyle(tickFont=TICK_FONT)
            pw.getAxis("left").setStyle(tickFont=TICK_FONT)

            legend = pg.LegendItem((80, 60), offset=(60, 20))
            legend.setParentItem(pw.graphicsItem())

            self.plots[label] = pw
            self.legends[label] = legend

            self.docks[label].addWidget(pw)

        # State
        self.selected_channel = None
        self.log_scale = False

        # Connect interactions
        self.filter_combo.currentTextChanged.connect(self._on_filter_changed)
        self.clear_btn.clicked.connect(self._on_clear_pressed)
        self.share_axes_btn.toggled.connect(self._on_share_axes_toggled)
        self.log_btn.toggled.connect(self._on_log_toggled)

    # ---------------------------------------------------------
    # Filtering
    # ---------------------------------------------------------
    def _on_filter_changed(self, text):
        self.selected_channel = None if text == "All" else int(text)
        self._apply_filter()

    def _apply_filter(self):
        for adc_label in self.labels:
            for ch, curve in self.curves[adc_label].items():
                curve.setVisible(self.selected_channel is None or ch == self.selected_channel)

    # ---------------------------------------------------------
    # Clear button
    # ---------------------------------------------------------
    def _on_clear_pressed(self):
        """Clear decoder histograms AND displayed curves."""
        parent_window = self.window()
        buffers = parent_window.reader_thread.np_buffers
        buffers.clear_histograms()
        buffers.clear_buffers()
        # Reset visuals
        for adc_label in self.labels:
            for ch, curve in self.curves[adc_label].items():
                curve.setData([0], [])
            # Also clear caches
            self.original_y[adc_label].clear()

    # ---------------------------------------------------------
    # Share axes
    # ---------------------------------------------------------
    def _on_share_axes_toggled(self, enabled):
        if enabled:
            master = self.plots["A"].getPlotItem()
            for lbl in self.labels:
                if lbl != "A":
                    self.plots[lbl].getPlotItem().setXLink(master)
        else:
            for lbl in self.labels:
                self.plots[lbl].getPlotItem().setXLink(None)

    # ---------------------------------------------------------
    # Log scale toggle
    # ---------------------------------------------------------
    def _on_log_toggled(self, enabled):
        self.log_scale = enabled
        self._redraw_all_curves()

    def _redraw_all_curves(self):
        """Apply log/linear transform (reversible) using cached originals."""
        for adc_label in self.labels:
            for ch, curve in self.curves[adc_label].items():

                # Must have original linear cached
                if ch not in self.original_y[adc_label]:
                    continue

                y_linear = self.original_y[adc_label][ch]
                x = curve.xData
                if x is None:
                    continue

                # Apply transform
                if self.log_scale:
                    y_display = np.log10(y_linear + 1)
                else:
                    y_display = y_linear

                curve.setData(x, y_display, stepMode=True)

    # ---------------------------------------------------------
    # Update from histogram data (called from PlotManager)
    # ---------------------------------------------------------
    def update_plot(self, updates: dict):
        """
        updates[ch][adc_label] = (counts, bin_edges)
        """
        for ch, adc_info in updates.items():
            for adc_label, (counts, bin_edges) in adc_info.items():

                x = bin_edges
                y_linear = counts.astype(float)

                # Cache linear data
                self.original_y[adc_label][ch] = y_linear

                # Convert for display
                if self.log_scale:
                    y_display = np.log10(y_linear + 1)
                else:
                    y_display = y_linear

                # Create new curve if needed
                if ch not in self.curves[adc_label]:
                    color = pg.intColor(ch, hues=16, values=1, maxValue=255, alpha=220)
                    curve = pg.PlotCurveItem(
                        x, y_display, stepMode=True,
                        fillLevel=0,
                        pen=color,
                        brush=color
                    )
                    self.plots[adc_label].addItem(curve)
                    self.curves[adc_label][ch] = curve
                    self.legends[adc_label].addItem(curve, f"Ch {ch}")

                else:
                    # Update existing curve
                    self.curves[adc_label][ch].setData(x, y_display, stepMode=True)

        self._apply_filter()
