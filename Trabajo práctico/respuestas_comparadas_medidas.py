import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

w = np.logspace(0, 5, num=1000000)

h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])
w2, mag2, phase2 = h2.bode(w)

w_measure = [10, 30, 100, 300, 1000, 3000, 10000, 18800]
mag_measure = [-13.8, -2.43, 4.40, 11.1, 4.08, 0.34, -7.13, -10.3]

window_size = 0.5
_, ax = plt.subplots(figsize=(window_size * 16, window_size * 9))

ax.semilogx(w2, mag2, label='$H_{db}$ (normalizada)')
ax.semilogx(w_measure, mag_measure, label='$H_{db}$ (medida)', linewidth=4)
ax.grid()
ax.set(xlabel='Frecuencia (rad/s)', ylabel='Ganancia (dB)')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()
