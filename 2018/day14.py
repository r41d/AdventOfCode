#!/usr/bin/env python3

input = 920831

from collections import deque
from itertools import cycle, islice

def env(l, index, count):
    aux = islice(cycle(l), index, index+count)
    return list(aux)

scoreboard = [3,7]
elfo = 0
elfi = 1
made = 0

def new_recipes(scoreboard, elfo, elfi):
	#print(scoreboard, len(scoreboard), elfo, elfi)
	cur1 = scoreboard[elfo]
	cur2 = scoreboard[elfi]
	return list(map(int, str(cur1+cur2)))

for cnt in range(1000):
	#print(scoreboard)
	new_ones = new_recipes(scoreboard, elfo, elfi)
	scoreboard += new_ones
	made += len(new_ones)
	elfo = (elfo + 1 + scoreboard[elfo]) % len(scoreboard)
	elfi = (elfi + 1 + scoreboard[elfi]) % len(scoreboard)
	#print(elfo, elfi, scoreboard)
	next10scores_1 = ''.join(map(str, env(scoreboard, elfo+1, 10)))
	next10scores_2 = ''.join(map(str, env(scoreboard, elfi+1, 10)))
	# print(made, next10scores_1, next10scores_2)
	stops = [x+10 for x in [5, 9, 18, 2018]]
	if len(scoreboard) in stops or len(scoreboard)-1 in stops or len(scoreboard)+1 in stops:
	 	print(len(scoreboard), next10scores_1)
	if cnt > 3000:
		break
