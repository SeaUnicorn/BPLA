# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:17:23 2018

@author: Evgeniya
"""

class dictionary(object):
    key = "default="
    value = 0.0
    name = "default"
    unit = "default"
    def __init__(self, key, value, unit):
        self.key = key
        self.value = value
        self.name = key.strip('=')
        self.unit = unit
    def setv(self, value):
        self.value = value


def initDict():
     d = []
     d.append(dictionary("time=", 0.0, "h")) #in-game day time
     d.append(dictionary("airspeed=", 0.0, "m/s")) #airspeed indicator reading
     d.append(dictionary("altitude=", 0.0, "m")) #altimeter reading
     d.append(dictionary("vario=", 0.0, "m/s")) #pneumatic variometer reading
     d.append(dictionary("evario=", 0.0, "m/s")) #electronic variometer reading
     d.append(dictionary("nettovario=", 0.0, "m/s")) #netto variometer value
     d.append(dictionary("integrator=", 0.0, "m/s")) #integrator value
     d.append(dictionary("compass=", 0.0, "degrees")) #compass reading
     d.append(dictionary("slipball=", 0.0, "rad")) #slip ball deflection angle
     d.append(dictionary("turnrate=", 0.0, "rad/s")) #turn indicator reading 
     d.append(dictionary("yawstringangle=", 0.0, "rad")) #yawstring angle
     d.append(dictionary("radiofrequency=", 0.0, "mhz")) #radiofrequency
     d.append(dictionary("yaw=", 0.0, "rad")) #yaw
     d.append(dictionary("pitch=", 0.0, "rad")) #pitch
     d.append(dictionary("bank=", 0.0, "rad")) #bank
     
     d.append(dictionary("quaternionx=", 0.0, "c.u.")) #quaternion x
     d.append(dictionary("quaterniony=", 0.0, "c.u.")) #quaternion y
     d.append(dictionary("quaternionz=", 0.0, "c.u.")) #quaternion z
     d.append(dictionary("quaternionw=", 0.0, "c.u.")) #quaternion w
     d.append(dictionary("ax=", 0.0, "m/s2")) #acceleration vector x
     d.append(dictionary("ay=", 0.0, "m/s2")) #acceleration vector y
     d.append(dictionary("az=", 0.0, "m/s2")) #acceleration vector z
     d.append(dictionary("vx=", 0.0, "m/s")) #speed vector x
     d.append(dictionary("vy=", 0.0, "m/s")) #speed vector y
     d.append(dictionary("vz=", 0.0, "m/s")) #speed vector z
     d.append(dictionary("rollrate=", 0.0, "rad/s")) #roll rate (local system) x
     d.append(dictionary("pitchrate=", 0.0, "rad/s")) #roll rate (local system) y
     d.append(dictionary("yawrate=", 0.0, "rad/s")) #roll rate (local system) z
     
     d.append(dictionary("gforce=", 0.0, "c.u.")) #g forces
     d.append(dictionary("height=", 0.0, "m")) #height of CG above ground
     d.append(dictionary("wheelheight=", 0.0, "m")) #height of wheel above ground
     d.append(dictionary("turbulencestrength=", 0.0, "c.u.")) #turbulence strength
     d.append(dictionary("surfaceroughness=", 0.0, "c.u.")) #surface roughness

     return d
 
def StringToDict(data, d):
    for a in d:
        s = a.key
        if(data.find(s) != -1):
            i = (data.rfind(s)+len(s))
            val = " "
            while data[i].isdigit() or data[i] == '.' or data[i] == '-':
                val= val+data[i]
                i= i+1
            try:
                a.setv(val)
            except :
                a.setv(-1)
    return d
                    

