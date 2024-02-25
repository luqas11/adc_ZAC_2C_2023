# Ejercicio 3b:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = -1000000 (s(s + 100000)) / ((s + 1000000)(s + 1000)(s + 1000))

from scipy import signal
from helpers import plot_all

h = signal.lti([0, -100e3], [-1e6, -1e3, -1e3], 1e6)

plot_all(h)
