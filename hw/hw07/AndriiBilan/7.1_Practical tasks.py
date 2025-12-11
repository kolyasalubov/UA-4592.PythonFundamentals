def largest_num(num1:int, num2:int):
    """
    Function returns the largest number of two numbers
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None
    
#------------------------------------------------------
import math

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
    area = math.pi * radius**2
    return round(area, 2)
    
def main():
    """
    Main function that calls functions that calculate areas of different shapes depending on users choise
    """
    print("Enter the number for a shape you want to calculate area for.\n1: rectangle\n2: triangle\n3: circle")
    user_input = input("Shape:")
    if user_input == "1":
        print("Area of a rectangle")
        user_length = float(input("Enter length of a rectengle: "))
        user_wigth = float(input("Enter wigth of a rectengle: "))
        print(area_rectangle(user_length, user_wigth))
    elif user_input == "2":
        print("Area of a triangle")
        user_base = float(input("Enter base of a triangle: "))
        user_height = float(input("Enter height of a triangle: "))
        print(area_triangle(user_base, user_height))
    elif user_input == "3":
        print("Area of a circle")
        user_radius = float(input("Enter radius of a circle: "))
        print(area_circle(user_radius))
    else:
        print("Wrong input")

#---------------------------------------------------------------------
def char_in_string(word:str):
    parsed = list(set(word))
    result = {}
    for char_parsed in parsed:
        count = 0
        for char in word:
            if char == char_parsed:
                count += 1
        result[char_parsed] = count
    return result




