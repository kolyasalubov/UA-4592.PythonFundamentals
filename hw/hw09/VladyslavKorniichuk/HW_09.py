import random
guess = 0
count = 0
num = random.randint(1, 100)

while guess != num and count < 10:
    guess = int(input("guess the number from 1 to 100: "))
    if guess > num:
        print("Lower")
        count += 1
    elif guess < num:
        print("Higher")
        count += 1
    else:
        print(f"Congrats the number was", num)

if count == 10:
    print("Game over ;(")





