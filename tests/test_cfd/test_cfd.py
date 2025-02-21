from unittest import TestCase


from src.chipboard_configuration_software.command_generator.board_components import cfd


class Test(TestCase):
    def test_get_mode_1_words(self):
        agnds = ["1.36 V", "1.43 V", "1.49 V", "1.56 V", "1.63 V", "1.69 V", "1.77 V", "1.84 V"]

        for agnd in agnds:
            add_mode, data = cfd.get_mode_1_words("disabled", agnd, "50")
            print("N")
            print(f"CFD:WRT:{add_mode:02X}{data:02X}")
