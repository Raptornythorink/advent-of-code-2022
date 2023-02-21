grid0 = []
elves = set()

class Elf:
    possible_moves = [([(-1, -1), (0, -1), (1, -1)], (0, -1)),
                      ([(-1, 1),  (0, 1),  (1, 1)],  (0, 1)),
                      ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
                      ([(1, -1),  (1, 0),  (1, 1)],  (1, 0))]
    around = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    move_index = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next_move = x, y

    def prepare_move(self, g):
        for pos in self.around:
            if g[self.y+pos[1]][self.x+pos[0]]:
                break
        else:
            self.next_move = self.x, self.y
            return self.next_move
        for i in range(4):
            for pos in self.possible_moves[(self.move_index + i)%4][0]:
                if g[self.y+pos[1]][self.x+pos[0]]:
                    break
            else:
                self.next_move = self.x + self.possible_moves[(self.move_index + i)%4][1][0], self.y + self.possible_moves[(self.move_index + i)%4][1][1]
                break
        else:
            self.next_move = self.x, self.y
        return self.next_move

    def move(self):
        self.x, self.y = self.next_move

    def cancel_move(self):
        self.next_move = self.x, self.y

y = 0

while True:
    a = input()
    if not a:
        break
    line = []
    for x in range(len(a)):
        if a[x] == '#':
            line.append(True)
            elves.add(Elf(x, y))
        else:
            line.append(False)
    grid0.append(line)
    y += 1

w = len(grid0[0])

grid = [[False for _ in range(w+20)] for _ in range(10)]
for line in grid0:
    grid.append([False for _ in range(10)] + line + [False for _ in range(10)])
for _ in range(10):
    grid.append([False for _ in range(w+20)])

height, width = len(grid), len(grid[0])

for elf in elves:
    elf.x += 10
    elf.y += 10

for _ in range(10):
    next_moves = []
    for elf in elves:
        next_moves.append(elf.prepare_move(grid))
    seen = set()
    dupes = set([x for x in next_moves if x in seen or seen.add(x)])
    for elf in elves:
        if elf.next_move in dupes:
            elf.cancel_move()
        else:
            elf.move()
    grid = [[False for _ in range(width)] for _ in range(height)]
    for elf in elves:
        grid[elf.y][elf.x] = True
    Elf.move_index += 1

ymin = 0
while True not in grid[ymin]:
    ymin += 1
ymax = height - 1
while True not in grid[ymax]:
    ymax -= 1
xmin = 0
while True not in [grid[y][xmin] for y in range(height)]:
    xmin += 1
xmax = width - 1
while True not in [grid[y][xmax] for y in range(height)]:
    xmax -= 1

total = 0
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        total += not grid[y][x]

print(total)
