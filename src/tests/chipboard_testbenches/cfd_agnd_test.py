from tm_devices import DeviceManager
from tm_devices.drivers import MDO3K
from tm_devices.drivers.pi.scopes.tekscope_3k_4k import tekscope_3k_4k
import time

from src.uart_link import middleware

agnd_trim_options = {"1.36 V": {"command": "CFD:WRT:0100",
                                "measured_value": 0},
                     "1.43 V": {"command": "CFD:WRT:0104",
                                "measured_value": 0},
                     "1.49 V": {"command": "CFD:WRT:0108",
                                "measured_value": 0},
                     "1.56 V": {"command": "CFD:WRT:010C",
                                "measured_value": 0},
                     "1.63 V": {"command": "CFD:WRT:0110",
                                "measured_value": 0},
                     "1.69 V": {"command": "CFD:WRT:0114",
                                "measured_value": 0},
                     "1.77 V": {"command": "CFD:WRT:0118",
                                "measured_value": 0},
                     "1.84 V": {"command": "CFD:WRT:011C",
                                "measured_value": 0}}

data_dir = r'./data/agnd_tests'
print(f'**********************************************\n'
      f'     Automated AGND TEST script               \n'
      f'**********************************************\n'
      f'Set up the following before continuing:  \n'
      f'1. Chipboard is powered on and programmed     \n'
      f'2. Scope channel 1 probe is connected to AGND net on chipboard and grounded\n'
      f'\n'
      f'\n'
      f'The data will be saved to {data_dir}. \n'
      f'Type enter to continue, exit to exit: ')

if input() == "exit":
    print("Exiting!")
    exit(1)

uart_link = middleware.UartMiddleware()
uart_link.connect_to_device('/dev/ttyUSB0')
uart_link.send_stx()

# Connect to the oscilloscope
with DeviceManager(verbose=True) as dm:
    scope: MDO3K = dm.add_scope("10.229.115.178")

    # Define the channel to configure (e.g., CH1)
    channel = 1  # Channel number, e.g., CH1 for channel 1

    # Turn on the specified channel
    scope.write(f"SELECT:CH{channel} ON")

    # Set the vertical scale for the channel
    vertical_scale = 2  # in volts/div
    scope.write(f"CH{channel}:SCALE {vertical_scale}")

    # Set the vertical offset for the channel
    vertical_offset = 0  # in volts
    scope.write(f"CH{channel}:OFFSET {vertical_offset}")

    # Configure the horizontal time base
    time_base = 0.01  # in seconds/div
    scope.write(f"HOR:MAIN:SCALE {time_base}")

    # Set up the cycle mean measurement for the channel
    scope.write(f"MEASUREMENT:MEAS{channel}:SOURCE CH{channel}")
    scope.write(f"MEASUREMENT:MEAS{channel}:TYPE MEAN")
    scope.write(f"MEASUREMENT:MEAS{channel}:STATE ON")
    print("Oscilloscope configured for AGND cycle mean measurement.")

    time.sleep(0.5)
    input("continue? press enter...")
    uart_link.send_CMD(message="RESET CFD", command_string="CFD:RST:\0")

    for agnd_value, config in agnd_trim_options.items():
        ack = uart_link.send_CMD(message=f"AGND setting {agnd_value}, command = {config['command']}",
                                 command_string=f"{config['command']}\0")

        time.sleep(1)
        # Fetch the cycle mean measurement result
        if ack:
            voltage = scope.query(f"MEASUREMENT:MEAS{channel}:VALUE?")
            config["measured_value"] = voltage
            print(f"Measured: {voltage}")
        else:
            config["measured_value"] = -1

uart_link.send_etx()
uart_link.cleanup()
