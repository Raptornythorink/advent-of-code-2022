from ast import literal_eval

i = 1
pairs = [[[2]], [[6]]]

def compare_ints(i1, i2):
    if i1 == i2:
        return None
    return i1 < i2

def compare_lists(l1, l2):
    if not l1 and not l2:
        return None
    if l2 and not l1:
        return True
    if l1 and not l2:
        return False
    if isinstance(l1[0], int) and isinstance(l2[0], int):
        comparison = compare_ints(l1[0], l2[0])
    elif isinstance(l1[0], int):
        comparison = compare_lists([l1[0]], l2[0])
    elif isinstance(l2[0], int):
        comparison = compare_lists(l1[0], [l2[0]])
    else:
        comparison = compare_lists(l1[0], l2[0])
    if comparison == None:
        return compare_lists(l1[1:], l2[1:])
    if not comparison:
        return False
    if comparison:
        return True

def addpair(pairs, pair):
    n = len(pairs)
    for i in range(n):
        if compare_lists(pair, pairs[i]):
            pairs.insert(i, pair)
            return pairs
    pairs.append(pair)
    return pairs

while True:
    a = input()
    if not a:
        break
    pairs = addpair(pairs, literal_eval(a))
    pairs = addpair(pairs, literal_eval(input()))
    input()

print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))