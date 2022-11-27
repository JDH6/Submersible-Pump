#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:11:14 2022

@author: jacovaneeden
"""

import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of taps: "))
T = int(input("Enter time period (in seconds): "))

def taps(t,N):
    K = 0.0001
    output = N * K
    return output


Pressure_Initial_psi = 14.6959
Pressure_Initial = Pressure_Initial_psi * 6894.76 #psi to pascals
TankVolume = 302.833
Vlow = TankVolume - (Pressure_Initial * TankVolume) / 344738
Vhigh = TankVolume - (Pressure_Initial * TankVolume) / 413685

Flow_well_to_tank = 1.00944

print(Vlow,Vhigh)

t = 0 #A counter for time that is independent from n
Vl = [0] #Volume list with initial volume
n = 0 #a counter for time
V = 0 #Initial Volume 
VfromWell = 0
VfromWellInitial = 0

while n < T:
    if V < 0: break
    if Vl[-1] <= Vlow:
        t = 1
        Vstart = Vl[-1]
        while V <= Vhigh:
            V = Vstart + ((Flow_well_to_tank - taps(t,N)) * (t))
            if V <= 0: break
            VfromWell = VfromWellInitial + ((Flow_well_to_tank - taps(t,N)) * (t)) * 0.264172 #The total volume pumped from well converted to gallons
            t = t + 1
            Vl.append(V)
            n = n + 1
            if n >= T: break
        VfromWellInitial = VfromWell
    else: 
        t = 1
        Vstart = Vl[-1]
        while V > Vlow:
            V = Vstart + ((- taps(t,N)) * (t))
            t = t + 1
            if V <= 0: break
            Vl.append(V)
            n = n + 1
            if n >= T: break
            
nList = np.linspace(0,n-1,n+1)

if len(nList) == 0:
    nEnd = 0
else:
    nEnd = int(nList[-1])

if len(Vl) != T:
    if nEnd == 0:
        nList = [0]
    for i in range(nEnd,T-1,1):
        Vl.append(Vl[-1])
    for i in range(nEnd,T-1,1):
        nList = np.append(nList,i-nEnd)  

Vl = [item * 0.264172 for item in Vl] #Converting litres to gallons

plt.plot(nList,Vl)
plt.xlabel('Time (seconds)')
plt.ylabel('Volume (gallons)')
plt.show()

print('Total Volume Pumped: ', VfromWell,'gallons')





