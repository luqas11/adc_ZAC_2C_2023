import matplotlib.pyplot as plt
from matplotlib import axes
from scipy import signal
import numpy as np

PLOT_RESOLUTION = 100000

def plot_all(sys: signal.lti):
    """
    Plotea los diagramas de Bode de módulo y fase y las respuestas al impulso y al escalón
    de un sistema LTI dado.

    Parameters
    ----------
    sys : signal.lti
        Sistema LTI a plotear
    """
    w, mag, phase = sys.bode(n=PLOT_RESOLUTION)
    ts, ys = sys.step(N=PLOT_RESOLUTION)
    ti, yi = sys.impulse(N=PLOT_RESOLUTION)

    window_size = 0.8
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(window_size * 16, window_size * 9), tight_layout=True)

    ax1.semilogx(w, mag)
    ax1.grid()
    add_zp(sys, ax1)
    ax1.set_xlabel("Frecuencia [rad/s]")
    ax1.set_ylabel("Amplitud [dB]")
    ax1.set_title('Bode')

    ax3.semilogx(w, phase)
    ax3.grid()
    add_zp(sys, ax3)
    ax3.set_xlabel("Frecuencia [rad/s]")
    ax3.set_ylabel("Fase [°]")
    ax3.set_title('Fase')

    ax2.plot(ts, ys)
    ax2.grid()
    ax2.set_xlabel("Tiempo [s]")
    ax2.set_ylabel("Tensión [V]")
    ax2.set_title('Respuesta al escalón')

    ax4.plot(ti, yi)
    ax4.grid()
    ax4.set_xlabel("Tiempo [s]")
    ax4.set_ylabel("Tensión [V]")
    ax4.set_title('Respuesta al impulso')

    plt.show()

def add_zp(sys: signal.lti, ax: axes.Axes):
    """
    Agrega al gráfico indicado los polos y ceros de un sistema LTI dado, en forma de líneas verticales.

    Si los polos o ceros son complejos, utiliza su módulo.

    Parameters
    ----------
    sys : signal.lti
        Sistema LTI para el cual plotear los polos y ceros
    ax : axes.Axes
        Gráfico sobre el cual plotear
    """
    ax.axvline(color='r', linewidth=1, linestyle="--", label="Ceros")
    for z in sys.zeros:
        _z = -z
        if (type(_z) == np.complex128):
            _z = np.abs(_z)
        ax.axvline(x=_z, color='r', linewidth=1, linestyle="--")

    ax.axvline(color='b', linewidth=1, linestyle="--", label="Polos")
    for p in sys.poles:
        _p = -p
        if (type(_p) == np.complex128):
            _p = np.abs(_p)
        ax.axvline(x=_p, color='b', linewidth=1, linestyle="--")

    ax.legend()
