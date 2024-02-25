# Ejercicio 6d:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 10 (s + 1) / ((s + 0.01)(s + 10))

from scipy import signal
from helpers import plot_all

h = signal.lti([-1], [-1/100, -10], 10)

plot_all(h)
