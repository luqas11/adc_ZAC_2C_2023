from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-10000, -100], [-5000, -200], -1)

plot(sys)