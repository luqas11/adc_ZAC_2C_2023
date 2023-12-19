from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([1e3, 1e3], [-1e3, -1e3], -1)

plot(h)
