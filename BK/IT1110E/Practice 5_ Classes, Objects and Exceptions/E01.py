import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass

# These classes are used for the purpose of raising exception, you just need to raise when necessary

class LengthException(Exception):
    pass

class InvalidTriangleException(Exception):
    pass

class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            if (width <= 0 or height <= 0): raise LengthException
            self.width = width
            self.height = height
        except LengthException as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return self.width * self.height
    
class Circle(Figure):
    def __init__(self, radius):
        try:
            self.radius = radius
        except LengthException as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return (self.radius**2) * math.pi
    
class Triangle(Figure):
    def __init__(self, a, b, c):
        try:
            if (a <= 0 or b <= 0 or c <= 0): raise LengthException
            if (a + b <= c or b + c <= a or c + a <= b): raise InvalidTriangleException
            self.a = a
            self.b = b
            self.c = c
        except (LengthException, InvalidTriangleException) as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter()/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))