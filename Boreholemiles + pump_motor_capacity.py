import numpy as np
import matplotlib.pyplot as plt
#---------------CONSTANTS-------------------------------------------------

rho = 1000 #water density
g = 9.81 #gravitational constant
pi = 3.14 #pi

#---------------SYSTEM CHARACTERISTICS------------------------------------

Pn = 5595 #nominal power (W)
es = 0.64 #starting pump efficiency
el = 0.265 #lowered pump efficiency
Rb = 0.1524 #borehole radius (m)
Rv = 0.0254 #valve radius (m)
boreholeDiameter = 0.1524
initialWaterTableHeight = 91.44

#---------------VARIABLES THAT WE EDIT---------------------------------------

startTime = 0 
endTime = 3
boreholeFlowRateOut = 5.0472 * 10**-3
boreholeFlowRateIn = 1*10**-7

#----------------------------------------------------------------------------

endpoint=False

netFlow = boreholeFlowRateIn - boreholeFlowRateOut
boreholeCrossSectionArea = np.pi * (boreholeDiameter / 2)**2



def waterTableHeight(t):
    return initialWaterTableHeight + ((netFlow * t) / boreholeCrossSectionArea)

xValues = []
yValues = [] 
EpValues = []                                    

for t in range(startTime, endTime + 1):
    xValues.append(t)
    yValues.append(waterTableHeight(t))
    Vb = pi*waterTableHeight(t)*(Rb**2-Rv**2) #Volume of borehole
    if waterTableHeight(t)>=7.62:
        Pr = es*Pn #real power for submerged pump
    else:
        Pr = el*Pn #real power for partially submerged pump
    Egp = rho*Vb*g*waterTableHeight(t) #GPE energy required to pump water to tanks
    EpValues.append(t*Pr)
    if any(EpValues) >= Egp : #if electrical energy output less than or equal to energy to move water
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