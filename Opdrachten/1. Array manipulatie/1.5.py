# Wat is de output van deze code?
#
# A: 21
# B: 14
# C: 15

arr = ["a", "start", "b", "c", "d", "e", "end", "f"]
result = 0
hasStarted = True
for item in arr:
    if item == "start":
        hasStarted = True
    if item == "end":
        hasStarted = False
    if not hasStarted:
        continue
    if item == "a":
        result += 1
    if item == "b":
        result += 2
    if item == "c":
        result += 3
    if item == "d":
        result += 4
    if item == "e":
        result += 5
    if item == "f":
        result += 6

print(result)
