grids = [[] for _ in range(6)]

for _ in range(50):
    a = input()
    if not a:
        break
    grids[0].append(a[50:100])
    grids[1].append(a[100:])

for _ in range(50):
    a = input()
    if not a:
        break
    grids[2].append(a[50:])

for _ in range(50):
    a = input()
    if not a:
        break
    grids[3].append(a[:50])
    grids[4].append(a[50:100])

for _ in range(50):
    a = input()
    if not a:
        break
    grids[5].append(a)

input()
commands = input()

for i in range(len(grids[0][0])):
    if grids[0][0][i] == ".":
        break

from time import time
st = time()
x, y, f = i, 0, 0
dir = "R"

dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

grid_dirs = {(0, "R") : (1, "R"), (0, "L") : (3, "R"), (0, "D"): (2, "D"), (0, "U"): (5, "R"),
             (1, "R") : (4, "L"), (1, "L") : (0, "L"), (1, "D"): (2, "L"), (1, "U"): (5, "U"),
             (2, "R") : (1, "U"), (2, "L") : (3, "D"), (2, "D"): (4, "D"), (2, "U"): (0, "U"),
             (3, "R") : (4, "R"), (3, "L") : (0, "R"), (3, "D"): (5, "D"), (3, "U"): (2, "R"),
             (4, "R") : (1, "L"), (4, "L") : (3, "L"), (4, "D"): (5, "L"), (4, "U"): (2, "U"),
             (5, "R") : (4, "U"), (5, "L") : (0, "D"), (5, "D"): (1, "D"), (5, "U"): (3, "U")}

n = len(commands)
i = 0

def rotate(dir, turn):
    if (dir == "U" and turn == "R") or (dir == "D" and turn == "L"):
        return "R"
    elif (dir == "R" and turn == "R") or (dir == "L" and turn == "L"):
        return "D"
    elif (dir == "D" and turn == "R") or (dir == "U" and turn == "L"):
        return "L"
    elif (dir == "L" and turn == "R") or (dir == "R" and turn == "L"):
        return "U"

def go_forward(g, x, y, f, dir, nt):
    if nt == 0:
        return x, y, dir, f
    dx, dy = dirs[dir]
    if y+dy >= 50:
        nf, ndir = grid_dirs[(f, "D")]
        if ndir == "D":
            nx, ny = x, 0
        elif ndir == "L":
            nx, ny = 49, x
        if g[nf][ny][nx] == "#":
            return x, y, dir, f
        return go_forward(g, nx, ny, nf, ndir, nt-1)
    elif y+dy < 0:
        nf, ndir = grid_dirs[(f, "U")]
        if ndir == "U":
            nx, ny = x, 49
        elif ndir == "R":
            nx, ny = 0, x
        if g[nf][ny][nx] == "#":
            return x, y, dir, f
        return go_forward(g, nx, ny, nf, ndir, nt-1)
    elif x+dx >= 50:
        nf, ndir = grid_dirs[(f, "R")]
        if ndir == "R":
            nx, ny = 0, y
        elif ndir == "L":
            nx, ny = 49, 49-y
        elif ndir == "U":
            nx, ny = y, 49
        if g[nf][ny][nx] == "#":
            return x, y, dir, f
        return go_forward(g, nx, ny, nf, ndir, nt-1)
    elif x+dx < 0:
        nf, ndir = grid_dirs[(f, "L")]
        if ndir == "L":
            nx, ny = 49, y
        elif ndir == "R":
            nx, ny = 0, 49-y
        elif ndir == "D":
            nx, ny = y, 0
        if g[nf][ny][nx] == "#":
            return x, y, dir, f
        return go_forward(g, nx, ny, nf, ndir, nt-1)
    elif g[f][y+dy][x+dx] == "#":
        return x, y, dir, f
    return go_forward(g, x+dx, y+dy, f, dir, nt-1)

while i < n:
    if commands[i].isdigit():
        if i+1 < n and commands[i+1].isdigit():
            ntiles = 10 * int(commands[i]) + int(commands[i+1])
            i += 2
        else:
            ntiles = int(commands[i])
            i += 1
        dx, dy = dirs[dir]
        x, y, dir, f = go_forward(grids, x, y, f, dir, ntiles)
        print(x, y, f)
    else:
        dir = rotate(dir, commands[i])
        i += 1

dirs_score = {"R": 0, "D": 1, "L": 2, "U": 3}

print(x, y, f)

if f == 0:
    a, b = 50+x, y
elif f == 1:
    a, b = 100+x, y
elif f == 2:
    a, b = 50+x, 50+y
elif f == 3:
    a, b = x, 100+y
elif f == 4:
    a, b = 50+x, 100+y
elif f == 5:
    a, b = x, 150+y

print(1000*(b+1) + 4*(a+1) + dirs_score[dir])
print(time()-st)

# > 2673