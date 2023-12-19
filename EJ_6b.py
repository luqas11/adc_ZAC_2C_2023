from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0], [-100, -1e3], 10)

plot(sys)
