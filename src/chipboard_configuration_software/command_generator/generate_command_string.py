from itertools import chain
from typing import List, Any

from .commands.cfd_commands import generate_cfd_commands
from .commands.delay_commands import generate_delay_commands
from .commands.mux_commands import generate_mux_commands
from .commands.psd_commands import generate_psd_commands


def generate_commands(config) -> List[str]:
    """
    Top level entry point for this module. Takes in a configuration and generates commands if possible for all the
    individually present sections.


    :param config: complete configuration dictionary for one chipboard.
    :return: list of all commands
    """

    commands = []

    if config is None:
        return []

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
