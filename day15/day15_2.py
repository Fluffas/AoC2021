import sys
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

with open(sys.argv[1], "r") as file:
    cave = [[int(c) for c in line.strip()] for line in file.readlines()]

    cave_matrix = []
    for y in range(5):
        cave_row = []
        for x in range(5):
            curr_cave = []
            for row in cave:
                curr_row = []
                for d in row:
                    d = d + x + y
                    if d > 9:
                        d = d % 9
                    curr_row.append(d)
                curr_cave.append(curr_row)
            cave_row.append(curr_cave)
        cave_matrix.append(cave_row)

    big_cave = []
    for cave_row in cave_matrix:
        for x in range(len(cave_row[0])):
            big_cave_row = []
            for y in range(len(cave_row)):
                big_cave_row += cave_row[y][x]
            big_cave.append(big_cave_row)

    grid = Grid(matrix=big_cave)
    start = grid.node(0, 0)
    end = grid.node(len(big_cave[0]) - 1, len(big_cave) - 1)
    d = DijkstraFinder()

    path, _ = d.find_path(start, end, grid)

    risk = sum([big_cave[y][x] for (x, y) in path[1:]])
    print(risk)
