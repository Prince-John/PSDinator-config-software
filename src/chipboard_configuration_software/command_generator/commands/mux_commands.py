from typing import List

from .configuration_types.chipboard_config_types import MuxConfigurationDict
from ..board_components import mux

mux_command_prefix = "MUX:"


def generate_mux_commands_backup(mux_config: dict) -> str:
    try:
        mux_word = mux.generate_mux_word(int(mux_config["channel"]),
                                         (True if mux_config["enable"] == "True" else False))
    except ValueError as e:
        print(f"ERROR in MUX config, command not generated: {e}")
        return ""

    mux_command_string = f'MUX:{mux_word:02X}\0'

    return [mux_command_string]


def generate_preamp_mux_subcommands(mux_config):
    preamp_mux_prefix = "AMP:"

    try:
        mux_word = mux.generate_mux_word(int(mux_config["preamp_output"]), True)
    except ValueError as e:
        print(f"Could not parse channel, pre amp mux disabled. ")
        mux_word = mux.generate_mux_word(0, False)

    mux_command_string = f'{mux_command_prefix}{preamp_mux_prefix}{mux_word:02X}\0'
    return mux_command_string


def generate_or_mux_subcommands(mux_config):
    or_mux_prefix = "ORO:"
    or_mux_map = {"psd_0": 0,
                  "psd_1": 1,
                  "cfd": 2,
                  "psd_0_or_psd_1": 3}

    mux_command_string = ""

    if mux_config["or_output"] in or_mux_map:
        mux_word = or_mux_map[mux_config["or_output"]]
        mux_command_string = f'{mux_command_prefix}{or_mux_prefix}{mux_word:02X}\0'

    return mux_command_string


def generate_intx_mux_subcommands(mux_config):
    intx_mux_prefix = "INT:"
    intx_mux_map = {"psd_0": 0,
                    "psd_1": 1,
                    }

    mux_command_string = ""

    if mux_config["intx_output"] in intx_mux_map:
        mux_word = intx_mux_map[mux_config["intx_output"]]
        mux_command_string = f'{mux_command_prefix}{intx_mux_prefix}{mux_word:02X}\0'

    return mux_command_string


def generate_psd_cfd_mux_subcommands(mux_config):
    psd_cfd_mux_prefix = "CFD:"
    psd_cfd_mux_map = {"psd_0": 0,
                       "psd_1": 1,
                       }

    mux_command_string = ""

    if mux_config["psd_cfd_output"] in psd_cfd_mux_map:
        mux_word = psd_cfd_mux_map[mux_config["psd_cfd_output"]]
        mux_command_string = f'{mux_command_prefix}{psd_cfd_mux_prefix}{mux_word:02X}\0'

    return mux_command_string


def generate_mux_commands(mux_config: MuxConfigurationDict) -> List[str]:
    mux_commands = []

    for component, component_dict in mux_config.items():

        match component:

            case "preamp_output":
                mux_commands.append(generate_preamp_mux_subcommands(mux_config))

            case "or_output":
                mux_commands.append(generate_or_mux_subcommands(mux_config))

            case "intx_output":
                mux_commands.append(generate_intx_mux_subcommands(mux_config))

            case "psd_cfd_output":
                mux_commands.append(generate_psd_cfd_mux_subcommands(mux_config))

    return mux_commands
