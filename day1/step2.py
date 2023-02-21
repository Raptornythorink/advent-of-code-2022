maxC1 = 0
maxC2 = 0
maxC3 = 0
currentC = 0
while True:
    a = input()
    if a == "over":
        break
    elif a == "":
        maxC3 = max(maxC3, min(maxC2, currentC))
        maxC2 = max(maxC2, min(maxC1, currentC))
        maxC1 = max(maxC1, currentC)
        currentC = 0
    else:
        currentC += int(a)
print(maxC1, maxC2, maxC3, maxC1 + maxC2 + maxC3) 