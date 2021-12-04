import sys


def check_board(board, called_nums):
    for row in board:
        if all(num in called_nums for num in row):
            return True

    columns = []
    for i in range(len(board)):
        columns.append([row[i] for row in board])
    for col in columns:
        if all(num in called_numbers for num in col):
            return True


with open(sys.argv[1], "r") as file:
    inputs = file.read().split("\n\n")
    numbers = [int(x) for x in inputs[0].split(',')]
    boards = [[[int(y) for y in n.split()] for n in b.split('\n')]
              for b in [foo for foo in inputs[1:]]]

    called_numbers = []
    for n in numbers:
        called_numbers.append(n)
        for b in boards:
            if check_board(b, called_numbers):
                print('bingo!')
                print(
                    sum(list(set(sum(b, [])) - set(called_numbers))) *
                    called_numbers[-1])
                sys.exit()
