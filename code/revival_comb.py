import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
tau_C = 140e-6  # 140 µs
t_max = 1.5e-3  # 1.5 ms
dt = 1e-6       # 1 µs
width = 10e-6   # Gaussian width

t = np.arange(0, t_max, dt)
MP = tau_C
revival_times = np.arange(0, t_max, MP)

# Time-Lattice fidelity (Gaussian revivals)
def gaussian(t, center, width):
    return np.exp(-((t - center)**2) / (2 * width**2))

fidelity_lattice = np.sum([gaussian(t, tau, width) for tau in revival_times], axis=0)
fidelity_lattice /= np.max(fidelity_lattice)

# 1D exponential decay
fidelity_1d = np.exp(-t / tau_C)

# Export data
df = pd.DataFrame({
    'time_ms': t * 1e3,
    'fidelity_lattice': fidelity_lattice,
    'fidelity_1d': fidelity_1d
})
df.to_csv('revival_comb_data.csv', index=False)

# Plot
plt.figure(figsize=(14, 6))
plt.plot(t * 1e3, fidelity_lattice, color='blue', linewidth=2, label='Time-Lattice')
plt.plot(t * 1e3, fidelity_1d, color='orange', linestyle='--', linewidth=2, label='1-D time')

# Peak markers and annotations
plt.scatter(revival_times * 1e3, np.ones_like(revival_times), color='blue', s=25, label='Revival peaks')

for tau in revival_times:
    if tau < 0.75e-3:
        plt.text(tau * 1e3, 0.02, f'{int(tau * 1e6)} µs', ha='center', fontsize=8)
    plt.axvline(tau * 1e3, color='gray', linestyle=':', linewidth=0.5, alpha=0.4)

# Styling
plt.title(r'Revival Comb: $\tau_C = MP = 140\,\mu s$', fontsize=16)
plt.xlabel(r'Time (ms)', fontsize=14)
plt.ylabel(r'Fidelity', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=12)

# Decay formula
plt.text(1.05, 0.9, r'$f(t) = e^{-t/\tau_C}$', transform=plt.gca().transAxes, fontsize=12)

plt.tight_layout()
plt.savefig('revival_comb_plot_final.png', dpi=300)
plt.show()