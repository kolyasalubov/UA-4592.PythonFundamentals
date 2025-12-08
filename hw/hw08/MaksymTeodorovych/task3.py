import  task3main 
print('''Програма вираховує площу:
      1.Прямокутника
      2.Трикутника
      3.Кола''')
choice = int(input("Оберіть відповідну цифру: "))
match choice:
    case 1:
        rectangle_length = float(input("Введіть довжину прямокутника:"))
        rectangle_width = float(input("Введіть ширину прямокутника:"))
        print(f"Площа прямокутника = {task3main.calculates_rectangle_area(rectangle_length, rectangle_width)}")
    case 2:
        triangle_side_length = float(input("Введіть довжину сторони трикутника: "))
        triangle_heigth_length = float(input("Введіть довжину висоти трикутника: "))
        print(f"Площа трикутника = {task3main.calculates_triangle_area(triangle_side_length, triangle_heigth_length)}")
    case 3:
        circle_radius = float(input("Введіть радіус кола: "))
        print(f"Площа кола: {task3main.calculates_circle_area(circle_radius)}")
    case _:
        print("Ви ввели невірну цифру")