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
es = 0.64 #pump efficiency
Rb = 0.1524 #borehole radius (m)
Rv = 0.0254 #valve radius (m)
boreholeDiameter = 0.1524
initialWaterTableHeight = 65.532 #equivalent to 215ft. Is the distance from top of motor to water table 60ft below ground level.


#---------------VARIABLES THAT WE EDIT---------------------------------------

startTime = 0 
endTime = 3
boreholeFlowRateOut = 5.0472 * 10**-3  #INCORRECT
boreholeFlowRateIn = 1*10**-7  #Research a value
Flow_well_to_tank = 1.00944

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
    Pr = es*Pn
    h = (-18.288-(initialWaterTableHeight-waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea)))
    #Gpe = abs(rho*Vb*g*(-18.288-(initialWaterTableHeight-waterTableHeight(t, initialWaterTableHeight, netFlow, boreholeCrossSectionArea)))) #GPE energy required to pump water to tanks. Note that this is negative, hence we take the modulus.
    motorPower = rho*g*Flow_well_to_tank
    if motorPower >= Pr:
        endpoint=True
    else:
        endpoint=False

if endpoint==True:
    print('Motor has reached maximum power in', endTime, 'seconds')
elif endpoint==False:
    print('Motor did not meet maximum power in', endTime, 'seconds')




# plt.plot(xValues,yValues, 'go--', linewidth=2, markersize=12)
plt.xlabel('Time (seconds)')
plt.ylabel('Water table height (metres)')
plt.title('Water table height measured from the bottom of the borehole')
plt.plot(motorPower, t, 'b-', linewidth=2, markersize=12)