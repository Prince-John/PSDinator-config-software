from unittest import TestCase, main

from src.chipboard_configuration_software.command_generator import generate_command_string as command_gen


class Test(TestCase):

    def setUp(self):
        self.config = {
            "chipboard_number": 0,
            "cfd": {
                "nowlin_mode": "short",
                "nowlin_delay": "1",
                "lockout_DAC": "",
                "lockout_mode": "disabled",
                "cfd_pulse_width": "50",
                "agnd_trim": "1.77",
                "global_enable": "True",
                "global_Mode": "False",
                "le_out_enable": "False",
                "external_agnd_enable": "False",
                "test_point": "AVSS",
                "test_point_channel": "0",
                "negative_polarity": "False",
                "channels": {
                    "0": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "1": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "2": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "3": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "4": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "5": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "6": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "7": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "8": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "9": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "10": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "11": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "12": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "13": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "14": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    },
                    "15": {
                        "enable": "True",
                        "leading_edge_DAC_value": 0,
                        "sign_bit": "False"
                    }

                }
            },
            "psd": {
                "polarity": "pos",
                "bias": "low",
                "gain": {
                    "a": "500",
                    "b": "10000",
                    "c": "10000"
                },
                "delay": {
                    "a": {
                        "range": "0",
                        "dac_value": "2.5"
                    },
                    "b": {
                        "range": "0",
                        "dac_value": "0"
                    },
                    "c": {
                        "range": "0",
                        "dac_value": "0"
                    }
                },
                "width": {
                    "a": {
                        "range": "0",
                        "dac_value": "0"
                    },
                    "b": {
                        "range": "0",
                        "dac_value": "0"
                    },
                    "c": {
                        "range": "0",
                        "dac_value": "0"
                    }
                },
                "vtc_range": "250 ns",
                "auto_veto_time": "0",
                "trigger_mode": "3",
                "test_mode": "on",
                "channels": {
                    "0": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "1": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "2": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "3": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "4": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "5": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "6": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "7": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "8": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "9": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "10": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "11": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "12": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "13": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "14": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    },
                    "15": {
                        "enable": "True",
                        "offset_dac": {
                            "a": "0",
                            "b": "0",
                            "c": "0"
                        }
                    }
                }
            },
            "delay": {
                "0": {
                    "value": "0",
                    "address": "0"
                },
                "1": {
                    "value": "0",
                    "address": "0"
                },
                "2": {
                    "value": "0",
                    "address": "0"
                },
                "3": {
                    "value": "0",
                    "address": "0"
                },
                "4": {
                    "value": "0",
                    "address": "0"
                },
                "5": {
                    "value": "0",
                    "address": "0"
                },
                "6": {
                    "value": "0",
                    "address": "0"
                },
                "7": {
                    "value": "0",
                    "address": "0"
                },
                "8": {
                    "value": "0",
                    "address": "0"
                },
                "9": {
                    "value": "0",
                    "address": "0"
                },
                "10": {
                    "value": "0",
                    "address": "0"
                },
                "11": {
                    "value": "0",
                    "address": "0"
                },
                "12": {
                    "value": "0",
                    "address": "0"
                },
                "13": {
                    "value": "0",
                    "address": "0"
                },
                "14": {
                    "value": "0",
                    "address": "0"
                },
                "15": {
                    "value": "0",
                    "address": "0"
                },
                "16": {
                    "value": "0",
                    "address": "0"
                },
                "17": {
                    "value": "0",
                    "address": "0"
                }

            },
            "mux": {"enable": True,
                    "channel": 0}
        }

    def test_generate_psd_commands(self):
        commands = command_gen.generate_psd_commands(self.config["psd"])

        for command in commands:
            print(command)

        self.fail()

    def test_generate_delay_commands(self):
        command = command_gen.generate_delay_commands(self.config["delay"])

        self.assertEqual(41, len(command))

        print(command)


if __name__ == '__main__':
    main()
