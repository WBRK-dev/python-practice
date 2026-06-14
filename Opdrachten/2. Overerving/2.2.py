# Wat is de output van deze code?
#
# A: "...woof howl"
# B: "...woof"
# C: "... howl"

class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return super().sound() + "woof"

class Beagle(Dog):
    def sound(self):
        return super().sound() + " howl"

print(Beagle().sound())
