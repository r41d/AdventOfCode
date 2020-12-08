#!/usr/bin/env python3

goal = 2020

with open("day01input.txt", 'r') as f:
    numbers = f.readlines()
numbers = [int(n) for n in numbers]
#print(numbers)

# Part 1

matrix = list(x+y for x in numbers for y in numbers)
#print(len(matrix))

for idx, num in enumerate(matrix):
    if num == goal:
        realIdx = idx // len(numbers)
        print("Part one:", numbers[realIdx] * (2020-numbers[realIdx]))
        break

# Part 2

matrix3 = list((x, y, z, x+y+z) for x in numbers for y in numbers for z in numbers)

for value in matrix3:
    (x, y, z, num) = value
    if num == goal:
        print("Part two:", x*y*z)
        break
