import sys

with open(sys.argv[1], "r") as file:
    bins = [line.strip() for line in file.readlines()]

    gamma = ''
    for i in range(len(bins[0])):
        gamma += str(round(sum([int(b[i]) for b in bins]) / len(bins)))

    epsilon = gamma.replace('0', 'a').replace('1', '0').replace('a', '1')

    print(int(gamma, 2) * int(epsilon, 2))
