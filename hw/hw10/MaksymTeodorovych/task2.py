#==========task1===========
# class Ball(object):
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type
#==========task2===========
# class Ghost(object):
#     import random
#     def __init__(self):
#         options = ["white", "yellow", "purple", "red"]
#         self.color = self.random.choice(options)
#==========task3===========
# class Human():
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
# def God():
#     people = []
#     Adam = Man()
#     Eve = Woman()
#     people.append(Adam)
#     people.append(Eve)
#     return people
# print(God())
#==========task4===========
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"
#==========task5===========
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         self.volume = round(4/3 * math.pi * self.radius**3, 5)
#         return self.volume
#     def get_surface_area(self):
#         surface_area = round(4 * math.pi * self.radius**2, 5)
#         return surface_area
#     def get_density(self):
#         get_density = self.mass / self.volume
#         return get_density
#==========task6===========
# def class_name_changer(cls, new_name):
#     if not new_name.isalnum() or not new_name[0].isupper():
#         raise ValueError
#     cls.__name__ = new_name
#     return cls