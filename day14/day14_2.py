import sys

with open(sys.argv[1], "r") as file:
    poly, rules = [f for f in file.read().split("\n\n")]
    rules = {a: b for l in rules.split("\n") for (a, b) in [l.split(" -> ")]}

    poly_count = {}
    for i, c in enumerate(poly[:-1]):
        pair = c + poly[i + 1]
        poly_count[pair] = poly.count(pair)

    char_count = {}
    for c in set(poly):
        char_count[c] = poly.count(c)

    for _ in range(40):
        new_poly_c = {}
        for k, v in poly_count.items():
            p1 = k[0] + rules[k]
            p2 = rules[k] + k[1]
            if p1 in new_poly_c:
                new_poly_c[p1] += v
            else:
                new_poly_c[p1] = v
            if p2 in new_poly_c:
                new_poly_c[p2] += v
            else:
                new_poly_c[p2] = v

            char_count[rules[k]] += v

        poly_count = new_poly_c

    print(max(i for i in char_count.values()) - min(i for i in char_count.values()))
