# Ejercicio 3c:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = (2s/(5RC)) / (s^2 + s/(5RC) + 1/((RC)^2))
# Donde R = 100 y C = 0.000001

from scipy import signal
from helpers import plot_all

R = 100
C = 1e-6

h = signal.lti([2/(5*R*C), 0], [1, 1/(5*R*C), 1/((R*C)**2)])

plot_all(h)
