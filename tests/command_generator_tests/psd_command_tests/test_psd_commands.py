import random
from unittest import TestCase

from chipboard_configuration_software.command_generator.commands import psd_commands
# noinspection PyProtectedMember
from chipboard_configuration_software.command_generator.commands.psd_commands import generate_psd_trigger_subcommands, \
    generate_psd_global_enable_subcommands, _get_channel_enable, generate_psd_dac_subcommands

psd_test_config = {"global_enable": "True",
                   "polarity": "pos",
                   "trigger_mode": "3",
                   "serial_register_settings_": {
                       "bias": "high",
                       "gain": {
                           "a": "500",
                           "b": "10000",
                           "c": "10000"
                       },
                       "test_mode": "off",
                       "vtc_range": "2 us",
                       "delay_ranges": {
                           "a": "0",
                           "b": "0",
                           "c": "0"
                       },
                       "width_ranges": {
                           "a": "0",
                           "b": "0",
                           "c": "0"
                       },
                       "channel_enables": {
                           "0": "False",
                           "1": "False",
                           "2": "False",
                           "3": "False",
                           "4": "False",
                           "5": "False",
                           "6": "False",
                           "7": "False",
                           "8": "False",
                           "9": "False",
                           "10": "False",
                           "11": "False",
                           "12": "False",
                           "13": "False",
                           "14": "False",
                           "15": "False"
                       }
                   },
                   "octal_dac_settings": {
                       "delay_voltages": {
                           "a": "0",
                           "b": "0",
                           "c": "0"
                       },
                       "width_voltages": {
                           "a": "0",
                           "b": "0",
                           "c": "0"
                       },
                       "auto_veto_time": "2",
                       "multiplicity_offset": "0"
                   },
                   "channel_offset_dacs": {
                       "0": {
                           "a": "0",
                           "b": "0",
                           "c": "0"
                       },
                       "1": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "2": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "3": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "4": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "5": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "6": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "7": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "8": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "9": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "10": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "11": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "12": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "13": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "14": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       },
                       "15": {
                           "a": "0",
                           "b": "0",
                           "c": "0"

                       }
                   }
                   }
trigger_test_config = {
    "trigger_mode": "3"
}
global_enable_config = {
    "global_enable": "3"
}


class TestPsdIndividualCommands(TestCase):

    def test_trigger_command_is_string_and_null_terminated(self):
        config = {"trigger_mode": "3"}
        command = generate_psd_trigger_subcommands(config)

        self.assertIsInstance(command, str, "Command should be a string")
        self.assertTrue(command.endswith('\0'), f"Command should be null-terminated, got: {repr(command)}")

    def test_trigger_command_has_correct_prefix(self):
        config = {"trigger_mode": "3"}
        command = generate_psd_trigger_subcommands(config)

        self.assertTrue(command.startswith("PSD:TRG:"), f"Expected prefix 'PSD:TRG:', got: {command}")

    def test_trigger_command_has_correct_length(self):
        config = {"trigger_mode": "3"}
        command = generate_psd_trigger_subcommands(config)

        expected_length = len("PSD:TRG:00\0")
        self.assertEqual(len(command), expected_length, f"Expected length {expected_length}, got {len(command)}")

    def test_trigger_command_correct_mapping(self):
        """Test correct trigger_mode to hex string mapping."""
        trigger_mode_map = {
            1: "03",
            2: "01",
            3: "00",
            "1": "03",
            "2": "01",
            "3": "00"
        }

        for mode_input, expected_hex in trigger_mode_map.items():
            with self.subTest(mode_input=mode_input):
                config = {"trigger_mode": str(mode_input)}
                command = generate_psd_trigger_subcommands(config)
                expected_cmd = f"PSD:TRG:{expected_hex}\0"
                self.assertEqual(command, expected_cmd, f"Expected '{expected_cmd}', got '{command}'")

    def test_trigger_command_invalid_modes_raise_exception(self):
        """Ensure invalid or missing trigger_mode raises an error."""
        failing_configs = [
            {"trigger_mode": "invalid"},
            {"trigger_mode": None},
            {"trigger_mode": 4},
            {"trigger_mode": ""},
            {}
        ]

        for bad_config in failing_configs:
            with self.subTest(mode_input=bad_config.get("trigger_mode", "<missing>")):
                with self.assertRaises(Exception):
                    _ = generate_psd_trigger_subcommands(bad_config)

    def test_global_enable_command_is_string_and_null_terminated(self):
        config = {"global_enable": "True"}
        command = generate_psd_global_enable_subcommands(config)

        self.assertIsInstance(command, str, "Command should be a string")
        self.assertTrue(command.endswith('\0'), f"Command should be null-terminated, got: {repr(command)}")

    def test_global_enable_command_has_correct_prefix(self):
        config = {"global_enable": "True"}
        command = generate_psd_global_enable_subcommands(config)

        self.assertTrue(command.startswith("PSD:GEN:"), f"Expected prefix 'PSD:GEN:', got: {command}")

    def test_global_enable_command_has_correct_length(self):
        config = {"global_enable": "True"}
        command = generate_psd_global_enable_subcommands(config)

        expected_length = len("PSD:GEN:01\0")
        self.assertEqual(len(command), expected_length, f"Expected length {expected_length}, got {len(command)}")

    def test_global_enable_command_correct_mapping(self):
        """Test 'True' and 'False' values map to correct hex codes."""
        expected_map = {
            "True": "01",
            "False": "00",
            "true": "00",
            "FALSE": "00",
            "None": "00",
            "1": "00",
        }

        for bool_str, hex_val in expected_map.items():
            with self.subTest(value=bool_str):
                config = {"global_enable": bool_str}
                command = generate_psd_global_enable_subcommands(config)
                expected_cmd = f"PSD:GEN:{hex_val}\0"
                self.assertEqual(command, expected_cmd, f"Expected '{expected_cmd}', got '{command}'")

    def test_global_enable_command_invalid_values_raise_exception(self):
        """Invalid or missing values should raise an error."""
        bad_configs = [
            {},
        ]

        for bad_config in bad_configs:
            with self.subTest(value=bad_config.get("global_enable", "<missing>")):
                with self.assertRaises(Exception):
                    _ = generate_psd_global_enable_subcommands(bad_config)


