def move_score(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    return 3

def battle_score(res):
    if res == "X":
        return 0
    elif res =="Y":
        return 3
    elif res == "Z":
        return 6

def move_convertor(move1, res):
    if (move1 == "A" and res == "X") or (move1 == "B" and res == "Z") or (move1 == "C" and res == "Y"):
        return "Z"
    elif (move1 == "B" and res == "X") or (move1 == "C" and res == "Z") or (move1 == "A" and res == "Y"):
        return "X"
    elif (move1 == "C" and res == "X") or (move1 == "A" and res == "Z") or (move1 == "B" and res == "Y"):
        return "Y"

total = 0

while True:
    a = input()
    if a == "over":
        break
    m1, res = a.split()
    m2 = move_convertor(m1, res)
    total += move_score(m2) + battle_score(res)

print(total)
