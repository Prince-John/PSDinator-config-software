"""

    Setup script and utility functions to load custom waveforms into the in bulit AFG for MDO3000 series scopes.
    Uses Beta commands to set up signals with modified triggering settings.

"""
from time import sleep
from typing import Tuple

import numpy as np

# AFG:RUNMode BURST
# AFG:TRIGger:COUnt 1
# AFG:TRIGger:INTerval 1.5e-3
# AFG:OUTPut:STATE 1


import sys

from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.drivers import MDO3K
from src.chipboard_configuration_software.uart_link.utils import print_with_bars


def generate_exponential_tail_pulse(amplitude=1.0, rise_time=10.0, fall_time=100.0, sampling_rate=2_500_000_000,
                                    delay=50.0, max_points=131_072, max_sample_rate=2_500_000_000) -> (Tuple, str):
    """
    Generate an exponential tail pulse with a configurable delay and rise time. The decay rate is autoconfigured to be
    fall to 10% of max amplitude within the specified fall time.[ tau = fall_time/5 ]
    This is intended to generate voltage points and times series to be compatible with MDO3000 series inbuilt arbitrary
    AFG.

    Parameters:
        amplitude (float): Peak amplitude of the pulse.
        rise_time (float): Time for the pulse to rise (in ns).
        fall_time (float): Time for the pulse to fall (in ns, approximately 5-6 times tau).
        sampling_rate (int): Number of samples per second (limited by max sample rate).
        delay (float): Time delay before the pulse starts (in ns).
        max_points (int): Maximum number of points allowed.
        max_sample_rate (int): Maximum sampling rate allowed.

    Returns:
        tuple: Time array (in seconds) and a comma-separated list of exponential tail pulse values.
    """
    # Calculate tau from fall time (using 5*tau as approximation for fall time)
    tau = fall_time / 5.0

    # Ensure the sampling rate does not exceed the max allowed value
    sampling_rate = min(sampling_rate, max_sample_rate)

    # Convert sampling rate to samples per ns
    sample_interval = 1e9 / sampling_rate  # Sample interval in ns

    # Ensure the total duration does not exceed the max record length constraint
    max_duration = max_points * sample_interval  # Maximum allowable time span in ns
    if rise_time + fall_time + delay > max_duration:
        raise ValueError(
            f"Total duration (rise_time + fall_time + delay) exceeds max duration {max_duration:.3f} ns allowed by "
            f"sampling rate and max points.")

    total_samples = int((rise_time + fall_time + delay) / sample_interval)
    t = np.linspace(0, (rise_time + fall_time + delay) * 1e-9, total_samples)  # Convert to seconds
    pulse = np.zeros_like(t)

    print(sample_interval)

    start_index = int(delay / sample_interval)
    rise_end_index = min(start_index + int(rise_time / sample_interval), total_samples)
    fall_end_index = max(rise_end_index + int(fall_time / sample_interval), total_samples)

    # Linear rise
    pulse[start_index:rise_end_index] = np.linspace(0, amplitude, rise_end_index - start_index)

    # Exponential fall
    pulse[rise_end_index:fall_end_index] = amplitude * np.exp(
        -(t[rise_end_index:fall_end_index] - t[rise_end_index]) / (tau * 1e-9))

    return t, ",".join(f"{value:.6e}" for value in pulse)


if __name__ == "__main__":

    try:

        with DeviceManager(verbose=True) as dm:
            dm.visa_library = PYVISA_PY_BACKEND
            scope: MDO3K = dm.add_scope("10.229.115.11")
            print_with_bars("Connected to Scope, Exponential Tail pulse generating utility")

            amplitude = float(input("Enter amplitude: "))
            rise_time = float(input("Enter rise time (ns): "))
            fall_time = float(input("Enter fall time (ns): "))
            delay = float(input("Enter delay (ns): "))

            pulse_rate = float(input("Enter pulse interval (ms): "))

            t, pulse_data = generate_exponential_tail_pulse(amplitude, rise_time, fall_time, delay=delay)

            scope.write("AFG:OUTPut:STATE 0")
            scope.write("AFG: OUTPut:LOAd: IMPEDance FIFty")
            scope.write("AFG:RUNMode BURST")
            scope.write("AFG:TRIGger:COUnt 1")
            scope.write(f"AFG:TRIGger:INTerval {pulse_rate}e-3")
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
