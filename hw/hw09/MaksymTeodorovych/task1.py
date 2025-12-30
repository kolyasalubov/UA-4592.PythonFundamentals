import random
i = 0
random_number = random.randint(1,100) 
print(random_number)
while i < 10:
    if int(input("Введіть число: ")) == random_number:
        print("Вітаю, ви вгадали!!!")
        break
    else:
        print("Спробуйте ще раз:")
        i += 1
else:
    print("Ви зробили більше 10 спроб, гру закінчено")