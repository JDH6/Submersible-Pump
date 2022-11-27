import numpy as np

#---------------CONSTANTS-------------------------------------------------

rho = 1000 #water density
g = 9.81 #gravitational constant
pi = 3.14 #pi

#---------------SYSTEM CHARACTERISTICS------------------------------------

t = np.linspace(0, 3600, num=3600, endpoint=False) #time is intervals to an hour, endpoint has been defined and not reached
Pn = 5595 #nominal power (W)
es = 0.64 #starting pump efficiency
el = 0.265 #lowered pump efficiency
Rb = 0.1524 #borehole radius (m)
Rv = 0.0254 #valve radius (m)

#-------------------------------------------------------------------------

while waterTableHeight(t)>=7.62:
    Pr = es*Pn #real power for submerged pump
    Vb = pi*waterTableHeight*(Rb**2-Rv**2) #Volume of borehole
else:
    Pr = el*Pn #real power for partially submerged pump
Egp = rho*Vo*g*waterTableHeight #real voltage for partially submerged pump
Ep = Pr*t #Electrical energy ouptut of motor
if any(Ep) <= Egp : #if electrical energy output less than or equal to energy to move water
    endpoint=True #boolean value true, endpoint reached