import re
password = input("Enter your password: ")

allowed = re.match(r'^[A-Za-z0-9$#@]{6,16}$',password)
has_uppercase = bool(re.search(r'[A-Z]', password))
has_lowercase = bool(re.search(r'[a-z]', password))
has_special = bool(re.search(r'[$#@]', password))
has_digit = bool(re.search(r'\d', password))

status = "valid" if allowed and has_uppercase and has_lowercase and has_special and has_digit else "invalid"

print("Your password:", status)