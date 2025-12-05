
#====================Task1========================
num1 = 10
num2 = 5

def largest_number(num1: int, num2: int) -> int:
    """this funnction returns the 
    largest number of two numbers"""
    return num1 if num1 > num2 else num2

result = largest_number(num1, num2)
print(f"{result} is largest number")
#=================================================



#====================Task2========================
def calculates_rectangle_area(rectangle_length: float, rectangle_width: float) -> float:
    """this function calculate 
    the area of a rectangle"""
    rectangle_area = rectangle_length * rectangle_width
    return rectangle_area


def calculates_triangle_area(triangle_side_lenght: float, triangle_height_lenght: float) -> float:
    """this function calculate
    the area of a triangle"""
    triangle_area = 1/2 * triangle_side_lenght * triangle_height_lenght
    return triangle_area


def calculates_circle_area(circle_radius: float) -> float:
    """this function calculate
    the area of a circle"""
    PI = 3.14
    circle_area = circle_radius * PI
    return circle_area


print('''Програма вираховує площу:
      1.Прямокутника
      2.Трикутника
      3.Кола''')
choice = int(input("Оберіть відповідну цифру: "))
match choice:
    case 1:
        rectangle_length = float(input("Введіть довжину прямокутника:"))
        rectangle_width = float(input("Введіть ширину прямокутника:"))
        print(f"Площа прямокутника = {calculates_rectangle_area(rectangle_length, rectangle_width)}")
    case 2:
        triangle_side_length = float(input("Введіть довжину сторони трикутника: "))
        triangle_heigth_length = float(input("Введіть довжину висоти трикутника: "))
        print(f"Площа трикутника = {calculates_triangle_area(triangle_side_length, triangle_heigth_length)}")
    case 3:
        circle_radius = float(input("Введіть радіус кола: "))
        print(f"Площа кола: {calculates_circle_area(circle_radius)}")
    case _:
        print("Ви ввели невірну цифру")
#=================================================



#====================Task3========================
def calculate_characters(input_line: str) -> str:
    """this function calculate the number
    of characters included in line"""
    list_of_characters = {}
    result = {}
    for characters in input_line:
        if characters in result:
            continue
        else:
            number_character = input_line.count(characters)
            result.update({characters : number_character})
    return result


print("""Програма рахує кількість символів в рядку""")
input_line = input("Введіть рядок: ")
print(f"У вашому рядку {calculate_characters(input_line)} символів")
#=================================================