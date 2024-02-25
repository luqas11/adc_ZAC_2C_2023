# Ampliación del comportamiento de la respuesta a la señal cuadrada de 1rad/s del circuito normalizado simulado numéricamente con SciPy.

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

h = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])

window_size = 0.5
_, ax = plt.subplots(nrows=1, ncols=2, figsize=(window_size * 16, window_size * 9))

w = 1
t = np.linspace(0, 3*np.pi/w, num=10000)
u = signal.square(w*t)
t, y, _ = signal.lsim(h, U=u, T=t)

ax[0].plot(t, y)
ax[0].grid()
ax[0].set_xlim(3, 3.5)
ax[0].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[0].set_title('Centrado en t = 3.14s')

w = 1
t = np.linspace(0, 3*np.pi/w, num=10000)
u = signal.square(w*t)
t, y, _ = signal.lsim(h, U=u, T=t)

ax[1].plot(t, y)
ax[1].grid()
ax[1].set_xlim(6.1, 6.7)
ax[1].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[1].set_title('Centrado en t = 6.28s')

plt.tight_layout()
plt.show()
