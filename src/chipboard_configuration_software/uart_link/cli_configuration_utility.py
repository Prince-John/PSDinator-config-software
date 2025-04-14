import json

from chipboard_configuration_software.command_generator import generate_command_string
from chipboard_configuration_software.gui.configuration_helper import read_config, write_config, ConfigurationDiffer
from chipboard_configuration_software.uart_link.middleware import UartMiddleware
from chipboard_configuration_software.uart_link.utils import print_with_bars


if __name__ == '__main__':
    uart_link = UartMiddleware()
    print("Uart Link is up, no device connected!")

    chipboard_config = ConfigurationDiffer(old_config_path=r'../configurations/single_board_config.json',
                                           temp_path=r'../configurations/single_board_config_temp.json')

    original_config = read_config(r'../configurations/single_board_config.json')
    write_config(r'../configurations/single_board_config_temp.json', original_config)
    config = original_config

    try:
        while input("Read config changes (Y)?") == "Y":
            config = read_config(r'../configurations/single_board_config_temp.json')
            input("Read Changes? Enter to continue")
            changed_config = chipboard_config.get_changes()
            print_with_bars(f"Command changes: {json.dumps(changed_config, indent=4)}")

    except KeyboardInterrupt:
        print("Interrupted by user, exiting config edit loops")

    commands = generate_command_string.generate_commands(config)

    print_with_bars("Generated Commands Listed below")
    for command in commands:
        print(command)

    devices = uart_link.get_available_devices()

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

    config_mode_status = uart_link.send_stx()
    if config_mode_status is False:
        print("Unable to get into chipboard configuration mode! Exiting..")
        exit(1)

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

    for command in commands:
        # input(f"Send next command:  {command}? ")
        uart_link.send_CMD(command_string=command, message=f"Sending:- {command}")

    uart_link.send_etx()
    uart_link.cleanup()
