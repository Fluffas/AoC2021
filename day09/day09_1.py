import sys

with open(sys.argv[1], "r") as file:
    heightmap = [[int(c) for c in line.strip()] for line in file.readlines()]

    low_points = []
    for y, row in enumerate(heightmap):
        for x, point in enumerate(row):
            maxx = len(row) - 1
            maxy = len(heightmap) - 1
            match x, y:
                # Top left
                case 0, 0:
                    compare = [row[x+1], heightmap[y+1][x]]
                # Top right
                case x, 0 if x == maxx:
                    compare = [row[x-1], heightmap[y+1][x]]
                # Bottom left
                case 0, y if y == maxy:
                    compare = [row[x+1], heightmap[y-1][x]]
                # Bottom right
                case x, y if x == maxx and y == maxy:
                    compare = [row[x-1], heightmap[y-1][x]]
                # Top edge
                case x, 0 if x != 0 and x != maxx:
                    compare = [row[x-1], row[x+1], heightmap[y+1][x]]
                # Bottom edge
                case x, y if y == maxy and x != 0 and x != maxx:
                    compare = [row[x-1], row[x+1], heightmap[y-1][x]]
                # Left edge
                case 0, y if y != 0 and y != maxy:
                    compare = [row[x+1], heightmap[y-1][x], heightmap[y+1][x]]
                # Right edge
                case x, y if x == maxx and y != 0 and y != maxy:
                    compare = [row[x-1], heightmap[y-1][x], heightmap[y+1][x]]
                # Everything else
                case _:
                    compare = [row[x-1], row[x+1],
                               heightmap[y-1][x], heightmap[y+1][x]]

            if all(n > point for n in compare):
                low_points.append(point)

    print(sum(p + 1 for p in low_points))
