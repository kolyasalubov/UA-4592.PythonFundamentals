import math

def calculates_rectangle_area(rectangle_length: float, rectangle_width: float) -> float:
    """this function calculate 
    the area of a rectangle"""
    rectangle_area = rectangle_length * rectangle_width
    return rectangle_area


def calculates_triangle_area(triangle_side_lenght: float, triangle_height_lenght: float) -> float:
    """this function calculate
    the area of a triangle"""
    triangle_area = 1/2 * triangle_side_lenght * triangle_height_lenght
    return triangle_area


def calculates_circle_area(circle_radius: float) -> float:
    """this function calculate
    the area of a circle"""
    circle_area = math.pow(circle_radius,2) * math.pi
    return circle_area

