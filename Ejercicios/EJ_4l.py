# Ejercicio 4l:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (-s^2 + -100) / (s^2 + s + 100)

from scipy import signal
from helpers import plot_all

h = signal.lti([-1, 0, -100], [1, 1, 100])

plot_all(h)
