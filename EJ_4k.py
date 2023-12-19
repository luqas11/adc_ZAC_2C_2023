from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0], [-10, -10.2, -990], 1)

plot(sys)
