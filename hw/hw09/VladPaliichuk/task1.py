import random
import pygame
import sys

number = random.randint(1, 100)
number_attempts = 10
print(number)
for i in range(number_attempts):
    try:
        user_num = int(input("Вгадайте число (1–100): "))
    except ValueError:
        print("Будь ласка, введіть число!")
        continue

    if user_num == number:
        print("Вітаємо! Ви вгадали число")

        pygame.init()
        screen = pygame.display.set_mode((400, 200))

        image = pygame.image.load("hw/hw09/VladPaliichuk/my_image.jpg")
        image = pygame.transform.scale(image, (400, 200))

        screen.blit(image, (0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    elif user_num < number:
        print("Число більше.")
    else:
        print("Число менше.")

    if i == number_attempts - 1:
        print("Ви програли. Номер був:", number)
