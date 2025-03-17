from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)