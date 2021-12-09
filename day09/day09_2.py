import sys

with open(sys.argv[1], "r") as file:
    heightmap = [[int(c) for c in line.strip()] for line in file.readlines()]

    basins = []
    for y, row in enumerate(heightmap):
        for x, point in enumerate(row):
            if point != 9:
                maxx = len(row) - 1
                maxy = len(heightmap) - 1
                match x, y:
                    # Top left
                    case 0, 0:
                        compare = [(x + 1, y), (x, y + 1)]
                    # Top right
                    case x, 0 if x == maxx:
                        compare = [(x - 1, y), (x, y + 1)]
                    # Bottom left
                    case 0, y if y == maxy:
                        compare = [(x + 1, y), (x, y - 1)]
                    # Bottom right
                    case x, y if x == maxx and y == maxy:
                        compare = [(x - 1, y), (x, y - 1)]
                    # Top edge
                    case x, 0 if x != 0 and x != maxx:
                        compare = [(x - 1, y), (x + 1, y), (x, y + 1)]
                    # Bottom edge
                    case x, y if y == maxy and x != 0 and x != maxx:
                        compare = [(x - 1, y), (x + 1, y), (x, y - 1)]
                    # Left edge
                    case 0, y if y != 0 and y != maxy:
                        compare = [(x + 1, y), (x, y - 1), (x, y + 1)]
                    # Right edge
                    case x, y if x == maxx and y != 0 and y != maxy:
                        compare = [(x - 1, y), (x, y - 1), (x, y + 1)]
                    # Everything else
                    case _:
                        compare = [(x - 1, y), (x + 1, y),
                                   (x, y - 1), (x, y + 1)]

                appended = False
                for i, b in enumerate(basins):
                    if any(p in compare for p in b):
                        if appended:
                            basins[i] = list(
                                set(basins[i]).union(set(basins[added])))
                            basins.remove(basins[added])
                        else:
                            added = i
                            basins[i].append((x, y))
                            appended = True
                if not appended:
                    basins.append([(x, y)])

    basin_sizes = [len(b) for b in basins]
    basin_sizes.sort()
    print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
