import sympy

calcs = {}
values = {}
xs = sympy.Symbol('x')

while True:
    a = input()
    if not a:
        break
    name, calc = a.split(": ")
    if name == "root":
        root = calc.split()[::2]
    elif name == "humn":
        values["humn"] = xs
    elif len(calc) <= 3:
        values[name] = int(calc)
    else:
        calcs[name] = calc.split()

from time import time
st = time()

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
        val = v1 / v2
    values[monkey] = val
    return val

print(sympy.solve((test(root[0]) - test(root[1])), (xs)))
print(time()-st)