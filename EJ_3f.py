from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-2, 0, -2],[1, 1, 2])

plot(sys)
