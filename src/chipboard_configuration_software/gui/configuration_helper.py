import json
import os

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


class ConfigurationManager:

    def __init__(self):
        self.current_chip_config = None

        if os.path.isfile(tempfile_path):
            print("Found Autosave file.")
            self.configuration = read_config(tempfile_path)

        else:
            self.configuration = {"configuration_name": "default_config.json",
                                  "date_modified": "07-28-23",
                                  "configuration": [
                                      dict(chipboard_number=chipboard_index,
                                           cfd=dict(nowlin_mode="short",
                                                    nowlin_delay="1",
                                                    lockout_DAC="",
                                                    lockout_mode="disabled",
                                                    cfd_pulse_width="50",
                                                    agnd_trim="1.77",
                                                    global_enable="True",
                                                    global_Mode="False",
                                                    le_out_enable="False",
                                                    external_agnd_enable="False",
                                                    test_point="AVSS",
                                                    test_point_channel="0",
                                                    negative_polarity="False",
                                                    leading_edge_DACs=[
                                                        dict(channel=index,
                                                             enable="True",
                                                             leading_edge_DAC_value=None,
                                                             sign_bit="False")
                                                        for index in range(16)]
                                                    ),
                                           psd=dict(polarity="pos",
                                                    bias="low",
                                                    gain={subchannel: "0"
                                                          for subchannel in ['a', 'b', 'c']},
                                                    delay={subchannel: dict(range="0", dac_value="0")
                                                           for subchannel in ['a', 'b', 'c', 't']},
                                                    width={subchannel: dict(range="0", dac_value="0")
                                                           for subchannel in ['a', 'b', 'c', 't']},
                                                    auto_veto_time="0",
                                                    channels={index: {"enable": "True",
                                                                      "offset_dac": {subchannel: "0" for subchannel in
                                                                                     ['a', 'b', 'c']}
                                                                      }
                                                              for index in range(16)}
                                                    ),
                                           delay=dict(channels={index: {"value": "0",
                                                                        "multiplier": "0"}
                                                                for index in range(16)})

                                           )
                                      for chipboard_index in range(16)
                                  ]
                                  }

            write_config(tempfile_path, self.configuration)

        self.set_current_chip(0)

    def set_current_chip(self, chip_number: int) -> None:
        """
        Sets the `current_chip_config` variable to the one corresponding to the chip_number index input.
        This is a utility function that allows for easier reference of the current chip configurations.
        """
        self.current_chip_config = self.configuration["configuration"][chip_number]

    def modify_DAC_value(self, channel: int, key: str, value):
        leading_edge_DACs = self.current_chip_config["channels"]

        leading_edge_DACs[channel][key] = str(value)

        pass

    def get_DAC_values(self, key: str) -> list:
        """
        This function returns a list of the current DAC values corresponding to the current key

        Args: key: key of the list of current values to be retrieved. Options are `enable`, `sign_bit`,
        and `leading_edge_DAC_value`

        Returns: A list of DAC values in corresponding data type

        raises: TypeError: if a key is not valid(sign_bit or leading_edge_DAC_value)

        """

        leading_edge_DACs = self.current_chip_config["cfd"]["channels"]

        if key == 'enable' or key == 'sign_bit':
            return [(DAC[key] == "True") for DAC in leading_edge_DACs]
        elif key == 'leading_edge_DAC_value':
            return [DAC[key] for DAC in leading_edge_DACs]
        else:
            raise TypeError('{0} is not a valid DAC key.'.format(key))
