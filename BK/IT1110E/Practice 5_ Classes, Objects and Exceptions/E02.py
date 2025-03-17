import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass
    
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_height_a(self):
        return self.area()*2/self.a
    
    def get_height_b(self):
        return self.area()*2/self.b
        
    def get_height_c(self):
        return self.area()*2/self.c