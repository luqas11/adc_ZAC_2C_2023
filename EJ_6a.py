from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([-5e3, -20e3], [-10e3, -10e3], 1)

plot(h)
