def move(stacks, nop, source, dest):
    for _ in range(nop):
        stacks[dest].append(stacks[source].pop())

nstacks = int(input())
stacks = [[] for _ in range(nstacks)]

while True:
    a = input()
    if a[1] == "1":
        break
    for i in range(nstacks):
        crate = a[4*i + 1]
        if crate != " ":
            stacks[i].append(crate)

for i in range(nstacks):
    stacks[i].reverse()

input()

while True:
    a = input()
    if a == "":
        break
    command = a.split()
    nop = int(command[1])
    source = int(command[3]) - 1
    dest = int(command[5]) - 1
    move(stacks, nop, source, dest)

for stack in stacks:
    print(stack[-1], end="")