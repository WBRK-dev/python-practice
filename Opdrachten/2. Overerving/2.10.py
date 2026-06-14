# Wat is de output van deze code?
#
# A: ACB
# B: ABC
# C: A

class A:
    def __init__(self):
        self.val = "A"

class B(A):
    def __init__(self):
        super().__init__()
        self.val += "B"

class C(A):
    def __init__(self):
        super().__init__()
        self.val += "C"

class D(B, C):
    def __init__(self):
        super().__init__()

d = D()
print(d.val)
