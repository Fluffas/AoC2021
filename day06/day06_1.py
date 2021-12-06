import sys


def simulate(lf, days):
    for _ in range(days):
        for i in range(len(lf)):
            if lf[i] == 0:
                lf[i] = 6
                lf.append(8)
            else:
                lf[i] -= 1

    return len(lf)


with open(sys.argv[1], "r") as file:
    lanternfish = [int(x) for x in file.readline().split(',')]
    print(simulate(lanternfish, 80))