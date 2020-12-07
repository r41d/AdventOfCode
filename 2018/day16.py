#!/usr/bin/env python3

import re
import copy
import time
import pprint
import collections

registers = "\[(\d), (\d), (\d), (\d)\]"
before_regex = re.compile("^Before: %s$" % registers)
instruction_regex = re.compile("^(\d+) (\d) (\d) (\d)$")
after_regex = re.compile("^After:  %s$" % registers)

with open("day16input.txt", 'r') as f:
	raw = f.read()
	desc, code = raw.split("\n\n\n\n")
	desc = [d for d in desc.split("\n") if len(d)]
	code = code.split("\n")
	# print(len(desc), len(code))
	# print(desc)
	# print(code)

class VM():
	def __init__(self, reg = [0] * 4):
		self.registers = reg
		self.allops = [
			self.addr, self.addi, self.mulr, self.muli,
			self.banr, self.bani, self.borr, self.bori,
			self.setr, self.seti,
			self.gtir, self.gtri, self.gtrr,
			self.eqir, self.eqri, self.eqrr
		]

	def set_register(self, num, val):
		assert 0 <= num < len(self.registers)
		self.registers[num] = val

	def addr(self, A, B, C):
		self.set_register(C, self.registers[A] + self.registers[B])
	def addi(self, A, B, C):
		self.set_register(C, self.registers[A] + B)

	def mulr(self, A, B, C):
		self.set_register(C, self.registers[A] * self.registers[B])
	def muli(self, A, B, C):
		self.set_register(C, self.registers[A] * B)

	def banr(self, A, B, C):
		self.set_register(C, self.registers[A] & self.registers[B])
	def bani(self, A, B, C):
		self.set_register(C, self.registers[A] & B)

	def borr(self, A, B, C):
		self.set_register(C, self.registers[A] | self.registers[B])
	def bori(self, A, B, C):
		self.set_register(C, self.registers[A] | B)

	def setr(self, A, _, C):
		self.set_register(C, self.registers[A])
	def seti(self, A, _, C):
		self.set_register(C, A)

	def gtir(self, A, B, C):
		self.set_register(C, 1 if A > self.registers[B] else 0)
	def gtri(self, A, B, C):
		self.set_register(C, 1 if self.registers[A] > B else 0)
	def gtrr(self, A, B, C):
		self.set_register(C, 1 if self.registers[A] > self.registers[B] else 0)

	def eqir(self, A, B, C):
		self.set_register(C, 1 if A == self.registers[B] else 0)
	def eqri(self, A, B, C):
		self.set_register(C, 1 if self.registers[A] == B else 0)
	def eqrr(self, A, B, C):
		self.set_register(C, 1 if self.registers[A] == self.registers[B] else 0)

	def run_test(self, testcase):
		possibleOps = []
		for op in self.allops:
			self.registers = copy.deepcopy(testcase.before)
			op(*testcase.code[1:])
			if self.registers == testcase.after:
				possibleOps.append(op.__name__)
		return possibleOps


class TestCase():
	def __init__(self, before, code, after): # all are [int,int,int,int]
		self.before = before
		self.code = code
		self.after = after
	def __repr__(self):
		return "%s -> %s -> %s" % (self.before, ' '.join(map(str, self.code)), self.after)

tests = []
for i, s in enumerate(desc):
	if i % 3 == 0:
		b, i, a = desc[i], desc[i+1], desc[i+2]
		before = list(map(int, before_regex.search(b).group(1,2,3,4)))
		instruction = list(map(int, instruction_regex.search(i).group(1,2,3,4)))
		after = list(map(int, after_regex.search(a).group(1,2,3,4)))
		newtest = TestCase(before, instruction, after)
		tests.append(newtest)

vm = VM()
counts = {op:collections.Counter() for op in range(16)}
for t in tests:
	possible = vm.run_test(t)
	# if t.code[0] == 14:
	# 	print(t, possible)
	for p in possible:
		counts[t.code[0]][p] += 1
#pprint.pprint(counts)

# Part 1 calculation
testing = {t:vm.run_test(t) for t in tests}
print(len([len(t) for t in testing.values() if len(t) >= 3]))


counterCopy = copy.deepcopy(counts)

opcodes = {}
while len(counterCopy) > 0:
	time.sleep(1)
	pprint.pprint(counterCopy)
	for opIdx, cnts in counterCopy.items():
		if len(cnts) <= 1:
			print("len <= 1 case")
			opcodes[opIdx] = list(cnts.values())[0]
			del counterCopy[opIdx]
			break
		sorted_cnts = sorted(cnts.items(), reverse=True, key=lambda kv: kv[1])
		print(sorted_cnts)
		if sorted_cnts[0][1] > sorted_cnts[1][1]:
			print("most_common case")
			opcodes[opIdx] = sorted_cnts[0][0]
			del counterCopy[opIdx]
			break
	print("Found codes:", opcodes)

print(opcodes)


# code = [c.strip() for c in code if len(c)]
# program = []
# for c in code:
# 	#print(c)
# 	ins = list(map(int, instruction_regex.search(c).group(1,2,3,4)))
# 	program.append(ins)
