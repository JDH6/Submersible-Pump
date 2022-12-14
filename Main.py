# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:14:34 2022

@author: phill
"""

import numpy as np
import matplotlib.pyplot as plt

#---------------CONSTANTS--------------------------------------------------

rho = 1000 #water density
g = 9.81 #gravitational constant
pi = 3.14 #pi

#---------------SYSTEM CHARACTERISTICS-------------------------------------

t = np.linspace(0, 3600, num=3600, endpoint=False) #time is intervals to an hour, endpoint has been defined and not reached
Pn = 5595 #nominal power (W)
es = 0.64 #starting pump efficiency
el = 0.265 #lowered pump efficiency
boreholeDiameter = 0.1524
Rb = 0.0764 #borehole radius (m)
Rv = 0.01252 #valve radius (m)
initialWaterTableHeight = 91.44 #water table height at start (m)

#---------------VARIABLES THAT WE EDIT---------------------------------------

startTime = 0 
endTime = 3
boreholeFlowRateOut = 5.0472 * 10**-3
boreholeFlowRateIn = 1*10**-7

#------------Jaco's work-------------------------------------------------------------

T = 604800

def taps(t):
    K = 0.0001
    return K
    

K = 0.0001
t = 0
Vl = [0]
n = 0
V = 0
VfromWell = 0
while n < T:
    if Vl[-1] <= 214:
        t = 1
        Vstart = Vl[-1]
        while V <= 228:
            V = Vstart + ((1.00944 - taps(t)) * (t))
            VfromWell = VfromWell + ((1.00944 - K) * (t))
            t = t + 1
            n = n + 1
            Vl.append(V)
            if n >= T:
                break
    else:
        t = 1
        Vstart = Vl[-1]
        while V > 214:
            V = Vstart + ((- taps(t)) * (t))
            t = t + 1
            n = n + 1
            Vl.append(V)
            if n >= T:
                break
            
n = np.linspace(1,n,n+1)

plt.plot(n,Vl)
plt.xlabel('Time (seconds)')
plt.ylabel('Volume (litres)')

print(VfromWell)

#------Miles & Phillip work combined-----------

endpoint=True

netFlow = boreholeFlowRateIn - boreholeFlowRateOut
boreholeCrossSectionArea = np.pi * (boreholeDiameter / 2)**2



def waterTableHeight(t):
    return initialWaterTableHeight + ((netFlow * t) / boreholeCrossSectionArea)

xValues = []
yValues = [] 
EpValues = []                                    

for t in range(startTime, endTime + 1):
    xValues.append(t)
    yValues.append(waterTableHeight(t))
    Vb = pi*waterTableHeight(t)*(Rb**2-Rv**2) #Volume of borehole
    if waterTableHeight(t)>=7.62:
        Pr = es*Pn #real power for submerged pump
    else:
        Pr = el*Pn #real power for partially submerged pump
    Egp = rho*Vb*g*waterTableHeight(t) #GPE energy required to pump water to tanks
    EpValues.append(t*Pr)
    if Egp > any(EpValues) : #if electrical energy output less than or equal to energy to move water
        endpoint=True #boolean value true, motor broke endpoint reached
        endTime = t
        break
    else:
        endpoint=False #boolean value false, motor did not break
    
if endpoint==True:
    print('Motor has broken in', endTime, 'seconds')
elif endpoint==False:
    print('Motor did not fail in', endTime, 'seconds')
