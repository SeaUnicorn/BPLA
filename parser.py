# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import dictionary as dictry

#d = dict("time=" = 0.0, airspeed = 0.0, altitude = 0.0, vario = 0.0, evario = 0.0, nettovario = 0.0, integrator = 0.0, compass = 0.0, slipball = 0.0, turnrate = 0.0, yawstringangle = 0.0, radiofrequency = 0.0, yaw = 0.0, pitch = 0.0, bank = 0.0, quaternionx = 0.0, quaterniony = 0.0, quaternionz = 0.0, quaternionw = 0.0, ax =0.0, ay = 0.0, az = 0.0, vx = 0.0, vy = 0.0, vz = 0.0, rollrate = 0.0, pitchrate = 0.0, yawrate = 0.0, gforce = 0.0, height = 0.0, wheelheight = 0.0, turbulencestrength = 0.0, surfaceroughness = 0.0 )
d = dictry.initDict()
data = "b'time=12.0274821691107\r\nairspeed=18.2518310546875\r\naltitude=921.0400390625\r\nvario=2.94780850410461\r\nevario=-4.92492914199829\r\nnettovario=-4.11020231246948\r\nintegrator=-5.10884189605713\r\ncompass=269.242828369141\r\nslipball=-0.0443850643932819\r\nturnrate=-0.329691261053085\r\nyawstringangle=0.298072576522827\r\nradiofrequency=123.5\r\nyaw=4.69917392730713\r\npitch=0.331385463476181\r\nbank=0.200987860560417\r\nquaternionx=-0.0978995338082314\r\nquaterniony=0.164830029010773\r\nquaternionz=-0.00993972364813089\r\nquaternionw=0.981359660625458\r\nax=-3.03251528739929\r\nay=0.179045662283897\r\naz=-3.47918820381165\r\nvx=20.6327610015869\r\nvy=-2.43534064292908\r\nvz=4.13383197784424\r\nrollrate=-0.177867025136948\r\npitchrate=-0.101789727807045\r\nyawrate=0.0678432583808899\r\ngforce=0.69383991603093\r\nheight=416.286682128906\r\nwheelheight=415.140686035156\r\nturbulencestrength=0.504481792449951\r\nsurfaceroughness=0\r\n'"

dictry.StringToDict(data, d)

for a in d:
    print (str(a.name)+" = " +str(a.value) + " " + str(a.unit) + "\n")

        
    