# Comparación de diagramas de Bode de:
# - El circuito teórico simulado numéricamente con SciPy
# - El circuito normalizado simulado numéricamente con SciPy

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

w = np.logspace(0, 4, num=1000000)

# Función de transferencia del circuito teórico
h1 = signal.TransferFunction([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])
w1, mag1, phase1 = h1.bode(w)

# Función de transferencia del circuito normalizado
h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])
w2, mag2, phase2 = h2.bode(w)

window_size = 0.5
_, ax = plt.subplots(nrows=2, ncols=1, figsize=(window_size * 16, window_size * 9))

ax[0].semilogx(w1, mag1, label='$H_{db}$ (teórico)')
ax[0].semilogx(w2, mag2, label='$H_{db}$ (normalizado)')
ax[0].grid()
ax[0].set(xlabel='Frecuencia (rad/s)', ylabel='Ganancia (dB)')
ax[0].legend(loc='upper left')
ax[0].set_title('Diagrama de módulo')

ax[1].semilogx(w1, phase1, label='$φ_{deg}$ (teórico)')
ax[1].semilogx(w2, phase2, label='$φ_{deg}$ (normalizado)')
ax[1].grid()
ax[1].set(xlabel='Frecuencia (rad/s)', ylabel='Fase (°)')
ax[1].legend(loc='upper left')
ax[1].set_title('Diagrama de fase')

plt.tight_layout()
plt.show()
