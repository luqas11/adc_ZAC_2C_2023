# Ejercicio 3o:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = -1 ((s - 1000)(s - 1000)) / ((s + 1000)(s + 1000))

from scipy import signal
from helpers import plot_all

h = signal.lti([1e3, 1e3], [-1e3, -1e3], -1)

plot_all(h)
