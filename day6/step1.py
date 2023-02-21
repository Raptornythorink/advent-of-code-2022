end = 4
seq = []
a = input()
for i in range(4):
    seq.append(a[i])
while len(set(seq)) < 4:
    seq.pop(0)
    seq.append(a[end])
    end += 1
print(end)
