#!/usr/bin/env python3

import numpy

input = 9424

def calc(x, y, serialNumber=input):
	rackID = x + 10
	pwrLvl = rackID * y
	pwrLvl += serialNumber
	pwrLvl *= rackID
	pwrLvl %= 1000
	pwrLvl //= 100
	pwrLvl -= 5
	return pwrLvl

# print(calc(122,79,57))
# print(calc(217,196,39))
# print(calc(101,153,71))

def prepare(input):
	matrix = numpy.zeros(shape=(301, 301)) # row 0 and col 0 unused
	for y in range(1, matrix.shape[1]):
		for x in range(1, matrix.shape[0]):
			matrix[x,y] = calc(x,y,input)
	return matrix

def part1(input):
	matrix = prepare(input)

	sX, sY, largest = 0, 0, 0
	for y in range(1, matrix.shape[1]-4):
		for x in range(1, matrix.shape[0]-4):
			sumsum = sum(sum(matrix[ x:x+3 , y:y+3 ]))
			if sumsum > largest:
				sX, sY = x, y
				largest = sumsum

	print(sX, sY, sep=',')

def part2(input):
	matrix = prepare(input)

	sX, sY, size, largest = 0, 0, 0, 0
	for s in range(1, 301):
		for y in range(1, matrix.shape[1] - s - 1):
			for x in range(1, matrix.shape[0] - s - 1):
				sumsum = sum(sum(matrix[ x:x+s , y:y+s ]))
				if sumsum > largest:
					sX, sY = x, y
					size = s
					largest = sumsum

	print(sX, sY, size, sep=',')


part1(input)
part2(input)
