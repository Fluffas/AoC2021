import sys
import statistics

with open(sys.argv[1], "r") as file:
    positions = [int(x) for x in file.readline().split(',')]
    distances = [abs(x - int(statistics.mean(positions))) for x in positions]
    print(sum([d * (d + 1) / 2 for d in distances]))
