import time
from threading import Thread

from vpython import *
import numpy as np

cylinder(pos=vector(0, 0, 0),
         axis=vector(0, 0, 1),
         length=4,
         radius=2,
         color=vector(0.5, 0, 0))

c1 = curve(vector(0, 0, 2), vector(0, 0, 6))
c2 = curve(vector(0, 0, 6), vector(4, 0, 6))
cylinder(pos=vector(5, 0, 4),
         axis=vector(0, 0, 1),
         length=4,
         radius=1,
         color=vector(0.5, 0, 0))

c3 = curve(vector(5, 0, 8), vector(5, 0, 12))
c3 = curve(vector(5, 0, 12), vector(10, 0, 12))
c5 = curve(vector(10, 0, 12), vector(10, 0, 10))

mybox = box(pos=vector(10, 0, 10), axis=vector(0, 0, 1), length=2, height=2, width=2)
pos1 = [[10, 0, 11],
        [10, 0, 7]]
c6 = curve(pos=pos1)
i = 0
while (i < 10):
    c6.pop()
    c6.pop()
    c6.append(vector(pos1[0][0], pos1[0][1], pos1[0][2]))
    c6.append(vector(pos1[1][0] + i, pos1[1][1] + i, pos1[1][2] + i))
    time.sleep(10)
    i = i + 1
