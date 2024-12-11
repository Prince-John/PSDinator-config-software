import sys
import time

import serial
from serial.tools.list_ports import comports

from src.command_generator import generate_command_string
from src.gui.configuration_helper import read_config
from src.uart_link.utils import *
from src.uart_link.ascii_constants import *


# from ..gui.configuration_helper import read_config
# from ..command_generator import generate_command_string


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

        if device in self.get_available_devices(print_output=False):
            self.serial_handler.port = device
            self.serial_handler.open()
            print(f"Connected to {device} at {self.serial_handler.baudrate} baud!")
        else:
            raise IOError("Device is not available")

    def send_stx(self):
        print("")
        print("Sending STX to enter configuration mode.", flush=True)
        buff = [STX, NUL]
        byte_array = bytearray(buff)
        self.serial_handler.write(byte_array)
        self.wait_ack()

    def wait_ack(self, timeout=5):
        print("Waiting for an ACK or NAK...", flush=True)
        start_time = time.time()

        while True:
            # Check for timeout
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                print("Timeout: No response received.")
                return False

            # Check if there's data in the buffer
            if self.serial_handler.in_waiting:
                byte = self.serial_handler.read(1)
                if byte == ACK:
                    print("Received ACK ...")
                    return True
                if byte == NAK:
                    print("Received NAK ...")
                    return False

    def send_etx(self):
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
        return self.wait_ack()

    def cleanup(self) -> None:
        """
        Closes up any open device connections + #TODO other closeout housekeeping

        :return: None
        """
        self.serial_handler.close()


if __name__ == '__main__':
    uart_link = UartMiddleware()
    print("Uart Link is up, no device connected!")
    devices = uart_link.get_available_devices()

    config = read_config(r'../configurations/single_board_config.json')

    commands = generate_command_string.generate_commands(config)

    print_with_bars("Generated Commands Listed below")
    for command in commands:
        print(command)

    try:
        device_index = int(input("Enter the index of the device to connect to: "))
        if 0 <= device_index < len(devices):
            uart_link.connect_to_device(devices[device_index])
        else:
            print("Invalid device index selected.")
            exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)

    uart_link.send_stx()
    try:
        while input("Enter debug commands (Y)?") == "Y":

            command_string = [input("Enter command string\n")]

            for command in command_string:
                uart_link.send_CMD(f"Sending:- {command}", f"{command}\0")
    except KeyboardInterrupt:
        print("Interrupted by user, exiting...")
        uart_link.send_etx()
        uart_link.cleanup()
        sys.exit(0)

        print(commands)
    for command in commands:
        # input(f"Send next command:  {command}? ")
        uart_link.send_CMD(command_string=command, message=f"Sending:- {command}")

    uart_link.send_etx()
    uart_link.cleanup()
