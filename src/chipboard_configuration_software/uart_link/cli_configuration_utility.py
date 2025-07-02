import json
import sys

from chipboard_configuration_software.command_generator import generate_command_string
from chipboard_configuration_software.uart_link.middleware import UartMiddleware
from chipboard_configuration_software.uart_link.utils import print_with_bars

if __name__ == '__main__':
    uart_link = UartMiddleware()
    print("Uart Link is up, no device connected!")


    # configuration_manager = ConfigurationManager()
    #
    # chipboard_config = ConfigurationDiffer(old_config_path=r'../configurations/single_board_config.json',
    #                                        temp_path=r'../configurations/single_board_config_temp.json')
    #
    # config = configuration_manager.current_chipboard_config
    #
    # try:
    #     while input("Modify configuration (Y/n)?") == "Y":
    #         input("Read Changes? Enter to continue ...")
    #         changed_config = configuration_manager.get_changes()
    #         print_with_bars(f"Command changes: {json.dumps(changed_config, indent=4)}")
    #         config = changed_config
    # except KeyboardInterrupt:
    #     print("Interrupted by user, exiting config edit loops")
    #
    # commands = generate_command_string.generate_commands(config)
    #
    # print_with_bars("Generated Commands Listed below")
    # for command in commands:
    #     print(command)

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

    """for command in commands:
        # input(f"Send next command:  {command}? ")
        uart_link.send_CMD(command_string=command, message=f"Sending:- {command}")
"""
    uart_link.send_etx()
    uart_link.cleanup()
