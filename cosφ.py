import numpy as np
import matplotlib.pyplot as plt

# Constants
C = 16e-6        # Capacitance in farads (F)
R = 8e-3         # Resistance in ohms (Ω)
L = 90.3e-12     # Inductance in henries (H)

# Frequency range (logarithmic scale for a broad view)
frequencies = np.logspace(3, 10, 500)  # from 1 kHz to 10 GHz
omega = 2 * np.pi * frequencies           # Angular frequency (rad/s)

# Calculate cos(phi) as a function of frequency
numerator = C * R
denominator = np.sqrt((C * R) ** 2 + (C * omega * L) ** 2)
cos_phi = numerator / denominator

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies, cos_phi)
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.legend()
plt.show()