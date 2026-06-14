# Wat is de output van deze code?
#
# A: bd
# B: ac
# C: abcd

arr = ["a", "b", "c", "d"]
result = ""
for i, v in enumerate(arr):
    if i % 2 == 1:
        result += v
print(result)
