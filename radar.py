# ==========================================================
# Radar Signal Detection Using FFT (Simulation)
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# STEP 1 : Define Radar Parameters
# ==========================================================

fs = 1000                 # Sampling frequency (Hz)
T = 1                     # Signal duration (seconds)
N = fs * T                # Number of samples

t = np.linspace(0, T, N, endpoint=False)

f_signal = 50             # Radar transmitted frequency (Hz)

# ==========================================================
# STEP 2 : Generate Transmitted Radar Signal
# ==========================================================

tx_signal = np.sin(2 * np.pi * f_signal * t)

# ==========================================================
# STEP 3 : Simulate Target Reflection
# Introduce delay to represent reflected signal
# ==========================================================

delay_samples = 40

rx_signal = np.roll(tx_signal, delay_samples)

# ==========================================================
# STEP 4 : Add Noise
# ==========================================================

noise = 0.5 * np.random.randn(N)

rx_noisy = rx_signal + noise

# ==========================================================
# STEP 5 : Apply FFT
# ==========================================================

fft_output = np.fft.fft(rx_noisy)

fft_magnitude = np.abs(fft_output)

freq = np.fft.fftfreq(N, 1/fs)

# ==========================================================
# STEP 6 : Detect Peak Frequency
# ==========================================================

half_N = N // 2

peak_index = np.argmax(fft_magnitude[:half_N])

peak_frequency = freq[peak_index]

peak_amplitude = fft_magnitude[peak_index]

print("===================================")
print("Radar Signal Detection Using FFT")
print("===================================")

print(f"Detected Peak Frequency : {peak_frequency:.2f} Hz")
print(f"Peak Amplitude          : {peak_amplitude:.2f}")

# ==========================================================
# STEP 7 : Estimate Target Distance
# ==========================================================

c = 3e8                    # Speed of light (m/s)

time_delay = delay_samples / fs

distance = (c * time_delay) / 2

print(f"Estimated Target Distance : {distance:.2f} meters")

# ==========================================================
# STEP 8 : Plot Results
# ==========================================================

plt.figure(figsize=(12,8))

# ----------------------------------------------------------
# Transmitted Signal
# ----------------------------------------------------------

plt.subplot(3,1,1)

plt.plot(t, tx_signal)

plt.title("Transmitted Radar Signal")

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.grid(True)

# ----------------------------------------------------------
# Received Noisy Signal
# ----------------------------------------------------------

plt.subplot(3,1,2)

plt.plot(t, rx_noisy)

plt.title("Received Signal with Noise")

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.grid(True)

# ----------------------------------------------------------
# FFT Spectrum
# ----------------------------------------------------------

plt.subplot(3,1,3)

plt.plot(freq[:half_N], fft_magnitude[:half_N])

plt.title("FFT Frequency Spectrum")

plt.xlabel("Frequency (Hz)")

plt.ylabel("Magnitude")

plt.grid(True)

plt.tight_layout()

plt.show()

# ==========================================================
# END OF PROJECT
# ==========================================================