class TestHelperFunctions(TestCase):

    def test_all_channels_disabled(self):
        """All channels disabled should return (0xFF, 0xFF)"""
        input_dict = {str(i): "False" for i in range(16)}
        result = _get_channel_enable(input_dict)
        expected = (0xFF, 0xFF)
        self.assertEqual(result, expected)

    def test_all_channels_enabled(self):
        """All channels enabled should return (0x00, 0x00)"""
        input_dict = {str(i): "True" for i in range(16)}
        result = _get_channel_enable(input_dict)
        expected = (0x00, 0x00)
        self.assertEqual(result, expected)

    def test_alternating_channels_enabled(self):
        """Even channels enabled, odd disabled → (0x55, 0x55)"""
        input_dict = {
            str(i): "True" if i % 2 == 0 else "False"
            for i in range(16)
        }
        result = _get_channel_enable(input_dict)
        expected = (0x55, 0x55)
        self.assertEqual(result, expected)

    def test_single_channel_enabled(self):
        """Only channel 0 enabled, rest disabled → (0x7F, 0xFF)"""
        input_dict = {str(i): "False" for i in range(16)}
        input_dict["0"] = "True"
        result = _get_channel_enable(input_dict)
        expected = (0x7F, 0xFF)
        self.assertEqual(expected, result)

    def test_lowercase_true_is_treated_as_false(self):
        """'true' (lowercase) is not accepted — treated as disabled"""
        input_dict = {str(i): "true" for i in range(16)}  # all lowercase "true"
        result = _get_channel_enable(input_dict)
        expected = (0xFF, 0xFF)
        self.assertEqual(result, expected)

    def test_partial_input_raises_exception(self):
        """Missing any channels should raise an exception"""
        incomplete_dict = {str(i): "True" for i in range(15)}  # missing one channel
        with self.assertRaises(Exception):
            _ = _get_channel_enable(incomplete_dict)

    def test_empty_input_raises_exception(self):
        """Completely empty input should also raise"""
        with self.assertRaises(Exception):
            _ = _get_channel_enable({})


