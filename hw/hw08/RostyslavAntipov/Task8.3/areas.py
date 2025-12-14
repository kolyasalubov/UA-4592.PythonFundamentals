"""Module with functions for calculating areas"""
from math import pi, pow  # Импортируем из встроенного модуля math!


def area_of_rectangle(a, b):
    """Rectangle area: S = a * b"""
    return a * b


def area_of_triangle(h, a):
    """Triangle area: S = 0.5 * h * a"""
    return 0.5 * h * a


def area_of_circle(r):
    """Circle area: S = pi * r ** 2"""
    return pi * pow(r, 2)