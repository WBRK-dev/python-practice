# Wat is de output van deze code?
#
# A: True True
# B: True False
# C: False True

class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 2

obj = B()
print(hasattr(obj, "a"), hasattr(obj, "b"))
