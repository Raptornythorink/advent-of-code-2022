def move_score(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    return 3

def battle_score(move1, move2):
    if (move1 == "A" and move2 == "Y") or (move1 == "B" and move2 == "Z") or (move1 == "C" and move2 == "X"):
        return 6
    if (move1 == "A" and move2 == "X") or (move1 == "B" and move2 == "Y") or (move1 == "C" and move2 == "Z"):
        return 3
    if (move1 == "A" and move2 == "Z") or (move1 == "B" and move2 == "X") or (move1 == "C" and move2 == "Y"):
        return 0

total = 0

while True:
    a = input()
    if a == "over":
        break
    m1, m2 = a.split()
    total += move_score(m2) + battle_score(m1, m2)

print(total)

