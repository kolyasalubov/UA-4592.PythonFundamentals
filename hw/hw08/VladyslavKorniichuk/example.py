# task 1
# import re
#
# correct_psw = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"
# password = input("Give me ur password: ")
#
# if re.fullmatch(correct_psw, password):
#     print("passed")
# else:
#     print("rejected, ur password should contain:")
#     print("at least 1 lowercase letter (a-z) and 1 uppercase (A-Z)")
#     print("at least 1 number (0-9), at least 1 special character")
#     print("min length 6 char, max length 16 char")

# task 2

import math
from math import pow, pi

def rectangle(num1, num2):
    formula = num1 * num2
    print(f"The area of rectangle is: ", formula)

def triangle(num1, num2):
    formula = (0.5 * num1 * num2)
    print(f"The area of triangle is: ", formula)

def circle(num1):
    formula = round(math.pi * math.pow(num1, 2), 2)
    print(f"The area of circle is: ", formula)

