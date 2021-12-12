import sys


class cave:
    def __init__(self, name):
        self.name = name
        self.big = name.isupper()
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def find_paths(cave, path=[], twice=False):
    path.append(cave.name)
    if cave.name == "end":
        paths.append(path)
        return

    for n in cave.neighbors:
        n = caves[n]
        if n.big or n.name not in path:
            find_paths(n, path.copy(), twice)
        elif not twice and n.name != "start":
            find_paths(n, path.copy(), True)


with open(sys.argv[1], "r") as file:
    inputs = [[i for i in line.strip().split("-")] for line in file.readlines()]

    caves = {}
    for i in set(sum(inputs, [])):
        caves[i] = cave(i)
    for c1, c2 in inputs:
        caves[c1].neighbors.append(c2)
        caves[c2].neighbors.append(c1)

    paths = [[]]
    find_paths(caves["start"])
    paths.remove([])

    print(len(paths))
