# Task1. Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__ (self, lenght, width):
        super().__init__(4)
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght*self.width

rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())