"""
Module to generate bit-strings required con configure the LTC1660 dac

"""
from __future__ import annotations


def generate_dac_word(channel: int, value: float | int) -> int:
    """
Generates the 16 bit word required to configure the LTC1660 DAC.
    :param channel: DAC channel to configure range: 1-8
    :param value: Voltage setting, if type float 0.0V - 5.0V, if int expects unsigned bits for configuration.


    :return: (uint16) 2 byte DAC configuration bitstring

    :raises: ValueError
    """
    max_voltage = 5.0
    min_voltage = 0.0

    if isinstance(value, int):
        k = value
    else:
        if not isinstance(value, float) or value < min_voltage or value > max_voltage:
            raise ValueError("DAC voltage must be between 0.0 V-5.0 V")

        k = int((value / 5.0) * 1023)  # scales up to 1023 because of 10 bit limit.

    if channel < 1 or channel > 8:
        raise ValueError("DAC channel must be between 1 - 8")

    data_word = (channel << 12) | (k << 2) | 0x1  # making the don't care bits 0b01.

    return data_word


def generate_dac_sleep_word() -> int:
    """
Returns the bit sequence required to put DAC in sleep mode.

From the datasheet:
Sleep mode is initiated by performing a load sequence
to address 1110b (the DAC input word D7-D0 [D9-D0]
is ignored). Once in Sleep mode, a load sequence to any
other address (including “No Change” addresses 0000b
and 1001-1101b) causes the LTC1660 to Wake

    :return: (uint16) 2 byte DAC sleep bitstring
    """
    sleep_word = 0xE << 12 | 0x1
    return sleep_word


def generate_dac_wake_word() -> int:
    """
Returns the bit sequence required to wake up DAC without any change to output settings.

    :return: (uint16) 2 byte DAC wake bitstring

    """
    wake_word = 0x0 | 0x1
    return wake_word
