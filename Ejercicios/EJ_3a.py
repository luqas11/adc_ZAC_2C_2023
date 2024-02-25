# Ejercicio 3a:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = -1 ((s + 10000)(s + 100)) / ((s + 5000)(s + 200))

from scipy import signal
from helpers import plot_all

h = signal.lti([-10000, -100], [-5000, -200], -1)

plot_all(h)
