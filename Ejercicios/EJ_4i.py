# Ejercicio 4i:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 0.0001 ((s + 1)(s + 10000)) / (s^2 + s + 100)

from scipy import signal
from helpers import plot_all
import numpy as np

h = signal.lti([-1, -10000], [-0.5 + np.emath.sqrt(-99.75), -0.5 - np.emath.sqrt(-99.75)], 1/10000)

plot_all(h)
