from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0, 0], [-1, -100, -100], 10e6)

plot(sys)