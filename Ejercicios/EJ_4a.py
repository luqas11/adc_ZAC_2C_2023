# Ejercicio 4a:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 1000 ((s + 100)(s + 10)) / ((s + 1000)(s + 1))

from scipy import signal
from helpers import plot_all

h = signal.lti([-100, -10], [-1000, -1], 1000)

plot_all(h)
