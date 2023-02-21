grid = []

while True:
    a = input()
    if not a:
        break
    grid.append([int(x) for x in a])

width, height = len(grid[0]), len(grid)

def visible_from_left(g, i, j):
    score = 0
    for y in range(j):
        score += 1
        if g[i][j-1-y] >= g[i][j]:
            break
    return score

def visible_from_right(g, w, i, j):
    score = 0
    for y in range(j+1, w):
        score += 1
        if g[i][y] >= g[i][j]:
            break
    return score

def visible_from_top(g, i, j):
    score = 0
    for x in range(i):
        score += 1
        if g[i-1-x][j] >= g[i][j]:
            break
    return score

def visible_from_bottom(g, h, i, j):
    score = 0
    for x in range(i+1, h):
        score += 1
        if g[x][j] >= g[i][j]:
            break
    return score

max_score = 0

for i in range(height):
    for j in range(width):
        max_score = max(max_score, 
            visible_from_left(grid, i, j) * visible_from_right(grid, width, i, j) *
            visible_from_top(grid, i, j) * visible_from_bottom(grid, height, i, j)
        )

print(max_score)
