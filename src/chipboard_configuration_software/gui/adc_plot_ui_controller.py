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

        logger.info("ADC Plots GUI initialized and ready.")

    def _setup_fifo_and_thread(self):
        create_fifo("/tmp/daq_pipe")
        max_counts = int(self.ui.comboBox_event_count.currentText())
        self.decoded_reader_thread = DecodePipeReaderThread("/tmp/daq_pipe", max_points=max_counts)
        self.decoded_reader_thread.start()

    def _get_or_create_bar(self, adc_type: str, ch: int) -> pg.BarGraphItem:
        if ch in self.bar_items[adc_type]:
            return self.bar_items[adc_type][ch]

        color = CHANNEL_COLORS[ch]
        bar = pg.BarGraphItem(x=[], height=[], width=1, brush=color)
        self.bar_items[adc_type][ch] = bar
        self.plots[adc_type].addItem(bar)
        self.legends[adc_type].addItem(bar, f"CH {ch}")
        return bar

    def _setup_plot_area(self):
        layout_widget: pg.GraphicsLayoutWidget = self.ui.adc_plot_layout_widget

        font = QFont()
        font.setPointSize(14)

        self.plots = {}
        self.bar_items = {'a': {}, 'b': {}, 'c': {}, 't': {}}  # per-channel bar graphs
        self.text_items = {}
        self.legends = {}

        for row, adc_type in enumerate(("a", "b", "c", "t")):
            plot = layout_widget.addPlot(row=row, col=0)
            plot.setTitle(f"ADC {adc_type.upper()}")
            plot.setLabel("left", "Count")
            plot.setLabel("bottom", "ADC Value")
            plot.setXRange(-32768, 32767)
            plot.enableAutoRange("y", True)
            plot.setDownsampling(mode='peak')
            plot.setMouseEnabled(x=True, y=False)

            # Create persistent text label (for peak/FWHM stats)
            text_item = TextItem("", anchor=(1, 1), color='w')
            text_item.setFont(font)
            plot.addItem(text_item)

            # Setup legend per ADC type
            legend = pg.LegendItem((80, 60), offset=(60, 20))
            legend.setParentItem(plot.graphicsItem())

            # Save references
            self.plots[adc_type] = plot
            self.text_items[adc_type] = text_item
            self.legends[adc_type] = legend

    def _connect_signals(self):

        for i in range(16):
            self.ui.comboBox_channel_selection.addItem(f"{i}")

        options = np.logspace(2, 5, num=10, base=10)

        for i in options:
            self.ui.comboBox_event_count.addItem(f"{int(i)}")

        self.decoded_reader_thread.histogram_ready.connect(self._on_histogram_ready)
        self.ui.button_clear_all.clicked.connect(self._on_clear_plots_clicked)
        self.ui.comboBox_event_count.currentTextChanged.connect(self._on_max_counts_changed)
        self.ui.comboBox_channel_selection.currentTextChanged.connect(self._on_channel_selection_changed)

    def update_ui(self, config: ChipboardConfigurationDict = None):
        if config is None:
            config = self.chipboard_config
        pass

    def closeEvent(self, event):
        if self.decoded_reader_thread.isRunning():
            self.decoded_reader_thread.stop()
        try:
            os.unlink("/tmp/daq_pipe")
        except FileNotFoundError:
            pass
        event.accept()

    @Slot(int, str, np.ndarray, np.ndarray, float, float)
    def _on_histogram_ready(self, channel, adc_type, bins, counts, peak, fwhm):
        plot = self.plots[adc_type]

        # Compute histogram centers
        x = (bins[:-1] + bins[1:]) / 2
        width = bins[1] - bins[0]

        if self.selected_channel is None:
            # All channels mode: plot this channel as an overlay
            bar = self._get_or_create_bar(adc_type, channel)#TODO - make this return all 3 bar items in a channel
            bar.setOpts(x=x, height=counts, width=width)
        elif self.selected_channel == channel:
            # Single-channel mode
            # Clear other channels’ bars for this adc_type
            for ch, bar in self.bar_items[adc_type].items():
                bar.setOpts(x=[], height=[], width=1)

            bar = self._get_or_create_bar(adc_type, channel)
            bar.setOpts(x=x, height=counts, width=width)

            label = self.text_items[adc_type]
            label.setText(f"FWHM: {fwhm:.2f}\nPeak: {peak:.0f}")
            label.setPos(peak + 10, max(counts) * 0.75)

        self.ui.label_status_adc.setText(
            f"CH {channel} : ADC {adc_type.upper()} ({'All' if self.selected_channel is None else f'CH {self.selected_channel}'})")

    @Slot(int, str, np.ndarray, np.ndarray, float, float)
    def __on_histogram_ready(self, channel, adc_type, bins, counts, peak, fwhm):
        if adc_type not in self.bar_items:
            return

        x = (bins[:-1] + bins[1:]) / 2
        width = bins[1] - bins[0]

        bar_item = self.bar_items[adc_type]
        plot = self.plots[adc_type]
        label = self.text_items[adc_type]

        bar_item.setOpts(x=x, height=counts, width=width)

        label.setText(f"FWHM: {fwhm:.2f}\nPeak: {peak:.0f}")
        label.setPos(peak + 10, max(counts) * 0.75)

        # plot.enableAutoRange("y")

    @Slot()
    def _on_clear_plots_clicked(self):
        """Slot for clear plots """
        logger.debug(f"clear plots clicked.")
        self.clear_plots()

    def clear_plots(self):
        self.histogram_data = defaultdict(lambda: {'a': [], 'b': [], 'c': []})
        self.decoded_reader_thread.clear_histogram_data()
        for adc_type in ('a', 'b', 'c'):
            for bar in self.bar_items[adc_type].values():
                bar.setOpts(x=[], height=[], width=1)
            self.text_items[adc_type].setText("")

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
