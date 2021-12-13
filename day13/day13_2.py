import sys

with open(sys.argv[1], "r") as file:
    coords, instructions = [f for f in file.read().split("\n\n")]
    coords = [[int(c) for c in line.split(",")] for line in coords.split()]
    instructions = [
        [a, int(b)]
        for line in instructions.split("\n")
        for (a, b) in [line.split()[2].split("=")]
    ]

    paper = coords
    for (axis, c_fold) in instructions:
        if axis == "x":
            for i in [[x, y] for (x, y) in paper if x == c_fold]:
                paper.remove(i)
            folding = [[x, y, x - c_fold] for (x, y) in paper if x > c_fold]
            for (x, y, x_offset) in folding:
                paper.remove([x, y])
                if [c_fold - x_offset, y] not in paper:
                    paper.append([c_fold - x_offset, y])
        else:
            for i in [[x, y] for (x, y) in paper if y == c_fold]:
                paper.remove(i)
            folding = [[x, y, y - c_fold] for (x, y) in paper if y > c_fold]
            for (x, y, y_offset) in folding:
                paper.remove([x, y])
                if [x, c_fold - y_offset] not in paper:
                    paper.append([x, c_fold - y_offset])

    x_size = max(x for (x, y) in paper)
    y_size = max(y for (x, y) in paper)
    final_paper = []
    for y in range(y_size + 1):
        line = []
        for x in range(x_size + 1):
            if [x, y] in paper:
                line.append("#")
            else:
                line.append(".")
        final_paper.append(line)

    for line in final_paper:
        print(line)
