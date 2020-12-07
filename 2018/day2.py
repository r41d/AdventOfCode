#!/usr/bin/env python3

import sys
import collections
import Levenshtein

with open("day2input.txt", 'r') as f:
    sequences = f.readlines()
    sequences = [s.strip() for s in sequences]
counts = [collections.Counter(seq).most_common() for seq in sequences]
counts = [set([x[1] for x in com]) for com in counts]
count2 = sum([1 for x in counts if 2 in x])
count3 = sum([1 for x in counts if 3 in x])
print("Part one:", count2 * count3)

for x in sequences:
    for y in sequences:
        ham = Levenshtein.hamming(x, y)
        if ham == 1:
            diffs = [i for i in range(len(x)) if x[i] != y[i]]
            assert len(diffs) == 1
            dif = diffs[0]
            print("Part two:", x[:dif] + x[dif+1:] )
            sys.exit(0)
