#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:11:14 2022

@author: jacovaneeden
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


T = np.linspace(0,15)
K = 2
v0 = 5


h = 6

def dT(y,t):
    dB = 5.6/(9.81*h)*t
    dO = K*t
    dT = dB - dO
    return dT


result = odeint(dT, v0, T)

plt.plot(t,result)

