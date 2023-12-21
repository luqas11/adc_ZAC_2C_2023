from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([200e-6, 1.1], [100e-6, 1])

plot(h)
