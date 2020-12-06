"""
File that mainly handles the math behind the cell growth modeling for vibrio fischeri
Utilizes code written in parameter_monod_code.m
"""
import numpy as np
from scipy.integrate import odeint

"""Constants"""
umax = 0.43         # maximum growth rate
Ks = 1.2            # half-velocity constant
Yxs = 1.21          # yield coefficient for biomass/substrate
CONV_CONST = 10**8  # An experimental value that converts od600 to nominal cell density for E. coli; an estimate for vibrio fischeri.
NOM_CELL = 10**6    # Value represents x10^6 cells per mL
Kd = 0.43       # first-order death constant


def convert_cell_density(x, to_od600):
    """Converts cell density from od600 to nominal cell density or from nominal cell density to od600"""
    if to_od600:
        # Convert to od600
        x = (x * NOM_CELL) / CONV_CONST
    else:
        # Convert to nominal cell density
        x = (x * CONV_CONST) / NOM_CELL

    return x


def f(y, t, params):
    """A function that does derivatives"""
    X, S = y      # unpack current values of y
    umax, Ks, Yxs = params  # unpack parameters
    derivs = [X*umax*S/(Ks+S),      # list of dy/dt=f functions
             -X*umax*S/(Yxs*(Ks+S))]

    return derivs


def generate_growth(X0, S0, tStop, tInc):
    """
    Generates data points for plots modeling vibrio fischeri growth based on
    X0: initial cell concentration in od600
    S0: initial substrate in grams
    tStop: the time to end the simulation at in hours
    tInc: increment by this value from 0 until tStop
    """
    params = [umax, Ks, Yxs]
    y0 = [X0, S0]

    t = np.arange(0., tStop, tInc)

    psoln = odeint(f, y0, t, args=(params,))

    return t, psoln


def generate_peak(psoln, t):
    cell_d = []
    substrate = []

    for i in range(0, len(psoln) - 1):
        for j in (0, len(psoln[i]) - 1):
            if j == 0:
                cell = psoln[i][j]
                cell_d.append(cell)
            else:
                sub = psoln[i][j]
                substrate.append(sub)

    # select peak as when cell population grows < 1% in a time step
    x1 = cell_d[0]
    residuals = []  # calc difference between x2 and x1
    for i in range(1, len(cell_d)):
        x2 = cell_d[i]
        res = (x2 - x1) / x1
        residuals.append(res)
        x1 = x2

    i = 0
    len_resid = len(residuals)
    while i < len_resid and residuals[i] > 0.001:
        i = i+1

    if i >= len_resid:
        return -1, -1, -1, -1

    # residuals are 1 ahead of the cell density and substrate list
    peak_i = i + 1  # index that the peak occurs at
    peak = cell_d[peak_i]  # probably don't need this
    peak_time = t[peak_i]  # probably don't need this either

    t_stop = len(cell_d) - i

    return peak, peak_i, peak_time, t_stop


def f_d(X, t, Kd):
    return -Kd*X


def generate_death(peak, tInc, tStop):
    X0 = peak  # initial cell concentration (od600

    # Make time array for solution
    t_d = np.arange(0., tStop, tInc)

    # Call the ODE solver
    psoln_d = odeint(f_d, X0, t_d, args=(Kd,))

    return psoln_d





