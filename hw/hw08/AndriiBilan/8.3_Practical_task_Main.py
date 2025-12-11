from custom_area import *

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
        
main()
