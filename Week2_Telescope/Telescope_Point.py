#!/usr/bin/env python
import ephem,coords
import radiolab
import numpy as np
import matplotlib.pyplot as plt
import time,os,sys,threading

PointHome = False

## Global, static variable
obs = ephem.Observer() # We observe from Berkeley
Sun = ephem.Sun()

Berkeley_Lat = 37.8732
Berkeley_Lon = -122.2573
obs.lat = coords.ToRad(Berkeley_Lat)
obs.lon = coords.ToRad(Berkeley_Lon)

Sun = ephem.Sun()

obs.date = ephem.now()
Sun.compute(obs)
LST = obs.sidereal_time()

if PointHome:
    radiolab.pntHome()

def Update():
    global LST,obs,Sun
    obs.date = ephem.now()
    LST=obs.sidereal_time()
    Sun.compute(obs)
    radiolab.pntTo(alt=coords.ToDeg(Sun.alt), az=coords.ToDeg(Sun.az))

Update()
print LST
