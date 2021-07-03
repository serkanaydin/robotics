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
desiredOrientation = np.array([[cos(math.radians(45)), -sin(math.radians(45)), 0],
                      [sin(math.radians(45)), cos(math.radians(45)), 0],
                      [0, 0, 1]])
H01, H02, H03,H04,H05,H06 = homogenous_calculator(theta0, theta1, theta2, a1, a2, a3,desiredOrientation)
articulate.joint1.pos = get_position_from_homogenous_matrix(1)
articulate.joint2.pos = get_position_from_homogenous_matrix(2)

a1c = curve(vector(0, 0, 0), vector(0, 0, a1))
a2c = curve(vector(0, 0, a1), get_position_from_homogenous_matrix(2))
a3c = curve(get_position_from_homogenous_matrix(2), get_position_from_homogenous_matrix(3))

wrist = ThreeDegree(0.6, 0.3, get_position_from_homogenous_matrix(3), vector(0, 0, 1),
                    get_position_from_homogenous_matrix(4),get_position_from_homogenous_matrix(5),
                    get_position_from_homogenous_matrix(6), vector(0, 0, 1))
end =curve(get_position_from_homogenous_matrix(5),get_position_from_homogenous_matrix(6))
case=0
path=curve(pos=get_position_from_homogenous_matrix(6),color=vector(0.5,0.5,0))
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
    H01, H02, H03,H04,H05,H06= homogenous_calculator(theta0, theta1, theta2, a1, a2,a3, desiredOrientation)
    print(H06)
    articulate.joint1.pos = get_position_from_homogenous_matrix(1)
    joint1_axis = np.matmul(H01, [[0], [0], [1], [0]])
    articulate.joint1.axis = vector(joint1_axis[0][0], joint1_axis[1][0], joint1_axis[2][0])
    articulate.joint1.length = 4

    articulate.joint2.pos = get_position_from_homogenous_matrix(2)
    joint2_axis = np.matmul(H02, [[0], [0], [1], [0]])
    articulate.joint2.axis = vector(joint2_axis[0][0], joint2_axis[1][0], joint2_axis[2][0])
    articulate.joint2.length = 4

    wrist.joint0.pos = get_position_from_homogenous_matrix(3)
    joint3_axis = np.matmul(H03, [[0], [0], [1], [0]])
    wrist.joint0.axis = vector(joint3_axis[0][0], joint3_axis[1][0], joint3_axis[2][0])
    wrist.joint0.length = 0.1

    wrist.joint1.pos = get_position_from_homogenous_matrix(4)
    joint4_axis = np.matmul(H04, [[0], [0], [1], [0]])
    wrist.joint1.axis = vector(joint4_axis[0][0], joint4_axis[1][0], joint4_axis[2][0])
    wrist.joint1.length = 0.1

    wrist.joint2.pos = get_position_from_homogenous_matrix(5)
    joint5_axis = np.matmul(H05, [[0], [0], [1], [0]])
    wrist.joint2.axis = vector(joint5_axis[0][0], joint5_axis[1][0], joint5_axis[2][0])
    wrist.joint2.length = 0.1

    a2c.pop()
    a2c.append(get_position_from_homogenous_matrix(2)+ articulate.joint2.axis /2)
    a3c.pop()
    a3c.pop()
    a3c.append(get_position_from_homogenous_matrix(2)+ articulate.joint2.axis/2)
    a3c.append(get_position_from_homogenous_matrix(3))
    end.pop()
    end.pop()

    end.append(get_position_from_homogenous_matrix(5))
    end.append(get_position_from_homogenous_matrix(6))
    path.append(get_position_from_homogenous_matrix(6))

    time.sleep(1)
