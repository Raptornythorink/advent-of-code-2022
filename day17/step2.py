from tqdm import tqdm

pattern = input()
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

grid = [[False for _ in range(7)] for _ in range(1000)]

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
    return g[50:] + [[False for _ in range(7)] for _ in range(50)]

for _ in range(9990):
    piece = ir
    ymax = find_ymax(grid)
    if ymax > 950:
        grid = shift(grid)
        shifted += 50
        ymax -= 50
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

base_pattern = []

for _ in range(10):
    piece = ir
    ymax = find_ymax(grid)
    if ymax > 950:
        grid = shift(grid)
        shifted += 50
        ymax -= 50
    x, y = 2, ymax + 5
    moves = ""
    while not test_fallen(grid, piece, x, y):
        y -= 1
        if pattern[ip] == "<":
            x -= move_left(grid, piece, x, y)
        else:
            x += move_right(grid, piece, x, y)
        ip += 1
        ip %= np
        moves += pattern[ip]
    grid = rest(grid, piece, x, y)
    base_pattern.append((piece, moves))
    ir += 1
    ir %= nr

current_pattern = [x for x in base_pattern]
pattern_starts = []

for i in range(10000):
    piece = ir
    ymax = find_ymax(grid)
    if ymax > 950:
        grid = shift(grid)
        shifted += 50
        ymax -= 50
    x, y = 2, ymax + 5
    moves = ""
    while not test_fallen(grid, piece, x, y):
        y -= 1
        if pattern[ip] == "<":
            x -= move_left(grid, piece, x, y)
        else:
            x += move_right(grid, piece, x, y)
        ip += 1
        ip %= np
        moves += pattern[ip]
    grid = rest(grid, piece, x, y)
    current_pattern.pop(0)
    current_pattern.append((piece, moves))
    for j in range(10):
        if current_pattern[j] != base_pattern[j]:
            break
    else:
        pattern_starts.append(10000+i)
    ir += 1
    ir %= nr

if len(pattern_starts) > 2 and pattern_starts[2] - pattern_starts[1] == pattern_starts[1] - pattern_starts[0]:
    pattern_length = pattern_starts[1] - pattern_starts[0]

    remainder = (1000000*1000000-20000-pattern_length) % pattern_length

    for i in range(remainder):
        piece = ir
        ymax = find_ymax(grid)
        if ymax > 950:
            grid = shift(grid)
            shifted += 50
            ymax -= 50
        x, y = 2, ymax + 5
        moves = ""
        while not test_fallen(grid, piece, x, y):
            y -= 1
            if pattern[ip] == "<":
                x -= move_left(grid, piece, x, y)
            else:
                x += move_right(grid, piece, x, y)
            ip += 1
            ip %= np
            moves += pattern[ip]
        grid = rest(grid, piece, x, y)
        current_pattern.pop(0)
        current_pattern.append((piece, moves))
        ir += 1
        ir %= nr

    ymax_before_pattern = find_ymax(grid) + shifted

    for i in range(pattern_length):
        piece = ir
        ymax = find_ymax(grid)
        if ymax > 950:
            grid = shift(grid)
            shifted += 50
            ymax -= 50
        x, y = 2, ymax + 5
        moves = ""
        while not test_fallen(grid, piece, x, y):
            y -= 1
            if pattern[ip] == "<":
                x -= move_left(grid, piece, x, y)
            else:
                x += move_right(grid, piece, x, y)
            ip += 1
            ip %= np
            moves += pattern[ip]
        grid = rest(grid, piece, x, y)
        current_pattern.pop(0)
        current_pattern.append((piece, moves))
        ir += 1
        ir %= nr

    ymax_after_pattern = find_ymax(grid) + shifted
    pattern_height = ymax_after_pattern - ymax_before_pattern
    total_height = ymax_after_pattern + ((1000000*1000000-20000-pattern_length)//pattern_length)*pattern_height+1
    print(total_height)
else:
    print("couldn't find any patterns")
    print(pattern_starts)
