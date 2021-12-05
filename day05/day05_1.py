import sys

with open(sys.argv[1], "r") as file:
    inputs = [[[int(n) for n in c.split(',')]
               for c in line.strip().split(' -> ')]
              for line in file.readlines()]

    coords = {}
    for (x1, y1), (x2, y2) in inputs:
        if x1 == x2 or y1 == y2:
            line = [(a, b) for a in range(min(x1, x2),
                                          max(x1, x2) + 1)
                    for b in range(min(y1, y2),
                                   max(y1, y2) + 1)]

            for c in line:
                if c in coords:
                    coords[c] += 1
                else:
                    coords[c] = 1

    print(len([num for num in coords.values() if num > 1]))