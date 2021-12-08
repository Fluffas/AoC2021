import sys

with open(sys.argv[1], "r") as file:
    patterns = [[[d for d in p.split()] for p in line.strip().split(' | ')]
                for line in file.readlines()]

    ans = 0
    for signals, digits in patterns:
        values = {}
        # Find the easy values and remove them from the list
        values[1] = next((s for s in signals if len(s) == 2), None)
        signals.remove(values[1])
        values[7] = next((s for s in signals if len(s) == 3), None)
        signals.remove(values[7])
        values[4] = next((s for s in signals if len(s) == 4), None)
        signals.remove(values[4])
        values[8] = next((s for s in signals if len(s) == 7), None)
        signals.remove(values[8])

        # Find the rest of the values and remove them from the list
        values[9] = next((s for s in signals if len(
            s) == 6 and all(l in s for l in values[4])), None)
        signals.remove(values[9])
        values[0] = next((s for s in signals if len(
            s) == 6 and all(l in s for l in values[1])), None)
        signals.remove(values[0])
        values[6] = next((s for s in signals if len(s) == 6), None)
        signals.remove(values[6])

        values[3] = next((s for s in signals if len(
            s) == 5 and all(l in s for l in values[1])), None)
        signals.remove(values[3])
        values[5] = next((s for s in signals if len(
            s) == 5 and all(l in values[9] for l in s)), None)
        signals.remove(values[5])
        values[2] = next((s for s in signals if len(s) == 5), None)
        signals.remove(values[2])

        # Sort values for easy comparison
        for i in values:
            values[i] = sorted(values[i])

        # Get the output value
        out = ''
        for d in digits:
            for k, v in values.items():
                if sorted(d) == v:
                    out += str(k)

        ans += int(out)

    print(ans)
