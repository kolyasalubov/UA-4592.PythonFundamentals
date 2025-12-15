import random

guess_number = random.randint(1, 100)
print(f"Hidenn num: {guess_number}")

attempts = 10

user_guess = 0

try_for_user = "Try again\nEnter the new number: "

def user_input(str: str = "Enter the number: "):
    global user_guess
    user_guess = int(input(str))

def check(value: int):
    '''
    Check answer from user
    '''
    if value < guess_number:
        print(f"Your number ({value}) is smaller")
        user_input(try_for_user)
        print("==============================")
        check(user_guess)
    elif value > guess_number:
        print(f"Your number ({value}) is bigger")
        user_input(try_for_user)
        print("==============================")
        check(user_guess)
    else:
        print(f"Your number ({value}) is the hidden number. You win")


print("Guess the number GAME")
print("==============================")

user_input()

print("==============================")

check(user_guess)

print("==============================")

