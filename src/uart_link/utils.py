def print_with_bars(text: str, symbol: str ='*', border_length: int = 40) -> None:
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