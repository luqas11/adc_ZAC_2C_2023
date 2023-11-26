from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([2e3, 600e3, 0], [1, 2540, 114.4e3, 36e6])

plot(sys)
