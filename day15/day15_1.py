import sys
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

with open(sys.argv[1], "r") as file:
    cave = [[int(c) for c in line.strip()] for line in file.readlines()]

    grid = Grid(matrix=cave)
    start = grid.node(0, 0)
    end = grid.node(len(cave[0]) - 1, len(cave) - 1)
    d = DijkstraFinder()

    path, _ = d.find_path(start, end, grid)

    risk = sum([cave[y][x] for (x, y) in path[1:]])
    print(risk)
