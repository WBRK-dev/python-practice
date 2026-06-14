# Wat is de output van deze code?
#
# A: 2
# B: 4
# C: 9

arr = [1, 2, 3, 4, 5]
arr.reverse()
total = 0
for x in arr:
    if x % 2 != 0:
        total += x
print(total)
