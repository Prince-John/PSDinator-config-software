from unittest import TestCase

from src.chipboard_configuration_software.command_generator.board_components import psd


class Test(TestCase):
    def test_bit_append_left(self):
        self.assertEqual(psd.bit_append_left(0xf, 0b1010, 4), 0b1111)
        self.assertEqual(psd.bit_append_left(0xf, 0b1010), 0b10101111)
        self.assertEqual(0b11, psd.bit_append_left(0xf, 0b1010, 2))
        self.assertEqual(0b101111, psd.bit_append_left(0xf, 0b10))
        self.assertEqual(0b001111, psd.bit_append_left(0xf, 0b00))


def format_binary_with_spaces(number: int, total_bits: int = 50) -> str:
    # Format the number as a binary string with leading zeros
    binary_string = f'{number:0{total_bits}b}'

    # Ensure the binary string length is divisible by 4 by padding if necessary
    padding_length = 0  # (4 - len(binary_string) % 4) % 4
    padded_binary = '0' * padding_length + binary_string

    # Split the padded binary string into groups of 4
    grouped_binary = ' '.join([padded_binary[i:i + 4] for i in range(0, len(padded_binary), 4)])

    return grouped_binary


class TestBitSequenceOutputs(TestCase):

    def test_generate_psd_serial_word(self):
        ch_bit_mask = 0b10001010
        gains = (500, 10000, 500)
        delays = (0, 1, 2)
        widths = ("3", 1, "2")
        chip_id = 0b11100011
        word = psd.generate_psd_serial_word(ch_bit_mask, gains, delays, widths, "2 us", "high", "on", chip_id)

        test_mode = 1
        bias_mode = 0
        vtc = 0

        actual_word = chip_id << 40 | test_mode << 39 | bias_mode << 38 | vtc << 37 | 2 << 35 | 2 << 33 | 1 << 31 | \
                      1 << 29 | 3 << 27 | 0 << 25 | 0 << 22 | 4 << 19 | 0 << 16 | ch_bit_mask

        print(format_binary_with_spaces(word, 48))
        print(format_binary_with_spaces(actual_word, 48))
        print(format_binary_with_spaces(actual_word ^ word, 48))
        self.assertEqual(actual_word, word)


class TestGeneratePsdDacWords(TestCase):
    def test_generate_psd_dac_words(self):
        test_out = psd.generate_psd_dac_words(12, 3, "a")
        good_out = (0b01100, 0b0001100)

        self.assertEqual(test_out, good_out, msg=f"Failed for {test_out} != {good_out}")

    def test_get_dac_value(self):
        test_out = psd.get_dac_value(-1)
        good_output = 0b10001

        for i, good_output in {(-15, 0b11111), (0, 0b00000), (15, 0b01111)}:
            test_out = psd.get_dac_value(i)

            self.assertEqual(test_out, good_output, msg=f"Failed for {i:05b} != {good_output:05b}")


class TestPsdTriggerWord(TestCase):
    def test_generate_psd_trigger_word(self):

        for test_case, good_out in [(1, 0x3), (2, 0x1), (3, 0x0), ("1", 0x3), ("2", 0x1), ("3", 0x0)]:
            self.assertEqual(psd.generate_psd_trigger_word(test_case), good_out)

    def test_invalid_type(self):
        # Test invalid types to raise TypeError
        with self.assertRaises(TypeError) as context:
            psd.generate_psd_trigger_word(1.0)  # Float type, invalid
        self.assertEqual(str(context.exception), "Not a valid trigger mode type, str | int expected")

        with self.assertRaises(TypeError) as context:
            psd.generate_psd_trigger_word([1])  # List type, invalid
        self.assertEqual(str(context.exception), "Not a valid trigger mode type, str | int expected")

        with self.assertRaises(TypeError) as context:
            psd.generate_psd_trigger_word({"mode": 1})  # Dict type, invalid
        self.assertEqual(str(context.exception), "Not a valid trigger mode type, str | int expected")

    def test_invalid_value(self):
        # Test invalid values to raise ValueError
        with self.assertRaises(ValueError) as context:
            psd.generate_psd_trigger_word(4)  # Integer outside of valid range
        self.assertEqual(str(context.exception), "Not a valid trigger mode value")

        with self.assertRaises(ValueError) as context:
            psd.generate_psd_trigger_word("4")  # String outside of valid range
        self.assertEqual(str(context.exception), "Not a valid trigger mode value")

        with self.assertRaises(ValueError) as context:
            psd.generate_psd_trigger_word("mode")  # Completely invalid string
        self.assertEqual(str(context.exception), "Not a valid trigger mode value")
