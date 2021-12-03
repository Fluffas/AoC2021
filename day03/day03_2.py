import sys


def find_ratings(common, data):
    for i in range(len(data[0])):
        if len(data) == 1:
            return data[0]
        if sum([int(a[i]) for a in data]) >= len(data) / 2:
            c = str(int(common))
        else:
            c = str(int(not common))
        data = [b for b in data if b[i] == c]
    return data[0]


with open(sys.argv[1], "r") as file:
    bins = [line.strip() for line in file.readlines()]
    oxy = find_ratings(common=True, data=bins)
    co2 = find_ratings(common=False, data=bins)

    print(int(oxy, 2) * int(co2, 2))
