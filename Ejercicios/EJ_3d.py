# Ejercicio 3d:
# Determinar el diagrama de Bode de módulo y fase y las respuestas al escalón y al impulso de los circuitos con las siguientes funciones de transferencia:
# H1(s) = (40s^2) / (21s^2 + 2s + 21)
# H2(s) = (40) / (21s^2 + 2s + 21)
# H3(s) = (-40s) / (21s^2 + 2s + 21)
# H4(s) = (-190000s) / (s^2 + 952s + 100000000)

from scipy import signal
from helpers import plot_all

h1 = signal.lti([40, 0, 0], [21, 2, 21])
h2 = signal.lti([40], [21, 2, 21])
h3 = signal.lti([-40, 0], [21, 2, 21])
h4 = signal.lti([-190e3, 0], [1, 952, 100e6])

plot_all(h1)
plot_all(h2)
plot_all(h3)
plot_all(h4)
