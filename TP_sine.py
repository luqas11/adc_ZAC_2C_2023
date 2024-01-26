import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def sine_response(x):
    return 0.635 * np.sin(1000*x) - 0.464 * np.cos(1000*x) + 0.218 * np.exp(-20*x) * np.cos(118*x) - 0.126 * np.exp(-20*x) * np.sin(118*x) + 0.246 * np.exp(-2500*x)

t = np.arange(0.0, 0.3, 1e-6)
y = sine_response(t)

fig, ax = plt.subplots()
ax.plot(t, y)
ax.grid()

plt.show()
