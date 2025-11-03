import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602176634e-19          # Elementary charge in Coulombs
hbar = 1.0545718e-34         # Reduced Planck's constant in Joule-seconds
vf = 1e6                     # Fermi velocity in m/s
kB = 1.380649e-23            # Boltzmann constant in J/K
T = 300                      # Temperature in Kelvin
E0 = 0.2                     # Offset in eV, adjust as needed

# Define the range of Ef (Fermi energy) values, in eV
Vf_range = np.arange(-0.5, 0.501, 0.001)  # Ef values in eV

# Calculate the coefficient outside the logarithm
coeff = 2 * e**2 * kB * T / (np.pi * (hbar * vf)**2)

# Compute Cq for each Ef value (unit: F/m^2)
Cq = coeff * np.log(2 * (1 + np.cosh((Vf_range + E0) * e / (kB * T))))

# Convert Cq to μF/cm^2
Cq_uFcm2 = np.abs(Cq) * 1e6 / 1e4    # (F/m^2) * 1e6(μF/F) / 1e4(cm^2/m^2)

# Plot Cq vs Ef
plt.figure(figsize=(7,5))
plt.plot(Vf_range, Cq_uFcm2, 'r-', linewidth=2)
plt.xlabel('E_F (eV)')
plt.ylabel(r'$C_q$ ($\mu$F/cm$^2$)')
plt.title('Quantum Capacitance $C_q$ vs $E_F$')
plt.grid(True)
plt.tight_layout()
plt.show()
