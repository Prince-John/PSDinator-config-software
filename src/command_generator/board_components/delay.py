
def assemble_command_byte(channel: int, delay: int) -> int:
    """
    Assembles the 8 bit word that is sent to configure the delay

    :param channel: channel (red = 1, green = 2, blue = 3, or test = 0)
    :param delay: delay from 0-64 ns, delays in multiples of 2ns if not a multiple of
                  2ns it rounds down to the nearest multiple.

    :return: (uint8) 1 byte delay configuration bitstring
    :raises: ValueError: if channel or delay is out of bounds.

    """
    if channel < 0 or channel > 3:
        raise ValueError("Not a valid color")

    if not isinstance(delay, int) or delay < 0 or delay > 31:
        raise ValueError("delay_multiplier must be an integer between 0 and 31")

    delay_multiplier = delay // 2
    command_byte = 0x7F & (channel << 5) | delay_multiplier

    return command_byte
