import sys


def get_neighbors(y_pos, x_pos, y_max, x_max):
    return [
        [_y, _x]
        for _x in range(x_pos - 1, x_pos + 2)
        for _y in range(y_pos - 1, y_pos + 2)
        if _x >= 0
        and _y >= 0
        and _x <= x_max
        and _y <= y_max
        and not (_x == x_pos and _y == y_pos)
    ]


with open(sys.argv[1], "r") as file:
    octos = [[int(o) for o in line.strip()] for line in file.readlines()]
    ymax = len(octos) - 1
    xmax = len(octos[0]) - 1

    step = 0
    while not all(o == 0 for o in sum(octos, [])):
        step += 1
        octos = [[o + 1 for o in r] for r in octos]
        flashing = [
            [y, x] for x in range(xmax + 1) for y in range(ymax + 1) if octos[y][x] > 9
        ]
        flashed = []
        while len(flashing) > 0:
            for y, x in flashing:
                neighs = get_neighbors(y, x, ymax, xmax)
                for n_y, n_x in neighs:
                    if [n_y, n_x] not in flashed:
                        octos[n_y][n_x] += 1
                        if octos[n_y][n_x] > 9:
                            if [n_y, n_x] not in flashing:
                                flashing.append([n_y, n_x])
                octos[y][x] = 0
                flashing.remove([y, x])
                flashed.append([y, x])

    print(step)
