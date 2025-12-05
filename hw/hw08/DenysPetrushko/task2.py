# HW 08 Task 2
# ==============================================
# variant 1
# Use Python.re
# ==============================================

import re

def validate_password(password):
    # Regex pattern
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
    
    if re.fullmatch(pattern, password):
        return True
    else:
        return False


# Get password from user
pwd = input("Enter your password: ")

if validate_password(pwd):
    print("Valid password.")
else:
    print("Invalid password.")


# ==============================================
# variant 2
# Use only Python
# ==============================================

def validate_password(password):
    # Conditions
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "$#@"

    # Check length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check each character
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_lower and has_upper and has_digit and has_special


# Get password from user
pwd = input("Enter your password: ")

if validate_password(pwd):
    print("Valid password.")
else:
    print("Invalid password.")

