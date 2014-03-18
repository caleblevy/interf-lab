#!/usr/bin/env python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import coords

theta = phi = np.linspace(0,2*np.pi)
(alpha,beta) = np.meshgrid(theta,phi)

x = np.zeros(np.size(alpha))
y = np.zeros(np.size(alpha))
z = np.zeros(np.size(alpha))


count = 0

for I in range(50):
    for J in range(50):
        CVec = coords.ToCart([alpha[I,J],beta[I,J]])
        x[count] = CVec[0]; y[count] = CVec[1]; z[count] = CVec[2]
        count += 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)

plt.show()
