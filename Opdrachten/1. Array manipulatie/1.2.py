# Wat is de output van deze code?
#
# A: [3, 4, 5, 2]
# B: De applicatie gooit een error
# C: [1, 1, 9, 6]

arr = [3, 1, 4, 1, 5, 9, 2, 6]

result = []
for i in range(len(arr)):
    if i % 2 == 0:
        result.append(arr[i])

print(result)
