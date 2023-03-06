# @title 3D кольцо

import numpy as np
from math import *
import os


def get_empty_screen(size_of_screen):
    scr = [[empty for n in range(size_of_screen[0])] for m in range(size_of_screen[1])]
    return scr


def show_it(what):
    for i in what:
        print("".join(i))


def get_vectors_lenght(p1, p2):
    lenght = sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)

    return lenght


class Sphere:
    def __init__(self, size_of_screen, R=5):
        self.R = R
        self.size_of_screen = size_of_screen

        self.coords_in_2D = []
        self.adapted_coords = []
        self.sphere_coords = []
        self.coords_with_depht = []

        self.point = np.array([1, 0, 0])
        self.light = np.array([1.5, 2, 1])
        self.next_lite = []
        self.colors = [" ", ".", ":", "c", "O"]
        self.length_massive = []

        self.columns_center = size_of_screen[0] // 2
        self.rows_center = size_of_screen[1] // 2
        self.h = (self.columns_center / self.rows_center) / 2

    def get_sphere_coords(self):
        self.sphere_coords.clear()

        alpha = beta = 0
        d = 60

        for i in range(d):
            rotation_Y = np.array([[cos(alpha), 0, sin(alpha)],
                                   [0, 1, 0],
                                   [-sin(alpha), 0, cos(alpha)]])

            next_point = np.dot(self.point, rotation_Y)

            alpha += 6.3 / d

            for i in range(d):
                rotation_Z = np.array([[cos(beta), -sin(beta), 0],
                                       [sin(beta), cos(beta), 0],
                                       [0, 0, 1]])

                rotation_X = np.array([[1, 0, 0],
                                       [0, cos(beta), -sin(beta)],
                                       [0, sin(beta), cos(beta)]])

                # double_rotation = np.dot(rotation_X, rotation_Z)

                self.sphere_coords.append(np.dot(next_point, rotation_Z))
                beta += 6.3 / d

    def get_2D_coords(self):
        self.coords_in_2D.clear()

        to_2D = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]])

        for p in self.sphere_coords:
            self.coords_in_2D.append(np.dot(p, to_2D))

        return self.coords_in_2D

    def get_rotate_light(self, angle):
        self.next_lite = []

        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])

        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])

        double_rotation = np.dot(rotation_Z, rotation_X)

        self.next_lite = np.dot(self.light, double_rotation)

    def get_adapted_coords(self):
        self.adapted_coords.clear()
        self.length_massive.clear()

        for p in self.coords_in_2D:
            x, y = p[0], p[1]
            l = get_vectors_lenght(p, self.next_lite)

            self.length_massive.append(l)
            self.adapted_coords.append(
                [round(x * self.R * self.h + self.columns_center), round(y * self.h / 2 * self.R + self.rows_center),
                 l])

    def draw_it(self):
        scr = get_empty_screen(size_of_screen)
        m = max(self.length_massive)

        for p in self.adapted_coords:
            l = p[2]

            if l > m * 0.95:
                scr[p[1]][p[0]] = self.colors[4]

            elif m * 0.95 > l > m * 0.9:
                scr[p[1]][p[0]] = self.colors[3]

            elif m * 0.9 > l > m * 0.8:
                scr[p[1]][p[0]] = self.colors[2]

            elif m * 0.5 > l > m * 0.8:
                scr[p[1]][p[0]] = self.colors[1]

            elif m * 0.5 > l:
                scr[p[1]][p[0]] = self.colors[0]

        return scr


size_of_screen = (120, 30)

empty = " "

sp = Sphere(size_of_screen, 7)

a = 0
while a <= 10:
    os.system("cls")

    sp.get_sphere_coords()
    sp.get_2D_coords()
    sp.get_rotate_light(a)
    sp.get_adapted_coords()
    sphere = sp.draw_it()

    show_it(sphere)

    a += 0.1
