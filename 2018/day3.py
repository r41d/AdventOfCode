#!/usr/bin/env python3

import sys
import re

import numpy
import namedlist

# format: #<id> @ <x>,<y>: <width>x<height>
box_regex = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
Box = namedlist.namedlist('Box', 'i x y w h overlaps')

with open("day3input.txt", 'r') as f:
	box_strings = [x.strip() for x in f.readlines()]

boxes = []
for boxstr in box_strings:
	i, x, y, w, h = box_regex.search(boxstr).group(1,2,3,4,5)
	boxes.append(Box(int(i), int(x), int(y), int(w), int(h), False))

dimX = 1 + max([box.x+box.w for box in boxes])
dimY = 1 + max([box.y+box.h for box in boxes])
matrix = numpy.zeros(shape=(dimX+1, dimY+1))
for b in boxes:
	matrix[b.x : b.x+b.w , b.y : b.y+b.h] += 1

print("Part one:", len(numpy.extract(matrix > 1, matrix)))

for b in boxes:
	boxrange = matrix[b.x : b.x+b.w , b.y : b.y+b.h]
	if len(numpy.extract(boxrange > 1, boxrange)) > 1:
		b.overlaps = True

overlapfree = [b for b in boxes if not b.overlaps]
assert len(overlapfree) == 1
print("Part two:", overlapfree[0].i)
