import sys
sys.setrecursionlimit(10**7)
walls = set()
blizzards = set()
dirs = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}

class Blizzard:
    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.dx, self.dy = dirs[dir]
    def move(self, w, h):
        self.x += self.dx
        self.y += self.dy
        if self.x == 0:
            self.x = w
        elif self.x == w+1:
            self.x = 1
        elif self.y == 0:
            self.y = h
        elif self.y == h+1:
            self.y = 1

y = 0

while True:
    a = input()
    if not a:
        break
    width = len(a)
    for x in range(len(a)):
        if a[x] == '#':
            walls.add((x, y))
        elif a[x] != '.':
            blizzards.add(Blizzard(x, y, a[x]))
    y += 1

height = y
end = width-2, height-1

grids = []

for _ in range(10 * (height + width)):
    bpos = set()
    for b in blizzards:
        bpos.add((b.x, b.y))
        b.move(width-2, height-2)
    grids.append(walls | bpos)

moves = [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]
print("testing")
d = {}

def test(x, y, g, t, s):
    if t >= 9 * (height + width):
        d[(x, y, t)] = float('inf')
        return
    if (x, y) == end:
        d[(x, y, t)] = t
        return
    if (x, y) in s and s[(x, y)] >= 5:
        d[(x, y, t)] = float('inf')
        return
    else:
        ns = s.copy()
        if (x, y) in s:
            ns[(x, y)] += 1
        else:
            ns[(x, y)] = 1
    res = float('inf')
    for (nx, ny) in moves:
        if (x+nx, y+ny) == end:
            res = t+1
            break
        if (x+nx, y+ny, t+1) in d:
            res = min(res, d[(x+nx, y+ny, t+1)])
        elif 0<=x+nx<=width and 0<=y+ny<=height and (x+nx, y+ny) not in g[t+1]:
            test(x+nx, y+ny, g, t+1, ns)
            res = min(res, d[(x+nx, y+ny, t+1)])
    d[(x, y, t)] = res
    return

test(1, 0, grids, 0, {})
print(d[1, 0, 0])
