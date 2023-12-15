from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0, -5e3], [-10e3, -10e3, -10e3], -20e3)

plot(sys)
