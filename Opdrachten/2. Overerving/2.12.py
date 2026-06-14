# Wat is de output van deze code?
#
# A: 4
# B: 3
# C: 1

class P:
    def m(self):
        return 1

class Q(P):
    def m(self):
        return super().m() + 1

class R(P):
    def m(self):
        return super().m() + 2

class S(Q, R):
    def m(self):
        return super().m()

obj = S()
print(obj.m())
