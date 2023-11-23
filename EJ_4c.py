from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0], [-1000, -1/10], 100e3)

plot(sys)
