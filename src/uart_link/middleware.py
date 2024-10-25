from curses.ascii import ACK

import serial
from serial.tools.list_ports import comports
from utils import *
from ascii_constants import *


class UartMiddleware:

    def __init__(self):
        """
        Middle ware object that opens and manages the configuration and data acquisition link between the chipboard
        and this host software.
        """

        self.configuration_change_list = None
        self.configuration = None
        self.usb_location = None
        self.serial_handler = serial.Serial(baudrate=3000000)
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

    def connect_to_device(self, device: str):

        if device in self.get_available_devices():
            self.serial_handler.port = device
            self.serial_handler.open()
            print(f"Connected to {device} at {self.serial_handler.baudrate} baud!")
        else:
            raise IOError("Device is not available")

    def wait_ack(self):
        print("Waiting for a ACK or NAK...", flush=True)
        while True:
            if self.serial_handler.in_waiting:
                byte = self.serial_handler.read(1)
                if byte == ACK:
                    print("Received ACK ...")
                    break
                if byte == NAK:
                    print("Received NAK ...")
                    break

    def send_ETX(self):
        print("")
        print("Sending ETX to exit configuration mode.", flush=True)
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
        self.wait_ack()

    def cleanup(self) -> None:
        """
        Closes up any open device connections + #TODO other closeout housekeeping

        :return: None
        """
        self.serial_handler.close()


if __name__ == '__main__':
    uart_link = UartMiddleware()
    print("Uart Link is up, no device connected!")
    uart_link.get_available_devices()
    uart_link.connect_to_device('/dev/ttyUSB0')
    uart_link.cleanup()
