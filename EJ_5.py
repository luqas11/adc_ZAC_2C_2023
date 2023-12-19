from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([0], [-50, -50, -50], 12500)

plot(h)
