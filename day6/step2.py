end = 14
seq = []
a = input()
for i in range(14):
    seq.append(a[i])
while len(set(seq)) < 14:
    seq.pop(0)
    seq.append(a[end])
    end += 1
print(end)
