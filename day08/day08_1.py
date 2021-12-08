import sys

with open(sys.argv[1], "r") as file:
    patterns = [[[d for d in p.split()] for p in line.strip().split(' | ')]
                for line in file.readlines()]

    print(len(sum([[d for d in digits if len(d) in [2, 3, 4, 7]]
          for _, digits in patterns], [])))
