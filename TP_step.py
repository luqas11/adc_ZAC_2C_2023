import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def step_response(x):
    return 1.94 * np.exp(-20*x) * np.sin(118*x) + 0.714 * np.exp(-20*x) * np.cos(118*x) - 0.714 * np.exp(-2500*x)

_t = np.arange(0.0, 0.5, 1e-6)
_y = step_response(_t)

h = signal.lti([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])
t, y = signal.step(h, T=_t)

window_size = 0.5
_, axs = plt.subplots(ncols=1, nrows=2, figsize=(window_size * 16, window_size * 9))
axs[0].plot(t, y)
axs[0].grid()
axs[1].plot(_t, _y)
axs[1].grid()

plt.show()
