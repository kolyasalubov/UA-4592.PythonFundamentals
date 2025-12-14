"""Main program for calculating areas"""
import areas


print("Calculate area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Choose a shape (1/2/3): ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    result = areas.area_of_rectangle(a, b)
    print(f"Area of rectangle: {result}")

elif choice == "2":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    result = areas.area_of_triangle(h, a)
    print(f"Area of triangle: {result}")

elif choice == "3":
    r = float(input("Enter radius r: "))
    result = areas.area_of_circle(r)
    print(f"Area of circle: {result}")

else:
    print("Invalid choice!")