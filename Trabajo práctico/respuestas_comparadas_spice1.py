import matplotlib.pyplot as plt
from scipy import signal
from helpers import read_csv

t_spice, y_spice = read_csv(columns_names=["Tiempo", "Tension"], filename='escalon_spice')

h1 = signal.TransferFunction([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])
h2 = signal.TransferFunction([2e3, 667e3, 0], [1, 2540, 114e3, 34.3e6])

window_size = 0.5
fig, ax = plt.subplots(figsize=(window_size * 16, window_size * 9))

t1, y1 = h1.step(N=100000)
t2, y2 = h2.step(N=100000)

ax.plot(t1, y1, label='$v_o$ (original)')
ax.plot(t2, y2, label='$v_o$ (normalizada)')
ax.plot(t_spice, y_spice, label='$v_o$ (LTspice)')
ax.grid()
ax.set(xlabel='Tiempo (s)', ylabel='Tensión (V)')
ax.legend()
ax.set_title('Respuesta al escalón')

plt.tight_layout()
plt.show()
