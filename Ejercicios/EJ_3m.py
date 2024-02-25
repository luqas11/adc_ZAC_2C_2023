# Ejercicio 3m:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (-66700s) / (s^2 + 1330s + 100000000)

from scipy import signal
from helpers import plot_all

h = signal.lti([-66.7e3, 0],[1, 1.33e3, 100e6])

plot_all(h)
