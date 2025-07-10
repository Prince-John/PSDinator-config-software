import logging
import time

import serial
from serial.tools.list_ports import comports

from chipboard_configuration_software.uart_link.utils import print_with_bars

# from utils import print_with_bars
from .ascii_constants import *

logger = logging.getLogger(__name__)


class CommandRejectedError(Exception):
    def __init__(self, message, command=None):
        """Raised when a command is NAK'd by the device, meaning it was rejected or unrecognized."""

        super().__init__(message)
        self.command = command


class UartMiddleware:

    def __init__(self, baudrate: int = 3000000):
        """
        Middle ware object that opens and manages the configuration and data acquisition link between the chipboard
        and this host software.
        """

        self.configuration_change_list = None
        self.configuration = None
        self.usb_location = None
        self.serial_handler = serial.Serial(baudrate=baudrate)
        self.available_ports = comports()

    def get_available_devices(self, print_output: bool = True) -> list:
        """
        Updates the `available_ports` list and optionally prints out the descriptions and available devices to console.

        :param print_output: Defaults to True, prints formatted descriptions of available serial devices.
        :return: List with just device paths
        """

        self.available_ports = comports()

        if print_output:

            print_with_bars("Available Serial Devices")

            for index, port in enumerate(self.available_ports):
                print(f"Device #{index}: {port.device}\n\tDescription: {port.description}\n\tHWID: {port.hwid}")

        return [port.device for port in self.available_ports]

    def connect_to_device(self, device: str) -> str:

        if device in self.get_available_devices(print_output=False):
            self.serial_handler.port = device
            self.serial_handler.open()
            status = f"Connected to {device} at {self.serial_handler.baudrate} baud!"
            print(status)
            return status
        else:
            raise IOError("Device is not available")

    def send_stx(self):

        logger.info("Sending STX to enter configuration mode.")
        buff = [STX, NUL]
        byte_array = bytearray(buff)
        self.serial_handler.write(byte_array)
        try:
            self.wait_ack()
        except (TimeoutError, CommandRejectedError) as e:
            raise ConnectionRefusedError(e)

    def wait_ack(self, timeout=0.5):
        logger.info("Waiting for an ACK or NAK...")
        start_time = time.time()

        while True:
            # Check for timeout
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                logger.error("Timeout: No response received.")
                raise TimeoutError("Timeout: No response received.")

            # Check if there's data in the buffer
            if self.serial_handler.in_waiting:
                byte = self.serial_handler.read(1)
                if byte == ACK:
                    logger.info("Received ACK ...")
                    return True
                if byte == NAK:
                    logger.info("Received NAK ...")
                    raise CommandRejectedError("Received NAK ...")

    def send_etx(self):
        logger.info("Sending ETX to exit configuration mode.")
        buff = [ETX, NUL]
        byte_array = bytearray(buff)
        self.serial_handler.write(byte_array)

        self.wait_ack()

    def send_CMD(self, message, command_string, dry_run=False):
        print("")
        print(message)

        if dry_run:
            print("dry_run is True, nothing was sent!")
            return

        byte_array = command_string.encode(encoding="ascii")
        self.serial_handler.write(byte_array)

        try:
            self.wait_ack()
        except (CommandRejectedError, TimeoutError) as e:
            logger.warning(f"Error with sending {command_string}: {e}")
            raise CommandRejectedError(f"Error with sending {command_string[:-1]}: {e}")

    def get_data(self, bytes_expected, timeout=5):

        start_time = time.time()
        while True:
            # Check for timeout
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                logger.error("Error getting data: Timeout: No response received.")
                raise TimeoutError("Timeout: No response received.")

            if self.serial_handler.in_waiting:
                return self.serial_handler.read(bytes_expected)

    def cleanup(self) -> None:
        """
        Closes up any open device connections + #TODO other closeout housekeeping

        :return: None
        """
        self.serial_handler.close()
