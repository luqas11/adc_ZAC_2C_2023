from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-1e3], [0, -10, -100], 1e3)

plot(sys)
