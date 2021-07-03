from vpython import *


class ThreeDegree:
    def __init__(self, length=4,radius=1,joint0_pos=vector(0, 0, 0), joint0_axis=vector(0, 0, 1),
                 joint1_pos=vector(0, 0, 0), joint1_axis=vector(0, 1, 0),
                 joint2_pos=vector(0, 0, 0), joint2_axis=vector(0, 1, 0)):
        self.joint0 = cylinder(pos=joint0_pos,
                               axis=joint0_axis,
                               length=length,
                               radius=radius,
                               color=vector(0.5, 0, 0))

        self.joint1 = cylinder(
            pos=joint1_pos,
            axis=joint1_axis,
            length=length,
            radius=radius,
            color=vector(0.5, 0, 0))

        self.joint2 = cylinder(
            pos=joint2_pos,
            axis=joint2_axis,
            length=length,
            radius=radius,
            color=vector(0.5, 0, 0))
