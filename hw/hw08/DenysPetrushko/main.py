# Task 3

import areas

def main():
    print("Choose a figure:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        # Rectangle area
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print("Area of rectangle:", areas.rectangle_area(a, b))

    elif choice == "2":
        # Triangle area
        a = float(input("Enter base a: "))
        h = float(input("Enter height h: "))
        print("Area of triangle:", areas.triangle_area(a, h))

    elif choice == "3":
        # Circle area
        r = float(input("Enter radius r: "))
        print("Area of circle:", areas.circle_area(r))

    else:
        print("Invalid choice.")


main()
