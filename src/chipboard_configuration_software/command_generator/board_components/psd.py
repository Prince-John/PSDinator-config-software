"""
Generates the bit strings for the configuration register on the PSD chips, the on-chip offset cancelling DACs, and
triggering mode selection.

"""
from __future__ import annotations

from typing import List, Union, Literal

from .utils import bit_append_left, sanitize_resistance_string

BIAS_MODES = Literal["high", "low"]
POLARITY_MODES = Literal["positive", "negative"]
VTC_RANGES = Literal["250 ns", "2 us"]
SUBCHANNEL_RANGES = Literal[0, 1, 2, 3, "0", "1", "2", "3"]


def generate_psd_serial_word(channel_enable_low_mask: int,
                             gain_settings: tuple,
                             subchannel_delay_ranges: tuple[SUBCHANNEL_RANGES, SUBCHANNEL_RANGES, SUBCHANNEL_RANGES],
                             subchannel_width_ranges: tuple,
                             vtc_range: VTC_RANGES,
                             bias_mode: BIAS_MODES,
                             polarity_mode: POLARITY_MODES,
                             chip_id: int
                             ) -> int:
    """

    Serial word definition:
        [Chip ID]-[Polarity]-[Bias Mode]-[VTC Range]-[Range Word]-[Gain Word]-[Unused]-[Channel Enable]
         <47:40> -  <39>    -   <38>    -   <37>    -   <36:25>  -  <24:16>  - <15:8> -    <7:0>

    Range Word Definition:
        --[Width Range C]-[Delay Range C]-[Width Range B]-[Delay Range B]-[Width Range A]-[Delay Range A]--
        --   <36:35>     -   <34:33>     -   <32:31>     -   <30:29>     -   <28:27>     -   <26:25>     --

    Gain Word Definition:
        --[Gain Range C]-[Gain Range C]-[Gain Range B]--
        --   <24:22>     -   <21:19>     -   <18:16>  --

    :param channel_enable_low_mask:
    :param gain_settings:
    :param subchannel_delay_ranges:
    :param subchannel_width_ranges:
    :param vtc_range:
    :param bias_mode:
    :param polarity_mode:
    :param chip_id: should be zero for both

    :rtype: int
    :return: 48 bit PSD configuration shift register word
    """

    gain_word = get_gain_word(gain_settings)
    range_word = get_range_word(subchannel_delay_ranges, subchannel_width_ranges)
    vtc_range_bit = get_vtc_range(vtc_range)
    bias_mode_bit = get_mode_bit(bias_mode)
    polarity_mode_bit = get_mode_bit(polarity_mode)
    channel_enable_mask_upper_byte = 0xFF
    channel_enable_mask_lower_byte = check_bitstring(channel_enable_low_mask)
    # chip_id should always be 0 for PSDv4
    chip_id = 0
    #print(f"Range word: {range_word:0b}")
    # assembling the serial word
    serial_word = chip_id << 40 | polarity_mode_bit << 39 | bias_mode_bit << 38 | vtc_range_bit << 37 | \
                  range_word << 25 | gain_word << 16 | channel_enable_mask_upper_byte << 8 | \
                  channel_enable_mask_lower_byte

    #print(f"Serial word: {serial_word:048b}")
    return serial_word


