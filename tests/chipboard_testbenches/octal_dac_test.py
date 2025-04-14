from typing import List

from tm_devices import DeviceManager
from tm_devices.drivers import MDO3K
import time
import numpy as np

from chipboard_configuration_software.command_generator.board_components import dac
from chipboard_configuration_software.uart_link import middleware
from chipboard_configuration_software.uart_link.utils import print_with_bars

data_dir = r'./data/octal_dac_tests'

net_names = ["MULT_OFFSET", "RESET_CV", "DELA", "WIDTHA", "DELB", "WIDTHB", "DELC", "WIDTHC"]

octal_dac_mapping = {net_name: {"pin_number": 1,
                                "dac_channel": index+1,
                                "recommended_via": "",
                                "measured_voltages": []}
                     for index, net_name in enumerate(net_names)}

voltage_settings = list(np.arange(0, 5.1, 0.5))


def measure_dac_channel(net_name, dac_channel_number, pin_number, recommended_via) -> List[float]:
    print_with_bars(
        f"Place channel {channel} scope probe on a via connected to DAC channel net {net_name} (U1 pin{pin_number})",
        symbol='#',
        border_length=88)
    scope.write(f'CH{channel}:LABel "{net_name}"')
    input("continue? press enter...")

    data = []

    for target_voltage in voltage_settings:
        dac_word = dac.generate_dac_word(channel=dac_channel_number, value=target_voltage)

        command = f"DAC:{dac_word:04X}\0"
        uart_link.send_CMD(message=f"DAC setting {target_voltage}, command = {command}",
                           command_string=f"{command}\0")
        time.sleep(2)
        measured_voltage = float(scope.query(f"MEASUREMENT:MEAS{channel}:VALUE?"))

        data.append(measured_voltage)

    return data


print(f'**********************************************\n'
      f'     Automated Octal DAC TEST script               \n'
      f'**********************************************\n'
      f'Set up the following before continuing:  \n'
      f'1. Chipboard is powered on and programmed     \n'
      f'2. Scope is connected to the same subnet as the chipboard computer\n'
      f'\n'
      f'\n'
      f'The data will be saved to {data_dir}. \n'
      f'Press enter to continue, type exit to exit: ')

if input() == "exit":
    print("Exiting!")
    exit(1)

uart_link = middleware.UartMiddleware()
devices = uart_link.get_available_devices()

try:
    device_index = int(input("\nEnter the index of the device to connect to: "))
    if 0 <= device_index < len(devices):
        uart_link.connect_to_device(devices[device_index])
    else:
        print("Invalid device index selected.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit(1)

config_mode_status = uart_link.send_stx()
if config_mode_status is False:
    print("Unable to get into chipboard configuration mode! Exiting..")
    exit(1)

# Connect to the oscilloscope
with DeviceManager(verbose=True) as dm:
    scope: MDO3K = dm.add_scope("10.229.115.178")

    # Define the channel to configure (e.g., CH1)
    channel = 1
    vertical_scale = 2  # in volts/div
    vertical_offset = 0
    time_base = 0.001  # in seconds/div

    scope.write(f"SELECT:CH{channel} ON")
    scope.write(f"CH{channel}:SCALE {vertical_scale}")
    scope.write(f"HOR:MAIN:SCALE {time_base}")

    # Set up the cycle mean measurement for the channel
    scope.write(f"MEASUREMENT:MEAS{channel}:SOURCE CH{channel}")
    scope.write(f"MEASUREMENT:MEAS{channel}:TYPE MEAN")
    scope.write(f"MEASUREMENT:MEAS{channel}:STATE ON")
    print("Oscilloscope configured for Octal DAC cycle mean measurement.")

    time.sleep(0.5)

    for net_name, mapping in octal_dac_mapping.items():
        mapping["measured_voltages"] = measure_dac_channel(net_name, mapping["dac_channel"],
                                                           mapping["pin_number"],
                                                           mapping["recommended_via"])

col_width = 15

# Iterate and print the data
for net_name, details in octal_dac_mapping.items():
    print(f"\nNet Name: {net_name}")
    print(f"{'Target Voltage'.center(col_width)} | {'Measured Voltage'.center(col_width)}")
    print("-" * (col_width * 2))

    # Iterate over target and measured voltages
    for target, measured in zip(voltage_settings, details["measured_voltages"]):
        print(f"{f'{target:.2f}'.center(col_width)} | {f'{measured:.2f}'.center(col_width)}")

uart_link.send_etx()
uart_link.cleanup()
