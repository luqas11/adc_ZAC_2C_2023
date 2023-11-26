from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([0], [-50, -50, -50], 12500)

plot(sys)
