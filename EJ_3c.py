from scipy import signal
import sys
sys.path.append('././modules')
from plotting import plot

R = 100
C = 1e-6

sys = signal.lti([2/(5*R*C), 0], [1, 1/(5*R*C), 1/((R*C)**2)])

plot(sys)
