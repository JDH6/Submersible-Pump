import numpy as np
rho = 1000 #water density
g = 9.81 #gravitational constant
pi = 3.14 #pi
Rb = 7.62 #borehole radius (m)
Rv = 1.27 #valve radius (m)
t = np.linspace(0, 3600, num=3600, endpoint=False) #time is intervals to an hour, endpoint has been defined and not reached
Pn = 5595 #nominal power
Vn = 220 #nominal voltage
es = 0.64 #starting pump efficiency
el = 0.265 #lowered pump efficiency
while waterTableHeight>=7.62:
    Pr = es*Pn #real power for submerged pump
    Vr = es*Vn #real voltage for submervged pump
    Vo = pi*waterTableHeight*(Rb**2-Rv**2) #Volume of borehole
else:
    Pr = el*Pn #real power for partially submerged pump
Egp = rho*Vo*g*waterTableHeight #real voltage for partially submerged pump
Ep = Pr*t #Electrical energy ouptu of motor
if any(Ep) == Egp : #if electrical energy output equals energy to move water
    endpoint=True #boolean true if motor output capacity equal to energy required to pump water