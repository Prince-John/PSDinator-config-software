import numpy as np
import pyqtgraph as pg
from pyqtgraph.dockarea import DockArea, Dock

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QPushButton,
)

from visualizer_app.core.base_plot import BasePlot

FONT_SIZE = 16
TITLE_SIZE = 20


class ADC2DSummaryView(BasePlot):
    """
    Corrected 2D Summary Plot:
    --------------------------
    • X axis: ADC code (binned)
    • Y axis: channel (0–15)
    • Color: intensity from a shared colormap (viridis)
    • Scalar → colormap pipeline (correct for ColorBarItem)
    """

    name = "2D Summary Plots"

    ADC_LABELS = ["A", "B", "C", "T"]
    ADC_INDEX_MAP = {"A": 0, "B": 1, "C": 2, "T": 3}

    # ------------------------------------------------------------------
    # Main UI
    # ------------------------------------------------------------------
    def _create_main_widget(self):
        container = QWidget()
        layout = QVBoxLayout(container)

        ctrl = QHBoxLayout()

        # X-min
        lbl_min = QLabel("X-range Min:")
        lbl_min.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(lbl_min)

        self.range_min = QSpinBox()
        self.range_min.setRange(-32768, 32767)
        self.range_min.setValue(-1000)
        self.range_min.setStyleSheet(f"font-size: {FONT_SIZE}px; min-width: 90px;")
        ctrl.addWidget(self.range_min)

        # X-max
        lbl_max = QLabel("X-range Max:")
        lbl_max.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(lbl_max)

        self.range_max = QSpinBox()
        self.range_max.setRange(-32768, 32767)
        self.range_max.setValue(30000)
        self.range_max.setStyleSheet(f"font-size: {FONT_SIZE}px; min-width: 90px;")
        ctrl.addWidget(self.range_max)

        # Bin count
        lbl_bins = QLabel("Bins:")
        lbl_bins.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        ctrl.addWidget(lbl_bins)

        self.bin_count = QSpinBox()
        self.bin_count.setRange(16, 4096)
        self.bin_count.setValue(256)
        self.bin_count.setStyleSheet(f"font-size: {FONT_SIZE}px; min-width: 90px;")
        ctrl.addWidget(self.bin_count)

        # Clear plots
        self.btn_clear = QPushButton("Clear Plots")
        self.btn_clear.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        self.btn_clear.clicked.connect(self._on_clear)
        ctrl.addWidget(self.btn_clear)

        # Share X axis
        self.btn_share_x = QPushButton("Share X-Axis")
        self.btn_share_x.setCheckable(True)
        self.btn_share_x.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        self.btn_share_x.clicked.connect(self._on_share_x)
        ctrl.addWidget(self.btn_share_x)

        # Log toggle
        self.btn_log = QPushButton("Log Scale")
        self.btn_log.setCheckable(True)
        self.btn_log.setStyleSheet(f"font-size: {FONT_SIZE}px;")
        self.btn_log.toggled.connect(self._on_log_toggled)
        ctrl.addWidget(self.btn_log)

        ctrl.addStretch()
        layout.addLayout(ctrl)

        # Dock area
        self.area = DockArea()
        layout.addWidget(self.area)

        return container

    # ------------------------------------------------------------------
    # Setup plotting docks
    # ------------------------------------------------------------------
    def setup(self):

        self.plots = {}
        self.images = {}
        self.cbars = {}
        self.glws = {}

        # Shared colormap
        self.cmap = pg.colormap.get("viridis")

        docks = {
            "A": Dock("ADC A Summary", size=(400, 300)),
            "B": Dock("ADC B Summary", size=(400, 300)),
            "C": Dock("ADC C Summary", size=(400, 300)),
            "T": Dock("ADC T Summary", size=(400, 300)),
        }

        # Arrange docks
        self.area.addDock(docks["A"], "top")
        self.area.addDock(docks["B"], "right", docks["A"])
        self.area.addDock(docks["C"], "bottom", docks["A"])
        self.area.addDock(docks["T"], "bottom", docks["B"])

        # Create each panel
        for label, dock in docks.items():

            glw = pg.GraphicsLayoutWidget()
            self.glws[label] = glw

            # Main plot
            plot = glw.addPlot(0, 0)
            plot.setTitle(f"ADC {label} Summary", size=f"{TITLE_SIZE}pt")
            plot.setLabel("bottom", "ADC Code", size=f"{FONT_SIZE}pt")
            plot.setLabel("left", "Channel", size=f"{FONT_SIZE}pt")

            ticks_centered = [(i + 0.5, str(i)) for i in range(16)]
            plot.getAxis("left").setTicks([ticks_centered])

            plot.getAxis("bottom").setStyle(
                tickFont=QtGui.QFont("Helvetica", FONT_SIZE)
            )
            plot.getAxis("left").setStyle(
                tickFont=QtGui.QFont("Helvetica", FONT_SIZE)
            )

            # Scalar → colormap → ImageItem
            img = pg.ImageItem()
            plot.addItem(img)

            # Color bar
            cb = pg.ColorBarItem(
                values=(0, 1),
                colorMap=self.cmap,
                label="Counts",
                width=14,
                interactive=False,
            )
            cb.setImageItem(img, insert_in=plot)
            glw.addItem(cb, 0, 1)

            dock.addWidget(glw)

            self.plots[label] = plot
            self.images[label] = img
            self.cbars[label] = cb

    # ------------------------------------------------------------------
    # Main update loop
    # ------------------------------------------------------------------
    def update_plot(self, _unused):

        parent = self.window()
        buffers = parent.reader_thread.np_buffers

        x_min = self.range_min.value()
        x_max = self.range_max.value()
        bins_x = self.bin_count.value()

        if x_max <= x_min:
            return

        # Uniform bins
        edges = np.linspace(x_min, x_max, bins_x + 1)

        # Heatmaps per ADC
        heatmaps = {
            label: np.zeros((16, bins_x), dtype=np.float32)
            for label in self.ADC_LABELS
        }

        # Fill from rolling buffers
        for ch in range(16):
            data = buffers.get_channel(ch)
            if data.size == 0:
                continue

            for label in self.ADC_LABELS:
                idx = self.ADC_INDEX_MAP[label]
                adc_vals = data[:, idx]
                counts, _ = np.histogram(adc_vals, bins=edges)
                heatmaps[label][ch, :] = counts

        # Draw each ADC
        for label in self.ADC_LABELS:

            heat = heatmaps[label]

            # log mode
            if self.btn_log.isChecked():
                heat_proc = np.log10(heat + 1)
            else:
                heat_proc = heat

            max_val = heat_proc.max()
            if max_val <= 0:
                max_val = 1.0

            # Normalize scalar image
            normalized = heat_proc / max_val

            # Scalar → ImageItem (correct approach)
            scalar_img = normalized.T  # (bins, channels)

            img_item = self.images[label]
            img_item.setImage(scalar_img)

            # Position image
            rect = QtCore.QRectF(x_min, 0.0, x_max - x_min, 16.0)
            img_item.setRect(rect)

            plot = self.plots[label]
            plot.setLimits(xMin=x_min, xMax=x_max, yMin=None, yMax=None)
            plot.setXRange(x_min, x_max)
            plot.setYRange(0, 16)

            # Update colorbar
            self.cbars[label].setLevels((0.0, 1.0))
            #self.cbars[label].setColorMap(self.cmap)

    # ------------------------------------------------------------------
    # Controls
    # ------------------------------------------------------------------
    def _on_clear(self):
        parent = self.window()
        buffers = parent.reader_thread.np_buffers

        buffers.clear_histograms()
        buffers.clear_buffers()

        bins_x = self.bin_count.value()
        empty = np.zeros((bins_x, 16), dtype=np.float32)

        for label in self.ADC_LABELS:
            self.images[label].setImage(empty)
            self.cbars[label].setLevels((0.0, 1.0))

    def _on_share_x(self, checked):
        if checked:
            master = self.plots["A"]
            for lbl in self.ADC_LABELS:
                if lbl != "A":
                    self.plots[lbl].setXLink(master)
        else:
            for lbl in self.ADC_LABELS:
                self.plots[lbl].setXLink(None)

    def _on_log_toggled(self, _checked):
        self.update_plot(None)
