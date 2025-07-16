import copy
import json
import os
import logging
from datetime import datetime
from typing import List

from chipboard_configuration_software.command_generator.commands.configuration_types.cfd_config_types import \
    CFDConfigurationDict
from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict, MuxConfigurationDict, DelayConfigurationDict
from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import \
    ChipboardConfigurationDictKey
from chipboard_configuration_software.command_generator.commands.configuration_types.psd_config_types import \
    PSDConfigurationDict

logger = logging.getLogger(__name__)

tempfile_path = r"autosave_config.json"


def write_config(path: str, config: dict) -> None:
    """Accepts a config dictionary and writes it as a json file in the same folder at the given path.
    This does not validate the dictionary, ensure that the dictionary is validated as a valid chipboard configuration.

    Args:
        path: path of the config file.
        config: dictionary object that has the configuration in the standard format.
    """
    with open(path, 'w') as autosave_file:
        json.dump(config, autosave_file, indent=4)
        print("Configuration written to file.")


def read_config(path: str) -> dict:
    """Accepts a path and reads the json file into memory as the `configuration`
    This does not validate the dictionary, ensure that the dictionary is validated as a valid chipboard configuration.

    Args:
        path: path of the config file.

    """
    with open(path, 'r') as autosave_file:
        config = json.load(autosave_file)
        print("Configuration file {0} loaded.".format(path))
        return config


def read_single_chipboard_config(path: str, chipboard_number: int) -> dict:
    """Accepts a path and reads the json file into memory as the `configuration`
    This does not validate the dictionary, ensure that the dictionary is validated as a valid chipboard configuration.

    Args:
        path: path of the config file.
        chipboard_number: Index of chipboard configuration to load.
    """
    with open(path, 'r') as autosave_file:
        config = json.load(autosave_file)
        chipboard_config = config["configuration"][str(chipboard_number)]
        logger.info(f"Chipboard {chipboard_number} from configuration file {path} loaded.")

        return chipboard_config


def generate_default_configuration() -> dict:
    default_config = {"configuration_name": "default_config.json",
                      "date_modified": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                      "configuration": {
                          "0":
                              dict(chipboard_number=0,
                                   chipboard_acquisition_state="disabled",
                                   cfd=dict(common_settings=
                                            dict(nowlin_mode="short",
                                                 nowlin_delay="1 ns",
                                                 lockout_DAC="3",
                                                 lockout_mode="long",
                                                 cfd_pulse_width="100",
                                                 agnd_trim="1.43 V",
                                                 global_Mode="False",
                                                 le_out_enable="False",
                                                 test_point="AVSS",
                                                 test_point_channel="0",
                                                 negative_polarity="False"
                                                 ),
                                            individual_channel_settings={
                                                str(channel): {"enable": "False",
                                                               "leading_edge_DAC_value": "0"}
                                                for channel in range(0, 16)
                                            },
                                            global_enable="True"
                                            ),

                                   psd=dict(global_enable="False",
                                            test_mode={"status": "off", "channel": "0", "subchannel": "a"},
                                            serial_register_settings={
                                                "polarity": "positive",
                                                "bias": "high",
                                                "gain": {subchannel: "500"
                                                         for subchannel in ['a', 'b', 'c']},
                                                "vtc_range": "2 us",
                                                "delay_ranges": {subchannel: "0"
                                                                 for subchannel in ['a', 'b', 'c']},
                                                "width_ranges": {subchannel: "0"
                                                                 for subchannel in ['a', 'b', 'c']},
                                                "channel_enables": {
                                                    str(channel): "False" for channel in range(0, 16)
                                                }
                                            },
                                            octal_dac_settings={
                                                "delay_voltages": {subchannel: "0"
                                                                   for subchannel in ['a', 'b', 'c']},
                                                "width_voltages": {subchannel: "0"
                                                                   for subchannel in ['a', 'b', 'c']},
                                                "auto_veto_time": "2",
                                                "multiplicity_offset": "0"
                                            },
                                            trigger_mode="3",
                                            channel_offset_dacs={
                                                str(index): {subchannel: "0" for subchannel in ['a', 'b', 'c']}
                                                for index in range(16)}
                                            ),

                                   delay={str(index): {"value": "0"} for index in range(18)},

                                   mux={"preamp_output": "disabled",
                                        "or_output": "cfd",
                                        "intx_output": "psd_0",
                                        "psd_cfd_output": "psd_0"}
                                   )

                      }
                      }
    return default_config


