#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:09:08 2022

@author: milesweedon
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


startTime = 0 
endTime = 3600



waterTableHeight = 91.44 #initial water table height
boreholeCrossSectionArea = 0.01824146925
volumeOfPump = boreholeCrossSectionArea * 7.62
verticalPipeCrossSectionArea = 5.067074791 * 10**(-4)
boreholeFlowRateOut = 1.00944
boreholeFlowRateIn = 0.1




def volumeOfBorehole(waterTableHeight, boreholeCrossSectionArea, volumeOfPump, verticalPipeCrossSectionArea):
    vol = (waterTableHeight * boreholeCrossSectionArea) - volumeOfPump - (verticalPipeCrossSectionArea*(waterTableHeight-25))
    return vol
    
#print(verticalPipeCrossSectionArea)


newVolumeAfterTime = 0

while t < endTime:
    netFlow = boreholeFlowRateIn - boreholeFlowRateOut
    #print(netFlow)
    newVolumeAfterTime = volumeOfBorehole(waterTableHeight, boreholeCrossSectionArea, volumeOfPump, verticalPipeCrossSectionArea) + (netFlow)
    waterTableHeight = newVolumeAfterTime/(boreholeCrossSectionArea)
    t+=1
    #print(newVolumeAfterTime)
    
    
    
