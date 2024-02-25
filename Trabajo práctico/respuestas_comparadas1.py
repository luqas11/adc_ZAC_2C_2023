# Comparación de respuestas al escalón de:
# - El circuito teórico simulado numéricamente con SciPy
# - El circuito normalizado simulado numéricamente con SciPy

import matplotlib.pyplot as plt
from scipy import signal

# Función de transferencia del circuito teórico
h1 = signal.TransferFunction([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])

# Función de transferencia del circuito normalizado
h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])

window_size = 0.5
_, ax = plt.subplots(nrows=2, ncols=1, figsize=(window_size * 16, window_size * 9))

t1, y1 = h1.impulse(N=100000)
t2, y2 = h2.impulse(N=100000)

ax[0].plot(t1, y1, label='$v_o$ (teórico)')
ax[0].plot(t2, y2, label='$v_o$ (normalizado)')
ax[0].grid()
ax[0].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[0].legend()
ax[0].set_title('Respuesta al impulso')

t1, y1 = h1.step(N=100000)
t2, y2 = h2.step(N=100000)

ax[1].plot(t1, y1, label='$v_o$ (teórico)')
ax[1].plot(t2, y2, label='$v_o$ (normalizado)')
ax[1].grid()
ax[1].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[1].legend()
ax[1].set_title('Respuesta al escalón')

plt.tight_layout()
plt.show()
