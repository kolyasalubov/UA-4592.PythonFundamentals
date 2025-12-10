# Task3. Create an employee class. Each employee has characteristics such as name and salary. The class should have a counter that calculates the total number of employees, as well as a method that prints the total number of employees and a method that displays information about each employee in particular, namely the name and salary.
# In addition to creating a class, display information about the base classes from which the employee class is inherited (_base_), the class namespace (_dict), the class name (_name_), the module name in which the class is defined (_module_), the documentation bar (_doc_)


class Employee():
    """This is an Employee class"""

    counter = 0
    
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary
    
    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
    @classmethod
    def total_number(cls):
        print(f"Total number of employees: {cls.counter}")

    def __del__(self):
        Employee.counter -= 1

emp1 = Employee("John", 5000)
emp2 = Employee("Alice", 6000)

print("=========================================")

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

print("=========================================")

emp1.info()
emp2.info()
Employee.total_number()