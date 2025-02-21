import numpy as np
import matplotlib.pyplot as plt


def generate_exponential_tail_pulse(amplitude=1.0, rise_time=10.0, fall_time=100.0, sampling_rate=250_000_000,
                                    delay=50.0, max_points=128_000, max_sample_rate=250_000_000):
    """
    Generate an exponential tail pulse with a configurable delay while respecting hardware constraints.

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

    start_index = int(delay / sample_interval)
    rise_end_index = min(start_index + int(rise_time / sample_interval), total_samples)
    fall_end_index = min(rise_end_index + int(fall_time / sample_interval), total_samples)

    # Linear rise
    pulse[start_index:rise_end_index] = np.linspace(0, amplitude, rise_end_index - start_index)

    # Exponential fall
    pulse[rise_end_index:fall_end_index] = amplitude * np.exp(
        -(t[rise_end_index:fall_end_index] - t[rise_end_index]) / (tau * 1e-9))

    return t, ",".join(f"{value:.6e}" for value in pulse)


def plot_pulse(t, pulse):
    """Plot the generated exponential tail pulse."""
    plt.figure(figsize=(8, 4))
    plt.plot(t, pulse, label='Exponential Tail Pulse')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Exponential Tail Pulse')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    while True:
        try:
            amplitude = float(input("Enter amplitude: "))
            rise_time = float(input("Enter rise time (ns): "))
            fall_time = float(input("Enter fall time (ns): "))
            delay = float(input("Enter delay (ns): "))

            t, pulse_data = generate_exponential_tail_pulse(amplitude, rise_time, fall_time, delay= delay)
            plot_pulse(t, np.array(pulse_data.split(","), dtype=float))

        except ValueError as e:
            print(f"Error: {e}")

        cont = input("Do you want to generate another pulse? (y/n): ")
        if cont.lower() != 'y':
            break
