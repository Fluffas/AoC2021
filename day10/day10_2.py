import sys
import statistics

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def check_line(line):
    open_chunks = []
    for char in line:
        if char not in pairs.keys():
            if char != pairs[open_chunks[-1]]:
                return False
            else:
                open_chunks.pop()
        else:
            open_chunks.append(char)
    return True


def score_line(line):
    open_chunks = []
    for char in line:
        if char not in pairs.keys():
            open_chunks.pop()
        else:
            open_chunks.append(char)

    open_chunks.reverse()
    closing_chars = [pairs[o] for o in open_chunks]

    score = 0
    for c in closing_chars:
        score = score * 5 + scores[c]
    return score


with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]

    good_lines = [line for line in lines if check_line(line)]
    line_scores = [score_line(line) for line in good_lines]
    print(statistics.median(line_scores))
