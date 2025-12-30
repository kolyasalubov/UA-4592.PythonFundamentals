
#==========task1===========
# class Polygon:
#     """
#     docstring Polygon
#     """
    
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
        
#     def inputSides(self):
#         self.sides = [float(input(f"Enter side {str(i+1)}: ")) 
#                                               for i in range(self.n)]
    
#     def dispSides(self):
#         for i in range(self.n):
#             print(f"Side {i+1} is {self.sides[i]}")
 
            
# class Triangle(Polygon):
#     """
#     docstring Triangle
#     """
#     def __init__(self):
#         # Polygon.__init__(self, 3)
#         super().__init__(3)
                
#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         if a + b <= c or a + c <= b or c + b <= a:
#             return print("a triangle with such sides is impossible")
#         p = (a + b + c) / 2
#         area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
#         print(f"The area of the triangle is {round(area, 2)}")  

# t1 = Triangle()
# t1.inputSides()
# t1.dispSides()
# t1.findArea()
#==========task2===========
# class Human():
#     def __init__(self, name):
#         self.name = name
        
#     def display_message(self):
#         print(f"Hello, {self.name}")
        
#     @classmethod
#     def class_homo(cls):
#         print("Homosapiens")
    
#     @staticmethod
#     def arbitrary_message():
#         return "Welcome"
    
# human1 = Human("Tom")
# human1.display_message()
# Human.class_homo()
# print(human1.arbitrary_message())
#==========task3===========
# class Employee():
    
#     counter = 0
#     all_employee = {}
    
#     def __init__(self, name, salary):
#         """
#         Docstring for __init__
        
#         :param self: Description
#         :param name: Description
#         :param salary: Description
#         """
#         self.name = name
#         self.salary = salary
#         Employee.counter += 1
#         Employee.all_employee.update({self.name : self.salary})
    
#     @staticmethod
#     def total_number():
#         """
#         Docstring for total_number
#         """
#         print(f"Total number of employees: {Employee.counter}")
        
#     @staticmethod
#     def display_all_employee():
#         """
#         Docstring for display_all_employee
#         """
#         Employee.all_employee = Employee.all_employee.items()
#         for i in Employee.all_employee:
#             print(f"Name: {i[0]}, Salary: {i[1]}")

# emp1 = Employee("Tom", 1000)
# emp2 = Employee("Emma", 1500)
# Employee.total_number()
# Employee.display_all_employee()

# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)