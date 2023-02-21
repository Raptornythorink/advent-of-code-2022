monkeys = []

class Monkey:
    def __init__(self, num, items, operation, operand, quotient, true_target, false_target):
        self.num = num
        self.items = items
        self.operation = operation
        self.operand = operand
        if self.operand == "":
            if self.operation == "+":
                self.func = lambda x : 2 * x
            elif self.operation == "-":
                self.func = lambda x : 0
            else:
                self.func = lambda x : x ** 2
        else:
            if self.operation == "+":
                self.func = lambda x : x + self.operand
            elif operation == "-":
                self.func = lambda x : x - self.operand
            else:
                self.func = lambda x : x * self.operand
        self.quotient = quotient
        self.true_target = true_target
        self.false_target = false_target
        self.checked = 0

while True:
    a = input()
    if not a:
        break
    num = int(a[7:-1])
    a = input()
    items = list(map(int, a[18:].split(', ')))
    a = input()
    operation = a[23]
    if a[25] == "o":
        operand = ""
    else:
        operand = int(a[25:])
    a = input()
    quotient = int(a[21:])
    a = input()
    true_target = int(a[29:])
    a = input()
    false_target = int(a[30:])
    a = input()
    monkeys.append(Monkey(num, items, operation, operand, quotient, true_target, false_target))

for _ in range(20):
    for monkey in monkeys:
        while monkey.items:
            monkey.checked += 1
            item = monkey.items.pop(0)
            newitem = monkey.func(item) // 3
            if newitem % monkey.quotient:
                monkeys[monkey.false_target].items.append(newitem)
            else:
                monkeys[monkey.true_target].items.append(newitem)

max1, max2 = 0, 0

for monkey in monkeys:
    if monkey.checked > max1:
        max1, max2 = monkey.checked, max1
    elif monkey.checked > max2:
        max2 = monkey.checked

print(max1 * max2)