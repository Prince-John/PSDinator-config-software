import json
from itertools import chain
from typing import List
from .configuration_types.psd_config_types import PSDConfigurationDict, OctalDacSettingsDict, SubchannelOffsetDacDict, \
    SerialRegisterSettingsDict, RangeDict, ChannelEnableDict, ChannelOffsetDacDict, SubchannelKey, TestModeDict
from ..board_components import psd, dac

psd_command_prefix = "PSD:"


def generate_psd_commands_backup(psd_config: PSDConfigurationDict) -> List[str]:
    serial_command_string = [generate_psd_serial_subcommands(psd_config)]
    dac_command_strings = generate_psd_dac_subcommands(psd_config)
    trigger_command_string = [generate_psd_trigger_subcommands(psd_config)]
    octal_dac_commands = generate_octal_dac_psd_subcommands(psd_config)
    global_enable_commands = generate_psd_global_enable_subcommands(psd_config)

    psd_commands = [f'{psd_command}' for psd_command in
                    chain(serial_command_string, dac_command_strings, trigger_command_string)]

    psd_commands.extend(octal_dac_commands)
    psd_commands.extend(global_enable_commands)

    return psd_commands


def generate_psd_test_mode_subcommands(component_dict: TestModeDict) -> str:
    """
    Generates the commands required to put the PSD ASIC into its test mode.

    Example: TS0:0a01 => 0a- DAC address channel: 2 - subchannel: c   01- enable

    :param component_dict:
    :return: Returns the command string followed by 1 byte address ( 7 bits valid)
            [channel(5 MSB) + subchannel(2 LSB)] and 1 byte (1 bit valid) enable setting in ascii hex.
    """

    channel = component_dict["channel"]
    subchannel = component_dict["subchannel"]
    status = True if component_dict["status"].lower() == "on" else False

    if int(channel) > 15:
        raise ValueError(f"Channel {channel} exceeds maximum supported channel index (15)")

    test_mode_command_prefix = f"TS0:" if int(channel) < 8 else f"TS1:"

    address = psd.generate_psd_test_mode_word(int(channel) % 8, subchannel.lower())

    command = f"{psd_command_prefix}{test_mode_command_prefix}{address:02X}{int(status):02X}\0"

    return command


def generate_psd_commands(psd_config: PSDConfigurationDict) -> List[str]:
    psd_commands = []

    for component, component_dict in psd_config.items():

        match component:

            case "global_enable":
                psd_commands.append(generate_psd_global_enable_subcommands(psd_config))

            case "trigger_mode":
                psd_commands.append(generate_psd_trigger_subcommands(psd_config))

            case "octal_dac_settings":
                psd_commands.extend(generate_octal_dac_psd_subcommands(component_dict))

            case "channel_offset_dacs":
                psd_commands.extend(generate_psd_dac_subcommands(component_dict))

            case "serial_register_settings":
                psd_commands.append(generate_psd_serial_subcommands(component_dict))

            case "test_mode":
                psd_commands.append(generate_psd_test_mode_subcommands(component_dict))

    return psd_commands


def generate_octal_dac_psd_subcommands(psd_octal_dac_config: OctalDacSettingsDict) -> List[str]:
    dac_delay_map = {"a": 3, "b": 5, "c": 7}
    dac_width_map = {"a": 4, "b": 6, "c": 8}
    octal_dac_prefix = 'DAC:'
    dac_subcommands = []

    def generate_sub_channel_commands(subchannel_dict: dict, dac_map: dict) -> None:

        for subchannel, subchannel_value in subchannel_dict.items():
            dac_word = dac.generate_dac_word(dac_map[subchannel], float(subchannel_value))

            dac_subcommands.append(f'{octal_dac_prefix}{dac_word:04X}\0')

    for component, component_dict in psd_octal_dac_config.items():

        match component:

            case "delay_voltages":
                generate_sub_channel_commands(component_dict, dac_delay_map)

            case "width_voltages":
                generate_sub_channel_commands(component_dict, dac_width_map)

            case "auto_veto_time":
                auto_veto_reset = dac.generate_dac_word(2, float(psd_octal_dac_config["auto_veto_time"]))
                dac_subcommands.append(f'{octal_dac_prefix}{auto_veto_reset:04X}\0')

    return dac_subcommands


def generate_psd_trigger_subcommands(psd_config: dict) -> str:
    trigger_word = psd.generate_psd_trigger_word(psd_config["trigger_mode"])
    trig_string = f'{psd_command_prefix}TRG:{trigger_word:02X}\0'

    return trig_string


