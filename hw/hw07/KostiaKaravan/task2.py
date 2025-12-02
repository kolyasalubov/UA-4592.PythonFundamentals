def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height 

def circle_area(radius):
    return 3.14 * radius ** 2


print ("What you want to calculate area for?")

print ("1 - Rectangle")
print ("2 - Triangle")  
print ("3 - Circle")
choice = input("Enter number (1/2/3): ")
if choice == '1':
    l = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    print("Area of rectangle is:", rectangle_area(l, w))
elif choice == '2':
    b = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    print("Area of triangle is:", triangle_area(b, h))
elif choice == '3':
    r = float(input("Enter radius of circle: "))
    print("Area of circle is:", circle_area(r))