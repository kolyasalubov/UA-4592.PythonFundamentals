import random

num = random.randint(1,100)
attemps = 0;

win = False;
while attemps < 9:
    guess_num = int(input("Select number in range from 1 to 100: "))
    if guess_num == num:
        win = True
        break
    else:
        if guess_num > num:
            print(f"Random num is less than {guess_num}")
        else:
            print(f"Random num is greater than {guess_num}")

message = f"You lose, random number was {num}" 
if win:
    message = f"You WON! Random number was {num}"

print(message)