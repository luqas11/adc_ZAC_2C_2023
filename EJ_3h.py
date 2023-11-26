from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-1, 0, 0],[1, 333, 11e6])

plot(sys)
