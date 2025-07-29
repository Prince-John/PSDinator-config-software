import threading

import serial
import sys
import subprocess
from chipboard_configuration_software.uart_link.middleware import UartMiddleware


class DataAcquisitionThread(threading.Thread):
    def __init__(self,
                 serial_link: UartMiddleware,
                 binary_file_name: str,
                 stop_event: threading.Event):
        super().__init__(daemon=True)
        self.serial_link = serial_link
        self.binary_file_name = binary_file_name
        self.stop_event = stop_event
        self.event_count = 0
        # Save the original timeout so we can restore it later
        self._original_timeout = self.serial_link.serial_handler.timeout

        # Set temporary timeout for acquisition polling
        self.serial_link.serial_handler.timeout = 0.5  # seconds

    def run(self):
        self.serial_link.serial_handler.flushInput()
        self.serial_link.serial_handler.flushOutput()

        print(f"Starting data acquisition → {self.binary_file_name}")
        try:
            with open(self.binary_file_name, "wb") as fid_bin:

                while not self.stop_event.is_set():
                    try:
                        self._get_cobs_packet(fid_bin)
                    except serial.SerialTimeoutException:
                        continue
                    except Exception as e:
                        print(f"Error during packet read: {e}", flush=True)
                        break
        finally:
            print(f"{self.event_count} packets received and written to disk.", flush=True)
            print("Data acquisition thread exiting; file closed.")

    def _get_cobs_packet(self, fid_bin):
        """
        Read one COBS-encoded packet (terminated by b'\x00') from the serial link,
        write it to the binary file, and print the event count.

        :raises: serial.SerialTimeoutException
        """

        cobs_packet = self.serial_link.serial_handler.read_until(expected=b'\x00')

        if not cobs_packet:
            raise serial.SerialTimeoutException

        fid_bin.write(cobs_packet)
        self.event_count += 1
