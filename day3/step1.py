def priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1

def find_duplicates(l1, l2):
    return list(set(l1) & set(l2))

total = 0

while True:
    a = input()
    if a == "over":
        break
    n = len(a)
    c1 = []
    c2 = []
    for i in range(n//2):
        c1.append(a[i])
        c2.append(a[n//2 + i])
    total += priority(find_duplicates(c1, c2)[0])

print(total)

