from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        
    def set_width(self, side):
        self.width = side
        self.height = side
        
    def set_height(self, side):
        self.width = side
        self.height = side