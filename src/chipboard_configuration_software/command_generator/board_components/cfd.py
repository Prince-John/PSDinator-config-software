"""
Notes from Orabutt Thesis:

-When Lockout Mode is a logic high, shorter ≈110 nsec time steps are provided for a total lockout time
of 3.4 µsec. When the Lockout Mode is a logic low, a long mode is used providing ≈565
nsec time steps for a total lockout time of 16.6 µsec

-Oneshot width: It is provided with a two-bit pulse-width selection bus that allows the user to configure the output width
of this pulse(the CFD output pulse) between 50 nsec and 500 nsec
"""
from __future__ import annotations

from typing import Tuple, Literal, Type, List

NOWLIN_MODES: Type[str] = Literal["short", "long"]

TEST_POINT_SELECT_NODES: Type[str] = Literal[
    "AVSS", "lockout pulse", "leading edge detector pulse", "oneshot input",
    "oneshot pulse", "zero cross detector pulse"]
CAPACITOR_BUS_TIME_CONSTS: Type[str] = Literal[
    "1 ns", "2 ns", "3 ns", "4 ns", "5 ns", "6 ns", "7 ns", "8 ns", "9 ns", "10 ns", "11 ns", "12 ns", "13 ns", "14 ns",
    "15 ns", "16 ns", "24 ns", "36 ns", "48 ns", "60 ns", "72 ns", "84 ns", "96 ns",
    "108 ns", "120 ns", "132 ns", "144 ns", "156 ns", "168 ns", "180 ns", "192 ns"]
AGND_TRIM_VOLTAGES: Type[str] = Literal["1.36 V", "1.43 V", "1.49 V", "1.56 V", "1.63 V", "1.69 V", "1.77 V", "1.84 V"]

ONESHOT_WIDTH_SELECTS: Type[str] = Literal["50", "100", "200", "500"]

LOCKOUT_MODES: Type[str] = Literal["short", "long", "disabled"]
LOCKOUT_DAC_VALUES: Type[str] = Literal['110 ns', '220 ns', '330 ns', '440 ns', '550 ns', '660 ns', '770 ns', '880 ns', '990 ns', '1.10 us', '1.21 us', '1.32 us', '1.43 us', '1.54 us', '1.65 us', '1.76 us', '1.87 us', '1.98 us', '2.09 us', '2.20 us', '2.31 us', '2.42 us', '2.53 us', '2.64 us', '2.75 us', '2.86 us', '2.97 us', '3.08 us', '3.19 us', '3.30 us', '3.41 us', '535 ns', '1.1 us', '1.6 us', '2.1 us', '2.7 us', '3.2 us', '3.7 us', '4.3 us', '4.8 us', '5.3 us', '5.9 us', '6.4 us', '7.0 us', '7.5 us', '8.0 us', '8.6 us', '9.1 us', '9.6 us', '10.2 us', '10.7 us', '11.2 us', '11.8 us', '12.3 us', '12.8 us', '13.4 us', '13.9 us', '14.4 us', '15.0 us', '15.5 us', '16.1 us', '16.6 us']


def generate_individual_channel_word(channel: int, channel_enable: int | bool,
                                     leading_edge_DAC_value: int) -> tuple[int, int]:
    """
Generates the data word and address + mode word required to configure individual channel settings on the CFD chip.

 positive/negative polarity for dac, 1 sets it as negative polarity

    :param leading_edge_DAC_value: 5 bit LE DAC sign/magnitude value

    :param channel: channel number, type int (4 valid bits considered) from 0 to 15
    :param channel_enable: enable or disable channel, type bool, 1 bit int sets 1 as enable

    :return: tuple (8 bit address|mode word, 8 bit data word)
    """
    address_word = ((channel & 0xF) << 4) | 0x06

    if leading_edge_DAC_value < 0:
        sign = 0x1
    else:
        sign = 0x0

    magnitude = abs(leading_edge_DAC_value) & 0x1F

    data_word = (channel_enable << 6) | (sign << 5) | magnitude

    return address_word, data_word


def get_mode_0_words(nowlin_mode: NOWLIN_MODES,
                     test_point_select: TEST_POINT_SELECT_NODES,
                     test_point_channel: int,
                     capacitor_bus: CAPACITOR_BUS_TIME_CONSTS) -> Tuple[int, int]:
    nowlin_mode_map = {"long": 0,
                       "short": 1}

    test_point_select_map = {"AVSS": 0,
                             "lockout pulse": 1,
                             "leading edge detector pulse": 2,
                             "oneshot input": 3,
                             "oneshot pulse": 5,
                             "zero crossing detector pulse": 6}

    capacitor_bus_map = {"short": {"1 ns": 0,
                                   "2 ns": 1,
                                   "3 ns": 2,
                                   "4 ns": 3,
                                   "5 ns": 4,
                                   "6 ns": 5,
                                   "7 ns": 6,
                                   "8 ns": 7,
                                   "9 ns": 8,
                                   "10 ns": 9,
                                   "11 ns": 10,
                                   "12 ns": 11,
                                   "13 ns": 12,
                                   "14 ns": 13,
                                   "15 ns": 14,
                                   "16 ns": 15},
                         "long": {"12 ns": 0,
                                  "24 ns": 1,
                                  "36 ns": 2,
                                  "48 ns": 3,
                                  "60 ns": 4,
                                  "72 ns": 5,
                                  "84 ns": 6,
                                  "96 ns": 7,
                                  "108 ns": 8,
                                  "120 ns": 9,
                                  "132 ns": 10,
                                  "144 ns": 11,
                                  "156 ns": 12,
                                  "168 ns": 13,
                                  "180 ns": 14,
                                  "192 ns": 15}
                         }

    if test_point_channel > 15 or test_point_channel < 0:
        raise ValueError("Invalid test point channel selection")

    address_word = ((test_point_channel & 0xF) << 4) | 0x0

    try:
        nowlin_delay = capacitor_bus_map[nowlin_mode][capacitor_bus]
    except KeyError as e:

        raise ValueError(f"Invalid nowlin delay setting {capacitor_bus} for nowlin mode {nowlin_mode}")

    data_word = nowlin_mode_map[nowlin_mode] << 7 | test_point_select_map[test_point_select] << 4 | \
                nowlin_delay

    return address_word, data_word


