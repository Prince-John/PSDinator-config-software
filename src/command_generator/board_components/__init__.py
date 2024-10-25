"""
This package houses the interfaces for generating the raw bit strings for the individual ICs present on our chipboard.
The modules in this package do not deal with abstractions needed for functionality.

For instance the PSD delay width configuration requires setting DAC voltages. The `psd.py` module does not provide any
way to access the octal dac.

Ideally this package should not require any access to the configuration dictionary.
"""