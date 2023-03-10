from math import *
import numpy as np

def rotate(axis, point, angle):
    if axis == "X":
        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])
        return np.dot(point, rotation_X)

    elif axis == "Y":
        rotation_Y = np.array([[cos(angle), 0, sin(angle)],
                               [0, 1, 0],
                               [-sin(angle), 0, cos(angle)]])
        return np.dot(point, rotation_Y)

    elif axis == "Z":
        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])
        return np.dot(point, rotation_Z)

    elif axis == "XY" or axis == "YX":
        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])
        rotation_Y = np.array([[cos(angle), 0, sin(angle)],
                               [0, 1, 0],
                               [-sin(angle), 0, cos(angle)]])
        XY = np.dot(rotation_X, rotation_Y)

        return np.dot(point, XY)

    elif axis == "XZ" or axis == "ZX":
        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])
        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])
        XZ = np.dot(rotation_X, rotation_Z)

        return np.dot(point, XZ)

    elif axis == "YZ" or axis == "ZY":
        rotation_Y = np.array([[cos(angle), 0, sin(angle)],
                               [0, 1, 0],
                               [-sin(angle), 0, cos(angle)]])
        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])
        XY = np.dot(rotation_Y, rotation_Z)

        return np.dot(point, XY)

    elif axis == "XYZ":
        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])
        rotation_Y = np.array([[cos(angle), 0, sin(angle)],
                               [0, 1, 0],
                               [-sin(angle), 0, cos(angle)]])
        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])
        XY = np.dot(rotation_X, rotation_Y)
        YZ = np.dot(rotation_Y, rotation_Z)
        XYZ = np.dot(XY, YZ)

        return np.dot(point, XYZ)


def to_2D(point):
    to_2D = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])
    return np.dot(point, to_2D)
