#!/usr/bin/env python3

initial = "##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#."

transitions = {
	"..#..": ".",	"..#.#": ".",	"#.#..": ".",	".#..#": ".",
	"#....": ".",	"....#": ".",	".#.#.": "#",	"#.###": ".",
	"####.": ".",	".....": ".",	".#...": "#",	"#####": "#",
	".####": ".",	"#..#.": "#",	"#...#": "#",	".###.": ".",
	"###.#": "#",	"...##": "#",	"#.##.": "#",	".#.##": "#",
	"##.#.": "#",	"...#.": ".",	"..###": "#",	"###..": "#",
	"##...": ".",	"..##.": ".",	".##.#": ".",	"##.##": ".",
	".##..": ".",	"##..#": "#",	"#.#.#": ".",	"#..##": "#"
}

assert transitions['.....'] == '.' # otherwise things would get very ugly

def naive(generations=20):
	bufferL = 10
	bufferR = generations
	state = list(bufferL*'.' + initial + '.'*bufferR)

	for _ in range(generations):
		newstate = list("." * len(state))
		for i in range(2, len(state)-3):
			newstate[i] = transitions[''.join(state[i-2:i+3])]
		state = newstate
	plantsWithNumbers = list(zip(state, range(-bufferL, len(initial)+bufferR)))
	numbersOfPotsWithPlant = [p[1] for p in plantsWithNumbers if p[0] == '#']
	return sum(numbersOfPotsWithPlant)

def pattern(generations=50000000000):
	bufferL = 10
	bufferR = 1000
	state = list(bufferL*'.' + initial + '.'*bufferR)
	middle = ""

	for g in range(generations):
		newstate = list("." * len(state))
		for i in range(2, len(state)-3):
			newstate[i] = transitions[''.join(state[i-2:i+3])]
		state = newstate
		#print(''.join(state))
		newmiddle = ''.join(state).strip('.')
		if middle == newmiddle:
			#print("PATTERN FOUND in step %d!!!" % g)
			remaining = generations - g - 1
			plantsWithNumbers = list(zip(state, range(-bufferL, len(initial)+bufferR)))
			numbersOfPotsWithPlant = [p[1]+remaining for p in plantsWithNumbers if p[0] == '#']
			return sum(numbersOfPotsWithPlant)
		middle = newmiddle


print(naive(20))
print(pattern(50000000000))
