password = input()

valid = True

if len(password) < 6 or len(password) > 16:
    valid = False

if not any(c.islower() for c in password):
    valid = False

if not any(c.isupper() for c in password):
    valid = False

if not any(c.isdigit() for c in password):
    valid = False

if not any(c in "$#@" for c in password):
    valid = False

if valid:
    print("Valid password")
else:
    print("Invalid password")

