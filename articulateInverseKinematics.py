import math

import numpy
from vpython import *
import numpy as np

cyl1 = cylinder(pos=vector(0, 0, 0),
                axis=vector(0, 0, 1),
                length=4,
                radius=1,
                color=vector(0.5, 0, 0))

cyl2 = cylinder(
    axis=vector(0, 1, 0),
    length=4,
    radius=1,
    color=vector(0.5, 0, 0))

cyl3 = cylinder(
    axis=vector(0, 1, 0),
    length=4,
    radius=1,
    color=vector(0.5, 0, 0))

endX   =10
endY = 10
endZ = 10

a1 = 8
a2 = 8
a3 = 8

r1 = math.sqrt(math.pow(endX, 2) + math.pow(endY, 2))
r2=endZ-a1
r3= math.sqrt(math.pow(r1,2)+math.pow(r2,2))
fi2 = math.atan(r2/r1)
cosfi1=(math.pow(a3,2)-math.pow(a2,2) -math.pow(r3,2))
fi1=math.acos((math.pow(a3,2)-math.pow(a2,2) -math.pow(r3,2))/(-2*a2*r3))
fi3=math.acos((math.pow(r3,2)-math.pow(a3,2)-math.pow(a2,2))/(-2*a2*a3))

theta0=math.atan(endY/endX)
theta1=fi2-fi1
theta2=math.pi-fi3




R01 = np.matmul([[cos(theta0), -sin(theta0), 0],
                 [sin(theta0), cos(theta0), 0],
                 [0, 0, 1]],
                [[1, 0, 0],
                 [0, 0,-1],
                 [0, 1, 0]])
d01 = [[0], [0], [a1]]

H01 = [numpy.append(R01[0], d01[0][0]),
       numpy.append(R01[1], d01[1][0]),
       numpy.append(R01[2], d01[2][0]),
       [0, 0, 0, 1]]

R12 = np.matmul([[cos(theta1), -sin(theta1), 0],
                 [sin(theta1), cos(theta1), 0],
                 [0, 0, 1]],
                [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])
d12 = [[a2*cos(theta1)], [a2*sin(theta1)], [0]]

H12 = [numpy.append(R12[0], d12[0][0]),
       numpy.append(R12[1], d12[1][0]),
       numpy.append(R12[2], d12[2][0]),
       [0, 0, 0, 1]]

R23 = np.matmul([[cos(theta2), -sin(theta2), 0],
                 [sin(theta2), cos(theta2), 0],
                 [0, 0, 1]],
                [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

d23 = [[a3*cos(theta2)], [a3*sin(theta2)],[0]]

H23 = [numpy.append(R23[0], d23[0][0]),
       numpy.append(R23[1], d23[1][0]),
       numpy.append(R23[2], d23[2][0]),
       [0, 0, 0, 1]]
3
H02 = np.matmul(H01, H12)
H03 = np.matmul(H02, H23)
cyl2.pos = vector(H01[0][3], H01[1][3], H01[2][3])
cyl3.pos = vector(H02[0][3], H02[1][3], H02[2][3])

a1c = curve(vector(0, 0, 0), vector(0, 0, a1))
a2c = curve(vector(0, 0, a1), cyl3.pos)
a3c = curve(cyl3.pos, vector(H03[0][3], H03[1][3], H03[2][3]))

print(vector(H03[0][3], H03[1][3], H03[2][3]))
