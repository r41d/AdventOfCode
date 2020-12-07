#!/usr/bin/env python3

import functools
from scipy.spatial.distance import cityblock

with open("day15input.txt", 'r') as f:
	raw = [list(x) for x in f.readlines()]
	map = raw
	Y, X = len(map), len(map[0])

def cave(x, y, NEW=None):
	if NEW:
		map[y][x] = NEW
	return map[y][x]

def sort_order(m1, m2):
	if m1.pos[1] != m2.pos[1]:
		return m1.pos[1] < m2.pos[1]
	elif m1.pos[0] != m2.pos[0]:
		return m1.pos[0] < m2.pos[0]
	else:
		return 0

def sort_targets(t1, t2):
	if t1.hp != t2.hp:
		return h1.hp < t2.hp
	else:
		return sort_order(t1, t2)

class Monster():
	def __init__(self, x, y):
		self.pos = (x, y)
		self.dead = False
		self.hp = 200
		self.ap = 3
	def move(self, dir):
		newpos = [sum(x) for x in zip(self.pos, self.dir.value)]
		if cave(*newpos) == '.':
			self.pos = newpos
class Elf(Monster):
	def __repr__(self):
		return "<Elf x=%d y=%d>" % (self.pos[0], self.pos[1])
	def attack(self, goblins):
		targets = [g for g in goblins if cityblock(self.pos, g.pos) <= 1]
		if len(targets) < 1:
			return
		targets = sorted(targets, key=functools.cmp_to_key(sort_targets))
class Goblin(Monster):
	def __repr__(self):
		return "<Goblin x=%d y=%d>" % (self.pos[0], self.pos[1])
	def attack(self, elves):
		targets = [e for e in elves if cityblock(self.pos, e.pos) <= 1]
		if len(targets) < 1:
			return
		targets = sorted(targets, key=functools.cmp_to_key(sort_targets))


def find_entities():
	elves = []
	goblins = []
	for col in range(X):
		for row in range(Y):
			if cave(col,row) == 'E':
				elves.append(Elf(col, row))
			elif cave(col,row) == 'G':
				goblins.append(Goblin(col, row))
	return elves, goblins

elves, golins = find_entities()
