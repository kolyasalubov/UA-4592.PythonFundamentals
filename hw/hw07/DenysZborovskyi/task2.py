import math

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2


choice = input("Choose shape (rectangle / triangle / circle): ").lower()

if choice == "rectangle":
    w = float(input("Width: "))
    h = float(input("Height: "))
    print(rectangle_area(w, h))

elif choice == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print(triangle_area(b, h))

elif choice == "circle":
    r = float(input("Radius: "))
    print(circle_area(r))

else:
    print("Unknown shape")

