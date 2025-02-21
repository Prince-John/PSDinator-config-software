from ..board_components import mux


def generate_mux_commands(mux_config: dict) -> str:
    try:
        mux_word = mux.generate_mux_word(int(mux_config["channel"]), (True if mux_config["enable"] == "True" else False))
    except ValueError as e:
        print(f"ERROR in MUX config, command not generated: {e}")
        return ""

    mux_command_string = f'MUX:{mux_word:02X}\0'

    return [mux_command_string]
