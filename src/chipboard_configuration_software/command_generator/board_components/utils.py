from __future__ import annotations

import re
from typing import Union, List


def bit_append_left(initial_bits: int, additional_bits: Union[int, List[int]], final_bit_width: int = None,
                    initial_word_length: int | list[int] = None, print_debug=False) -> int:
    """
    Appends the additional bits to the left of initial bits, optionally restricts max word bit width.

    :param print_debug: Debug Print option
    :param initial_bits: The starting bit sequence as an integer.
    :param additional_bits: The bits to append to the left of the `initial_bits`, can be single int or a list of ints.
    :param final_bit_width: Optional; If provided, limits the result to this many bits.
    :param initial_word_length:Optional; If provided, enforces bit widths of initial word(s) by padding zeros.

    :return: The combined bit sequence as an integer
    """
    if isinstance(additional_bits, int):
        additional_bits_list = [additional_bits]
    else:
        additional_bits_list = additional_bits

    if isinstance(initial_word_length, int):
        initial_word_length = [initial_word_length]

    extended_word = initial_bits
    offset = 0
    if initial_word_length is not None:
        for additional_bits, initial_word_length in zip(additional_bits_list, initial_word_length):
            offset += initial_word_length
            extended_word = (additional_bits << offset) | extended_word

            if print_debug:
                print(f"extended word: {extended_word:0b},\n "
                      f"with additional bits  = {additional_bits:0b},"
                      f"offset = {offset}, current word length = {extended_word.bit_length()} "
                      f"initial_word_length = {initial_word_length}")
    else:
        for additional_bits in additional_bits_list:
            offset += extended_word.bit_length()
            extended_word = (additional_bits << offset) | extended_word

    if final_bit_width is not None:
        extended_word = extended_word & ((1 << final_bit_width) - 1)

    return extended_word


def sanitize_resistance_string(resistance_str: str) -> int:
    cleaned_str = re.sub(r'[,\sΩ]', '', resistance_str)  # REGEX to Remove commas, ohm symbols, and spaces

    try:
        return int(cleaned_str)
    except ValueError:
        raise ValueError(f"Invalid input: {resistance_str}")



def apply_number(configuration, number, start_bit, length):
    """Set `length` bits starting from `start_bit` to represent `number`."""
    mask = (1 << length) - 1  # Create a mask of `length` bits
    number &= mask  # Ensure `number` fits in the specified length
    configuration &= ~(mask << start_bit)  # Clear the target bits
    configuration |= (number << start_bit)  # Set the target bits to `number`
    return configuration


def toggle_bit(configuration, bit_position):
    """Toggle the bit at the specified position in the configuration byte."""
    return configuration ^ (1 << bit_position)
