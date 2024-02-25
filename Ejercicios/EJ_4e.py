# Ejercicio 4e:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 10000000 s^2 / ((s + 1)(s + 100)(s + 100))

from scipy import signal
from helpers import plot_all

h = signal.lti([0, 0], [-1, -100, -100], 10e6)

plot_all(h)
