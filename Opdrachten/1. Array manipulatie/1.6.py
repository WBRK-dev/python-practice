# Wat is de output van deze code?
#
# A: 7
# B: 10
# C: 15

arr = ["1", "2", "start", "3", "4", "end", "5"]

value = 0
hasStarted = False
for item in arr:
    if item == "start":
        hasStarted = True
    elif item == "end":
        hasStarted = False
    elif hasStarted:
        value += int(item)

print(value)
