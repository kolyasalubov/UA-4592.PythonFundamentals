#--------task1-------
# class MyError(Exception):
#     def __init__(self, number):
#         self.number = number
#     def __str__(self):
#         return repr(f"You input negative number: {self.number}. Try again.")
    
# def check_age(age_str):
#     try:
#         age = int(age_str)
#         if age < 0:
#             raise MyError(age)
#         if age % 2 == 0:
#             return "Ваш вік парний"
#         else:
#             print('Ваш вік непарний')
#     except ValueError:
#         return f"Ви введи невірний вік"
#     except MyError as e:
#         return str(e)
        
# age = input("Введіть ваш вік: ")
# print(check_age(age))

#--------task2-------

# class MyError(Exception):
#     def __init__(self, number):
#         self.number = number
#     def __str__(self):
#         return repr(f"You input incorect number: {self.number}. Try again.")

# try:
#     number_str = input("Введіть число: ")
#     number = int(number_str)
    
#     match number:
#         case 1:
#             print("Понеділок")
#         case 2:
#             print("Вівторок")
#         case 3:
#             print("Середа")
#         case 4:
#             print("Четвер")
#         case 5:
#             print("П'ятниця")
#         case 6:
#             print("Субота")
#         case 7:
#             print("Неділя")
#         case _:
#             raise MyError(number)
# except MyError as e:
#     print(e)
# except ValueError as j:
#     print(f"Число {number_str} невірне")