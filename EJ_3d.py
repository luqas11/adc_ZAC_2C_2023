from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h1 = signal.lti([40, 0, 0], [21, 2, 21])
h2 = signal.lti([40], [21, 2, 21])
h3 = signal.lti([-40, 0], [21, 2, 21])
h3_10k = signal.lti([-190e3, 0], [1, 952, 100e6])

plot(h1)
plot(h2)
plot(h3)
plot(h3_10k)
