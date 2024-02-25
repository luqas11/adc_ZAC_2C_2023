import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

h1 = signal.TransferFunction([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])
h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])

window_size = 0.5
_, ax = plt.subplots(nrows=3, ncols=1, figsize=(window_size * 16, window_size * 12))

w = 1
t = np.linspace(0, 10*np.pi/w, num=10000)
u = signal.square(w*t)
t1, y1, _ = signal.lsim(h1, U=u, T=t)
t2, y2, _ = signal.lsim(h2, U=u, T=t)

ax[0].plot(t1, y1, label='$v_o$ (original)')
ax[0].plot(t2, y2, label='$v_o$ (normalizada)')
ax[0].plot(t, u, label='$v_i$')
ax[0].grid()
ax[0].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[0].legend(loc='upper right')
ax[0].set_title('Frecuencia = 1rad/s')

w = 100
t = np.linspace(0, 10*np.pi/w, num=10000)
u = signal.square(w*t)
t1, y1, _ = signal.lsim(h1, U=u, T=t)
t2, y2, _ = signal.lsim(h2, U=u, T=t)

ax[1].plot(t1, y1, label='$v_o$ (original)')
ax[1].plot(t2, y2, label='$v_o$ (normalizada)')
ax[1].plot(t, u, label='$v_i$')
ax[1].grid()
ax[1].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[1].legend(loc='upper right')
ax[1].set_title('Frecuencia = 100rad/s')

w = 1000
t = np.linspace(0, 10*np.pi/w, num=10000)
u = signal.square(w*t)
t1, y1, _ = signal.lsim(h1, U=u, T=t)
t2, y2, _ = signal.lsim(h2, U=u, T=t)

ax[2].plot(t1, y1, label='$v_o$ (original)')
ax[2].plot(t2, y2, label='$v_o$ (normalizada)')
ax[2].plot(t, u, label='$v_i$')
ax[2].grid()
ax[2].set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax[2].legend(loc='upper right')
ax[2].set_title('Frecuencia = 1000rad/s')

plt.tight_layout()
plt.show()
