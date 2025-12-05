# HOME WORK
# Task3

import area

print("Choose a figure:")
print("1 — Rectangle")
print("2 — Triangle")
print("3 — Circle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Rectangle area:", area.rectangle_area(w, h))

elif choice == "2":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Triangle area:", area.triangle_area(b, h))

elif choice == "3":
    r = float(input("Enter radius: "))
    print("Circle area:", area.circle_area(r))

else:
    print("Invalid choice!")
