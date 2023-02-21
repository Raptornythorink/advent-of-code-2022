import networkx as nx

worth_valves = []
released = 0

graph = nx.DiGraph()

while True:
    a = input()
    if not a:
        break
    desc = a.split()
    name = desc[1]
    flow = int(desc[4][5:-1])
    try:
        links = a.split("valves ")[1].split(", ")
    except:
        links = [a.split("valve ")[1]]
    for link in links:
        graph.add_edge(name, link)
    if flow > 0:
        worth_valves.append((name, flow))
    elif name == "AA":
        worth_valves.append((name, flow))
        start = name, flow

lengths = {}

for valve1 in worth_valves:
    for valve2 in worth_valves:
        if valve2 != valve1:
            path_length = nx.shortest_path_length(graph, valve1[0], valve2[0])
            lengths[(valve1[0], valve2[0])] = path_length
            lengths[(valve2[0], valve1[0])] = path_length

def test(current, valves, lengths, opened, time, flow):
    if time == 0:
        return flow
    new_flow = current[1] * (time-1)
    result = flow + new_flow
    if len(valves) == len(opened):
        return flow+new_flow*time
    for valve in valves:
        if valve!=current and valve not in opened and lengths[(current[0], valve[0])]+1<time-1*(current[0]!="AA"):
            result = max(result, test(valve, valves, lengths, opened | set([current]), time-1*(current[0]!="AA")-lengths[(current[0], valve[0])], flow+new_flow))
    return result

print(test(start, worth_valves, lengths, set(), 30, 0))
