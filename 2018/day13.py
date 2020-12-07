#!/usr/bin/env python3

import numpy
import itertools
import functools
from enum import Enum
import os, sys

with open("day13input.txt", 'r') as f:
	raw = [list(x) for x in f.readlines()]
	Y, X = len(raw), len(raw[0])
	# array = numpy.char.array(raw)
	# array.shape = (len(raw), len(raw[0]))
def tracks(x, y, NEW=None):
	if NEW:
		raw[y][x] = NEW
	return raw[y][x]

class Dir(Enum):
	UP    = (0, -1)
	DOWN  = (0, +1)
	LEFT  = (-1, 0)
	RIGHT = (+1, 0)

class Turn(Enum):
	LEFT = 1
	STRAIGHT = 2
	RIGHT = 3

class Cart():
	def __init__(self, x, y, dir):
		self.pos = (x, y)
		self.dir = dir
		self.turn = Turn.LEFT
		self.crashed = False
	def nextturn(self):
		if   self.turn == Turn.LEFT:     self.turn = Turn.STRAIGHT
		elif self.turn == Turn.STRAIGHT: self.turn = Turn.RIGHT
		elif self.turn == Turn.RIGHT:    self.turn = Turn.LEFT
	def move(self):
		self.pos = [sum(x) for x in zip(self.pos, self.dir.value)]
		if tracks(*self.pos) in ['-', '|']:
			return
		elif tracks(*self.pos) == '+':
			if   self.turn == Turn.LEFT:
				if   self.dir == Dir.UP:    self.dir = Dir.LEFT
				elif self.dir == Dir.DOWN:  self.dir = Dir.RIGHT
				elif self.dir == Dir.LEFT:  self.dir = Dir.DOWN
				elif self.dir == Dir.RIGHT: self.dir = Dir.UP
			elif self.turn == Turn.STRAIGHT:
				pass
			elif self.turn == Turn.RIGHT:
				if   self.dir == Dir.UP:    self.dir = Dir.RIGHT
				elif self.dir == Dir.DOWN:  self.dir = Dir.LEFT
				elif self.dir == Dir.LEFT:  self.dir = Dir.UP
				elif self.dir == Dir.RIGHT: self.dir = Dir.DOWN
			self.nextturn()
		elif tracks(*self.pos) == '/':
			if   self.dir == Dir.UP:    self.dir = Dir.RIGHT
			elif self.dir == Dir.DOWN:  self.dir = Dir.LEFT
			elif self.dir == Dir.LEFT:  self.dir = Dir.DOWN
			elif self.dir == Dir.RIGHT: self.dir = Dir.UP
		elif tracks(*self.pos) == '\\':
			if   self.dir == Dir.UP:    self.dir = Dir.LEFT
			elif self.dir == Dir.DOWN:  self.dir = Dir.RIGHT
			elif self.dir == Dir.LEFT:  self.dir = Dir.UP
			elif self.dir == Dir.RIGHT: self.dir = Dir.DOWN

def poscmp(c1, c2):
	cmp = lambda a, b: (a > b) - (a < b)
	if cmp(c1.pos[1], c2.pos[1]) != 0:
		return cmp(c1.pos[1], c2.pos[1])
	else:
		return cmp(c1.pos[0], c2.pos[0])

def make_track(x, y):
	# case '-'
	if tracks(x-1, y) in ['\\', '-', '+'] and tracks(x+1, y) in ['-', '+']:
		tracks(x, y, '-')
	# case '|'
	elif tracks(x, y-1) in ['/', '|', '+'] and tracks(x, y+1) in ['/', '|', '+']:
		tracks(x, y, '|')
	else:
		print("Couldn't make track at", x, y)

def find_carts():
	carts = []
	for col in range(X):
		for row in range(Y):
			if tracks(col,row) == '<':
				carts.append(Cart(col, row, Dir.LEFT))
				make_track(col, row)
			elif tracks(col,row) == '>':
				carts.append(Cart(col, row, Dir.RIGHT))
				make_track(col, row)
			elif tracks(col,row) == '^':
				carts.append(Cart(col, row, Dir.UP))
				make_track(col, row)
			elif tracks(col,row) == 'v':
				carts.append(Cart(col, row, Dir.DOWN))
				make_track(col, row)
	return carts

def find_crash(carts):
	for c1, c2 in itertools.product(carts, carts):
		if c1 == c2:
			continue
		if c1.pos == c2.pos:
			# print("Crash at", c1.pos)
			c1.crashed = c2.crashed = True
			return c1.pos
	return None

def day13():
	first = True
	carts = find_carts()
	while True:
		carts = sorted([c for c in carts if not c.crashed], key=functools.cmp_to_key(poscmp))
		if len(carts) == 1:
			print("Last cart standing at", carts[0].pos)
			return
		for c in carts:
			c.move()
			if find_crash(carts):
				if first:
					print("First crash at", find_crash(carts))
					first = False


day13()
