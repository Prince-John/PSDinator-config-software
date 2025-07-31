import logging
import os
import time
from collections import defaultdict

from typing import get_args, cast, List
from ctypes import Structure, Union, c_uint8, c_int16, c_uint32, c_uint64, c_float, c_int, CDLL, POINTER, c_char_p

import pyqtgraph as pg

import numpy as np
from PySide6.QtCore import Slot, Qt, QObject, Signal, QThread, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QCheckBox, QComboBox, QSlider, QLineEdit, QWidget, QFileDialog
from pyqtgraph import TextItem

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict
from chipboard_configuration_software.gui.background_threads.decoded_pipe_reader import DecodePipeReaderThread
from chipboard_configuration_software.gui.configuration_helper import ConfigurationManager
from chipboard_configuration_software.gui.ui_files.adc_plot_ui_widget import Ui_adc_plots
from chipboard_configuration_software.gui.ui_files.qt_ui_modifications import MplCanvas
from chipboard_configuration_software.uart_link.middleware import UartMiddleware
from chipboard_configuration_software.c_decoder import event_decoder_lib

logger = logging.getLogger(__name__)


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

        self.ui.setupUi(self)
        self.chipboard_config: ChipboardConfigurationDict = config_handler.current_chipboard_config
        self.config_handler = config_handler
        self.update_ui()

        self.histogram_data = defaultdict(lambda: {'a': [], 'b': [], 'c': []})

        create_fifo("/tmp/daq_pipe")
        self.decoded_reader_thread = DecodePipeReaderThread("/tmp/daq_pipe")

        self.decoded_reader_thread.histogram_ready.connect(self._on_histogram_ready)

        self.decoded_reader_thread.start()

        self._setup_plot(self.ui.adc_a_widget, "ADC A")
        self._setup_plot(self.ui.adc_b_widget, "ADC B")
        self._setup_plot(self.ui.adc_c_widget, "ADC C")

        # Bar graph items
        self.hist_a = pg.BarGraphItem(x=[], height=[], width=1, brush='b')
        self.hist_b = pg.BarGraphItem(x=[], height=[], width=1, brush='g')
        self.hist_c = pg.BarGraphItem(x=[], height=[], width=1, brush='r')

        self.ui.adc_a_widget.addItem(self.hist_a)
        self.ui.adc_b_widget.addItem(self.hist_b)
        self.ui.adc_c_widget.addItem(self.hist_c)

        # Persistent text labels
        self.text_items = {
            'a': TextItem("", anchor=(1, 1), color='w'),
            'b': TextItem("", anchor=(1, 1), color='w'),
            'c': TextItem("", anchor=(1, 1), color='w'),
        }
        font = QFont()
        font.setPointSize(16)
        for k, item in self.text_items.items():
            item.setFont(font)
            plot_widget = getattr(self.ui, f'adc_{k}_widget')
            plot_widget.addItem(item)

        logger.info("ADC Plots GUI signals connected!")

    def _setup_plot(self, plot_widget: pg.PlotWidget, title: str):
        plot_widget.setTitle(title)
        plot_widget.setLabel("left", "Count")
        plot_widget.setLabel("bottom", "ADC Value")
        plot_widget.enableAutoRange("y", True)
        plot_widget.setXRange(-32768, 32767)
        plot_widget.setDownsampling(mode='peak')

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
        x = (bins[:-1] + bins[1:]) / 2
        width = bins[1] - bins[0]

        # Select plot and bargraph item
        if adc_type == 'a':
            bar = self.hist_a
            plot_widget = self.ui.adc_a_widget
        elif adc_type == 'b':
            bar = self.hist_b
            plot_widget = self.ui.adc_b_widget
        elif adc_type == 'c':
            bar = self.hist_c
            plot_widget = self.ui.adc_c_widget
        else:
            return

        # Update bar graph
        bar.setOpts(x=x, height=counts, width=width)

        # Update text label at peak
        label = self.text_items[adc_type]
        label.setText(f"FWHM: {fwhm:.2f}\nPeak: {peak:.0f}")
        label.setPos(peak + 10, max(counts) * 0.75)

        # Ensure Y autoscale remains enabled, and X interaction only
        plot_widget.setMouseEnabled(x=True, y=False)
        plot_widget.enableAutoRange(axis='y')

    @Slot(int, str, np.ndarray, np.ndarray, float, float)
    def __on_histogram_ready(self, channel, adc_type, bins, counts, peak, fwhm):
        x = (bins[:-1] + bins[1:]) / 2
        width = bins[1] - bins[0]

        # Update histogram
        if adc_type == 'a':
            self.hist_a.setOpts(x=x, height=counts, width=width)
        elif adc_type == 'b':
            self.hist_b.setOpts(x=x, height=counts, width=width)
        elif adc_type == 'c':
            self.hist_c.setOpts(x=x, height=counts, width=width)

        # Update annotation text
        text = f"FWHM: {fwhm:.2f}\nPeak: {peak:.0f}"
        label = self.text_items[adc_type]

        plot_widget = getattr(self.ui, f'adc_{adc_type}_widget')
        x_range, y_range = plot_widget.viewRange()
        label.setText(text)
        label.setPos(x_range[1], y_range[1])  # top-right

    #
    #     logger.info("ADC Plots GUI signals connected!")
    #
    # def _setup_plot(self, plot_widget: pg.PlotWidget, title: str):
    #     plot_widget.setTitle(title)
    #     plot_widget.setLabel("left", "Count")
    #     plot_widget.setLabel("bottom", "ADC Value")
    #     plot_widget.enableAutoRange("y", True)
    #     plot_widget.setXRange(-2048, 32767)
    #     plot_widget.setDownsampling(mode='peak')
    #
    # def closeEvent(self, event):
    #     if self.decoded_reader_thread.isRunning():
    #         self.decoded_reader_thread.stop()
    #     os.unlink("/tmp/daq_pipe")
    #     event.accept()
    #
    # def update_ui(self, config: ChipboardConfigurationDict = None):
    #     if config is None:
    #         config = self.chipboard_config
    #     pass
    #
    # def _add_histogram_text(self, plot_widget, text, font):
    #     # Remove any previous text items
    #     for item in plot_widget.items[:]:
    #         if isinstance(item, TextItem):
    #             plot_widget.removeItem(item)
    #
    #     label = TextItem(text, anchor=(1, 1), color='w')
    #     label.setFont(font)
    #     label.setPos(plot_widget.viewRange()[0][1], plot_widget.viewRange()[1][1])  # top-right corner
    #     plot_widget.addItem(label)
    #
    # # @Slot(int, str, np.ndarray, np.ndarray, float, float)
    # # def _on_histogram_ready(self, channel, adc_type, bins, counts, peak, fwhm):
    # #     x = (bins[:-1] + bins[1:]) / 2
    # #     width = bins[1] - bins[0]
    # #
    # #     if adc_type == 'a':
    # #         self.hist_a.setOpts(x=x, height=counts, width=width)
    # #     elif adc_type == 'b':
    # #         self.hist_b.setOpts(x=x, height=counts, width=width)
    # #     elif adc_type == 'c':
    # #         self.hist_c.setOpts(x=x, height=counts, width=width)
    #
    # from pyqtgraph import TextItem
    # from PySide6.QtGui import QFont
    #
    # @Slot(int, str, np.ndarray, np.ndarray, float, float)
    # def _on_histogram_ready(self, channel, adc_type, bins, counts, peak, fwhm):
    #     x = (bins[:-1] + bins[1:]) / 2
    #     width = bins[1] - bins[0]
    #
    #     # Font for annotations
    #     font = QFont()
    #     font.setPointSize(12)  # Adjust font size as needed
    #
    #     # Format annotation text
    #     text = f"FWHM: {fwhm:.2f}\nPeak: {peak:.0f}"
    #
    #     # Determine which histogram widget and clear previous annotations
    #     if adc_type == 'a':
    #         self.hist_a.setOpts(x=x, height=counts, width=width)
    #         self._add_histogram_text(self.ui.adc_a_widget, text, font)
    #     elif adc_type == 'b':
    #         self.hist_b.setOpts(x=x, height=counts, width=width)
    #         self._add_histogram_text(self.ui.adc_b_widget, text, font)
    #     elif adc_type == 'c':
    #         self.hist_c.setOpts(x=x, height=counts, width=width)
    #         self._add_histogram_text(self.ui.adc_c_widget, text, font)

    #
    # @Slot(int, str, np.ndarray, np.ndarray, float, float)
    # def _on_histogram_ready(self, channel: int, adc_type: str, bins: np.ndarray, counts: np.ndarray, peak, fwhm):
    #     plot_map = {
    #         'a': self.ui.adc_a_widget,
    #         'b': self.ui.adc_b_widget,
    #         'c': self.ui.adc_c_widget
    #     }
    #
    #     canvas = plot_map[adc_type]
    #     ax = canvas.ax
    #     ax.clear()
    #
    #     bin_centers = (bins[:-1] + bins[1:]) / 2
    #     ax.bar(bin_centers, counts, width=(bins[1] - bins[0]), align='center', color='blue')
    #
    #     ax.set_xlim(-2048, 32767)
    #
    #     widths = self.chipboard_config["psd"]["octal_dac_settings"]["width_voltages"]
    #     delays = self.chipboard_config["psd"]["octal_dac_settings"]["delay_voltages"]
    #     width_range = self.chipboard_config["psd"]["serial_register_settings"]["width_ranges"]
    #     delay_range = self.chipboard_config["psd"]["serial_register_settings"]["delay_ranges"]
    #     gain = self.chipboard_config["psd"]["serial_register_settings"]["gain"]
    #
    #     ax.set_title(f"Delay: {float(delays[adc_type]):.2f} V, range: {delay_range[adc_type]},  Width: {float(widths[adc_type]):.2f} V, "
    #                  f"range: {width_range[adc_type]}, Gain: {gain[adc_type]} Ω ")
    #
    #     ax.text(0.02, 0.95, f"Counts: {np.sum(counts)}", transform=ax.transAxes,
    #             fontsize=14, verticalalignment='top')
    #     ax.text(0.02, 0.85, f"Peak: {int(peak)}", transform=ax.transAxes,
    #             fontsize=14, verticalalignment='top')
    #     ax.text(0.02, 0.75, f"FWHM: {int(fwhm)}", transform=ax.transAxes,
    #             fontsize=14, verticalalignment='top')
    #
    #     canvas.draw_idle()
