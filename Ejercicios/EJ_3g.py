# Ejercicio 3f:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (-50s^2) / (s^2 + 100s + 1000000)

from scipy import signal
from helpers import plot_all

h = signal.lti([-50, 0, 0], [1, 100, 1e6])

plot_all(h)
