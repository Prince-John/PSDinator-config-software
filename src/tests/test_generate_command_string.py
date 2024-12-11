from unittest import TestCase

from src.command_generator import generate_command_string

class Test(TestCase):
    def test_get_cfd_individual_channel_commands(self):
        self.fail()


class Test(TestCase):
    def test_get_cfd_common_channel_commands(self):

        generate_command_string.get_cfd_common_channel_commands(cfd_config={
                "nowlin_mode": "short",
                "nowlin_delay": "10 ns",
                "lockout_DAC": "1",
                "lockout_mode": "disabled",
                "cfd_pulse_width": "50",
                "agnd_trim": "1.84 V",
                "global_enable": "True",
                "global_Mode": "False",
                "le_out_enable": "False",
                "test_point": "oneshot pulse",
                "test_point_channel": "0",
                "negative_polarity": "False",
                "leading_edge_DACs": {
                    "0": {
                        "enable": "True",
                        "leading_edge_DAC_value": 7,
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

                }} )

        self.fail()
