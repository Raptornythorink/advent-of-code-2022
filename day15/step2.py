couples = []

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

while True:
    a = input()
    if not a:
        break
    data = a.split()
    sx, sy, bx, by = list(map(int, [data[2][2:-1], data[3][2:-1], data[8][2:-1], data[9][2:]]))
    couples.append((sx, sy, bx, by, distance(sx, sy, bx, by)))

def test(couples):
    for couple in couples:
        r = couple[-1]+1
        for i in range(r+1):
            for x, y in [(couple[0]+i, couple[1]+r-i), (couple[0]-i, couple[1]+r-i), (couple[0]+i, couple[1]-r+i), (couple[0]-i, couple[1]-r+i)]:
                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    possible = True
                    for ncouple in couples:
                        if distance(ncouple[0], ncouple[1], x, y) <= ncouple[4]:
                            possible = False
                            break
                    if possible:
                        return 4000000*x+y

print(test(couples))
