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
pad = 100
grid = [[False for _ in range(w+2*pad)] for _ in range(pad)]
for line in grid0:
    grid.append([False for _ in range(pad)] + line + [False for _ in range(pad)])
for _ in range(pad):
    grid.append([False for _ in range(w+2*pad)])

height, width = len(grid), len(grid[0])

for elf in elves:
    elf.x += pad
    elf.y += pad

n = 0
while True:
    n += 1
    next_moves = []
    curr = set()
    for elf in elves:
        curr.add((elf.x, elf.y))
        next_moves.append(elf.prepare_move(grid))
    if curr == set(next_moves):
        break
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

print(n)
