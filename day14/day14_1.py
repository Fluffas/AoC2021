import sys

with open(sys.argv[1], "r") as file:
    poly, rules = [f for f in file.read().split("\n\n")]
    rules = {a: b for l in rules.split("\n") for (a, b) in [l.split(" -> ")]}

    for _ in range(10):
        new_poly = poly[0]
        for i, c in enumerate(poly[1:], start=1):
            pair = poly[i - 1] + c
            new_poly += rules[pair] + c

        poly = new_poly

    char_count = {}
    for c in set(poly):
        char_count[c] = poly.count(c)

    print(max(i for i in char_count.values()) - min(i for i in char_count.values()))