def generate_psd_serial_word_backup(channel_enable_low_mask: int,
                                    gain_settings: tuple,
                                    subchannel_delay_ranges: tuple[
                                        SUBCHANNEL_RANGES, SUBCHANNEL_RANGES, SUBCHANNEL_RANGES],
                                    subchannel_width_ranges: tuple,
                                    vtc_range: VTC_RANGES,
                                    bias_mode: BIAS_MODES,
                                    test_mode: POLARITY_MODES,
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
    :param chip_id: should be zero for both

    :rtype: int
    :return: 48 bit PSD configuration shift register word
    """

    gain_word = get_gain_word(gain_settings)
    range_word = get_range_word(subchannel_delay_ranges, subchannel_width_ranges)

    # assembling the serial word
    serial_word = bit_append_left(check_bitstring(channel_enable_low_mask),
                                  [0x00,
                                   gain_word,
                                   range_word,
                                   get_vtc_range(vtc_range),
                                   get_mode_bit(bias_mode),
                                   get_mode_bit(test_mode),
                                   check_bitstring(chip_id)],
                                  initial_word_length=[8, 8, 9, 12, 1, 1, 1, 8],
                                  final_bit_width=48)

    return serial_word


def generate_psd_test_mode_word(channel: int, sub_channel: Literal["a", "b", "c"]) -> int:
    """

This function returns an int with 7 valid bits [channel(5 MSB) + subchannel(2 LSB)] to encode the
PSD test mode channel selection.

    :return: (int) 7 bit address [channel(5 MSB) + subchannel(2 LSB)].

    """

    sub_channel_map = {"a": 0, "b": 1, "c": 2}

    if sub_channel not in sub_channel_map:
        raise ValueError("not a valid subchannel")

    if not isinstance(channel, int) or channel > 8 or channel < 0:
        raise ValueError("not a valid channel")

    address = channel << 2 | sub_channel_map[sub_channel]

    return address


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


def generate_psd_trigger_word(trigger_mode: int | Literal["1", "2", "3"]) -> int:
    """
This function generates the 2 bit trigger mode data word, with MSB = Bypass signal and LSB = Acq_ALL signal

#TODO: Acq_ALL is a fast signal this needs to be changed to not configure Acq_all using GUI.

    From Proctor Thesis mode look up table
Signal Names:   Acq_All                 Bypass
Mode 1          1 (prior to readout)    1
Mode 2          0                       1
Mode 3          0                       0

    :param trigger_mode: desired trigger mode 1, 2, or 3
    :return: 2 bit mode data word [Ack_All, Bypass(LSB)], type int
    """

    trigger_mode_map = {1: 0x3, 2: 0x1, 3: 0x0, "1": 0x3, "2": 0x1, "3": 0x0}

    if not isinstance(trigger_mode, (int, str)):
        raise TypeError("Not a valid trigger mode type, str | int expected")

    if trigger_mode not in trigger_mode_map:
        raise ValueError("Not a valid trigger mode value")

    return trigger_mode_map[trigger_mode]


def get_dac_value(dac_value: int) -> int:
    """
Converts pythons 2's complement into the 5 bit sign/mag notation expected by PSD.
    :rtype: 5 bit sign/mag notation int
    :return: 5 bit dac value in sign/mag notation (1 bit sign)+(4 bits mag)
    :type dac_value: int
    """
    if dac_value < 0:
        sign = 0x10
    else:
        sign = 0x00

    return (abs(dac_value) & 0x0F) | sign


def get_mode_bit(mode: BIAS_MODES | POLARITY_MODES | int) -> int:
    polarity_mode_map = {"positive": 0, "negative": 1}
    # Polarity Map disagrees with the proctor thesis but as of 2017 for PSDv4 an output swapper is added,
    # I'm not quite sure how that works but experimentally, for this bit set to '1' causes negative values on the
    # Analog A,B,C output buffers.

    bias_mode_map = {"high": 0, "low": 1}

    if isinstance(mode, int):
        return int(mode) & 0x1

    if mode in polarity_mode_map:
        return polarity_mode_map[mode]

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
    """
    Gain Word Definition:
        --[Gain Range C]-[Gain Range B]-[Gain Range A]--
        --   <24:22>     -   <21:19>     -   <18:16>  --

    :param gain_settings: (Gain A, Gain B, Gain C)
    :return:
    """

    gain_word = get_subchannel_gain_bits(gain_settings[2]) << 6 | \
                get_subchannel_gain_bits(gain_settings[1]) << 3 | \
                get_subchannel_gain_bits(gain_settings[0])

    return gain_word


def get_range_word(subchannel_delay_ranges: tuple, subchannel_width_ranges) -> int:
    """

     Range Word Definition:
            --[Width Range C]-[Delay Range C]-[Width Range B]-[Delay Range B]-[Width Range A]-[Delay Range A]--
            --   <36:35>     -   <34:33>     -   <32:31>     -   <30:29>     -   <28:27>     -   <26:25>     --

    :param subchannel_delay_ranges:
    :param subchannel_width_ranges:
    :return:
    """
    range_c = get_subchannel_range_bits(subchannel_width_ranges[2]) << 2 | \
              get_subchannel_range_bits(subchannel_delay_ranges[2])

    range_b = get_subchannel_range_bits(subchannel_width_ranges[1]) << 2 | \
              get_subchannel_range_bits(subchannel_delay_ranges[1])

    range_a = get_subchannel_range_bits(subchannel_width_ranges[0]) << 2 | \
              get_subchannel_range_bits(subchannel_delay_ranges[0])

    range_word = range_c << 8 | range_b << 4 | range_a

    return range_word


def get_subchannel_range_bits(delay_range: SUBCHANNEL_RANGES) -> int:
    """
   Returns the 2 delay and width setting bits. Default setting for PSD is 0

    Expects input to be a valid range setting 0-3.

    :return: 2 bit range bitstring. The return is of type int, only 2 LSB are valid.
    """

    valid_range_settings = {0: 0, 1: 1, 2: 2, 3: 3}

    delay_range = int(delay_range)

    if delay_range not in valid_range_settings:
        raise ValueError("Not a valid range setting")

    return valid_range_settings[delay_range]


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
    # must be an int
    if not isinstance(channel_mask, int):
        raise TypeError("Bitmask must be an integer")
    # must be in the range 0–255 inclusive
    if not 0 <= channel_mask <= 0xFF:
        raise ValueError("Bitmask must fit within 8 bits (0–255)")
    return channel_mask


def generate_global_enable_word(global_enable: bool):
    """
    Returns the status of the PSD global enable line. 1 bit value.

    This function is not strictly needed but is included for consistency with the way this program generates data words
    for configuration commands. It is a wrapper for typecasting bool to 1 bit int

    :param global_enable: global enable state of the CFD asic
    :return: Returns int with 1 valid bit for global enable bool input
    """

    if not isinstance(global_enable, bool):
        raise TypeError("Global Enable needs to be Type bool")

    if global_enable:
        return 1
    else:
        return 0
