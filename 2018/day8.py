#!/usr/bin/env python3
import re
import namedlist

with open("day8input.txt", 'r') as f:
	raw = [int(x) for x in [x.strip() for x in f.readlines()][0].split(" ")]

Node = namedlist.namedlist('Node', 'metadata children')

def build_tree(numbers):
	c, md, rest = numbers[0], numbers[1], numbers[2:]
	newnode = Node([], [])
	for i in range(c):
		child, rest = build_tree(rest)
		newnode.children.append(child)
	newnode.metadata, rest = rest[:md], rest[md:]
	return newnode, rest

HEAD = build_tree(raw)[0]

def summing(aux):
	return sum(aux.metadata) + sum([summing(c) for c in aux.children])
print(summing(HEAD))

def summing2(aux):
	if not aux.children:
		return sum(aux.metadata)
	else:
		indexes = [idx-1 for idx in aux.metadata if idx <= len(aux.children)]
		return sum([summing2(aux.children[idx]) for idx in indexes])
print(summing2(HEAD))
