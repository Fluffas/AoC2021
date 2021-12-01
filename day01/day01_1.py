import sys

with open(sys.argv[1], "r") as file:
    inputs = [int(line) for line in file.readlines()]
    print(len([a for i, a in enumerate(inputs[:-1]) if a < inputs[i + 1]]))
