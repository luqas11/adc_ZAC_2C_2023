from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-1, 0, -100], [1, 1, 100])

plot(sys)
