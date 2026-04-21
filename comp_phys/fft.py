"""
Fast Fourier Transform (FFT)

This module implements the Cooley-Tukey Fast Fourier Transform algorithm.
In physics, signals are often recorded in the "time domain" (e.g., amplitude vs time).
A Fourier Transform converts this into the "frequency domain" (amplitude vs frequency),
allowing us to see which frequencies make up the signal.

A direct Discrete Fourier Transform (DFT) takes O(N^2) operations, which is
too slow for large datasets.
The FFT takes O(N log N) operations by recursively dividing the signal into
even and odd indices. This is widely considered one of the most important
algorithms of the 20th century!

Note: We use Python's built-in `complex` numbers (e.g., 1 + 2j) and `cmath`
for the complex exponential.
"""

import cmath
import math

def fft(x):
    """
    Computes the 1D Fast Fourier Transform (FFT) of a complex array.

    Logic (Cooley-Tukey Algorithm):
    1. If the array size is 1, the FFT is just the array itself. (Base case)
    2. Otherwise, split the array into two halves:
       - 'even': The elements at indices 0, 2, 4...
       - 'odd': The elements at indices 1, 3, 5...
    3. Recursively compute the FFT of both halves.
    4. Combine the results using the "Twiddle Factors" (complex exponentials).

    CRITICAL REQUIREMENT:
    The length of the input array 'x' MUST be a power of 2 (e.g., 2, 4, 8, 16, 1024...).
    If it is not, this specific recursive algorithm will fail or give wrong results.
    In practice, we "zero-pad" signals to reach a power of 2.

    Args:
        x (list of complex/floats): The input signal in the time domain.

    Returns:
        list of complex: The frequency domain representation.
    """
    N = len(x)

    # Base case of the recursion
    if N <= 1:
        return x

    # Check if N is a power of 2 (a quick bitwise check)
    if N & (N - 1) != 0:
        raise ValueError("The length of the input array must be a power of 2.")

    # Split the array into even and odd parts
    # List slicing syntax: x[start:stop:step]
    even = fft(x[0::2])
    odd = fft(x[1::2])

    # Prepare the output array, initialized with zeros (as complex numbers)
    T = [0.0j] * N

    # Combine the recursive results
    # The math formula requires a "Twiddle Factor" W_N = exp(-2j * pi * k / N)
    for k in range(N // 2):
        # Calculate the twiddle factor for this frequency bin
        # cmath.exp computes e^(x + iy)
        twiddle = cmath.exp(-2j * math.pi * k / N) * odd[k]

        # The Cooley-Tukey butterfly operations
        T[k] = even[k] + twiddle
        T[k + N // 2] = even[k] - twiddle

    return T


def ifft(X):
    """
    Computes the 1D Inverse Fast Fourier Transform (IFFT).

    Logic:
    The inverse Fourier transform takes us back from Frequency Domain to Time Domain.
    Mathematically, the IFFT is almost identical to the FFT, but with two small changes:
    1. The sign inside the exponential is positive instead of negative.
    2. We must divide the final result by N.

    A neat trick to implement this without writing a whole new recursive function is to:
    1. Take the complex conjugate of the input.
    2. Run the normal FFT.
    3. Take the complex conjugate of the result.
    4. Divide by N.

    Args:
        X (list of complex): The input signal in the frequency domain.

    Returns:
        list of complex: The original time domain signal.
    """
    N = len(X)

    # 1. Conjugate the input
    X_conj = [x.conjugate() for x in X]

    # 2. Run normal FFT
    t_conj = fft(X_conj)

    # 3 & 4. Conjugate the result and divide by N
    t = [(val.conjugate() / N) for val in t_conj]

    return t


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    print("--- Fast Fourier Transform Examples ---")

    # Example: A simple signal with 8 data points (power of 2)
    # Let's say it's a DC signal (constant value 1.0 everywhere)
    time_signal = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    print("Original Time Domain Signal:")
    print(f"  {time_signal}")

    # Compute the FFT
    freq_signal = fft(time_signal)

    print("\nFrequency Domain (FFT Output):")
    for i, val in enumerate(freq_signal):
        # We round tiny floating point errors to 0 for cleaner printing
        real_part = round(val.real, 10)
        imag_part = round(val.imag, 10)
        print(f"  Bin {i}: {real_part} + {imag_part}j")

    print("\n(Notice that all the energy is in Bin 0! Bin 0 represents the DC or 'constant')")
    print("(frequency. Since our signal is a flat line, it has 0 frequency. Perfect!)")

    # Let's verify our IFFT can recreate the original signal
    reconstructed = ifft(freq_signal)

    print("\nReconstructed Time Signal (via IFFT):")
    # Taking the real part and rounding
    print(f"  {[round(val.real, 6) for val in reconstructed]}")
    print("(We successfully got back our original 1.0s array!)")
