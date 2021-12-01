import sys

with open(sys.argv[1], "r") as file:
    inputs = [int(line) for line in file.readlines()]
    windows = [
        a + inputs[i + 1] + inputs[i + 2] for i, a in enumerate(inputs[:-2])
    ]
    print(len([a for i, a in enumerate(windows[:-1]) if a < windows[i + 1]]))
