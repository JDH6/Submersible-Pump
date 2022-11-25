#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:11:14 2022

@author: jacovaneeden
"""

import numpy as np
import matplotlib.pyplot as plt

T = 604800
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
            V = Vstart + ((1.00944 - K) * (t))
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
            V = Vstart + ((- K) * (t))
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




