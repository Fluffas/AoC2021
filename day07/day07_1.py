import sys
import statistics

with open(sys.argv[1], "r") as file:
    positions = [int(x) for x in file.readline().split(',')]
    print(sum([abs(x - statistics.median(positions)) for x in positions]))
