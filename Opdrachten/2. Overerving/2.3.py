# Wat is de output van deze code?
#
# A: 10
# B: 20
# C: AttributeError

class Parent:
    def __init__(self):
        self.__value = 10

    def get_value(self):
        return self.__value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 20

child = Child()
print(child.get_value())
