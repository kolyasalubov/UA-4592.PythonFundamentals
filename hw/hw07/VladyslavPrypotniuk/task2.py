def triangle_area(a: float, h: float) -> float:
    return a * h * 0.5

def rectangle_area(a: float, b: float) -> float:
    return a * b

def circle_area(r: float) -> float:
    PI = 3.14
    return PI * r**2


figure = input("Enter a figure (rectangle,triangle,circle):")

match figure:
    case 'circle':
        r = float(input("Enter the radius:"))
        area = circle_area(r)
        print(f"Area:{area} m2")
    case 'triangle':
        a = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        area = triangle_area(a, h)
        print(f"Area:{area} m2")
    case 'rectangle':
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        area = rectangle_area(a, b)
        print(f"Area:{area} m2")
    case _:
        print("Unknown figure")

