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

class Bird(Animal):
    pass

class Bat(Mammal):
    pass

bat = Bat()
print(isinstance(bat, Animal))
print(isinstance(bat, Mammal))
print(isinstance(bat, Bird))
