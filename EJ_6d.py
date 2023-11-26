from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-1], [-1/100, -10], 10)

plot(sys)
