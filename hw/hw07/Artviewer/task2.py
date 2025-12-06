type_param = input("Enter entity type (triangle, rectangle, circle): ")

def calculate_entity(type: str) -> float:
    """Calculates area of different geometric entities based on type and arguments."""

    match type:
            case 'rectangle':
                length = float(input("Enter length of the rectangle: "))
                width = float(input("Enter width of the rectangle: "))
                return process_rectangle(length, width)
            case 'triangle':
                base = float(input("Enter base of the triangle: "))
                height = float(input("Enter height of the triangle: "))
                return process_triangle(base, height)
            case 'circle':
                radius = float(input("Enter radius of the circle: "))
                return process_circle(radius)
            case _:
                return "Wrong type"
    

def process_triangle(base: float, height: float) -> float:
    """Processes triangle area calculation."""
    return 0.5 * base * height

def process_rectangle(length: float, width: float) -> float:
    """Processes rectangle area calculation."""
    return length * width

def process_circle(radius: float) -> float:
    """Processes circle area calculation."""
    import math
    return math.pi * radius ** 2

result = calculate_entity(type_param)
print(f"Area of {type_param} is: {result}")