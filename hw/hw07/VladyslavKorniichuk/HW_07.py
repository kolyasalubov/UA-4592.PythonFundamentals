# task 1
# def bigger(num1, num2):
#     """
#     docstring
#     this func returns the greatest value
#     """
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
# print(bigger(10, 5))

# task 2
# def rectangle(num1, num2):
#     formula = num1 * num2
#     print(f"The area of rectangle is: ", formula)
#
# def triangle(num1, num2):
#     formula = (0.5 * num1 * num2)
#     print(f"The area of triangle is: ", formula)
#
# def circle(num1):
#     formula = round(3.14 * num1 ** 2, 2)
#     print(f"The area of circle is: ", formula)
#
# choose = int(input("Choose the figure, to calculate the area of it: 1 for rectangle, 2 for triangle and 3 for circle: "))
# if choose == 1:
#     num1 = float(input("Enter length: "))
#     num2 = float(input("Enter width: "))
#     if num1 <= 0 or num2 <= 0:
#         print("Error, the value should be greater than 0")
#     else:
#         rectangle(num1, num2)
#
# elif choose == 2:
#     num1 = float(input("Enter base: "))
#     num2 = float(input("Enter height: "))
#     if num1 <= 0 or num2 <= 0:
#         print("Error, the value should be greater than 0")
#     else:
#         triangle(num1, num2)
#
# elif choose == 3:
#     num1 = float(input("Enter R: "))
#     if num1 <= 0:
#         print("Error, the value should be greater than 0")
#     else:
#         circle(num1)
#
# else:
#     print("invalid number")

# task 3
# word = input("Enter ur word: ")
#
# def counter(string):
#     string = {}
#     for i in word:
#         if i in string:
#             string[i] = string[i] + 1
#         else:
#             string[i] = 1
#
#     print(string)
#
# counter(word)





