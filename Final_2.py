from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot
import numpy as np

h = signal.lti([np.sqrt(10)], [1/40e3, 200/40e3, 1])

plot(h)
