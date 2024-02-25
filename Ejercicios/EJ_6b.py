# Ejercicio 6b:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 10 s / ((s + 100)(s + 1000))

from scipy import signal
from helpers import plot_all

h = signal.lti([0], [-100, -1e3], 10)

plot_all(h)
