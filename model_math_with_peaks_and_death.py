# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:38:25 2020
@author: David Wang
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


### Cell Growth Modeling

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
tStop = 28
tInc = 1
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# print time, and array of cell density and substrate
print('t')
print(t)
print('psoln')
print(psoln)

# make separate lists containing cell density and substrate
cell_d = []
substrate = []

for i in range(0,len(psoln)-1):
    for j in (0,len(psoln[i])-1):
        if j == 0:
            cell = psoln[i][j]
            cell_d.append(cell)
        else:
            sub = psoln[i][j]
            substrate.append(sub)

# print list of cell density and substrate
print('cell density')
print(cell_d)
print('substrate')
print(substrate)

# select peak as when cell population grows < 1% in a time step
x1 = cell_d[0]
residuals = []
for i in range(1,len(cell_d)):
    x2 = cell_d[i]
    res = (x2-x1)/x1
    residuals.append(res)
    x1 = x2

# print list of residuals
print('residuals')
print(residuals)

# count = 0
i = 0
while residuals[i] > 0.001:
    i = i+1
    peak = 0
    # count += 1
    # print('count')
    # print(count)

peak_residual = residuals[i]

# residuals are 1 ahead of the cell density and substrate list
peak_i = i+1
peak = cell_d[peak_i]
peak_time = t[peak_i]

# print peak residual, peak cell density, and corresponding time
print('peak residual')
print(peak_residual)
print('peak')
print(peak)
print('peak_time')
print(peak_time)

### Cell Death Modeling

# find the time to model cell death after peak
t_post_d = len(cell_d)-i

# setup differential equation for cell death
def f_d(X, t, Kd):
    return -Kd*X

# Parameters
Kd = 0.43       # first-order death constant

# Initial values
X0 = peak     # initial cell concentration (od600)

# Make time array for solution
tStop = t_post_d
tInc = 1
t_d = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln_d = odeint(f_d, X0, t_d, args=(Kd,))

print('death psoln')
print(psoln_d)

# Plot results
fig = plt.figure(1, figsize=(8,8))

# Plot X as a function of time
ax1 = fig.add_subplot(311)

# plot from begining to peak for cell growth
ax1.plot(t[:peak_i+1], psoln[:peak_i+1,0],'k')

# plot peak point
ax1.plot(t[peak_i], psoln[peak_i, 0],'ro')

# plot from peak point to end of range for cell death
ax1.plot(t[peak_i:],psoln_d[:,0],'--k')

ax1.set_xlabel('Time (hrs)')
ax1.set_ylabel('X (od600)')


# # Plot S as a function of time
ax2 = fig.add_subplot(312)
ax2.plot(t, psoln[:,1],'k')
ax2.set_xlabel('Time (hrs)')
ax2.set_ylabel('S (g)')


plt.tight_layout()
plt.show()