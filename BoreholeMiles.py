#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:09:08 2022

@author: milesweedon
"""

import numpy as np
import matplotlib.pyplot as plt


class BoreHole():
    
    def __init__(self):

        #Note that at time t = 0, the height is 300 ft above aquifier
        
        #---------------VARIABLES THAT WE EDIT---------------------------------------
        
        self.startTime = 0 
        self.endTime = 3
        self.boreholeFlowRateOut = 5.0472 * 10**-3
        self.boreholeFlowRateIn = 1*10**-7
        self.boreholeDiameter = 0.1524
        
        #----------------------------------------------------------------------------
        
        self.initialWaterTableHeight = 91.44
        self.netFlow = self.boreholeFlowRateIn - self.boreholeFlowRateOut
        self.boreholeCrossSectionArea = np.pi * (self.boreholeDiameter / 2)**2
    
        self.waterTableHeightCalculation()
    
    
    def waterTableHeight(self, t):
        return self.initialWaterTableHeight + ((self.netFlow * t) / self.boreholeCrossSectionArea)
    
    
    
    def waterTableHeightCalculation(self):
        self.xValues = []
        self.yValues = []                                      
    
        for t in range(self.startTime, self.endTime + 1):
            self.xValues.append(t)
            self.yValues.append(self.waterTableHeight(t))
            
        while True:
            self.selectOutput = input("Would you like to plot a graph of the water table height? \n")
            if self.selectOutput == "Yes":
                self.plotOfWaterTableHeight()
                break
            elif self.selectOutput == "No":
                break
            else:
                print("Please type either 'Yes' or 'No'.\n")
            
        
    
    def plotOfWaterTableHeight(self):
        plt.plot(self.xValues,self.yValues, 'go--', linewidth=2, markersize=12)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Water table height (metres)')
        plt.title('Water table height measured from the bottom of the borehole')