def get_mode_1_words(lockout_mode, agnd_trim_voltage, oneshot_width_select) -> Tuple[int, int]:
    """



    :param lockout_mode: Lockout time range, (1)short (110 ns steps, max 3.4 us) or (0)long (535ns steps, max 16.6 us)
    :param agnd_trim_voltage: Internal AGND voltage setting, also accepts 3-bit int representing the trim bits
    :param oneshot_width_select: This sets the length of the output CFD pulse.

    :return:  tuple (0x01, 8 bit data word)
    """

    lockout_mode_map = {"short": 1, "long": 0, "disabled": 0}  # TODO: Verify this
    agnd_trim_voltage_map = {"1.36 V": 0, "1.43 V": 1, "1.49 V": 2, "1.56 V": 3,
                             "1.63 V": 4, "1.69 V": 5, "1.77 V": 6, "1.84 V": 7}
    oneshot_width_select_map = {"50": 0, "100": 1, "200": 2, "500": 3}

    address_word = 0x01

    lockout_bits = lockout_mode_map[lockout_mode]
    agnd_bits = agnd_trim_voltage_map[agnd_trim_voltage]
    oneshot_width_bits = oneshot_width_select_map[oneshot_width_select]

    data_word = lockout_bits << 5 | agnd_bits << 2 | oneshot_width_bits

    return address_word, data_word


def get_mode_5_words(lockout_enable, lockout_dac: int | LOCKOUT_DAC_VALUES) -> Tuple[int, int]:
    """

    :param lockout_enable:
    :param lockout_dac: 5 bit unsigned int lockout dac value
    :return:
    """

    lockout_mode_map = {"short": 1, "long": 1, "disabled": 0}  # TODO: Verify this
    lockout_bits = lockout_mode_map[lockout_enable]
    data_word = lockout_bits << 5 | (lockout_dac & 0x1F)

    address_word = 0x05

    return address_word, data_word


def generate_common_channel_words(nowlin_mode: int | NOWLIN_MODES,
                                  test_point_select: TEST_POINT_SELECT_NODES,
                                  test_point_channel: int,
                                  capacitor_bus: CAPACITOR_BUS_TIME_CONSTS,
                                  lockout_mode: int | LOCKOUT_MODES,
                                  agnd_trim_voltage: int | AGND_TRIM_VOLTAGES,
                                  oneshot_width_select: int | ONESHOT_WIDTH_SELECTS,
                                  lockout_dac_input: int| LOCKOUT_DAC_VALUES) -> List[Tuple[int, int], ...]:
    """

This function generates the (address-mode,data) 8-bit words that are used to configure the common channel for the CFD
chip. 3 pairs of add-mode, data words are required to completely configure the common channel of CFD chip. This returns
a list of the three configuration word tuples.

Mode 0 is returned last since the test point channel selection is reset when address lines change on the common bus.
Passing it last ensures that the address lines correspond to the selected test point channel.
#TODO A bug is present here that prevents mode 0 words from being latched if the channel selection != 0

    :param lockout_dac_input:
    :param nowlin_mode: Nowlin mode length, also accepts 1 bit int (0: Long, 1: Short)
    :param test_point_select: Internal test point selection to route the test point pin.
    :param test_point_channel: Channel selection for the test point
    :param capacitor_bus: Nowlin delay length
    :param lockout_mode: Lockout time range, (1)short (110 ns steps, max 3.4 us) or (0)long (565ns steps, max 16.6 us),
            disabled sets lockout enable
    :param agnd_trim_voltage: Internal AGND voltage setting, also accepts 3-bit int representing the trim bits
    :param oneshot_width_select: This sets the length of the output CFD pulse.


    :return: List of 3 tuples (8-bit address|mode word, 8-bit data word)
    """

    mode_0 = get_mode_0_words(nowlin_mode, test_point_select, test_point_channel, capacitor_bus)
    mode_1 = get_mode_1_words(lockout_mode, agnd_trim_voltage, oneshot_width_select)
    mode_5 = get_mode_5_words(lockout_mode, lockout_dac_input)

    return [mode_5, mode_1, mode_0]


def generate_global_enable_word(global_enable: bool):
    """
    Returns the status of the CFD global enable line. 1 bit value.

    This function is not strictly needed but is included for consistency with the way this program generates data words
    for configuration commands. It is a wrapper for typecasting bool to 1 bit int

    :param global_enable: global enable state of the CFD asic
    :return: Returns int with 1 valid bit for global enable bool input
    """

    if global_enable:
        return 1
    else:
        return 0
