# Ejercicio 3h:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (-s^2) / (s^2 + 333s + 11000000)

from scipy import signal
from helpers import plot_all

h = signal.lti([-1, 0, 0], [1, 333, 11e6])

plot_all(h)
