from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-66.7e3, 0],[1, 1.33e3, 100e6])

plot(sys)
