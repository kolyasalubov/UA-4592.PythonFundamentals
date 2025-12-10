# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated


class Ghost:
    import random

    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = self.random.choice(colors)

# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

def God():
    paradise = []
    man = Man()
    paradise.append(man)
    woman = Woman()
    paradise.append(woman)
    return paradise

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

# Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes

# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

# або

class Person():
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"


# Now that we have a Block let's move on to something slightly more complex: a Sphere.

# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)

# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

# Example
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208
# Any feedback would be much appreciated

class Sphere(object):
    import math

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * self.math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * self.math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * self.math.pi * (self.radius ** 3)
        density = self.mass / volume
        return round(density, 5)
    
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,

# and went off. Although Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, that Timmy yet has to learn them.

def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError
    cls.__name__ = new_name
    return cls