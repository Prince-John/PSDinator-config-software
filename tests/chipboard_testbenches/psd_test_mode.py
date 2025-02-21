import sys

from src.chipboard_configuration_software.command_generator.board_components import psd
from src.chipboard_configuration_software.command_generator.commands.global_commands import generate_single_dac_command
from src.chipboard_configuration_software.gui.configuration_helper import read_config, write_config
from src.chipboard_configuration_software.uart_link.middleware import UartMiddleware


def generate_psd_test_mode_command(channel: int, subchannel: tuple("a", "b", "c"), enable: bool) -> str:

    test_mode_command_prefix = f"TS0:" if int(channel) < 8 else f"TS1:"

    address = psd.generate_psd_test_mode_word(enable, int(channel) % 8, subchannel)

    command_string = f"PSD:{test_mode_command_prefix}{address:02X}{int(enable):02X}\0"

    return command_string

if __name__ == '__main__':

    uart_link = UartMiddleware()

    print_with_bars("PSD Test Mode utility")

    connect_to_chipboard_prompt(uart_link)
    config = read_config(r'../configurations/single_board_config_backup_2.json')

    config_mode_status = uart_link.send_stx()
    if config_mode_status is False:
        print("Unable to get into chipboard configuration mode! Exiting..")
        exit(1)

    while True:
        try:

            channel = int(input("Enter channel number: \t"))
            subchannel = input("Enter subchannel: \t")
            enable = input("Enable Y/n? \t")


            command = generate_single_dac_command(dac, value)

            uart_link.send_CMD(message=f"DAC {dac} set to {value}, command = {command}",
                               command_string=f"{command}")

            update_single_dac_setting(config, channel=dac, value=value)

            write_config(r'../configurations/single_board_config_backup_2.json', config=config)
        except ValueError:
            print("Invalid input. Please enter a valid DAC channel.")

        except KeyboardInterrupt:
            print("Exiting...")
            break

    uart_link.send_etx()
    uart_link.cleanup()
    sys.exit(0)
