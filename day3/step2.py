def priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1

def find_duplicates(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))

counter = 0
total = 0
lines = [[], [], []]

while True:
    a = input()
    if a == "over":
        break
    lines[counter] = list(a)
    counter += 1
    if counter == 3:
        counter = 0
        total += priority(find_duplicates(lines[0], lines[1], lines[2])[0])

print(total)
