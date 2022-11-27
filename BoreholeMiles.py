#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:09:08 2022

@author: milesweedon
"""

import numpy as np
import matplotlib.pyplot as plt


#Note that at time t = 0, the height is 300 ft above aquifier

#---------------VARIABLES THAT WE EDIT---------------------------------------

startTime = 0 
endTime = 3
boreholeFlowRateOut = 5.0472 * 10**-3
boreholeFlowRateIn = 1*10**-7
boreholeDiameter = 0.1524

#----------------------------------------------------------------------------

initialWaterTableHeight = 91.44
netFlow = boreholeFlowRateIn - boreholeFlowRateOut
boreholeCrossSectionArea = np.pi * (boreholeDiameter / 2)**2


'''
volumeOfPump = boreholeCrossSectionArea * 7.62
verticalPipeCrossSectionArea = 5.067074791 * 10**(-4)
volumeOfPipe = verticalPipeCrossSectionArea * 83.82

'''


def waterTableHeight(t):
    return initialWaterTableHeight + ((netFlow * t) / boreholeCrossSectionArea)

xValues = []
yValues = []                                      

for t in range(startTime, endTime + 1):
    xValues.append(t)
    yValues.append(waterTableHeight(t))

plt.plot(xValues,yValues, 'go--', linewidth=2, markersize=12)
plt.xlabel('Time (seconds)')
plt.ylabel('Water table height (metres)')
plt.title('Water table height measured from the bottom of the borehole')
