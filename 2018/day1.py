#!/usr/bin/env python3

with open("day1input.txt", 'r') as f:
    numbers = f.readlines()
freqs = [int(f.strip()) for f in numbers]
print("Part one:", sum(freqs))

acc = 0
reached = {acc}
steps = 0
while True:
    for f in freqs:
        steps += 1
        acc += f
        if acc in reached:
            print("Part two:", acc, "- found after", steps, "steps")
            break
        reached.add(acc)
