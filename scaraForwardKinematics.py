import math
import time

import numpy
from vpython import *
import numpy as np

cyl1 = cylinder(pos=vector(0, 0, 0),
                axis=vector(0, 0, 1),
                length=4,
                radius=1,
                color=vector(0.5, 0, 0))

cyl2 = cylinder(
    axis=vector(0, 0, 1),
    length=4,
    radius=1,
    color=vector(0.5, 0, 0))

mybox = box(axis=vector(0, 0, -1), length=2, height=2, width=2)

theta0 = math.radians(45)
theta1 = math.radians(90)
print(sin(theta1))
a1 = 8
a2 = 8
a3 = 8
a4 = 8
a5 = 8
a6 = 8
d = 8
R01 = np.matmul([[cos(theta0), -sin(theta0), 0],
                 [sin(theta0), cos(theta0), 0],
                 [0, 0, 1]],
                [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])
d01 = [[a2 * cos(theta0)], [a2 * sin(theta0)], [a1]]

H01 = [numpy.append(R01[0], d01[0][0]),
       numpy.append(R01[1], d01[1][0]),
       numpy.append(R01[2], d01[2][0]),
       [0, 0, 0, 1]]

R12 = np.matmul([[cos(theta1), -sin(theta1), 0],
                 [sin(theta1), cos(theta1), 0],
                 [0, 0, 1]],
                [[1, 0, 0],
                 [0, -1, 0],
                 [0, 0, -1]])
d12 = [[a4 * cos(theta1)], [a4 * sin(theta1)], [a3]]

H12 = [numpy.append(R12[0], d12[0][0]),
       numpy.append(R12[1], d12[1][0]),
       numpy.append(R12[2], d12[2][0]),
       [0, 0, 0, 1]]

R23 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

d23 = [[0], [0], [a3 + a6 + d]]

H23 = [numpy.append(R23[0], d23[0][0]),
       numpy.append(R23[1], d23[1][0]),
       numpy.append(R23[2], d23[2][0]),
       [0, 0, 0, 1]]

H02 = np.matmul(H01, H12)
H03 = np.matmul(H02, H23)
cyl2.pos = vector(H01[0][3], H01[1][3], H01[2][3])
mybox.pos = vector(H02[0][3], H02[1][3], H02[2][3] - a5)

a1c = curve(vector(0, 0, 0), vector(0, 0, a3))
a2c = curve(vector(0, 0, a3), cyl2.pos)
a3c = curve(cyl2.pos, cyl2.pos + vector(0, 0, a3))
a4c = curve(cyl2.pos + vector(0, 0, a3), vector(H02[0][3], H02[1][3], H02[2][3]))
a5c = curve(vector(H02[0][3], H02[1][3], H02[2][3]), vector(H02[0][3], H02[1][3], H02[2][3] - a5))
a6c = curve(vector(H02[0][3], H02[1][3], H02[2][3] - a5), vector(H03[0][3], H03[1][3], H03[2][3]))
print(cyl2.pos)
