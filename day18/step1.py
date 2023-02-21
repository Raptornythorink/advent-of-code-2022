cubes = {}
adjacent_cubes = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

while True:
    a = input()
    if not a:
        break
    x, y, z = tuple(map(int, a.split(',')))
    cubes[(x, y, z)] = 6
    for [nx, ny, nz] in adjacent_cubes:
        if (x+nx, y+ny, z+nz) in cubes:
            cubes[(x, y, z)] -= 1
            cubes[(x+nx, y+ny, z+nz)] -= 1

print(sum(cubes.values()))
