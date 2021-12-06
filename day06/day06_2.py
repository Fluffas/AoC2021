import sys


def simulate(lf_count, days):
    for _ in range(days):
        lf_count_new = {6: 0, 8: 0}
        for d, c in lf_count.items():
            if d == 0:
                lf_count_new[6] += c
                lf_count_new[8] += c
            else:
                lf_count_new[d - 1] = c
        lf_count = lf_count_new

    return sum(lf_count.values())


with open(sys.argv[1], "r") as file:
    lanternfish = [int(x) for x in file.readline().split(',')]

    lanternfish_count = {}
    for i in range(8, -1, -1):
        lanternfish_count[i] = lanternfish.count(i)

    print(simulate(lanternfish_count, 256))