# Wat is de output van deze code?
#
# A: [5, 7, 9]
# B: [1, 2, 3, 4, 5, 6]
# C: De applicatie gooit een error

a = [1, 2, 3]
b = [4, 5, 6]
result = []
for x, y in zip(a, b):
    result.append(x + y)
print(result)
