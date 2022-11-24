#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:11:14 2022

@author: jacovaneeden
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


K = 0.1 #K = constant flow rate of water from the tank from the taps (this can be adjusted accordingly)
v0 = 0 #v0 = initial volume of water in the tank
T = 3600 #T = time period of running simulation in seconds
t = np.linspace(0,T) #t = time period list in seconds


def pump(y,t): #A function representing the pump in operation
    fW = 5.6/(9.81)*t #fW = the flow rate from the well to the tank
    fO = K #fO = the constant flow of K litres per second
    dT = fW - fO
    return dT

switch = 0

for t in range(1,T):
    fO = K 
    V = K * t
    if V < 214: 
        switch = 1
    while switch == 1:
        V = V + odeint(pump(), v0, t)
        if V > 229:
            switch = 0
        



plt.plot(t,V)

