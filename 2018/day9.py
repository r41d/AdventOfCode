#!/usr/bin/env python3

from collections import deque, defaultdict

def marble_game(players, turns):
	marbles = list(reversed(range(1, turns+1)))
	circle = deque([0])
	curIdx = 0
	scores = defaultdict(int)
	while marbles:
		for p in range(1, players+1):
			if not marbles:
				break
			t = marbles.pop()
			if t % 23 == 0:
				scores[p-1] += t
				rmIdx = (curIdx - 7) % len(circle)
				circle.rotate(-rmIdx)
				scores[p-1] += circle.popleft()
				circle.rotate(rmIdx + 6)
			else:
				circle.append(t)
				circle.rotate(-1)
				#print("--> Added", t, "to idx", curIdx)
			curIdx = len(circle) - 2
			#print(p, t, len(circle), circle)
	return scores.values()

print(max(marble_game(426, 72058)))
print(max(marble_game(426, 7205800)))
