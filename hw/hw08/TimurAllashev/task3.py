import task3module

figure_type = input("Enter the type of figure (circle, rectangle, triangle): ").strip().lower()

match figure_type:
    case "circle":
            area = task3module.calculate_area_of_circle()
    case "rectangle":
            area = task3module.calculate_area_of_rectangle()
    case "triangle":
            area = task3module.calculate_area_of_triangle()
    case _:
        print("Unknown figure type.")
        exit()

print(f"The area of the {figure_type} is: {area}")
