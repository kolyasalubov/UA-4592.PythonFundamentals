# Write a Python program to check the validity of a password (input from users).
# Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

def rules():
    print ("At least 1 letter between [a-z] and 1 letter between [A-Z].")
    print ("At least 1 number between [0-9].")
    print ("At least 1 character from [$#@].")
    print ("Minimum length 6 characters.")
    print ("Maximum length 16 characters.")

def validation(password: str):
    if len(password) < 6: 
        return print("Minimum length 6 characters.")
    
    elif len(password) > 16:
        return print("Maximum length 16 characters.")
    
    elif not any(char.isupper() for char in password):
        return print("1 letter between [A-Z].")
        
    elif not any(char.islower() for char in password):
        return print("At least 1 letter between [a-z]")
    
    elif not any(char.isdigit() for char in password):
        return print("At least 1 number between [0-9].")
    
    elif not ("$" in password or "#" in password or "@" in password):
        return print("At least 1 character from [$#@]")
    
    else:
        return print("Password is valid.")
