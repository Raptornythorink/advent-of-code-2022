import networkx as nx

grid = []
start = 0, 0
starts = []
end = 0, 0
i = 0

while True:
    a = input()
    if not a:
        break
    grid.append([])
    j = 0
    for c in a:
        if c == "S":
            start = i, j
            grid[-1].append(0)
        elif c == "a":
            starts.append((i, j))
            grid[-1].append(0)
        elif c == "E":
            end = i, j
            grid[-1].append(25)
        else:
            grid[-1].append(ord(c) - 97)
        j += 1
    i += 1

width = len(grid[0])
height = len(grid)

def possible_moves(g, w, h, i, j):
    moves = []
    if j > 0 and g[i][j-1] <= g[i][j] + 1 and (i, j-1):
        moves.append((i, j-1))
    if j < w-1 and g[i][j+1] <= g[i][j] + 1 and (i, j+1):
        moves.append((i, j+1))
    if i > 0 and g[i-1][j] <= g[i][j] + 1 and (i-1, j):
        moves.append((i-1, j))
    if i < h-1 and g[i+1][j] <= g[i][j] + 1 and (i+1, j):
        moves.append((i+1, j))
    return moves

graph = nx.DiGraph()
for i in range(height):
    for j in range(width):
        for ni, nj in possible_moves(grid, width, height, i, j):
            graph.add_edge(str((i, j)), str((ni, nj)))

shortest = nx.dijkstra_path_length(graph, str(start), str(end))
for other_start in starts:
    try:
        shortest = min(shortest, nx.dijkstra_path_length(graph, str(other_start), str(end)))
    except:
        pass
print(shortest)
