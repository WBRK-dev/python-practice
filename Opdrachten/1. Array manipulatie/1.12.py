# Wat is de output van deze code?
#
# A: [1, 1, 3, 4, 5] [5, 4, 3, 1, 1]
# B: [5, 4, 3, 1, 1] [5, 4, 3, 1, 1]
# C: De applicatie gooit een error

arr = [3, 1, 4, 1, 5]
result = sorted(arr)
arr.sort(reverse=True)
print(result, arr)
