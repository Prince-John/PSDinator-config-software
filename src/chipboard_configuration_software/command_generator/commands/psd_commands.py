from itertools import chain
from typing import List
from ..board_components import psd, dac


def generate_psd_commands(psd_config: dict) -> List[str]:
    psd_command_prefix = f'PSD:'
    serial_command_string = [generate_psd_serial_subcommands(psd_config)]
    dac_command_strings = generate_psd_dac_subcommands(psd_config)
    trigger_command_string = [generate_psd_trigger_subcommands(psd_config)]
    octal_dac_strings = generate_octal_dac_psd_subcommands(psd_config)

    psd_commands = [f'{psd_command_prefix}{psd_command}' for psd_command in
                    chain(serial_command_string, dac_command_strings, trigger_command_string)]

    psd_commands.extend(octal_dac_strings)

    return psd_commands


def generate_octal_dac_psd_subcommands(psd_config: dict) -> List[str]:
    dac_delay_map = {"a": 3, "b": 5, "c": 7}
    dac_width_map = {"a": 4, "b": 6, "c": 8}
    octal_dac_prefix = 'DAC:'
    dac_subcommands = []

    auto_veto_reset = dac.generate_dac_word(2, float(psd_config["auto_veto_time"]))
    dac_subcommands.append(f'{octal_dac_prefix}{auto_veto_reset:04X}\0')
    subchannel_dict: dict
    for subchannel, subchannel_dict in psd_config["delay"].items():
        dac_word = dac.generate_dac_word(dac_delay_map[subchannel], float(subchannel_dict["dac_value"]))

        dac_subcommands.append(f'{octal_dac_prefix}{dac_word:04X}\0')

    for subchannel, subchannel_dict in psd_config["width"].items():
        dac_word = dac.generate_dac_word(dac_width_map[subchannel], float(subchannel_dict["dac_value"]))

        dac_subcommands.append(f'{octal_dac_prefix}{dac_word:04X}\0')

    return dac_subcommands


def generate_psd_trigger_subcommands(psd_config: dict) -> str:
    trigger_word = psd.generate_psd_trigger_word(psd_config["trigger_mode"])
    trig_string = f'TRG:{trigger_word:02X}\0'

    return trig_string


def generate_psd_dac_subcommands(psd_config: dict) -> List[str]:
    """
Example: DAC0:000a => 00 - DAC value, 0a- DAC address channel 2 - subchannel c

    :param psd_config:
    :return: Returns the command string followed by 1 byte dac value (5 valid bits) and 1 byte address ( 7 bits valid)
            [channel(5 MSB) + subchannel(2 LSB)] in ascii hex.


    """
    dac_command_strings = []

    for channel, channel_value in psd_config["channels"].items():
        dac_command_prefix = f"OD0:" if int(channel) < 8 else f"OD1:"

        for subchannel, dac_value in channel_value["offset_dac"].items():
            dac_value, address = psd.generate_psd_dac_words(int(dac_value), int(channel) % 8, subchannel)
            dac_command_strings.append(f"{dac_command_prefix}{dac_value:02X}{address:02X}\0")

    return dac_command_strings


def generate_psd_serial_subcommands(psd_config: dict) -> str:
    """


    :param psd_config:
    :return: Returns the command string with 96bit serial word in ascii hex
    """
    bitmask_lower, bitmask_upper = get_chanel_enable(psd_config["channels"])
    gains = tuple(psd_config["gain"].values())
    delay_ranges = tuple(range_dict["range"] for range_dict in psd_config["delay"].values())
    width_ranges = tuple(range_dict["range"] for range_dict in psd_config["width"].values())
    psd_0_serial_word = psd.generate_psd_serial_word(bitmask_lower, gains, delay_ranges, width_ranges,
                                                     psd_config["vtc_range"],
                                                     psd_config["bias"],
                                                     psd_config["test_mode"],
                                                     0x0)
    psd_1_serial_word = psd.generate_psd_serial_word(bitmask_upper, gains, delay_ranges, width_ranges,
                                                     psd_config["vtc_range"],
                                                     psd_config["bias"],
                                                     psd_config["test_mode"],
                                                     0x0)

    serial_command_string = f'SER:{psd_0_serial_word:012X}{psd_0_serial_word:012X}\0'
    return serial_command_string


def get_chanel_enable(channels: dict) -> (int, int):
    bitmask = 0x0
    for channel, channel_value in channels.items():
        if channel_value["enable"] == 'True':
            bitmask |= (1 << (15 - int(channel)))

    bitmask = 0xFFFF & ~bitmask
    bitmask_lower = (bitmask >> 8) & 0xFF
    bitmask_upper = bitmask & 0xFF

    return bitmask_lower, bitmask_upper
