buffers = []
cycle = 1
saved = []
x = 1

while True:
    a = input()
    if not a:
        while buffers:
            x += buffers[0]
            buffers.pop(0)
            if cycle % 40 == 20:
                saved.append([cycle, x])
            cycle += 1
        break
    command = a.split()
    if buffers:
        x += buffers[0]
        buffers.pop(0)
    if command[0] == "noop":
        buffers.append(0)
    elif command[0] == "addx":
        buffers.append(0)
        buffers.append(int(command[1]))
    if cycle % 40 == 20:
        saved.append([cycle, x])
    cycle += 1

total = 0
for cycle, value in saved:
    print(cycle, x)
    total += cycle * value
print(total)
