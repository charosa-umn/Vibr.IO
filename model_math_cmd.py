# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:38:25 2020

@author: David Wang
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, t, params):
    X, S = y      # unpack current values of y
    umax, Ks, Yxs = params  # unpack parameters
    derivs = [X*umax*S/(Ks+S),      # list of dy/dt=f functions
             -X*umax*S/(Yxs*(Ks+S))]
    return derivs


# Parameters
umax = 0.43         # maximum growth rate
Ks = 1.2       # half-velocity constant
Yxs = 1.21     # yield coefficient for biomass/substrate

# Initial values
X0 = 0.15     # initial cell concentration (od600)
S0 = 1.2     # initial initial mass substrate (g)

# Bundle parameters for ODE solver
params = [umax, Ks, Yxs]

# Bundle initial conditions for ODE solver
y0 = [X0, S0]

# Make time array for solution
tStop = 28.
tInc = 0.05
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# Plot results
fig = plt.figure(1, figsize=(8,8))


# Plot X as a function of time
ax1 = fig.add_subplot(311)
ax1.plot(t, psoln[:,0])
ax1.set_xlabel('Time (hrs)')
ax1.set_ylabel('X (od600)')


# Plot S as a function of time
ax2 = fig.add_subplot(312)
ax2.plot(t, psoln[:,1])
ax2.set_xlabel('Time (hrs)')
ax2.set_ylabel('S (g)')


plt.tight_layout()
plt.show()
