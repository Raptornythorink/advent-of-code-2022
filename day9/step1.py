xH, yH, xT, yT = 0, 0, 0, 0
pos = set()
pos.add((0, 0))

def move_head(xH, yH, dir):
    nxH, nyH = xH, yH
    if dir == "R":
        nxH += 1
    elif dir == "L":
        nxH -= 1
    elif dir == "U":
        nyH += 1
    else:
        nyH -= 1
    return nxH, nyH

def catch_head(xH, yH, xT, yT):
    nxH, nyH, nxT, nyT = xH, yH, xT, yT
    if xH - xT == 2:
        if yH - yT == 1:
            nyT += 1
        elif yH - yT == -1:
            nyT -= 1
        nxT += 1
    elif xH - xT == -2:
        if yH - yT == 1:
            nyT += 1
        elif yH - yT == -1:
            nyT -= 1
        nxT -= 1
    elif yH - yT == 2:
        if xH - xT == 1:
            nxT += 1
        elif xH - xT == -1:
            nxT -= 1
        nyT += 1
    elif yH - yT == -2:
        if xH - xT == 1:
            nxT += 1
        elif xH - xT == -1:
            nxT -= 1
        nyT -= 1
    return nxH, nyH, nxT, nyT

while True:
    a = input()
    if not a:
        break
    command = a.split()
    dir, num = command[0], int(command[1])
    for _ in range(num):
        xH, yH = move_head(xH, yH, dir)
        xH, yH, xT, yT = catch_head(xH, yH, xT, yT)
        pos.add((xT, yT))

print(len(pos))
