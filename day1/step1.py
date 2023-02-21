maxC = 0
currentC = 0
while True:
    a = input()
    if a == "over":
        break
    elif a == "":
        maxC = max(maxC, currentC)
        currentC = 0
    else:
        currentC += int(a)
print(maxC)