class ConfigurationDiffer:
    def __init__(self, old_config_path, temp_path=""):
        self.old_config = read_config(old_config_path)
        self.temp_path = temp_path
        self.stop_recurse_paths = {
            "psd.serial_register_settings",
            "cfd.individual_channel_settings.0",
            "cfd.individual_channel_settings.1",
            "cfd.individual_channel_settings.2",
            "cfd.individual_channel_settings.3",
            "cfd.individual_channel_settings.4",
            "cfd.individual_channel_settings.5",
            "cfd.individual_channel_settings.6",
            "cfd.individual_channel_settings.7",
            "cfd.individual_channel_settings.8",
            "cfd.individual_channel_settings.9",
            "cfd.individual_channel_settings.10",
            "cfd.individual_channel_settings.11",
            "cfd.individual_channel_settings.12",
            "cfd.individual_channel_settings.13",
            "cfd.individual_channel_settings.14",
            "cfd.individual_channel_settings.15",
            "cfd.common_settings",
            "delay",
            "mux.preamp_output",
            "mux.or_output",
            "mux.intx_output",
            "mux.psd_cfd_output"
        }

        write_config(self.temp_path, self.old_config)

    def get_changes(self, stop_recurse_paths: set[str] = None):
        if stop_recurse_paths is None:
            stop_recurse_paths = self.stop_recurse_paths
        new_config = read_config(self.temp_path)
        return self._recursive_diff(self.old_config, new_config, path="", stop_paths=stop_recurse_paths)

    def _recursive_diff(self, old, new, path: str, stop_paths: set[str]):
        # Stop at paths marked to include whole block
        if path in stop_paths or not isinstance(old, dict) or not isinstance(new, dict):
            return new if old != new else None

        diff = {}
        for key in new:
            new_path = f"{path}.{key}" if path else key
            old_val = old.get(key)
            new_val = new[key]

            child_diff = self._recursive_diff(old_val, new_val, new_path, stop_paths)
            if child_diff is not None:
                diff[key] = child_diff

        return diff if diff else None


