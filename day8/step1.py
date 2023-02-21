grid = []

while True:
    a = input()
    if not a:
        break
    grid.append([int(x) for x in a])

width, height = len(grid[0]), len(grid)

def visible_from_left(g, i, j):
    for y in range(j):
        if g[i][y] >= g[i][j]:
            return False
    return True

def visible_from_right(g, w, i, j):
    for y in range(j+1, w):
        if g[i][y] >= g[i][j]:
            return False
    return True

def visible_from_top(g, i, j):
    for x in range(i):
        if g[x][j] >= g[i][j]:
            return False
    return True

def visible_from_bottom(g, h, i, j):
    for x in range(i+1, h):
        if g[x][j] >= g[i][j]:
            return False
    return True

total = 0

for i in range(height):
    for j in range(width):
        total += (
            visible_from_left(grid, i, j) or visible_from_right(grid, width, i, j) or
            visible_from_top(grid, i, j) or visible_from_bottom(grid, height, i, j)
        )

print(total)