from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([-50, 0, 0], [1, 100, 1e6])

plot(h)
