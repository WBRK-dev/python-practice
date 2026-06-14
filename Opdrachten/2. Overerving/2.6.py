# Wat is de output van deze code?
#
# A: De applicatie gooit een error
# B: 6
# C: None

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

rect = Rectangle(2, 3)
print(rect.area())
