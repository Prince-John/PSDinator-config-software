from itertools import chain
from typing import List, Any

from .board_components import psd, mux, delay, cfd
from .board_components import dac


def generate_psd_commands(psd_config: dict) -> chain[str]:
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
    trig_string = f'TRG:{trigger_word:01X}\0'

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
                                                     0x1)

    serial_command_string = f'SER:{psd_1_serial_word:012X}{psd_0_serial_word:012X}\0'
    return serial_command_string


def get_chanel_enable(channels: dict) -> (int, int):
    bitmask = 0x0
    for channel, channel_value in channels.items():
        if channel_value["enable"]:
            bitmask |= (1 << int(channel))

    bitmask = 0xFFFF & ~bitmask
    bitmask_upper = (bitmask >> 8) & 0xFF
    bitmask_lower = bitmask & 0xFF
    return bitmask_lower, bitmask_upper


def generate_cfd_commands(cfd_config: dict) -> List[str]:
    cfd_command_prefix = "CFD:"

    cfd_write_register_prefix = "WRT:"
    cfd_common_channel_commands = get_cfd_common_channel_commands(cfd_config)
    cfd_individual_commands = get_cfd_individual_channel_commands(cfd_config)

    cfd_commands = [f'{cfd_command_prefix}{cfd_write_register_prefix}{cfd_command}' for cfd_command in
                    chain(cfd_individual_commands, cfd_common_channel_commands)]

    return cfd_commands


def get_cfd_common_channel_commands(cfd_config: dict) -> List[str]:
    cfd_common_channel_words = cfd.generate_common_channel_words(nowlin_mode=cfd_config["nowlin_mode"],
                                                                 test_point_select=cfd_config["test_point"],
                                                                 test_point_channel=int(
                                                                     cfd_config["test_point_channel"]),
                                                                 capacitor_bus=cfd_config["nowlin_delay"],
                                                                 lockout_mode=cfd_config["lockout_mode"],
                                                                 lockout_dac_input=int(cfd_config["lockout_DAC"]),
                                                                 agnd_trim_voltage=cfd_config["agnd_trim"],
                                                                 oneshot_width_select=cfd_config["cfd_pulse_width"])

    return [f"{add_mode:02X}{data:02X}\0" for add_mode, data in cfd_common_channel_words]


def get_cfd_individual_channel_commands(cfd_config: dict) -> List[str]:
    commands = []
    for channel, channel_dict in cfd_config["leading_edge_DACs"].items():
        add_mode, data = cfd.generate_individual_channel_word(channel=int(channel),
                                                              channel_enable=(True if channel_dict["enable"] == "True" else False),
                                                              leading_edge_DAC_input=channel_dict[
                                                                  "leading_edge_DAC_value"],
                                                              leading_edge_DAC_neg_polarity=(True if channel_dict["sign_bit"] == "True" else False))
        print((True if channel_dict["sign_bit"] == "True" else False))
        commands.append(f"{add_mode:02X}{data:02X}\0")

    return commands


def generate_delay_commands(delay_config: dict) -> str:
    """
        This is compliant with build v0.0.4 and sends 18 byte words with only delay values;
    """
    delay_value_word = ""

    for delay_dict in delay_config.values():
        delay_value = delay.generate_delay_word(int(delay_dict["value"]))
        delay_value_word += f'{delay_value:02X}'  # 1 byte per value

    delay_command_string = f'DLY:{delay_value_word}\0'
    return [delay_command_string]


def generate_mux_commands(mux_config: dict) -> str:
    try:
        mux_word = mux.generate_mux_word(int(mux_config["channel"]), (True if mux_config["enable"] == "True" else False))
    except ValueError as e:
        print(f"ERROR in MUX config, command not generated: {e}")
        return ""

    mux_command_string = f'MUX:{mux_word:02X}\0'

    return [mux_command_string]


def generate_tdc_commands():
    pass


def generate_global_chipboard_commands():
    pass


def generate_commands(config) -> List[str]:
    """
    Top level entry point for this module. Takes in a configuration and generates commands if possible for all the
    individually present sections.


    :param config: complete configuration dictionary for one chipboard.
    :return: list of all commands
    """

    commands = []

    for component, component_config in config.items():

        match component:

            case "psd":
                commands.extend(generate_psd_commands(component_config))
            case "cfd":
                commands.extend(generate_cfd_commands(component_config))
            case "delay":
                commands.extend(generate_delay_commands(component_config))
            case "mux":
                commands.extend(generate_mux_commands(component_config))

    return commands
