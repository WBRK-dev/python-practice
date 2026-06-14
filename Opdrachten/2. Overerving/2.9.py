# Wat is de output van deze code?
#
# A: 314.0
# B: 3.14
# C: De applicatie gooit een error

class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return 3.14 * self._r ** 2

c = Circle(10)
print(c.area)
