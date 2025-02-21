from ..board_components import delay


def generate_delay_commands(delay_config: dict) -> list[str]:
    """
        This is compliant with build v0.0.4 and sends 18 byte words with only delay values;
    """
    delay_value_word = ""

    for delay_dict in delay_config.values():
        delay_value = delay.generate_delay_word(int(delay_dict["value"]))
        delay_value_word += f'{delay_value:02X}'  # 1 byte per value

    delay_command_string = f'DLY:{delay_value_word}\0'
    return [delay_command_string]
