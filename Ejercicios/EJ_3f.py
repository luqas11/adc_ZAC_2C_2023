# Ejercicio 3f:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (-2s^2 - 2) / (s^2 + s + 2)

from scipy import signal
from helpers import plot_all

h = signal.lti([-2, 0, -2], [1, 1, 2])

plot_all(h)
