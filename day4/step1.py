total = 0

while True:
    a = input()
    if a == "over":
        break
    pair1, pair2 = a.split(',')
    sec1s, sec1e = pair1.split('-')
    sec2s, sec2e = pair2.split('-')
    sec1 = set([i for i in range(int(sec1s), int(sec1e) + 1)])
    sec2 = set([i for i in range(int(sec2s), int(sec2e) + 1)])
    if sec1 & sec2 in (sec1, sec2):
        total += 1

print(total)
