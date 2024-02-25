# Respuesta al escalón del circuito teórico calculada analíticamente.

import matplotlib.pyplot as plt
import numpy as np

# Función de respuesta calculada analíticamente
t = np.linspace(0.0, 0.5, num=10000)
y = 1.94 * np.exp(-20*t) * np.sin(118*t) + 0.714 * np.exp(-20*t) * np.cos(118*t) - 0.714 * np.exp(-2500*t)

window_size = 0.5
_, ax = plt.subplots(figsize=(window_size * 16, window_size * 9))

ax.plot(t, y)
ax.grid()
ax.set(xlabel='Tiempo (s)', ylabel='Tensión (V)')

plt.show()
