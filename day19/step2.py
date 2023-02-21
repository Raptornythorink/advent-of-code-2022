blueprints = []
maxcosts = []
score = 0

while True:
    a = input()
    if not a:
        break
    data = a.split()
    blueprints.append((int(data[6]), int(data[12]), int(data[18]), int(data[21]), int(data[27]), int(data[30])))
    maxcosts.append((max(int(data[6]), int(data[12]), int(data[18]), int(data[27])), int(data[21]), int(data[30])))

from time import time

st = time()
def test(state, blueprint, maxcost):
    if not state[0]:
        scores[state] = state[1][-1]
        return
    #if state[2][2] >= blueprint[-1] and state[2][0] >= blueprint[-2]:
    #    scores[state] = state[1][-1] + sum(state[2][-1] + i for i in range(state[0]-1))
    #    return
    nstates = []
    robots = []
    counter = 0
    gepos = False
    if state[1][0] >= blueprint[4] and state[1][2] >= blueprint[5]:
        counter += 1
        gepos = True
        robots.append(3)
        nstates.append([state[0]-1, [state[1][0]-blueprint[4], state[1][1], state[1][2]-blueprint[5], state[1][3]], list(state[2])])
    if state[1][0] >= blueprint[2] and state[1][1] >= blueprint[3] and state[1][2] < maxcost[2]:
        counter += 1
        robots.append(2)
        nstates.append([state[0]-1, [state[1][0]-blueprint[2], state[1][1]-blueprint[3], state[1][2], state[1][3]], list(state[2])])
    if state[1][0] >= blueprint[1] and state[2][1] < maxcost[1]:
        counter += 1
        robots.append(1)
        nstates.append([state[0]-1, [state[1][0]-blueprint[1], state[1][1], state[1][2], state[1][3]], list(state[2])])
    if state[1][0] >= blueprint[0] and state[2][0] < maxcost[0]:
        counter += 1
        robots.append(0)
        nstates.append([state[0]-1, [state[1][0]-blueprint[0], state[1][1], state[1][2], state[1][3]], list(state[2])])
    if counter < 4 and not gepos:
        robots.append(-1)
        nstates.append([state[0]-1, list(state[1]), list(state[2])])
    for j in range(len(nstates)):
        nstates[j] = (nstates[j][0], tuple([nstates[j][1][i] + state[2][i] for i in range(4)]), nstates[j][2])
    best = 0
    for i in range(len(nstates)):
        if robots[i] > -1:
            nstates[i][2][robots[i]] += 1
        nnstate = nstates[i][0], tuple(nstates[i][1]), tuple(nstates[i][2])
        if not nnstate in scores:
            test(nnstate, blueprint, maxcost)
        nbest = scores[nnstate]
        best = max(best, nbest)
    scores[state] = best
    return

start = (32, (0, 0, 0, 0), (1, 0, 0, 0))

result = 1
for i in range(len(blueprints)):
    scores = {}
    test(start, blueprints[i], maxcosts[i])
    print('------')
    print(scores[start])
    print('------')
    result *= scores[start]
    print(time()-st)
    st = time()
print(result)
