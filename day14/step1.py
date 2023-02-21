grid = set()

start = 500, 0
sx, sy = 500, 0
ymax = 0
count = 0

while True:
    a = input()
    if not a:
        break
    positions = a.split(' -> ')
    x2, y2 = tuple(map(int, positions[0].split(',')))
    for i in range(len(positions) - 1):
        x1, y1 = x2, y2
        x2, y2 = tuple(map(int, positions[i+1].split(',')))
        ymax = max(ymax, y1, y2)
        if y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                grid.add((x, y1))
        elif x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                 grid.add((x1, y))

while True:
    if sy > ymax:
        break
    if (sx, sy+1) in grid and (sx-1, sy+1) in grid and (sx+1, sy+1) in grid:
        count += 1
        grid.add((sx, sy))
        sx, sy = start
    elif (sx, sy+1) not in grid:
        sy += 1
    elif (sx-1, sy+1) not in grid:
        sx -= 1
        sy += 1
    elif (sx+1, sy+1) not in grid:
        sx += 1
        sy += 1

print(count)
