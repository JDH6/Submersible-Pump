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
K = 0.01 #flow rate per tap

def taps(t,N,k):
    K = k
    output = N * K
    return output

def Flow_well_to_tank(endPoint):
    if x == False:
        output = 1.00944 #Litres per second
    else:
        output = 0
    return output

def pumpPower(h):
    output = 1.00641168 * 9.81 * h
    return output

Pressure_Initial = 101325
TankVolume = 302.833
Vlow = TankVolume - (Pressure_Initial * TankVolume) / 344738
Vhigh = TankVolume - (Pressure_Initial * TankVolume) / 413685
x = False

print('Lower Bound of Volume (litres): ',Vlow,'\nUpper bound of Volume (litres): ',Vhigh)

t = 0 #A counter for time that is independent from n
Vl = [0] #Volume list with initial volume
pump = []
n = 0 #a counter for time
V = 0 #Initial Volume 
VfromWell = 0 #Total volume pumped from well.
VfromWellInitial = 0 #Volume from well when the pump turns off everytime after it has run
x = False
x1 = True

while n < T:
    if V < 0: break
    if Vl[-1] <= Vlow:
        t = 1 
        x = True
        Vstart = Vl[-1]
        VfromWellInitial += VfromWell
        while V <= Vhigh:
            if taps(n,N,K) != 0 and x == True:
                Vstart = Vstart + taps(n,N,K)*t
                x = False
            elif x == False:
                t = 0
                Vstart = Vl[-1]
                x = True
            V = Vstart + ((Flow_well_to_tank(x) - taps(n,N,K)) * t)
            VfromWell = VfromWellInitial + ((Flow_well_to_tank(x) - taps(n,N,K)) * t) * 0.264172 #The total volume pumped from well converted to gallons
            if V <= 0:
                V = 0
            pump.append(True)
            t = t + 1
            Vl.append(V)
            n = n + 1
            if n >= T: break
    else: 
        t = 1
        Vstart = Vl[-1]
        x1 == True
        while V > Vlow:
            if taps(n,N,K) == 0 and x1 == True:
                Vstart = Vl[-1]
                x1 = False
                t = 0
            elif x1 == False:
                Vstart = Vl[-1] + taps(n,N,K)*t
                x1 = True
            V = Vstart - taps(n,N,K) * t
            pump.append(False)
            t = t + 1
            if V <= 0:
                V = 0
            Vl.append(V)
            n = n + 1
            if n >= T: break
            
nList = np.linspace(0,n-1,n+1) #List of n values



Vl = [(302.833 - item) for item in Vl]
Vl = [((Pressure_Initial*302.833)/item) for item in Vl]
Vl = [item * 0.000145038 for item in Vl]

plt.plot(nList,Vl) #Plot the list of n against the list of Volumes
plt.xlabel('Time (seconds)')
plt.ylabel('Pressure (psi)')
plt.show()

print('Total Volume Pumped: ', VfromWell,'gallons')





