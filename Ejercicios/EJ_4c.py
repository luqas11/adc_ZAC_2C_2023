# Ejercicio 4c:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 100000 s / ((s + 1000)(s + 1/10))

from scipy import signal
from helpers import plot_all

h = signal.lti([0], [-1000, -1/10], 100e3)

plot_all(h)
