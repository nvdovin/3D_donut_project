from math import *
import numpy as np
import os


def show_it(what_to_show):
    for i in what_to_show:
        print("".join(i))


def get_empty_screen(size_of_screen):
    scr = [[empty for n in range(size_of_screen[0])] for m in range(size_of_screen[1])]
    return scr


class Cube:
    def __init__(self, size_of_screen, size=5):
        self.size = size
        self.cube_coords = [np.array([-1, 1, 1]),       # A
                            np.array([-1, -1, 1]),      # B
                            np.array([1, -1, 1]),       # C
                            np.array([1, 1, 1]),        # D
                            np.array([-1, 1, -1]),      # A`
                            np.array([-1, -1, -1]),     # B`
                            np.array([1, -1, -1]),      # C`
                            np.array([1, 1, -1])]       # D`
        self.rotated_coords = []
        self.adapted_coords = []
        self.scaled_coords = []
        self.size_of_screen = size_of_screen

        self.rows_center = self.size_of_screen[1] // 2
        self.columns_center = self.size_of_screen[0] // 2
        self.h = (self.columns_center // self.rows_center) // 2
        self.v = (24 // 11)
        self.line_coords = []

    def get_rotation_coords(self, angle):
        self.rotated_coords.clear()
        self.adapted_coords.clear()

        rotation_X = np.array([[1, 0, 0],
                               [0, cos(angle), -sin(angle)],
                               [0, sin(angle), cos(angle)]])

        rotation_Y = np.array([[cos(angle), 0, sin(angle)],
                               [0, 1, 0],
                               [-sin(angle), 0, cos(angle)]])

        rotation_Z = np.array([[cos(angle), -sin(angle), 0],
                               [sin(angle), cos(angle), 0],
                               [0, 0, 1]])

        double_rotate = np.dot(rotation_Y, rotation_Z)
        tripl_rotate = np.dot(double_rotate, rotation_X)

        interpretate_to_2D = np.array([[1, 0, 0],
                                       [0, 1, 0],
                                       [0, 0, 1]])

        for c in self.cube_coords:
            self.rotated_coords.append(np.dot(c, tripl_rotate))

        for c in self.rotated_coords:
            self.adapted_coords.append(np.dot(c, interpretate_to_2D))

        return self.adapted_coords

    def get_scaled_coords(self):
        self.scaled_coords.clear()

        for c in self.adapted_coords:
            x, y, z = c[0], c[1], (self.size / (self.size / 2) - c[2] / (self.size / (self.size / 2)))

            self.scaled_coords.append([round(x / z * self.size * self.h * self.v + self.columns_center), round(y / z * self.h * self.size + self.rows_center)])

        return self.scaled_coords

    def get_line_foo(self):
        self.line_coords.clear()

        for n in range(4):
            self.line_coords.extend(get_line_coords(self.scaled_coords[n], self.scaled_coords[n+4]))
            if n < 3:
                self.line_coords.extend(get_line_coords(self.scaled_coords[n], self.scaled_coords[n+1]))
                self.line_coords.extend(get_line_coords(self.scaled_coords[n+4], self.scaled_coords[n+5]))
            else:
                self.line_coords.extend(get_line_coords(self.scaled_coords[n-3], self.scaled_coords[n]))
                self.line_coords.extend(get_line_coords(self.scaled_coords[n+1], self.scaled_coords[n+4]))

    def draw_it_all(self):
        work_space = get_empty_screen(size_of_screen)

        for p in self.line_coords:
            work_space[p[1]][p[0]] = line

        for p in self.scaled_coords:
            work_space[p[1]][p[0]] = points

        return work_space


def get_line_coords(a, b):
    line_coords = []

    for n in range(4):
        check = b[0] - a[0]

        x = a[0]

        if a != b:
            if check >= 1:
                while b[0] != x:
                    y = ((b[1] - a[1]) / (b[0] - a[0])) * (x - a[0]) + a[1]
                    x += 1

                    line_coords.append([round(x), round(y)])

            elif check == 0:
                for y in range(a[1], b[1]):
                    line_coords.append([x, y])

            elif check <= -1:
                while b[0] != x:
                    y = ((b[1] - a[1]) / (b[0] - a[0])) * (x - a[0]) + a[1]
                    x -= 1

                    line_coords.append([round(x), round(y)])
        else:
            continue

    return line_coords


empty = " "
points, line = "@", "."

size_of_screen = (160, 40)
screen = get_empty_screen(size_of_screen)

cb = Cube(size_of_screen, 7)

def animate_cube():
    a = 0
    while a <= 10:
        os.system("cls")

        cb.get_rotation_coords(a)
        cb.get_scaled_coords()
        cb.get_scaled_coords()
        cb.get_line_foo()
        cube = cb.draw_it_all()

        show_it(cube)
        a += 0.1

animate_cube()
