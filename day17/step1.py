pattern = input()
from time import sleep
np = len(pattern)
nr = 5
ip = 0
ir = 0
shifted = 0

rocks = [
    [[True, True, True, True]],
    [[False, True, False], [True, True, True], [False, True, False]],
    [[True, True, True], [False, False, True], [False, False, True]]    ,
    [[True], [True], [True], [True]],
    [[True, True], [True, True]]
    ]

rocks_dim = [[4, 1], [3, 3], [3, 3], [1, 4], [2, 2]]

grid = [[False for _ in range(7)] for _ in range(3500)]

def find_ymax(g):
    n = len(g)
    for i in range(n):
        for e in g[n-1-i]:
            if e:
                return n-1-i
    return -1

def test_fallen(g, p, x, y):
    if y == 0:
        return True
    for j in range(rocks_dim[p][1]):
        for i in range(rocks_dim[p][0]):
            if rocks[p][j][i] and g[y+j-1][x+i]:
                return True
    return False

def rest(g, p, x, y):
    for j in range(rocks_dim[p][1]):
        for i in range(rocks_dim[p][0]):
            g[y+j][x+i] = rocks[p][j][i] or g[y+j][x+i]
    return g

def move_left(g, p, x, y):
    if x > 0:
        for i in range(rocks_dim[p][0]):
            for j in range(rocks_dim[p][1]):
                if rocks[p][j][i] and g[y+j][x+i-1]:
                    return False
        return True
    return False

def move_right(g, p, x, y):
    if x + rocks_dim[p][0] < 7:
        for i in range(rocks_dim[p][0]):
            for j in range(rocks_dim[p][1]):
                if rocks[p][j][i] and g[y+j][x+i+1]:
                    return False
        return True
    return False

def shift(g):
    return g[10:] + [[False for _ in range(7)] for _ in range(10)]

for _ in range(2022):
    piece = ir
    ymax = find_ymax(grid)
    if ymax > 3490:
        grid = shift(grid)
        shifted += 10
        ymax -= 10
    x, y = 2, ymax + 5
    while not test_fallen(grid, piece, x, y):
        y -= 1
        if pattern[ip] == "<":
            x -= move_left(grid, piece, x, y)
        else:
            x += move_right(grid, piece, x, y)
        ip += 1
        ip %= np
    grid = rest(grid, piece, x, y)
    ir += 1
    ir %= nr

print(find_ymax(grid) + shifted + 1, shifted)
