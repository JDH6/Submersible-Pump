#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:53:26 2022

@author: jacovaneeden
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

T = 500
v0 = 0

def pumpON(t,K): #A function representing the pump in operation
    K = 1
    dvdt = 1.00944 - K
    return dvdt
def pumpOFF(t,K):
    K = 0.1 
    dvdt = -K
    return dvdt       

n = 0
time = [0]
V = odeint(pumpON,v0,time)
Vl = [0]
while n < T:
    if Vl[-1] <= 214:
       time = [0]
       V0 = Vl[-1]
       while V[-1] <= 228:
           Vlend = V[-1]
           V = odeint(pumpON,Vlend,time)
           V = [element for tupl in V for element in tupl]
           Vend = V[-1]
           Vl.append(Vend)
           print(Vlend)
           t=time[-1]
           t2 = t + 1
           time.append(t2)
           n = n + 1
           if n > T - 1:
               break
    else:
       time = [0]
       V0 = Vl[-1]
       while Vl[-1] > 214:
           Vlend = V[-1]
           V = odeint(pumpOFF,Vlend,time)
           V = [element for tupl in V for element in tupl]
           Vend = V[-1]
           Vl.append(Vend)
           t=time[-1]
           t2 = t + 1
           time.append(t2)
           n = n + 1
           if n > T - 1:
               break
           
n = range(1,T+2)
            
print (n)

       
time.remove(1)

print(Vl)

plt.plot(n,Vl)
plt.xlabel('time')
plt.ylabel('Volume')




