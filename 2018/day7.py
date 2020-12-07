#!/usr/bin/env python3

import re

task_regex = re.compile("^Step ([A-Z]) must be finished before step ([A-Z]) can begin\.$")

with open("day7input.txt", 'r') as f:
	raw = [x.strip() for x in f.readlines()]
tasks = [task_regex.search(t).group(1,2) for t in raw]
alltasks = sorted(list(set([x[0] for x in tasks] + [x[1] for x in tasks])))

################################################################################

tasking = {t : [x[0] for x in tasks if x[1]==t] for t in alltasks}
taskorder = []

while tasking:
	do_it = sorted({a:b for a,b in tasking.items() if b==[]})[0]
	taskorder.append(do_it)
	del tasking[do_it]
	for a,b in tasking.items():
		if do_it in b:
			b.remove(do_it)

print("Part one:", "".join(taskorder))

################################################################################

tasking = {t : [x[0] for x in tasks if x[1]==t] for t in alltasks}
taskorder = []
workers = {}
worker_count = 5
totaltime = 0

while tasking or workers:
	good2go = sorted({a:b for a,b in tasking.items() if b==[]})
	if len(good2go) > 0 and len(workers) < worker_count:
		do_it = good2go[0]
		workers[do_it] = ord(do_it)-4
		del tasking[do_it] # remove task from pool
	elif len(workers) > 0:
		seconds = min(workers.values())
		workers = {t: s-seconds for t, s in workers.items()}
		donejobs = [t for t, s in workers.items() if s == 0]
		workers = {t: s for t, s in workers.items() if s > 0}
		totaltime += seconds
		# remove task from other jobs' prerequisites
		tasking = {t:[p for p in pre if p not in donejobs] for t,pre in tasking.items()}
	else:
		print("WTF!?!")
		break

print("Part two:", totaltime)
