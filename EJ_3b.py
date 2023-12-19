from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([0, -100e3], [-1e6, -1e3, -1e3], 1e6)

plot(h)
