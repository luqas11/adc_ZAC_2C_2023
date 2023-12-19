from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

h = signal.lti([0], [-10, -10.2, -990], 1)

plot(h)
