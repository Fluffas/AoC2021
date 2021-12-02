import sys

with open(sys.argv[1], "r") as file:
    inputs = [line.split() for line in file.readlines()]
    commands = [[c, int(x)] for c, x in inputs]

    hpos = 0
    depth = 0

    for c, x in commands:
        match c:
            case 'forward':
                hpos += x
            case 'up':
                depth -= x
            case 'down':
                depth += x

    print(hpos * depth)