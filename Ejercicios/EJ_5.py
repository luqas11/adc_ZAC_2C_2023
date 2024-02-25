# Ejercicio 5:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 12500 s / ((s + 50)(s + 50)(s + 50))

from scipy import signal
from helpers import plot_all

h = signal.lti([0], [-50, -50, -50], 12500)

plot_all(h)
