from random import randint

print("Enter number from 0 to 100: ")
x = int(input())

z = False
y = randint(0, 100)
for i in range(10):
    if x < y:
        print("Your number is less than the hidden one")
    elif x > y:
        print("Your number is greater than the hidden one")
    else:
        print("You win!")
        z = True
        break
    print("Enter number from 0 to 100: ")
    x = int(input())

    if z == False and i == 9:
        print("You lose! The hidden number was", y)