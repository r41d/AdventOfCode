#!/usr/bin/env python3

import operator
import string

def get_key_for_min_value(dic):
	return min(dic.items(), key=operator.itemgetter(1))[0]

with open("day5input.txt", 'r') as f:
	polymer = f.readlines()[0].strip()


shit = [x+x.upper() for x in string.ascii_lowercase]
shit = shit + [''.join(reversed(x)) for x in shit]

def full_obliterate(polymer : str):
	l = len(polymer)
	while True:
		for s in shit:
			polymer = polymer.replace(s, '')
		if len(polymer) < l:
			l = len(polymer)
		else:
			return polymer

print("Part one:", len(full_obliterate(polymer)))


polyRem = {c : len(full_obliterate(polymer.replace(c, '').replace(c.upper(), '')))
			for c in string.ascii_lowercase}

print("Part two:", polyRem[get_key_for_min_value(polyRem)])

