#1. Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type =  "regular"):
        self.ball_type =  ball_type

#2. Color Ghost
import random
class Ghost:
    def __init__(self):
        num = random.randint(0,3)
        colors = ["white", "yellow", "purple", "red"]
        self.color = colors[num]

#3. Basic subclasses - Adam and Eve
class Human:
    pass

class Woman(Human):
    pass

class Man(Human):
    pass

def God():
    return([Man(), Woman()])

#4. Classy Classes
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"

#5. Building Spheres
import math

class Sphere(object):
    def __init__(self,radius:float,mass:float):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = (4/3) * math.pi * math.pow(self.radius,3)
        return round(volume,5)
    
    def get_surface_area(self):
        area = 4 * math.pi * math.pow(self.radius,2)
        return round(area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    
#6. Dynamic Classes
import string
def class_name_changer(cls, new_name:str):
    if not new_name[0].isupper():
        raise ValueError
    elif new_name[0] not in string.ascii_uppercase:
        raise ValueError
    
    for letter in new_name:
        if letter not in string.ascii_letters and letter not in string.digits:
            raise ValueError
    cls.__name__ = new_name
