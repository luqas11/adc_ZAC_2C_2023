from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-100, -10], [-1000, -1], 1000)

plot(sys)
