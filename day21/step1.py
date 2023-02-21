calcs = {}
values = {}

while True:
    a = input()
    if not a:
        break
    name, calc = a.split(": ")
    if len(calc) <= 3:
        values[name] = int(calc)
    else:
        calcs[name] = calc.split()

def test(monkey):
    if monkey in values:
        return values[monkey]
    v1, v2 = test(calcs[monkey][0]), test(calcs[monkey][2])
    if calcs[monkey][1] == "+":
        val = v1 + v2
    elif calcs[monkey][1] == "-":
        val = v1 - v2
    elif calcs[monkey][1] == "*":
        val = v1 * v2
    else:
        val = v1 // v2
    values[monkey] = val
    return val

print(test("root"))