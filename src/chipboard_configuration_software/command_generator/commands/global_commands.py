from typing import List

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict
from chipboard_configuration_software.command_generator.board_components.dac import generate_dac_word


def generate_global_chipboard_commands(config_dict: ChipboardConfigurationDict) -> List[str]:
    """
    Generates misc global chipboard commands. Currently just a wrapper for the acq mode command.

    :param config_dict: Top Level Config Dict
    :return: List[str] of commands
    """

    commands = [generate_chipboard_mode_command(config_dict)]

    return commands


def generate_chipboard_mode_command(config_dict: ChipboardConfigurationDict) -> str:
    """
    Generates the command to set the chipboard into configuration only or acquisition mode.

    Command Format: ACQ:01 - Set to acquisition mode (acquisition enabled), ACQ:00 - configuration only mode (
    acquisition disabled).

    :param config_dict: Top Level Config Dict
    :return: str - ascii configuration command
    """
    mode_map = {"disabled": 0, "enabled": 1}

    chipboard_mode_command_prefix = "ACQ:"
    mode = config_dict["chipboard_acquisition_state"].lower()

    command = f"{chipboard_mode_command_prefix}{mode_map[mode]:02X}\0"

    return command


def generate_single_dac_command(channel: int, value: float) -> str:
    """
    Generates a single DAC command string for a given channel and value.

    :param channel: The DAC channel number to set, 1 indexed.
    :param value: The desired DAC output value in volts.
    :return: A formatted DAC command string in the form 'DAC:XXXX\\0',
             where XXXX is the 4-digit hexadecimal representation of the
             DAC word.
    :raises ValueError
    """
    octal_dac_prefix = 'DAC:'
    dac_word = generate_dac_word(channel, value)

    command = f'{octal_dac_prefix}{dac_word:04X}\0'

    return command
