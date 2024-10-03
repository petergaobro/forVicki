import random
from math import sin, cos, pi, log
from tkinter import *

Canvas_width = 640
Canvas_height = 640
Canvas_Center_x = Canvas_width / 2
Canvas_Center_y = Canvas_height / 2
Image_enlarge = 1
Hear_color = "#Fd798f"


def ForVicki(t, shrink_ratio: float = Image_enlarge):
    x = 16 * (sin(t) ** 3)
    y = -(15 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(3 * t))

    x *= shrink_ratio
    y *= shrink_ratio

    x += Canvas_Center_x
    y += Canvas_Center_y
    return int(x), int(y)


def VickiScatterInside(x, y, beta=0.15):
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())

    dx = ratio_x * (x - Canvas_Center_x)
    dy = ratio_y * (x - Canvas_Center_y)

    return x - dx, y - dy


def VickiShrink(x, y, ratio):
    force = -1 / (((x - Canvas_Center_x) ** 2 +
                   (y - Canvas_Center_y) ** 2) * 0.6)
    dx = ratio * (x - Canvas_Center_x)
    dy = ratio * (y - Canvas_Center_y)
    return x - dx, y - dy


def VickiCurve(peter):
    return 2 * (2 * sin(4 * peter)) / (2 * pi)


class MyHeart:
    def __init__(self, generate_frame=20):
        self._points = set()
        self._edge_diffusion_points = set()
        self._center_diffusion_points = set()
        self.all_points = {}
        self.VickiBuild(2000)

        self.random_halo = 1000
        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.VickiCalc(frame)

    def VickiBuild(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = ForVicki(t)
            self._points.add((x, y))

        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = VickiScatterInside(_x, _y, 0.3)
                self._edge_diffusion_points.add((x, y))
        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = VickiScatterInside(x, y, 0.2)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - Canvas_Center_x) ** 2 +
                      (y - Canvas_Center_y) ** 2) * 0.520)
        dx = ratio * force * (x - Canvas_Center_x) + random.randint(-2, 2)
        dy = ratio * force * (y - Canvas_Center_y) + random.randint(-2, 2)

        return x - dx, y - dy

    def VickiCalc(self, generate_frame):
        ratio = 15 * VickiCurve(generate_frame / 15 * pi)
        halo_radius = int(4 + 6 * (1 + VickiCurve(generate_frame / 15 * pi)))
        halo_number = int(3000 + 4000 * abs(VickiCurve(generate_frame / 15 * pi) ** 2))
        all_points = []
        heart_halo_points = set()