class TestPsdOffsetDacSubcommands(TestCase):
    def test_single_channel_single_subchannel(self):
        """Basic test: one channel, one subchannel, real DAC word gen."""
        config = {"0": {"a": "0"}}
        commands = generate_psd_dac_subcommands(config)

        self.assertEqual(len(commands), 1)
        cmd = commands[0]
        self.assertTrue(cmd.startswith("PSD:OD0:"), f"Bad prefix: {cmd}")
        self.assertTrue(cmd.endswith('\0'), f"Missing null terminator: {cmd}")
        self.assertEqual(len(cmd), len("PSD:OD0:0000\0"), f"Incorrect length: {cmd}")
        self.assertRegex(cmd, r"^PSD:OD0:[0-9A-F]{4}\0")

    def test_multiple_channels_and_subchannels(self):
        """Multiple channels and subchannels produce correct command list."""
        config = {
            "0": {"a": "1", "b": "2"},
            "8": {"c": "3"}
        }
        commands = generate_psd_dac_subcommands(config)

        self.assertEqual(len(commands), 3)

        for cmd in commands:
            self.assertTrue(cmd.startswith("PSD:OD0:") or cmd.startswith("PSD:OD1:"))
            self.assertTrue(cmd.endswith("\0"))
            self.assertRegex(cmd, r"^PSD:OD[01]:[0-9A-F]{4}\0")

    def test_partial_config_is_handled(self):
        """Empty channel entries are ignored without error."""
        config = {
            "0": {"a": "10"},
            "5": {},  # empty subchannel dict
            "15": {}  # empty subchannel dict
        }

        commands = generate_psd_dac_subcommands(config)

        self.assertEqual(len(commands), 1)
        self.assertTrue(commands[0].startswith("PSD:OD0:"))

    def test_empty_config_returns_empty_list(self):
        """Empty input returns empty command list."""
        config = {}
        commands = generate_psd_dac_subcommands(config)
        self.assertEqual(commands, [])

    def test_hex_output_is_zero_padded(self):
        """Value/address should be exactly 2 hex digits, padded if needed."""
        config = {"7": {"c": "1"}}  # channel < 8, subchannel 'c'
        commands = generate_psd_dac_subcommands(config)

        self.assertEqual(len(commands), 1)
        cmd = commands[0]
        self.assertRegex(cmd, r"^PSD:OD0:[0-9A-F]{4}\0", f"Not properly padded: {cmd}")

    def test_correct_command_prefix_for_high_channels(self):
        """Channels >= 8 should use 'OD1:' in command."""
        config = {"12": {"b": "5"}}
        commands = generate_psd_dac_subcommands(config)

        self.assertEqual(len(commands), 1)
        self.assertTrue(commands[0].startswith("PSD:OD1:"))

    def test_invalid_channel_key_raises(self):
        """Non-integer channel keys should raise ValueError."""
        config = {"invalid": {"a": "10"}}
        with self.assertRaises(ValueError):
            _ = generate_psd_dac_subcommands(config)

    def test_channel_index_above_15_raises(self):
        """Using a channel >15 should raise an exception."""
        invalid_config = {
            "16": {"a": "10"},
            "20": {"b": "5"},
        }

        for ch in invalid_config:
            with self.subTest(channel=ch):
                config = {ch: invalid_config[ch]}
                with self.assertRaises(ValueError):
                    _ = generate_psd_dac_subcommands(config)

    def test_multiple_randomized_partial_configs(self):
        """Use subtests to verify structure of many partial inputs."""
        channels = list(range(16))
        subchannels = ["a", "b", "c"]

        for _ in range(10):  # Try 10 randomized cases
            # Random number of channels and random DAC values
            selected_channels = random.sample(channels, k=random.randint(1, 16))
            config = {
                str(ch): {
                    random.choice(subchannels): str(random.randint(0, 31))
                }
                for ch in selected_channels
            }

            with self.subTest(config=config):
                commands = generate_psd_dac_subcommands(config)

                self.assertEqual(len(commands), len(config))
                for ch_str, cmd in zip(config.keys(), commands):
                    ch = int(ch_str)
                    expected_prefix = "PSD:OD0:" if ch < 8 else "PSD:OD1:"
                    self.assertTrue(cmd.startswith(expected_prefix), f"Wrong prefix for channel {ch}: {cmd}")
                    self.assertTrue(cmd.endswith('\0'), f"Missing null terminator: {cmd}")
                    self.assertEqual(len(cmd), len("PSD:OD0:0000\0"), f"Incorrect length: {cmd}")
                    self.assertRegex(cmd, r"^PSD:OD[01]:[0-9A-F]{4}\0", f"Bad hex format: {cmd}")
