grid = []

while True:
    a = input()
    if not a:
        break
    grid.append(a)

commands = input()

for i in range(len(grid[0])):
    if grid[0][i] == ".":
        break

from time import time
st = time()
x, y = i, 0
dir = "R"

dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

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

def go_forward(g, x, y, dx, dy, nt):
    if nt == 0:
        return x, y
    if y+dy >= len(g) or (dy > 0 and (x >= len(g[y+dy]) or g[y+dy][x] == " ")):
        for j in range(len(g)):
            try:
                if g[j][x] == "#":
                    return x, y
                if g[j][x] == ".":
                    return go_forward(g, x, j, dx, dy, nt-1)
            except:
                pass
    elif y+dy < 0 or (dy < 0 and (x >= len(g[y+dy]) or g[y+dy][x] == " ")):
        for j in range(len(g)-1, -1, -1):
            try:
                if g[j][x] == "#":
                    return x, y
                if g[j][x] == ".":
                    return go_forward(g, x, j, dx, dy, nt-1)
            except:
                pass
    if x+dx >= len(g[y]):
        for j in range(len(g[y])):
            try:
                if g[y][j] == "#":
                    return x, y
                if g[y][j] == ".":
                    return go_forward(g, j, y, dx, dy, nt-1)
            except:
                pass
    elif x+dx < 0 or x+dx >= len(g[y]) or g[y][x+dx] == " ":
        for j in range(len(g[y])-1, -1, -1):
            try:
                if g[y][j] == "#":
                    return x, y
                if g[y][j] == ".":
                    return go_forward(g, j, y, dx, dy, nt-1)
            except:
                pass
    elif g[y+dy][x+dx] == "#":
        return x, y
    return go_forward(g, x+dx, y+dy, dx, dy, nt-1)

while i < n:
    if commands[i].isdigit():
        if i+1 < n and commands[i+1].isdigit():
            ntiles = 10 * int(commands[i]) + int(commands[i+1])
            i += 2
        else:
            ntiles = int(commands[i])
            i += 1
        dx, dy = dirs[dir]
        x, y = go_forward(grid, x, y, dx, dy, ntiles)
    else:
        dir = rotate(dir, commands[i])
        i += 1

dirs_score = {"R": 0, "D": 1, "L": 2, "U": 3}

print(1000*(y+1) + 4*(x+1) + dirs_score[dir])
print(time()-st)
