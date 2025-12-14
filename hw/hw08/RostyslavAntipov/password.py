import re
def check_validality_of_password(password: str):
    if len(password) < 6:
        return False
    elif len(password) > 16:
        return False
    elif re.search(r'[a-z]', password) is None:
        return False
    elif re.search(r'[A-Z]', password) is None:
        return False
    elif re.search(r'[0-9]', password) is None:
        return False
    elif re.search(r'[$#@]', password) is None:
        return False
    else:
        return True
password = input("Enter your password: ")
if check_validality_of_password(password):
    print("Valid password")
else:
    print("Invalid password")
    