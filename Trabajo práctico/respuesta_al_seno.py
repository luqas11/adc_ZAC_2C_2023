# Respuesta a una señal senoidal de 1000rad/s del circuito teórico calculada analíticamente.

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 0.3, num=10000)
y = 0.635 * np.sin(1000*t) - 0.464 * np.cos(1000*t) + 0.218 * np.exp(-20*t) * np.cos(118*t) - 0.126 * np.exp(-20*t) * np.sin(118*t) + 0.246 * np.exp(-2500*t)

window_size = 0.5
_, ax = plt.subplots(figsize=(window_size * 16, window_size * 9))

ax.plot(t, y)
ax.grid()
ax.set(xlabel='Tiempo (s)', ylabel='Tensión (V)')

plt.show()
