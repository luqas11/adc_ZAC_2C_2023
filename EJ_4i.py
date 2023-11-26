import numpy as np
from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

sys = signal.lti([-1, -10000], [-0.5 + np.emath.sqrt(-99.75), -0.5 - np.emath.sqrt(-99.75)], 1/10000)

plot(sys)
