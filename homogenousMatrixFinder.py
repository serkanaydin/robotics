import math
from math import sin, cos
import numpy as np
from vpython import vector

H01 = []
H02 = []
H12 = []
H03 = []


def homogenous_calculator(theta0, theta1, theta2, a1, a2, a3):
    global H01, H02, H12, H03
    R01 = np.matmul([[cos(theta0), -sin(theta0), 0],
                     [sin(theta0), cos(theta0), 0],
                     [0, 0, 1]],
                    [[1, 0, 0],
                     [0, 0, -1],
                     [0, 1, 0]])
    d01 = [[0], [0], [a1]]

    H01 = [np.append(R01[0], d01[0][0]),
           np.append(R01[1], d01[1][0]),
           np.append(R01[2], d01[2][0]),
           [0, 0, 0, 1]]

    R12 = np.matmul([[cos(theta1), -sin(theta1), 0],
                     [sin(theta1), cos(theta1), 0],
                     [0, 0, 1]],
                    [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])
    d12 = [[a2 * cos(theta1)], [a2 * sin(theta1)], [0]]

    H12 = [np.append(R12[0], d12[0][0]),
           np.append(R12[1], d12[1][0]),
           np.append(R12[2], d12[2][0]),
           [0, 0, 0, 1]]

    R23 = np.matmul([[cos(theta2), -sin(theta2), 0],
                     [sin(theta2), cos(theta2), 0],
                     [0, 0, 1]],
                    [[0, 0, 1],
                     [1, 0, 0],
                     [0, 1, 0]])

    d23 = [[a3 * cos(theta2)], [a3 * sin(theta2)], [0]]

    H23 = [np.append(R23[0], d23[0][0]),
           np.append(R23[1], d23[1][0]),
           np.append(R23[2], d23[2][0]),
           [0, 0, 0, 1]]

    H02 = np.matmul(H01, H12)
    H03 = np.matmul(H02, H23)
    return H01, H02, H03


def homogenous_calculator_wrist(theta4, theta5, theta6, a1, a2, a3):
    global H01, H02, H12, H03

    R34 = np.matmul([[cos(theta4), -sin(theta4), 0],
                     [sin(theta4), cos(theta4), 0],
                     [0, 0, 1]],
                    [[0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 0]])
    d34 = [[0], [0], [0.6]]

    H34 = [np.append(R34[0], d34[0][0]),
           np.append(R34[1], d34[1][0]),
           np.append(R34[2], d34[2][0]),
           [0, 0, 0, 1]]

    R45 = np.matmul([[cos(theta5), -sin(theta5), 0],
                     [sin(theta5), cos(theta5), 0],
                     [0, 0, 1]],
                    [[0, 0, 1],
                     [1, 0, 0],
                     [0, 1, 0]])

    d45= [[0.1 * cos(theta5)], [0.1 * sin(theta5)], [0]]

    H45= [np.append(R45[0], d45[0][0]),
           np.append(R45[1], d45[1][0]),
           np.append(R45[2], d45[2][0]),
           [0, 0, 0, 1]]

    R56= np.matmul([[cos(theta6), -sin(theta6), 0],
                     [sin(theta6), cos(theta6), 0],
                     [0, 0, 1]],
                    [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

    d56 = [[0], [0], [0.1]]

    H56 = [np.append(R56[0], d45[0][0]),
           np.append(R45[1], d45[1][0]),
           np.append(R45[2], d45[2][0]),
           [0, 0, 0, 1]]

    H02 = np.matmul(H01, H12)
    H03 = np.matmul(H02, H23)
    return H01, H02, H03


def wrist_homonogenous_matrix_calculator(articalateOrientation, desiredOrientation):
    R36 = np.matmul(np.linalg.inv(articalateOrientation), desiredOrientation)
    theta5 = math.acos(R36[2, 2])
    theta4 = math.acos(R36[1, 2] / sin(theta5))
    theta6 = math.acos(R36[2, 0] / -sin(theta5))
    return theta4, theta5, theta6, R36


def get_position_from_homogenous_matrix(frame):
    if frame == 1:
        pos = np.matmul(H01, [[0], [0], [-2], [1]])
        return vector(pos[0][0], pos[1][0], pos[2][0])
    if frame == 2:
        pos = np.matmul(H02, [[0], [0], [-2], [1]])
        return vector(pos[0][0], pos[1][0], pos[2][0])
    if frame == 3:
        pos = np.matmul(H03, [[0], [0], [0], [1]])
        return vector(pos[0][0], pos[1][0], pos[2][0])
