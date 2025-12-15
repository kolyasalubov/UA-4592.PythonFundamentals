import random

num = random.randint(1,100)
print("You have 10 attempts to guess the number")

for attempt in range(10):
    user_num = int(input("Guess the number: "))
    if user_num < num:
        print("Wrong! The number is bigger")
    elif user_num > num:
        print("Wrong! The number is smaller")
    else:
        print(f"You guessed right! the number is {num}")
        break
    print(f"Attempts left: {9-attempt}")
    if attempt == 9:
        print("You lost!")