# Ejercicio 3k:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (s(s + 5000)) / ((s + 10000)(s + 10000)(s + 10000))

from scipy import signal
from helpers import plot_all

h = signal.lti([0, -5e3], [-10e3, -10e3, -10e3], -20e3)

plot_all(h)
