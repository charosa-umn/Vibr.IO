import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""Constants"""
umax = 0.43         # maximum growth rate
Ks = 1.2            # half-velocity constant
Yxs = 1.21          # yield coefficient for biomass/substrate


def f(y, t, params):
    X, S = y      # unpack current values of y
    umax, Ks, Yxs = params  # unpack parameters
    derivs = [X*umax*S/(Ks+S),      # list of dy/dt=f functions
             -X*umax*S/(Yxs*(Ks+S))]

    return derivs


def solve(X0, S0, tStop, tInc):
    params = [umax, Ks, Yxs]
    y0 = [X0, S0]

    t = np.arange(0., tStop, tInc)

    psoln = odeint(f, y0, t, args=(params,))
    return t, psoln

    # # Plot X as a function of time
    # fig = plt.figure(1, figsize=(8, 8))
    # ax1 = fig.add_subplot(311)
    # ax1.plot(t, psoln[:, 0])
    # ax1.set_xlabel('Time (hrs)')
    # ax1.set_ylabel('X (od600)')
    #
    # # Plot S as a function of time
    # ax2 = fig.add_subplot(312)
    # ax2.plot(t, psoln[:, 1])
    # ax2.set_xlabel('Time (hrs)')
    # ax2.set_ylabel('S (g)')
    #
    # plt.tight_layout()
    # plt.show()
