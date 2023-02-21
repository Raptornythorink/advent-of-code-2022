xHead, yHead = 0, 0
xTail, yTail = [0 for _ in range(9)], [0 for _ in range(9)]
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
    nxT, nyT = xT, yT
    if xH - xT == 2:
        if yH - yT >= 1:
            nyT += 1
        elif yH - yT <= -1:
            nyT -= 1
        nxT += 1
    elif xH - xT == -2:
        if yH - yT >= 1:
            nyT += 1
        elif yH - yT <= -1:
            nyT -= 1
        nxT -= 1
    elif yH - yT == 2:
        if xH - xT >= 1:
            nxT += 1
        elif xH - xT <= -1:
            nxT -= 1
        nyT += 1
    elif yH - yT == -2:
        if xH - xT >= 1:
            nxT += 1
        elif xH - xT <= -1:
            nxT -= 1
        nyT -= 1
    return nxT, nyT

while True:
    a = input()
    if not a:
        break
    command = a.split()
    dir, num = command[0], int(command[1])
    for _ in range(num):
        xHead, yHead = move_head(xHead, yHead, dir)
        xTail[0], yTail[0] = catch_head(xHead, yHead, xTail[0], yTail[0])
        for i in range(8):
            xTail[i+1], yTail[i+1] = catch_head(xTail[i], yTail[i], xTail[i+1], yTail[i+1])
        pos.add((xTail[-1], yTail[-1]))

print(len(pos))
