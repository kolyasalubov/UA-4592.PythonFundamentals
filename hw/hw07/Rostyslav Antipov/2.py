def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

# Menu
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Choose a shape (1/2/3): ")

if choice == "1":
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(f"Area: {area_of_rectangle(length, width)}")

elif choice == "2":
    base = float(input("Base: "))
    height = float(input("Height: "))
    print(f"Area: {area_of_triangle(base, height)}")

elif choice == "3":
    radius = float(input("Radius: "))
    print(f"Area: {area_of_circle(radius)}")

else:
    print("Invalid choice!")