import numpy as np
import matplotlib.pyplot as plt

'''
Assumptions:
    GPE is measured from the top of the borehole, hence GPE should always be negative. For calculations we must take the absolute value.
    Initial water table height is 60m below ground level height, like stated in the question.
    Water table height is measured from the top of the pump/motor, not from the bottom of the borehole.
'''


#---------------CONSTANTS-------------------------------------------------

rho = 1000 #water density
g = 9.81 #gravitational constant
#pi = 3.14 #pi

#---------------SYSTEM CHARACTERISTICS------------------------------------

#Pn = 5516 #nominal power (W) ???????
Pn = 5592.75 #nominal power (W) ???????

es = 0.64 #starting pump efficiency
el = 0.265 #lowered pump efficiency

Rb = 0.1524 #borehole radius (m)
Rv = 0.0254 #valve radius (m)
boreholeDiameter = 0.1524
initialWaterTableHeight = 65.532 #equivalent to 215ft. Is the distance from top of motor to water table 60ft below ground level.


#---------------VARIABLES THAT WE EDIT---------------------------------------

startTime = 0 
endTime = 3
boreholeFlowRateOut = 5.0472 * 10**-3  #INCORRECT
boreholeFlowRateIn = 1*10**-7  #Research a value

#----------------------------------------------------------------------------

endpoint=False

netFlow = boreholeFlowRateIn - boreholeFlowRateOut
boreholeCrossSectionArea = np.pi * (boreholeDiameter / 2)**2



def waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea):
    return initialWaterTableHeight + ((netFlow * t) / boreholeCrossSectionArea)

xValues = []
yValues = [] 
EpValues = []                                    

for t in range(startTime, endTime + 1):
    xValues.append(t)
    yValues.append(waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea))
    Vb = np.pi*waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea)*(Rb**2-Rv**2) #Volume of borehole 
   
    if waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea)>=0:
        Pr = es*Pn #real power for submerged pump
    else:
        Pr = el*Pn #real power for partially submerged pump
        
    Gpe = abs(rho*Vb*g*(-60-(initialWaterTableHeight-waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea)))) #GPE energy required to pump water to tanks. Note that this is negative, hence we take the modulus.
    
    energyRequired = Pr *  
    
    
    
    EpValues.append(t*Pr) #INCORRECT
    
    if  Gpe > any(EpValues) : #if electrical energy output less than or equal to energy to move water
        endpoint=True #boolean value true, motor broke endpoint reached
        endTime = t
        break
    else:
        endpoint=False #boolean value false, motor did not break
    
    

if endpoint==True:
    print('Motor has broken in', endTime, 'seconds')
elif endpoint==False:
    print('Motor did not fail in', endTime, 'seconds')





plt.plot(xValues,yValues, 'go--', linewidth=2, markersize=12)
plt.xlabel('Time (seconds)')
plt.ylabel('Water table height (metres)')
plt.title('Water table height measured from the bottom of the borehole')