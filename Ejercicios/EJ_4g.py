# Ejercicio 4g:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de un circuito con la siguiente función de transferencia:
# H(s) = 1000 (s + 1000) / (s(s + 10)(s + 100))

from scipy import signal
from helpers import plot_all

h = signal.lti([-1e3], [0, -10, -100], 1e3)

plot_all(h)
