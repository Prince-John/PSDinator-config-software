from src.chipboard_configuration_software.command_generator.board_components.dac import generate_dac_word


def generate_global_chipboard_commands():
    pass


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
