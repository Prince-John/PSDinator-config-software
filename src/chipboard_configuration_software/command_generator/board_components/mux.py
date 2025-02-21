"""
MUX data word generator module for ADG1206 analog multiplexer
"""


def generate_mux_word(channel: int, enable: bool) -> int:
    """
    Assembles the 8 bit word that is sent to configure the mux channel

    :param channel: input channel [0-15] to route to MUX pin on backplane.
    :param enable: enable the mux, if not True channel setting does not matter.

    :return: (uint8) 1 byte mux configuration bitstring
    :raises: ValueError: if channel  is out of bounds.

    """

    if channel < 0 or channel > 15:
        raise ValueError("Not a valid MUX channel")
    data = (channel << 1) | int(enable)
    return data
