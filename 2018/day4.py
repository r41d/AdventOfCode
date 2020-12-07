#!/usr/bin/env python3

import sys
import re
from enum import Enum, auto
import datetime
import pprint
import collections
from collections import OrderedDict
import operator

import numpy
import namedlist

# format: year-month-day hour:minute action
event_regex = re.compile("^\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.+)$")
Event = namedlist.namedlist('Event', 'ts Y M D h m action who')
shift_regex = re.compile("Guard #(\d+) begins shift")
class Action(Enum): BEGIN = auto(); ASLEEP = auto(); WAKEUP = auto()

def get_key_for_max_value(dic):
	return max(dic.items(), key=operator.itemgetter(1))[0]

with open("day4input.txt", 'r') as f:
	eventstr = [x.strip() for x in f.readlines()]

events = []
for evstr in eventstr:
	Y, M, D, h, m = map(int, event_regex.search(evstr).group(1,2,3,4,5))
	act = event_regex.search(evstr).group(6)
	if act == 'wakes up':
		action, who = Action.WAKEUP, None
	elif act == 'falls asleep':
		action, who = Action.ASLEEP, None
	elif shift_regex.search(act):
		action, who = Action.BEGIN, int(shift_regex.search(act).group(1))
	else:
		print("COULDN'T PARSE ACTION", act)
		sys.exit(1)
	events.append(Event(datetime.datetime(Y, M, D, h, m), Y, M, D, h, m, action, who))
events = sorted(events, key=lambda e: e.ts)
cur = None
for event in events:
	if event.action == Action.BEGIN:    cur = event.who
	elif event.action == Action.ASLEEP: event.who = cur
	elif event.action == Action.WAKEUP: event.who = cur
guards = set([x.who for x in events])

sleepsleep = {g : {x:0 for x in range(60)} for g in guards}
asleeptime = None
for e in events:
	if e.action == Action.ASLEEP:
		asleeptime = e.ts
	elif e.action == Action.WAKEUP:
		start = int(asleeptime.timestamp()) - 6*60
		end = int(e.ts.timestamp()) - 6*60
		sleepyminutes = [int(x/60%60) for x in list(range(start, end, 60))]
		for sleeping in sleepyminutes:
			sleepsleep[e.who][sleeping] += 1

sleepiest_guard = get_key_for_max_value({g:sum(s.values()) for g,s in sleepsleep.items()})
sleepiest_minute = get_key_for_max_value(sleepsleep[sleepiest_guard])
print("Part one:", sleepiest_guard*sleepiest_minute)

sleepiest_guard = None
sleepiest_minute_count = 0
for g, mins in sleepsleep.items():
	most_sleepy_minute = get_key_for_max_value(mins)
	if mins[most_sleepy_minute] > sleepiest_minute_count:
		sleepiest_minute_count = mins[most_sleepy_minute]
		sleepiest_guard = g
print("Part two:", sleepiest_guard*sleepiest_minute)
