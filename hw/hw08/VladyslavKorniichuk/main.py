import example

choose = int(input("Choose the figure, to calculate the area of it: 1 for rectangle, 2 for triangle and 3 for circle: "))
if choose == 1:
    num1 = float(input("Enter length: "))
    num2 = float(input("Enter width: "))
    if num1 <= 0 or num2 <= 0:
        print("Error, the value should be greater than 0")
    else:
        example.rectangle(num1, num2)

elif choose == 2:
    num1 = float(input("Enter base: "))
    num2 = float(input("Enter height: "))
    if num1 <= 0 or num2 <= 0:
        print("Error, the value should be greater than 0")
    else:
        example.triangle(num1, num2)

elif choose == 3:
    num1 = float(input("Enter R: "))
    if num1 <= 0:
        print("Error, the value should be greater than 0")
    else:
        example.circle(num1)

else:
    print("invalid number")