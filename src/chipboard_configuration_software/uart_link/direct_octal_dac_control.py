import sys

from chipboard_configuration_software.uart_link.utils import connect_to_chipboard_prompt
from chipboard_configuration_software.command_generator.commands.global_commands import generate_single_dac_command
from chipboard_configuration_software.gui.configuration_helper import read_config, write_config
from chipboard_configuration_software.uart_link.middleware import UartMiddleware

# Define the mapping of DAC channels to config keys
channel_map = {
    1: ("multiplicity_offset",),
    2: ("auto_veto_time",),
    3: ("delay", "a", "dac_value"),
    4: ("width", "a", "dac_value"),
    5: ("delay", "b", "dac_value"),
    6: ("width", "b", "dac_value"),
    7: ("delay", "c", "dac_value"),
    8: ("width", "c", "dac_value"),
}


def update_single_dac_setting(config: dict, channel: int, value: int):
    """
    Updates a single DAC setting in O(1) time using direct key lookup.

    :param config: The original configuration dictionary.
    :param channel: The DAC channel number to update.
    :param value: The new value to set.
    """
    if channel in channel_map:
        path = channel_map[channel]
        if len(path) == 1:
            config["psd"][path[0]] = str(value)  # Update "auto_veto_time"
        else:
            config["psd"][path[0]][path[1]][path[2]] = str(value)  # Nested update
        print(f"Updated DAC channel {channel} -> {value}")
    else:
        print(f"Invalid DAC channel: {channel}")


def print_current_settings(dac_settings: dict) -> None:
    """
    Prints the current DAC settings alongside their channel numbers in a formatted CLI table.

    :param dac_settings: The DAC configuration dictionary.
    """

    # Header
    print("+-------------+--------------------------+---------+")
    print("| DAC Channel | Setting Path             | Value(V)|")
    print("+-------------+--------------------------+---------+")

    # Rows
    for channel, path in channel_map.items():
        if len(path) == 1:
            value = dac_settings["psd"][path[0]]
        else:
            value = dac_settings["psd"][path[0]][path[1]][path[2]]

        setting_path = " -> ".join(path)
        print(f"| {channel:^11} | {setting_path:<24} | {value:^6} |")

    # Footer
    print("+-------------+--------------------------+---------+")


if __name__ == '__main__':
    uart_link = UartMiddleware()

    connect_to_chipboard_prompt(uart_link)
    config = read_config(r'../configurations/single_board_config.json')

    config_mode_status = uart_link.send_stx()
    if config_mode_status is False:
        print("Unable to get into chipboard configuration mode! Exiting..")
        exit(1)

    while True:
        try:
            print_current_settings(config)

            dac = int(input("Enter dac number: \t"))
            value = float(input("Enter voltage: \t"))

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
