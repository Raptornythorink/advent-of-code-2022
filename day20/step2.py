l = []
key = 811589153

while True:
    a = input()
    if not a:
        break
    l.append(int(a) * key)

n = len(l)
nl = [(l[i], i) for i in range(n)]

def shift(nli, x, i):
    j = nli.index((x, i))
    nli.pop(j)
    nli.insert((j+x)%(n-1), (x, i)) 

for _ in range(10):
    for i in range(n):
        shift(nl, l[i], i)

i0 = nl.index((0, l.index(0)))
print(nl[(i0 + 1000)%n][0] + nl[(i0 + 2000)%n][0] + nl[(i0 + 3000)%n][0])
