import logging
import os
import time
from collections import defaultdict

from typing import get_args, cast, List
from ctypes import Structure, Union, c_uint8, c_int16, c_uint32, c_uint64, c_float, c_int, CDLL, POINTER, c_char_p

import pyqtgraph as pg

import numpy as np
from PySide6.QtCore import Slot, Qt, QObject, Signal, QThread, QTimer
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QCheckBox, QComboBox, QSlider, QLineEdit, QWidget, QFileDialog
from pyqtgraph import TextItem, mkColor, hsvColor

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict
from chipboard_configuration_software.gui.background_threads.decoded_pipe_reader import DecodePipeReaderThread
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.adc_plot_ui_widget import Ui_adc_plots

import pyqtgraph as pg
from pyqtgraph.console import ConsoleWidget
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
from pyqtgraph.Qt import QtWidgets

logger = logging.getLogger(__name__)

ch: QColor
CHANNEL_COLORS = {
    ch: mkColor(QColor.fromHsvF((ch / 16.0) % 1.0, 0.6, 1.0))
    for ch in range(16)
}


def create_fifo(fifo_path=None):
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
        logger.info(f"Created new FIFO at {fifo_path}")


class ADCPlotsController(QWidget):
    status_message = Signal(str)

    def __init__(self, parent_ui, ui: Ui_adc_plots, config_handler: ConfigurationManager):
        super().__init__()
        self.parent_ui = parent_ui
        self.ui = ui
        self.config_handler = config_handler
        self.chipboard_config: ChipboardConfigurationDict = config_handler.current_chipboard_config

        self.ui.setupUi(self)
        self.histogram_data = defaultdict(lambda: {'a': [], 'b': [], 'c': [], 't': []})

        self.plots = {}
        self.bar_items = {}
        self.text_items = {}
        self.selected_channel = None

        self._setup_fifo_and_thread()
        self._setup_plot_area()
        self._connect_signals()
        self.hist_timer = QTimer(self)
        self.start_histogram_timer()

        logger.info("ADC Plots GUI initialized and ready.")

    def _setup_fifo_and_thread(self):
        create_fifo("/tmp/daq_pipe")
        max_counts = int(self.ui.comboBox_event_count.currentText())
        self.decoded_reader_thread = DecodePipeReaderThread("/tmp/daq_pipe", max_points=1000)
        self.decoded_reader_thread.start()

    def _setup_plot_area(self):
        area: pg.dockarea.DockArea = self.ui.adc_plot_layout_widget

        dock_A = Dock("Subchannel A", size=(500, 400))
        dock_B = Dock("Subchannel B", size=(500, 400))
        dock_C = Dock("Subchannel C", size=(500, 400))
        dock_T = Dock("TVC ", size=(500, 500))

        docks = [dock_A, dock_B, dock_C, dock_T]

        area.addDock(dock_A, 'top')
        area.addDock(dock_B, 'bottom', dock_A)
        area.addDock(dock_C, 'bottom', dock_B)
        area.addDock(dock_T, 'bottom', dock_C)

        self.plots = {}
        self.curves = {"A": {}, "B": {}, "C": {}, "T": {}}
        self.legends = {}

        labels = ["A", "B", "C", "T"]

        for dock, label in zip(docks, labels):
            plot = pg.PlotWidget()
            plot.setTitle(f"ADC {label}")
            plot.setLabel("left", "Count")
            plot.setLabel("bottom", "ADC Value")
            plot.enableAutoRange("y", True)
            plot.enableAutoRange("x", True)
            plot.setDownsampling(mode='peak')
            plot.setMouseEnabled(x=True, y=False)
            legend = pg.LegendItem((80, 60), offset=(60, 20))
            legend.setParentItem(plot.graphicsItem())
            dock.addWidget(plot)
            self.plots[label] = plot
            self.legends[label] = legend

    def _connect_signals(self):

        for i in range(16):
            self.ui.comboBox_channel_selection.addItem(f"{i}")

        options = [2 ** i for i in range(8, 16)]

        for i in options:
            self.ui.comboBox_event_count.addItem(f"{int(i)}")

        self.ui.button_clear_all.clicked.connect(self._on_clear_plots_clicked)
        self.ui.comboBox_event_count.currentTextChanged.connect(self._on_max_counts_changed)
        self.ui.comboBox_channel_selection.currentTextChanged.connect(self._on_channel_selection_changed)

    def update_ui(self, config: ChipboardConfigurationDict = None):
        if config is None:
            config = self.chipboard_config
        pass

    def start_histogram_timer(self, refresh_time_ms=150):
        self.hist_timer.timeout.connect(self._update_histograms_from_buffer)
        self.hist_timer.start(refresh_time_ms)

    def closeEvent(self, event):
        if self.decoded_reader_thread.isRunning():
            self.decoded_reader_thread.stop()
        try:
            os.unlink("/tmp/daq_pipe")
        except FileNotFoundError:
            pass
        event.accept()

    def update_histograms(self, updates):
        """
        updates: dict[int, dict[str, (counts, bin_edges)]]
            Output from ChannelBuffers.get_hit_histograms()
            Example:
            {
              0: {"A": (counts, bin_edges), "B": (...), ...},
              3: {"A": (counts, bin_edges), ...}
            }
        """
        for ch, adc_dict in updates.items():
            for adc_label, (counts, bin_edges) in adc_dict.items():
                # Compute step histogram points
                x = bin_edges
                y = counts

                if ch not in self.curves[adc_label]:
                    # Assign a distinct color per channel
                    color = pg.intColor(ch, hues=16, values=1, maxValue=255, alpha=200)
                    curve = pg.PlotCurveItem(x, y,
                                             stepMode=True,
                                             fillLevel=0,
                                             brush=color,
                                             pen=color,
                                             )
                    self.plots[adc_label].addItem(curve)
                    self.curves[adc_label][ch] = curve
                    self.legends[adc_label].addItem(curve, f'Ch: {ch}')
                else:
                    curve = self.curves[adc_label][ch]
                    curve.setData(x, y, stepMode=True)

    def _update_histograms_from_buffer(self, lifetime_hits=False):
        updates = self.decoded_reader_thread.np_buffers.get_hit_histograms(only_hits=True, lifetime_hits=lifetime_hits)
        if updates:
            self.update_histograms(updates)
            self.decoded_reader_thread.np_buffers.reset_hits()

    @Slot()
    def _on_clear_plots_clicked(self):
        """Slot for clear plots """
        logger.debug(f"clear plots clicked.")
        self.clear_plots()

    def clear_plots(self):
        self.decoded_reader_thread.np_buffers.clear_histograms()
        self._update_histograms_from_buffer(lifetime_hits=True)
        self.ui.label_status_adc.setText("Plots cleared.")

    @Slot(str)
    def _on_max_counts_changed(self, value):
        """Slot for max counts """
        logger.debug(f"max counts changed with value {value}")
        counts = int(value)
        self.decoded_reader_thread.set_histogram_counts(counts)
        self.clear_plots()
        self.ui.label_status_adc.setText(f"Histogram counts set to {counts}")

    @Slot(str)
    def _on_channel_selection_changed(self, value):
        """Slot for channel selection """
        logger.debug(f"channel selection changed with value {value}")
        if value == "All":
            self.selected_channel = None
        else:
            self.selected_channel = int(value)
