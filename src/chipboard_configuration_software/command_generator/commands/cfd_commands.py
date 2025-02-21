from itertools import chain
from typing import List

from ..board_components import cfd


def generate_cfd_commands(cfd_config: dict) -> List[str]:
    cfd_command_prefix = "CFD:"

    cfd_write_register_prefix = "WRT:"

    cfd_common_channel_commands = get_cfd_common_channel_commands(cfd_config)
    cfd_individual_commands = get_cfd_individual_channel_commands(cfd_config)
    cfd_global_enable_commands = generate_cfd_global_enable_subcommands(cfd_config)

    cfd_commands = [f'{cfd_command_prefix}{cfd_write_register_prefix}{cfd_command}' for cfd_command in
                    chain(cfd_individual_commands, cfd_common_channel_commands)]

    cfd_commands.extend(cfd_global_enable_commands)

    return cfd_commands


def generate_cfd_global_enable_subcommands(cfd_config: dict) -> List[str]:
    cfd_command_prefix = "CFD:"
    cfd_global_enable_prefix = "GEN:"

    global_enable_value = cfd.generate_global_enable_word(True if cfd_config["global_enable"] == "True" else False)
    subcommand = f"{cfd_command_prefix}{cfd_global_enable_prefix}{global_enable_value:02X}\0"

    return [subcommand]


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
    for channel, channel_dict in cfd_config["channels"].items():
        add_mode, data = cfd.generate_individual_channel_word(channel=int(channel),
                                                              channel_enable=(
                                                                  True if channel_dict["enable"] == "True" else False),
                                                              leading_edge_DAC_input=channel_dict[
                                                                  "leading_edge_DAC_value"],
                                                              leading_edge_DAC_neg_polarity=(True if channel_dict[
                                                                                                         "sign_bit"] == "True" else False))

        commands.append(f"{add_mode:02X}{data:02X}\0")

    return commands
