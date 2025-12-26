# ========== Task 1 ===========

def largest_of_two_numbers(arg1: float, arg2: float) -> float:
    """Return the largest of two numbers.
    Args: arg1 (float): _description_
        arg2 (float): _description_  """
    if arg1 > arg2:
        return arg1
    else:
        return arg2
print(largest_of_two_numbers(10, 20)) 
print(largest_of_two_numbers(15, -2))  

# ========= Task 2 ===========

PI = 3.14159

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius.
    Args: radius (float): _description_

    Returns: float: _description_
    """
    circle_area = PI * radius ** 2
    return circle_area

def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width.
    Args:
        length (float): _description_
        width (float): _description_

    Returns: float: _description_
    """
    rectangle_area = length * width
    return rectangle_area

def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle given its base and height.
    Args:
        base (float): _description_
        height (float): _description_
    Returns: float: _description_
    """
    triangle_area = 0.5 * base * height
    return triangle_area

choice = input("Enter the area you want to calculate (circle, rectangle, triangle): ").strip().lower()

if choice == "circle":
    r = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(r)
    print(f"The area of the circle is: {area}")
elif choice == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is: {area}")



# ========= Task 3 ===========

word = input("Enter a word: ")

def count_chars(word):
    """
    Count the occurrences of each character in a word.
    """
    result = {}
    for char in word:
        if char in result:
            result[char] +=1
        else:
            result[char] = 1
    return result

print(count_chars(word))
    
