# Wat is de output van deze code?
#
# A: De applicatie gooit een error
# B: 7
# C: 10

arr = ["1", "2", "start", "3", "4", "end", "5"]

value = 0
hasStarted = False
for item in arr:
    if item == "start":
        hasStarted = True
    if item == "end":
        hasStarted = False
    if hasStarted:
        value += int(item)

print(value)
