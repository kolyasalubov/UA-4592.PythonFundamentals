# HW 09
# Task 1

import random

num = random.randint(1, 100)
user_num = 0
number_of_lives = 10

def num_more_or_less():
    global user_num, num
    if user_num < num:
        print("Your number should be bigger")
    elif user_num > num:
        print("Your number should be smaller")

def check_lives():
    global number_of_lives, user_num, num
    if user_num != num:
        number_of_lives -= 1

def restart_game():
    global num, number_of_lives, user_num
    num = random.randint(1, 100)
    number_of_lives = 10
    user_num = 0
    print("Game restarted! You have 10 attempts.")

def start_game():
    global user_num, num, number_of_lives
    print("Welcome to the Number Guessing Game!")
    
    while number_of_lives > 0:
        user_num = int(input("Guess the number from 0 to 100: "))
        
        if user_num == num:
            print(f"You guessed the number {num} correctly! You win!")
            restart_game()
            continue
        
        num_more_or_less()
        check_lives()
        print(f"You have {number_of_lives} attempts left.\n")
    
    print(f"You lost, the correct number was {num}")
    restart_game()

start_game()
