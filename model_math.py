# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:38:25 2020

@author: David Wang
"""
import matplotlib.pyplot as plt
import numpy as np


C = 1.520
u = 0.117
g = 1.966

t = np.array(range(100))


input_choice = str(input('Type C to use (x10^6 cells)/mL, Type OD to use OD600:'+'\n' + '->'))

while not (input_choice == 'OD' or input_choice == 'C'):
   print('You did not input a valid response, please choose C or OD')
   input_choice = str(input('Type C to use (x10^6 cells)/mL, Type OD to use OD600:'+'\n' + '->'))
   
if input_choice == 'OD': 
    yo = float(input('Enter Cell Density in OD600:'+'\n' + '->'))
    
elif input_choice == 'C':
    yo = float(input('Enter Cell Density in (x10^6 cells)/mL:'+'\n' + '->'))*10**6/1E8
    


y = yo + C/(1+np.exp((4*u/C)*(g-t)+2))

if input_choice == 'C':
    y = y*1E8

j = y[0]
for i in y[1:-1]:
    if (i-j)/j > 0.01:
        j = i
    else:
        peak = j
        break
    
        
print('The peak concentration is ' + str(peak/1E8)+' x10^8 cells/ml')
print(y[-1])
plt.plot(t,y)

plt.title('Cell Density vs Time')

plt.xlabel('Time (hrs)')
plt.ylabel('Density (OD600)')

plt.grid(alpha=.4,linestyle='--')

plt.savefig('test_model.png', bbox_inches='tight')

plt.show()

