import re
def password_verification(password):
    """this funnction returns the 
    true if password is correct"""
    has_lowercase = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_uppercase = re.search(r"[A-Z]", password) 
    if has_lowercase and has_digit and has_uppercase and 6 < len(password) < 16:
        return True
    else:
        return False 

    
password = input("Enter your password:\n")
if password_verification(password):
    print("Your password is correct")
else:
    print("Your password is incorrect")