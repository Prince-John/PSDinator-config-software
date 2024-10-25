def generate_dac_word(channel: int, voltage: float) -> int:
    """
Generates the 16 bit word required to configure the LTC1660 DAC.
    :param channel: DAC channel to configure range: 1-8
    :param voltage: Voltage setting, 0.0V - 5.0V


    :return: (uint16) 2 byte DAC configuration bitstring

    :raises: ValueError
    """
    max_voltage = 5.0
    min_voltage = 0.0

    if voltage < min_voltage or voltage > max_voltage:
        raise ValueError("DAC voltage must be between 0.0V-5.0")
        return

    if channel < 1 or channel > 8:
        raise ValueError("DAC channel must be between 1 - 8")
        return

    k = int((voltage / 5.0) * 1024)

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
