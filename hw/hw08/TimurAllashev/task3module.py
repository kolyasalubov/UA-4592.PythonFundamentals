import math
def calculate_area_of_circle() -> float:
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius * 2

def calculate_area_of_rectangle() -> float:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def calculate_area_of_triangle() -> float:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height