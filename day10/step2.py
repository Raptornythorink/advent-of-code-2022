buffers = []
cycle = 0
screen = [['.' for _ in range(40)] for _ in range(6)]
x = 1

while True:
    a = input()
    if not a:
        while buffers:
            x += buffers[0]
            buffers.pop(0)
            if cycle % 40 in (x-1, x, x+1):
                screen[cycle//40][cycle%40] = "#"
            cycle += 1
        break
    command = a.split()
    if buffers:
        x += buffers[0]
        buffers.pop(0)
    if cycle % 40 in (x-1, x, x+1):
        screen[cycle//40][cycle%40] = "#"
    if command[0] == "noop":
        buffers.append(0)
    elif command[0] == "addx":
        buffers.append(0)
        buffers.append(int(command[1]))
    cycle += 1

for row in screen:
    for pixel in row:
        print(pixel, end="")
    print()