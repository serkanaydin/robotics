import numpy as np


def calculate_jacobian(H01, H02, H03):
    R00 = np.identity(3)
    R01 = np.array(H01)[0:3, 0:3]
    R02 = np.array(H02)[0:3, 0:3]

    d00 = np.array([0, 0, 0])
    d01 = np.array([H01[0][3], H01[1][3], H01[2][3]])
    d02 = np.array([H02[0][3], H02[1][3], H02[2][3]])
    d03 = np.array([H03[0][3], H03[1][3], H03[2][3]])

    firstColumn = np.cross(np.matmul(R00, np.array([0, 0, 1])), np.subtract(d03, d00))
    secondColumn = np.cross(np.matmul(R01, np.array([0, 0, 1])), np.subtract(d03, d01))
    thirdColumn = np.cross(np.matmul(R02, np.array([0, 0, 1])), np.subtract(d03, d02))

    jacobian = [firstColumn, secondColumn, thirdColumn]
    jacobian = np.transpose(jacobian)
    return jacobian
