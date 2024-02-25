# Comparación de diagramas de Bode generados a partir de:
# - El circuito normalizado simulado numéricamente con SciPy
# - El circuito implementado medido en laboratorio

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

w = np.logspace(0, 5, num=1000000)

# Función de transferencia del circuito normalizado
h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])
w2, mag2, phase2 = h2.bode(w)

# Datos de las mediciones de laboratorio
w_measured = [10, 30, 100, 300, 1000, 3000, 10000, 18800]
mag_measured = [-13.8, -2.43, 4.40, 11.1, 4.08, 0.34, -7.13, -10.3]

window_size = 0.5
_, ax = plt.subplots(figsize=(window_size * 16, window_size * 9))

ax.semilogx(w2, mag2, label='$H_{db}$ (normalizado)')
ax.semilogx(w_measured, mag_measured, label='$H_{db}$ (medido)', linewidth=4)
ax.grid()
ax.set(xlabel='Frecuencia (rad/s)', ylabel='Ganancia (dB)')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()
