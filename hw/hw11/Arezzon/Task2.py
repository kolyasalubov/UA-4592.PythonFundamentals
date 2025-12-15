# 2. Write a program that analyzes the entered number and, depending on the number, gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data.

day = input("Please enter a number (1-7) to get the corresponding day of the week: ")

def get_day_of_week(day_number):
    days = { 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    if day_number < 1 or day_number > 7:
        raise ValueError("Number must be between 1 and 7.")
    return days[day_number]
try:
    day_number = int(day)
    day_name = get_day_of_week(day_number)
    print(f"The day corresponding to number {day_number} is {day_name}.")  
except ValueError as e:
    print(f"Error: {e}") 