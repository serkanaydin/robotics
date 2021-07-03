import time
from vpython import *
from ThreeDegree import ThreeDegree
from homogenousMatrixFinder import *
from inverseKinematics import *
from JacobianCalculator import *

articulate = ThreeDegree()

a1 = 10
a2 = 12
a3 = 12

theta0, theta1, theta2 = getAngles(10, 10, 10, a1, a2, a3)

H01, H02, H03 = homogenous_calculator(theta0, theta1, theta2, a1, a2, a3)

articulate.joint1.pos = get_position_from_homogenous_matrix(1)
articulate.joint2.pos = get_position_from_homogenous_matrix(2)

a1c = curve(vector(0, 0, 0), vector(0, 0, a1))
a2c = curve(vector(0, 0, a1), get_position_from_homogenous_matrix(2))
a3c = curve(get_position_from_homogenous_matrix(2), get_position_from_homogenous_matrix(3))

wrist = ThreeDegree(0.6, 0.3, get_position_from_homogenous_matrix(3), vector(0, 0, 1),
                    get_position_from_homogenous_matrix(3) + vector(0, -0.3, 0.9), vector(0, 1, 0),
                    get_position_from_homogenous_matrix(3) + vector(0, 0, 1.2), vector(0, 0, 1))
a4c = curve(wrist.joint0.pos, wrist.joint1.pos)
a5c = curve(wrist.joint1.pos, wrist.joint2.pos)
a6c = curve(wrist.joint2.pos, wrist.joint2.pos + 2 * wrist.joint2.axis)

desiredOrientation = [[cos(math.radians(45)), -sin(math.radians(45)), 0],
                      [sin(math.radians(45)), cos(math.radians(45)), 0],
                      [0, 0, 1]]
case=0
path=curve(pos=get_position_from_homogenous_matrix(3),color=vector(0.5,0.5,0))
while True:
    jacobian = calculate_jacobian(H01, H02, H03)

    if (H03[0][3] < 12 and case == 0):
        dTheta0, dTheta1, dTheta2 = (1 * np.matmul(np.linalg.inv(jacobian), [0.6, 0.8, 0])) * 0.2
    elif (H03[0][3] >12 and case == 0):
        case = 1
    elif H03[0][3] < 15 and case == 1:
        dTheta0, dTheta1, dTheta2 = (1 * np.matmul(np.linalg.inv(jacobian), [0.8, -0.6, 0])) * 0.2
    elif H03[0][3] > 15 and case == 1:
        print("debug")
        case = 2
    elif H03[0][3] > 13.3 and case == 2:
        print("right")
        dTheta0, dTheta1, dTheta2 = (1 * np.matmul(np.linalg.inv(jacobian), [-0.6, -0.8, 0])) * 0.2
    elif H03[0][3] <13.3 and case == 2:
        case=3
    elif H03[0][3] > 9.9 and case == 3:
        dTheta0, dTheta1, dTheta2 = (1 * np.matmul(np.linalg.inv(jacobian), [-0.8, +0.6, 0])) * 0.2
    else:
        break

    theta0 += dTheta0
    theta1 += dTheta1
    theta2 += dTheta2
    H01, H02, H03 = homogenous_calculator(theta0, theta1, theta2, a1, a2, a3)
    path.append(get_position_from_homogenous_matrix(3))
    print(get_position_from_homogenous_matrix(3))

    articulateOrientation = np.array([H03[0][0:3], H03[1][0:3], H03[2][0:3]])
    theta4, theta5, theta6, R36 = wrist_homonogenous_matrix_calculator(articulateOrientation, desiredOrientation)

    wrist.joint0.axis = vector(R36[0][0], R36[1][0], R36[2][0])
    wrist.joint1.axis = vector(R36[0][1], R36[1][1], R36[2][1])
    wrist.joint2.axis = vector(R36[0][2], R36[1][2], R36[2][2])

    articulate.joint1.pos = get_position_from_homogenous_matrix(1)
    joint1_axis = np.matmul(H01, [[0], [0], [1], [0]])
    articulate.joint1.axis = vector(joint1_axis[0][0], joint1_axis[1][0], joint1_axis[2][0])
    articulate.joint1.length = 4

    articulate.joint2.pos = get_position_from_homogenous_matrix(2)
    joint2_axis = np.matmul(H02, [[0], [0], [1], [0]])
    articulate.joint2.axis = vector(joint2_axis[0][0], joint2_axis[1][0], joint2_axis[2][0])
    articulate.joint2.length = 4

    a2c.pop()
    a2c.append(get_position_from_homogenous_matrix(2)+vector(1,0,0))
    a3c.pop()
    a3c.pop()
    a3c.append(get_position_from_homogenous_matrix(2)+vector(1,0,0))
    a3c.append(get_position_from_homogenous_matrix(3))
    wrist.joint0.pos = get_position_from_homogenous_matrix(3)
    wrist.joint1.pos = get_position_from_homogenous_matrix(3) + vector(0, -0.3, 0.9)
    wrist.joint2.pos = get_position_from_homogenous_matrix(3) + vector(0, 0, 1.2)
    a4c.pop()
    a4c.pop()
    a5c.pop()
    a5c.pop()
    a6c.pop()
    a6c.pop()
    a4c.append(wrist.joint0.pos)
    a4c.append(wrist.joint1.pos)
    a5c.append(wrist.joint1.pos)
    a5c.append(wrist.joint2.pos)
    a6c.append(wrist.joint2.pos)
    a6c.append(wrist.joint2.pos + 2 * wrist.joint2.axis)
    time.sleep(1)
