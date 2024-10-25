"""
Generates the bit strings for the configuration register on the PSD chips, the on-chip offset cancelling DACs, and
triggering mode selection.

"""
from __future__ import annotations

from typing import List, Union, Literal

from .utils import bit_append_left, sanitize_resistance_string

BIAS_MODES = Literal["high", "low"]
TEST_MODES = Literal["off", "on"]
VTC_RANGES = Literal["250 ns", "2 us"]
SUBCHANNEL_RANGES = Literal[0, 1, 2, 3, "0", "1", "2", "3"]


def generate_psd_serial_word(channel_enable_low_mask: int,
                             gain_settings: tuple,
                             subchannel_delay_ranges: tuple[SUBCHANNEL_RANGES, SUBCHANNEL_RANGES, SUBCHANNEL_RANGES],
                             subchannel_width_ranges: tuple,
                             vtc_range: VTC_RANGES,
                             bias_mode: BIAS_MODES,
                             test_mode: TEST_MODES,
                             chip_id: int
                             ) -> int:
    """


    :param channel_enable_low_mask:
    :param gain_settings:
    :param subchannel_delay_ranges:
    :param subchannel_width_ranges:
    :param vtc_range:
    :param bias_mode:
    :param test_mode:
    :param chip_id:

    :rtype: int
    :return: 48 bit PSD configuration shift register word
    """

    gain_word = get_gain_word(gain_settings)
    range_word = get_range_word(subchannel_delay_ranges, subchannel_width_ranges)

    # assembling the serial word
    serial_word = bit_append_left(check_bitstring(channel_enable_low_mask)
                                  , [0x00,
                                     gain_word,
                                     range_word,
                                     get_vtc_range(vtc_range),
                                     get_mode_bit(bias_mode),
                                     get_mode_bit(test_mode),
                                     check_bitstring(chip_id)],
                                  initial_word_length=[8, 8, 9, 12, 1, 1, 1, 8],
                                  final_bit_width=48)

    return serial_word


def generate_psd_dac_words(dac_setting: int, channel: int, sub_channel: Literal["a", "b", "c"]) -> tuple[int, int]:
    """

This function returns a tuple containing the 5 bit signed DAC value as it first
element and 7 bit [channel(5 MSB) + subchannel(2 LSB)] address as its second element.


Notes from Proctor Thesis:

-Signed value: The offset-canceling DAC uses a sign/magnitude data representation. The
most significant bit determines polarity while the lower 4 bits provide magnitude
information.
-Subchannel Disc: subchannel address 00 selects the A integrator, 01 selects the B
integrator, and 10 selects the C integrator. The code 11 is currently
unused.


    :return: (5 bit int, 7 bit int) Returns a tuple containing the 5 bit signed DAC value as it first element and 7 bit
 address [channel(5 MSB) + subchannel(2 LSB)] as its second element.

    """

    sub_channel_map = {"a": 0, "b": 1, "c": 2}

    if sub_channel not in sub_channel_map:
        raise ValueError("not a valid subchannel")

    if not isinstance(channel, int) or channel > 8 or channel < 0:
        raise ValueError("not a valid channel")

    dac_value = get_dac_value(dac_setting)
    address = channel << 2 | sub_channel_map[sub_channel]

    return dac_value, address


def get_dac_value(dac_value: int) -> int:
    """
Converts pythons 2's complement into the 5 bit sign/mag notation expected by PSD.
    :rtype: 5 bit sign/mag notation int
    :return: 5 bit dac value in sign/mag notation
    :type dac_value: int
    """
    if dac_value < 0:
        sign = 0x10
    else:
        sign = 0x00

    return (abs(dac_value) & 0x0F) | sign


def get_mode_bit(mode: BIAS_MODES | TEST_MODES | int) -> int:
    test_mode_map = {"off": 0, "on": 1}
    bias_mode_map = {"high": 0, "low": 1}

    if isinstance(mode, int):
        return int(mode) & 0x1

    if mode in test_mode_map:
        return test_mode_map[mode]

    if mode in bias_mode_map:
        return bias_mode_map[mode]

    raise TypeError("Not a valid mode option")


def get_subchannel_gain_bits(resistance: str | int) -> int:
    """
    Returns the 3 gain setting bits from the gain resistance map. Default setting for PSD is 500 Ω

    Expects input to be a valid gain setting in ohms, can be an int or string with or without ',' and units (Ω/ohm).

    :return: 3 bit gain resistance bitstring. The return is of type int, only 3 LSB are valid.
    """

    resistance_setting_map = {500: 0,
                              1000: 1,
                              2000: 2,
                              5000: 3,
                              10000: 4,
                              20000: 5,
                              50000: 6,
                              100000: 7}

    if not isinstance(resistance, int):
        try:
            resistance = sanitize_resistance_string(resistance)
        except (TypeError, ValueError):
            raise TypeError("Not a valid resistance setting type, should be string or int in ohms ")

    if resistance not in resistance_setting_map:
        raise ValueError("Not a valid resistance setting")

    return resistance_setting_map[resistance]


def get_gain_word(gain_settings: tuple) -> int:
    gain_word = 0x00
    for index, gain in enumerate(gain_settings):
        gain_word = bit_append_left(gain_word, get_subchannel_gain_bits(gain), initial_word_length=3 * index)
    return gain_word


def get_range_word(subchannel_delay_ranges: tuple, subchannel_width_ranges) -> int:
    range_word = 0x00
    for index, (delay_range, width_range) in enumerate(zip(subchannel_delay_ranges, subchannel_width_ranges)):
        range_word = bit_append_left(range_word, get_subchannel_range_bits(delay_range),
                                     initial_word_length=(4 * index))
        range_word = bit_append_left(range_word, get_subchannel_range_bits(width_range),
                                     initial_word_length=(4 * index + 2))
    return range_word


def get_subchannel_range_bits(delay_range: SUBCHANNEL_RANGES) -> int:
    """
    Returns the 2 delay and width setting bits. Default setting for PSD is 0

    Expects input to be a valid range setting 0-3.

    :return: 2 bit range bitstring. The return is of type int, only 2 LSB are valid.
    """

    valid_range_settings = {0, 1, 2, 3}

    delay_range = int(delay_range)

    if delay_range not in valid_range_settings:
        raise ValueError("Not a valid range setting")

    return delay_range


def get_vtc_range(vtc_range: VTC_RANGES) -> int:
    """
Note about delay ranges from the PSDv4 update presentation,

'We decided for PSD4, rather than start the TVC on the rising edge
of the CFD pulse, we would start the TVC on the falling edge of its
CFD input. Width of CFD pulse implements the delay that we need!
This implies that both edges of the CFD pulse must possess very
low jitter. Integrator delays are still relative to the rising edge of the
CFD pulse, just as in PSD3.'

    :return:  1 bit vtc range bitstring. The return is of type int, only 1 LSB is valid.
    """
    vtc_range_map = {"250 ns": 1, "2 us": 0}

    if vtc_range not in vtc_range_map:
        raise ValueError("not a valid vtc range")

    return vtc_range_map[vtc_range]


def check_bitstring(channel_mask: int) -> int:
    if not isinstance(channel_mask, int) or channel_mask.bit_length() > 8:
        raise TypeError("Bitmask needs to be of type int with bit width = 8")

    return channel_mask
