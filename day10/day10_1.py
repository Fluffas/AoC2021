import sys

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def score_line(line):
    open_chunks = []
    for char in line:
        if char not in pairs.keys():
            if char != pairs[open_chunks[-1]]:
                return scores[char]
            else:
                open_chunks.pop()
        else:
            open_chunks.append(char)
    return 0


with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]
    print(sum(score_line(l) for l in lines))
