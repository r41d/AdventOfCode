#!/usr/bin/env python3

import re
import operator
import pprint
import numpy
import namedlist

star_regex = re.compile("^position=<\ ?(-?\d+),\ *(-?\d+)> velocity=<\ ?(-?\d+),\ *(-?\d+)>$")
Star = namedlist.namedlist('Star', 'x y i j')

with open("day10input.txt", 'r') as f:
	raw = [x.strip() for x in f.readlines()]
	parsed = [star_regex.search(r).group(1,2,3,4) for r in raw]
	stars = [Star(*map(int, x)) for x in parsed]


def onestep(stars):
	for s in stars:
		s.x, s.y = list(map(operator.add, (s.x, s.y), (s.i, s.j)))
	return stars

def boundaries(stars):
	xmin = min([s.x for s in stars])
	xmax = max([s.x for s in stars])
	ymin = min([s.y for s in stars])
	ymax = max([s.y for s in stars])
	area = (xmax-xmin) * (ymax-ymin)
	return xmin, xmax, ymin, ymax, area

def show(stars):
	xmin, xmax, ymin, ymax, area = boundaries(stars)

	view = [(s.x-xmin, s.y-ymin) for s in stars]
	#print(xmax-xmin, ymax-ymin)
	matrix = numpy.zeros(shape=(xmax-xmin+1, ymax-ymin+1))
	for s in view:
		matrix[s[0] , s[1]] = 1
	for y in range(matrix.shape[1]):
		for x in range(matrix.shape[0]):
			print("#" if matrix[x,y]>0 else " ", end='')
		print()
	#pprint.pprint(view)

it = stars
steps = 0
found = 0
while True:
	it = onestep(it)
	steps += 1
	_, _, _, _, area = boundaries(it)
	#print(area)
	if area < 1000:
		found = 1
		show(it)
		print(steps)
	if found and area > 5000:
		break
