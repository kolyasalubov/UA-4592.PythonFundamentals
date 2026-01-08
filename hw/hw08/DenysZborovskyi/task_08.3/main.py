from areas import rectangle_area, triangle_area, circle_area

figure = input("Choose figure (rectangle / triangle / circle): ")

if figure == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print(rectangle_area(a, b))

elif figure == "triangle":
    a = float(input("Enter base a: "))
    h = float(input("Enter height h: "))
    print(triangle_area(a, h))

elif figure == "circle":
    r = float(input("Enter radius r: "))
    print(circle_area(r))

else:
    print("Wrong figure")

