import string

def lower_fail_check(password:str):
    """
    Function checks if password has lower case letters
    """
    password_split = list(password)
    fail_check = True
    for char in password_split:
        if char in string.ascii_lowercase:
            fail_check = False
            break 
    return fail_check

def upper_fail_check(password:str):
    """
    Function checks if password has upper case letters
    """
    password_split = list(password)
    fail_check = True
    for char in password_split:
        if char in string.ascii_uppercase:
            fail_check = False
            break 
    return fail_check

def digit_fail_check(password:str):
    """
    Function checks if password has digits
    """
    password_split = list(password)
    fail_check = True
    for char in password_split:
        if char in string.digits:
            fail_check = False
            break 
    return fail_check

def special_fail_check(password:str):
    """
    Function checks if password has special characters
    """
    password_split = list(password)
    fail_check = True
    for char in password_split:
        if char in "$#@":
            fail_check = False
            break 
    return fail_check

def user_input():
    """
    Function allows user to input a password
    """
    u_input = input("Password:")
    return u_input
    

def password_check(password:str):
    """
    Function checks validity of a passsword
    """
    valid = True
    if len(password) < 6:
        print("Too short! Add more characters")
        valid = False
    if len(password) > 16:
        print("Too long! Remove sone characters")
        valid = False
    if lower_fail_check(password):
        print("Add at least 1 letter between [a-z]")
        valid = False
    if upper_fail_check(password):
        print("Add at least 1 letter between [A-Z]")
        valid = False
    if digit_fail_check(password):
        print("Add at least 1 number between [0-9]")
        valid = False
    if special_fail_check(password):
        print("Add at least 1 character from [$#@]")
        valid = False
    if valid:
        print("Password is valid")
    else:
        print("Invalid password! Try again")

password_check(user_input())

#Tests:
#password_check("123")
#password_check("12345867457608945786045876")
#password_check("asdasdasd")
#password_check("AAAAsss")
#password_check("##@")
#password_check("123aaasdD$$")
