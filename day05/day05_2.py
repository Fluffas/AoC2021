import sys
import os

with open(sys.argv[1], "r") as file:
    inputs = [[[int(n) for n in c.split(',')]
               for c in line.strip().split(' -> ')]
              for line in file.readlines()]

    coords = {}
    for (x1, y1), (x2, y2) in inputs:
        # Straight lines
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

        # Down right diagonal
        elif (x1 < x2 and y1 > y2) or (x2 < x1 and y2 > y1):
            line = [(a, b) for a, b in zip(
                range(min(x1, x2),
                      max(x1, x2) + 1), range(max(y1, y2),
                                              min(y1, y2) - 1, -1))]

            for c in line:
                if c in coords:
                    coords[c] += 1
                else:
                    coords[c] = 1

        # Up right diagonal
        else:
            line = [
                (a, b)
                for a, b in zip(range(min(x1, x2),
                                      max(x1, x2) +
                                      1), range(min(y1, y2),
                                                max(y1, y2) + 1))
            ]

            for c in line:
                if c in coords:
                    coords[c] += 1
                else:
                    coords[c] = 1

    print(len([num for num in coords.values() if num > 1]))
