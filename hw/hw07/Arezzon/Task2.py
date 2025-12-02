# Task2. Write a program that calculates the area of a rectangle, triangle and circle (write three functions to calculate the area. And call them in the main program depending on the user's choice).

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

print("Choose a figure:")
print("1 — Rectangle")
print("2 — Triangle")
print("3 — Circle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Rectangle area:", rectangle_area(w, h))

elif choice == "2":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Triangle area:", triangle_area(b, h))

elif choice == "3":
    r = float(input("Enter radius: "))
    print("Circle area:", circle_area(r))

else:
    print("Invalid choice!")
