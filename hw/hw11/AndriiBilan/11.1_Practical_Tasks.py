def check(number):
    if number < 0:
        raise ValueError
    if number % 2 == 1:
        return "Entered number is odd"
    elif number % 2 == 0:
        return "Entered number is even"
try:
    number = int(input("Enter your age: "))
    print(check(number))
except ValueError:
    print("Age can't be negative try again.")

#----------------------------------------------------

def day_week(num):
    try:
        num = int(num)
    except ValueError:
        return "Wrong input! Next time enter a number"
    if int(num) <= 0 or int(num) >= 8:
        raise ValueError("Wrong number! Next time enter a number corresponding to the day of the week")
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return days_of_week[num - 1]

    
user_num = input("Enter a number corresponding to the day of the week: ")
print(day_week(user_num))