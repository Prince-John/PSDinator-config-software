from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chipboard_configuration_software.uart_link.middleware import UartMiddleware


def print_with_bars(text: str, symbol: str = '*', border_length: int = 40) -> None:
    """
    Prints the input text with top and bottom borders on the console

    :param border_length: Length of border, default 40
    :param symbol: Border symbol, default *
    :param text: Text string to be printed.
    """
    print("")
    print(symbol * border_length)
    print(text)
    print(symbol * border_length)
    print("")


def connect_to_chipboard_prompt(link: "UartMiddleware") -> None:
    """
    Utility to present a cli prompt to show available UART devices, validate user input and start a middleware
    connection to user choice.

    :param link: UartMiddleware object to prompt for chipboard connection
    :return: None, exits the program with an error code
    """

    try:
        devices = link.get_available_devices()
        device_index = int(input("\n\nEnter the index of the device to connect to: "))
        if 0 <= device_index < len(devices):
            link.connect_to_device(devices[device_index])
        else:
            print("Invalid device index selected.")
            exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)
