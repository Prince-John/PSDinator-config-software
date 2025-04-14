"""

    Setup script and utility functions to load custom waveforms into the in bulit AFG for MDO3000 series scopes.
    Uses Beta commands to set up signals with modified triggering settings.

"""
from time import sleep

import numpy as np

# AFG:RUNMode BURST
# AFG:TRIGger:COUnt 1
# AFG:TRIGger:INTerval 1.5e-3
# AFG:OUTPut:STATE 1
# interrupt

import sys

from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.drivers import MDO3K
from src.chipboard_configuration_software.uart_link.utils import print_with_bars


def generate_test_square_pulse(amplitude, period, cycles):
    sample_interval_ns = 0.4e-9
    total_points = int(period * cycles / sample_interval_ns)

    time_series = np.linspace(0, period * cycles, total_points)
    pulse = np.zeros_like(time_series)
    for i in range(cycles):
        pulse[int((i * period / sample_interval_ns) + (period / (2 * sample_interval_ns))):int(
            (i * period / sample_interval_ns) + (period / sample_interval_ns))] = 1

    return time_series, ",".join(f"{value:.6e}" for value in pulse)


if __name__ == "__main__":

    try:

        with DeviceManager(verbose=True) as dm:
            dm.visa_library = PYVISA_PY_BACKEND
            scope: MDO3K = dm.add_scope("10.229.115.11")
            print_with_bars("Connected to Scope, square pulse generating utility")

            t, pulse_data = generate_test_square_pulse(0.5, 40e-9, 1)

            input()
            scope.write("AFG:OUTPut:STATE 0")
            scope.write("AFG: OUTPut:LOAd: IMPEDance FIFty")
            scope.write("AFG:RUNMode BURST")
            scope.write("AFG:TRIGger:COUnt 1")
            sleep(1)
            scope.write(f"AFG:ARBitrary:EMEM:POINTS:ENCdg ASCii")
            scope.write(f"AFG:ARBitrary:EMEM:POINTS {pulse_data}")
            sleep(3)

            scope.write("AFG:OUTPut:STATE 1")
            sleep(2)
            scope.write(f"AFG: PERIod {t[-1]}")


    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