def generate_psd_dac_subcommands(psd_offset_dac_config: ChannelOffsetDacDict) -> List[str]:
    """
    Example: OD0:000a => 00 - DAC value, 0a- DAC address channel 2 - subchannel c

    :param psd_offset_dac_config:
    :return: Returns the command string followed by 1 byte dac value (5 valid bits) and 1 byte address ( 7 bits valid)
            [channel(5 MSB) + subchannel(2 LSB)] in ascii hex.

    """

    dac_command_strings = []
    channel_value_dict: SubchannelOffsetDacDict
    for channel, channel_value_dict in psd_offset_dac_config.items():
        if int(channel) > 15:
            raise ValueError(f"Channel {channel} exceeds maximum supported channel index (15)")

        dac_command_prefix = f"OD0:" if int(channel) < 8 else f"OD1:"
        subchannel: SubchannelKey
        for subchannel, dac_value in channel_value_dict.items():
            dac_value, address = psd.generate_psd_dac_words(int(dac_value), int(channel) % 8, subchannel)
            dac_command_strings.append(f"{psd_command_prefix}{dac_command_prefix}{dac_value:02X}{address:02X}\0")

    return dac_command_strings


def generate_psd_serial_subcommands(psd_config: SerialRegisterSettingsDict) -> str:
    """
    Generates the ASCII subcommand required to program the 96 bit serial shift register for the PSD Chips.

    :param psd_config: psd configuration sub dictionary from the top level chipboard config dictionary.
                       Requires following keys:
                           channels
                           gain
                           delay["range"]
                           width["range"]
                           vtc_range
                           bias
                           test_mode

    :return: Returns the command string with 96bit serial word in ascii hex
    """
    bitmask_lower, bitmask_upper = _get_channel_enable(psd_config["channel_enables"])

    gains = _get_ordered_ranges(psd_config["gain"])
    delay_ranges = _get_ordered_ranges(psd_config["delay_ranges"])
    width_ranges = _get_ordered_ranges(psd_config["width_ranges"])

    psd_0_serial_word = psd.generate_psd_serial_word(channel_enable_low_mask=bitmask_lower,
                                                     gain_settings=gains,
                                                     subchannel_delay_ranges=delay_ranges,
                                                     subchannel_width_ranges=width_ranges,
                                                     vtc_range=psd_config["vtc_range"],
                                                     bias_mode=psd_config["bias"],
                                                     polarity_mode=psd_config["polarity"],
                                                     chip_id=0x0)

    psd_1_serial_word = psd.generate_psd_serial_word(channel_enable_low_mask=bitmask_upper,
                                                     gain_settings=gains,
                                                     subchannel_delay_ranges=delay_ranges,
                                                     subchannel_width_ranges=width_ranges,
                                                     vtc_range=psd_config["vtc_range"],
                                                     bias_mode=psd_config["bias"],
                                                     polarity_mode=psd_config["polarity"],
                                                     chip_id=0x0)

    serial_command_string = f'{psd_command_prefix}SER:{psd_1_serial_word:012X}{psd_0_serial_word:012X}\0'
    return serial_command_string


def _get_ordered_ranges(range_dict: RangeDict) -> tuple[int, int, int]:
    """
    Helper function to extract the subchannel values from a range_dict containing unordered "a", "b", "c"
    subchannel values and returns an ordered tuple (range_a, range_b, range_c) typecast as ints.

    :param range_dict: dict containing unordered "a", "b", "c" subchannel values
    :return: ordered tuple of ints in this order (a, b, c)
    """
    if "a" not in range_dict or "b" not in range_dict or "c" not in range_dict:
        raise KeyError("Incomplete configuration for serial register command generation")

    ordered_values = (int(range_dict["a"]), int(range_dict["b"]), int(range_dict["c"]))

    return ordered_values


def _get_channel_enable(channels: ChannelEnableDict) -> (int, int):
    bitmask = 0x0

    for channel, channel_value in channels.items():
        if channel_value == 'True':
            bitmask |= (1 << (15 - int(channel)))

    bitmask = 0xFFFF & ~bitmask
    bitmask_lower = (bitmask >> 8) & 0xFF
    bitmask_upper = bitmask & 0xFF

    return bitmask_lower, bitmask_upper


def generate_psd_global_enable_subcommands(psd_config: PSDConfigurationDict) -> str:
    psd_global_enable_prefix = "GEN:"
    global_enable_value = psd.generate_global_enable_word(True if psd_config["global_enable"] == "True" else False)
    subcommand = f"{psd_command_prefix}{psd_global_enable_prefix}{global_enable_value:02X}\0"

    return subcommand
