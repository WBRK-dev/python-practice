# Wat is de output van deze code?
#
# A: [4, 16]
# B: [1, 4, 9, 16, 25]
# C: [4, 16, 36]

arr = [1, 2, 3, 4, 5]
result = [x ** 2 for x in arr if x % 2 == 0]
print(result)
