import math

class Polygon:
    """
    This class creates polygonal shpes
    """
    def __init__(self,side_num:int):
        self.side_num = side_num

    def side_length(self):
        """
        This function creates list of side lengthes of a shape
        """
        length_list=[]
        for side in range(self.side_num):
            length = float(input(f"Enter a length of a side {side+1}: "))
            length_list.append(length)
        return length_list

class Triangle(Polygon):
    """
    This class creates triangles
    """
    def __init__(self):
        self.side_num = 3

    def side_length(self):
        side = super().side_length()
        if side[0] + side[1] <= side[2]:
            print(f"One of the sides should be less than the sum of the other two sides!")
        elif side[1] + side[2] <= side[0]:
            print(f"One of the sides should be less than the sum of the other two sides!")
        elif side[0] + side[2] <= side[1]:
            print(f"One of the sides should be less than the sum of the other two sides!")
        else:
            return side
        
    def area(self, length_list):
        """
        This function calculates the area of a triangle
        """
        s = (length_list[0] + length_list[1] + length_list[2]) / 2
        area = math.sqrt(s * (s - length_list[0]) * (s - length_list[1]) * (s - length_list[2]))
        return area

#Tests
#tri = Triangle()
#tri_side = tri.side_length()
#print(tri.area(tri_side))

#-----------------------------------------------------------------------------------------------------------------

class Human:
    def __init__(self, name:str) -> None:
        self.name = name

    def welcome(self):
        print(f"Welcome {self.name}")

    @classmethod
    def info(cls):
        print(f'{cls.__name__} is a species of "Homosapiens".')

    @staticmethod
    def static():
        print("static")

#Tests
#alex = Human("Alex")
#alex.welcome()
#Human.info()
#alex.static()

#---------------------------------------------------------------------------------------------------------------------------

class Employee:
    """
    This class creates object employee
    """
    employee_counter = 0
    employee_dict = {}
    def __init__(self,name:str,salary:int = 0):
        self.name = name
        self.salary = salary
        cls = self.__class__
        cls.employee_counter += 1
        cls.employee_dict[self.name] = self.salary
    
        
    @classmethod
    def employee_num(cls):
        """
        This function returns number of employees
        """
        print(f"Number of employees is {cls.employee_counter}")

    @classmethod
    def employee_info(cls):
        """
        This function lists all of the employees
        """
        print("Employee list:")
        for key, value in cls.employee_dict.items():
            print(f"{key} Salary: {value}")

    
#Tests
nina = Employee("Nina", 2000)
Employee.employee_num()
alex = Employee("Alex")
Employee.employee_num()
Employee.employee_info()
#print(Employee.__base__)
#print(Employee.__dict__)
#print(Employee.__name__)
#print(Employee.__module__)
#print(Employee.__doc__)