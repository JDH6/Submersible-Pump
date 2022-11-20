#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:11:14 2022

@author: jacovaneeden
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,15)
K = 2
h = 6

dB = 5.6/(9.81*h)

dO = K

dT = dB - dO


result = odeint(dT, 5, t)

plt.plot(t,result)

