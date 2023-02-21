xmin = 0
xmax = 0
couples = []

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

y = int(input())

while True:
    a = input()
    if not a:
        break
    data = a.split()
    sx, sy, bx, by = list(map(int, [data[2][2:-1], data[3][2:-1], data[8][2:-1], data[9][2:]]))
    d = distance(sx, sy, bx, by)
    xmin, xmax = min(xmin, sx - d), max(xmax, bx + d)
    couples.append((sx, sy, bx, by, d))

counter = 0

for x in range(xmin, xmax + 1):
    for couple in couples:
        if (x, y) == (couple[2], couple[3]):
            break
        if distance(couple[0], couple[1], x, y) <= couple[4]:
            counter += 1
            break

print(counter)
