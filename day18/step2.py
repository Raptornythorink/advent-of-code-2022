import networkx
cubes = {}
adjacent_cubes = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

xmax, ymax, zmax = 0, 0, 0
from time import time
while True:
    a = input()
    if not a:
        break
    x, y, z = tuple(map(int, a.split(',')))
    xmax, ymax, zmax = max(x, xmax), max(y, ymax), max(z, zmax)
    cubes[(x, y, z)] = 0
st = time()
graph = networkx.Graph()
for i in range(-1, xmax+2):
    for j in range(-1, ymax+2):
        for k in range(-1, zmax+2):
            if (i, j, k) not in cubes:
                graph.add_node((i, j, k))
                for ni, nj, nk in adjacent_cubes:
                    if (i+ni, j+nj, k+nk) not in cubes:
                        graph.add_edge((i, j, k), (i+ni, j+nj, k+nk))

for (x, y, z) in cubes:
    for (nx, ny, nz) in adjacent_cubes:
        if graph.has_node((x+nx, y+ny, z+nz)) and networkx.has_path(graph, (0, 0, 0), (x+nx, y+ny, z+nz)):
            cubes[(x, y, z)] += 1

print(sum(cubes.values()))

print(time()-st)