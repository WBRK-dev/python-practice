# Wat is de output van deze code?
#
# A: True
#    True
#    True
# B: True
#    True
#    False
# C: False
#    True
#    True

class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()
print(isinstance(dog, Mammal))
print(issubclass(Mammal, Animal))
print(issubclass(Dog, Mammal))
