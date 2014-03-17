#!/usr/bin/env python
import numpy as np
import ephem,radiolab,time
from matplotlib import pyplot as plt
import coords


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

RAMat = coords.RD_To_AA_Mat(LST,obs.lat)
RAMat
Sun_Co = [Sun.ra,Sun.dec]
Sun_Tel = coords.RD_To_AA(Sun_Co,LST,obs.lat)
