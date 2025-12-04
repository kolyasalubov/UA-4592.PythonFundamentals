# task 1
# ==================================================

def max_of_two(a, b):
	"""
    Returns the larger of two numbers.

    Parameters:
        a (int or float): the first number.
        b (int or float): the second number.

    Returns:
        int or float: the greater of the two numbers.
    """
	if a > b:
		return a
	else:
		return b


print(max_of_two(10, 7))



# task 2
# ==================================================

import math

def rectangle_area(width, height):
    """
    Returns the area of a rectangle.

    Parameters:
        width (float): the width of the rectangle.
        height (float): the height of the rectangle.

    Returns:
        float: the area of the rectangle.
    """
    return width * height


def triangle_area(base, height):
    """
    Returns the area of a triangle.

    Parameters:
        base (float): the base of the triangle.
        height (float): the height of the triangle.

    Returns:
        float: the area of the triangle.
    """
    return 0.5 * base * height


def circle_area(radius):
    """
    Returns the area of a circle.

    Parameters:
        radius (float): the radius of the circle.

    Returns:
        float: the area of the circle.
    """
    return math.pi * radius ** 2


# --- Main program ---
print("Choose a shape to calculate the area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Your choice: ")

if choice == "1":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Area of rectangle:", rectangle_area(w, h))

elif choice == "2":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of triangle:", triangle_area(b, h))

elif choice == "3":
    r = float(input("Enter radius: "))
    print("Area of circle:", circle_area(r))

else:
    print("Invalid choice!")



# task 3
# ==================================================

def count_characters(s):
    """
    Returns a dictionary showing how many times each character
    appears in the given string.

    Parameters:
        s (str): input string

    Returns:
        dict: dictionary {character: count}
    """
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


# Example:
print(count_characters("hello"))

