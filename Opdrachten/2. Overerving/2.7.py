# Wat is de output van deze code?
#
# A: Child
# B: Parent
# C: De applicatie gooit een error

class Parent:
    @classmethod
    def who(cls):
        return "Parent"

class Child(Parent):
    @classmethod
    def who(cls):
        return "Child"

print(Child.who())