class ConfigurationManager:
    """
    Auto save file path should be default tempfile until we get a save file path.

    After that the savefile location will be the autosave location.
    """

    def __init__(self, auto_save_file_path=tempfile_path):
        self.current_chipboard_config: ChipboardConfigurationDict = {}
        self.currently_loaded_chipboard_config: ChipboardConfigurationDict | None = None

        self.configuration_file_path = None
        self.__stop_recurse_paths = {
            "psd.serial_register_settings",
            "psd.test_mode",
            "cfd.individual_channel_settings.0",
            "cfd.individual_channel_settings.1",
            "cfd.individual_channel_settings.2",
            "cfd.individual_channel_settings.3",
            "cfd.individual_channel_settings.4",
            "cfd.individual_channel_settings.5",
            "cfd.individual_channel_settings.6",
            "cfd.individual_channel_settings.7",
            "cfd.individual_channel_settings.8",
            "cfd.individual_channel_settings.9",
            "cfd.individual_channel_settings.10",
            "cfd.individual_channel_settings.11",
            "cfd.individual_channel_settings.12",
            "cfd.individual_channel_settings.13",
            "cfd.individual_channel_settings.14",
            "cfd.individual_channel_settings.15",
            "cfd.common_settings",
            "delay",
            "mux.preamp_output",
            "mux.or_output",
            "mux.intx_output",
            "mux.psd_cfd_output"

        }
        if os.path.isfile(auto_save_file_path):
            logger.info("Found Autosave file!")
            self.configuration = read_config(auto_save_file_path)

        else:
            self.configuration = generate_default_configuration()
            write_config(auto_save_file_path, self.configuration)
            logger.info("No autosave file found, using default configuration.")

        self.auto_save_file_path = auto_save_file_path

        self.current_chipboard_number = 0
        self._set_current_chipboard(self.current_chipboard_number)
        self.current_device = None

    def _set_current_chipboard(self, chipboard_number: int) -> None:
        """
        Sets the `current_chipboard_config` variable to the one corresponding to the chipboard_number index input.
        This is a utility function that allows for easier reference of the current chipboard configuration.
        """
        logger.debug(f'Updating current single chipboard config')
        self.current_chipboard_config = self.configuration["configuration"][str(chipboard_number)]
        self.current_chipboard_number = chipboard_number

    def __recursive_diff(self, old: dict, new: dict, path: str, stop_paths: set[str]) -> dict | None:
        """
        Internal helper function that recursively traverses through 2 chipboard configs and returns a configuration
        dict with only changes. The recursive traversal stops once it comes across a stop path and returns the entire
        dict below that point.
        """
        if path in stop_paths or not isinstance(old, dict) or not isinstance(new, dict):
            return new if old != new else None

        diff = {}
        for key in new:
            new_path = f"{path}.{key}" if path else key
            old_val = old.get(key)
            new_val = new[key]

            child_diff = self.__recursive_diff(old_val, new_val, new_path, stop_paths)
            if child_diff is not None:
                diff[key] = child_diff

        return diff if diff else None

    def get_changes(self, stop_recurse_paths: set[str] = None) -> ChipboardConfigurationDict:
        """
        Calculates the differences between the currently loaded configuration on the chipboard and current state of the
        configuration on the utility. The last loaded configuration is also the same as the autosave file.
        It returns a dict with all the related information needed to generate a command string.

        :param stop_recurse_paths: Optional, set[str] of '.' seperated paths of keys which should be the last
        traversed configuration subdict. This should almost never be used.
        :return: dict of changed commands.
        """
        if stop_recurse_paths is None:
            stop_recurse_paths = self.__stop_recurse_paths

        new_config = self.current_chipboard_config

        if self.currently_loaded_chipboard_config is None:
            return self.current_chipboard_config
        else:
            old_config = self.currently_loaded_chipboard_config

        return self.__recursive_diff(old_config, new_config, path="", stop_paths=stop_recurse_paths)

    def get_currently_loaded_chipboard_config(self, component: ChipboardConfigurationDictKey = None) -> \
            ChipboardConfigurationDict | PSDConfigurationDict | CFDConfigurationDict | DelayConfigurationDict | MuxConfigurationDict:
        """
        This returns  the last valid loaded configuration onto the current chipboard. If the current chipboard has
        not been loaded with any configuration then this returns the last auto saved configuration from disk.

        If component is present it returns the last valid loaded component configuration subdict. If the component has
        not been loaded yet, it returns the component subdict from last auto saved configuration from disk.

        Always use this method instead of directly accessing the class attribute. Edge cases can exist during
        application start up where the `current_chipboard_config` might contain changes from GUI that have not yet
        been loaded onto the chipboard and `currently_loaded_chipboard_config` is None.

        :return:  currently_loaded_chipboard_config Type[ChipboardConfigurationDict]

        """
        if self.currently_loaded_chipboard_config is None:
            return read_single_chipboard_config(self.auto_save_file_path, self.current_chipboard_number)[component]
        if component is None:
            return self.currently_loaded_chipboard_config

        try:
            return self.currently_loaded_chipboard_config[component]
        except KeyError:
            return read_single_chipboard_config(self.auto_save_file_path, self.current_chipboard_number)[component]

    def update_currently_loaded_chipboard_config(self, component: ChipboardConfigurationDictKey = None) -> None:

        if component is None:
            self.currently_loaded_chipboard_config = copy.deepcopy(self.current_chipboard_config)
        else:
            if self.currently_loaded_chipboard_config is None:
                self.currently_loaded_chipboard_config = {}

            self.currently_loaded_chipboard_config[component] = copy.deepcopy(self.current_chipboard_config[component])

    def reset_currently_loaded_chipboard_config(self) -> None:
        """
        Sets the currently_loaded_config attribute to None.
        :return: None
        """

        self.currently_loaded_chipboard_config = None

    def save_current_configuration(self, configuration_file_path: str = None) -> None:
        """
        Saves the complete current state of the class attribute `configuration` to the current `configuration_file_path`
        location on disk. Updates the last saved date and `configuration_file_path` if provided.


        :param configuration_file_path: Optional Save File Path, assumes input is correct/validated.
        :type configuration_file_path: str
        :return: None
        """
        if configuration_file_path is not None:
            self.configuration_file_path = configuration_file_path

        if self.configuration_file_path is None:
            self.configuration_file_path = self.auto_save_file_path
        self.configuration["date_modified"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        write_config(path=self.configuration_file_path, config=self.configuration)

    def load_saved_configuration(self, configuration_file_path: str) -> None:
        """
        Loads the configuration file present on disk into the class attribute `configuration`.
        Updates the current chipboard dict as well;
        Sets `currently_loaded_chipboard_config` to None
        Updates class attribute `configuration_file_path` to one passed as function argument

        TODO: Validation of loaded configurations.

        :param configuration_file_path: Save File Path, assumes input is correct/validated.
        :return: None
        """

        self.configuration = read_config(configuration_file_path)
        self.configuration_file_path = configuration_file_path
        self._set_current_chipboard(self.current_chipboard_number)
        self.currently_loaded_chipboard_config = None

        # update tempfile TODO: THis is a bad bodge to get psd checkboxes to update correctly. Fix this you lazy bitch.
        self.auto_save_file_path = self.configuration_file_path
