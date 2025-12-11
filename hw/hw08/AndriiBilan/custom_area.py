from math import pow, pi

def area_rectangle(length:float, width:float):
    """
    Function returns area of a rectangle it takes length and width of the rectangle as parameters
    """
    area = length * width
    return round(area, 2)

def area_triangle(base:float, height:float, ):
    """
    Function returns area of a tiangle it takes base and hight of the triangle as parameters
    """
    area = 0.5 * base * height
    return round(area, 2)

def area_circle(radius:float):
    """
    Function returns area of a circle it takes radius of the circle as parameter
    """
    area = pi * pow(radius,2)
    return round(area, 2)