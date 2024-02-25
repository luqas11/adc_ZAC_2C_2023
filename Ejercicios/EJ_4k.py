# Ejercicio 4k:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 1 s / ((s + 10)(s^2 + 1000s + 10100))

from scipy import signal
from helpers import plot_all

h = signal.lti([0], [-10, -10.2, -990], 1)

plot_all(h)
