import math


def getAngles(X, Y, Z, a1, a2, a3):
    r1 = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))
    r2 = Z - a1
    r3 = math.sqrt(math.pow(r1, 2) + math.pow(r2, 2))
    fi2 = math.atan(r2 / r1)
    fi1 = math.acos((math.pow(a3, 2) - math.pow(a2, 2) - math.pow(r3, 2)) / (-2 * a2 * r3))
    fi3 = math.acos((math.pow(r3, 2) - math.pow(a3, 2) - math.pow(a2, 2)) / (-2 * a2 * a3))
    theta1 = math.atan(Y / X)
    theta2 = fi2 - fi1
    theta3 = math.pi - fi3
    return theta1, theta2, theta3
