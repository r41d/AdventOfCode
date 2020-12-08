#!/usr/bin/env python3

import re
import namedlist

# format: <min>-<max> <letter>: <password>
# example: 5-9 g: ggccggmgn
password_regex = re.compile("^(\d+)-(\d+) ([a-z]): ([a-z]+)$")
Password = namedlist.namedlist('Password', 'min max letter password')

with open("day02input.txt", 'r') as f:
    input = [x.strip() for x in f.readlines()]
    passwords = []
    for pw_str in input:
        min, max, letter, pw = password_regex.search(pw_str).group(1,2,3,4)
        passwords.append(Password(int(min), int(max), letter, pw))

def valid(password):
    count = password.password.count(password.letter)
    return count in range(password.min, password.max+1)

# for pw in passwords:
#     print(pw, valid(pw))

print("Part one:", sum([valid(x) for x in passwords]))

# Part 2:

def valid2(password):
    pos1 = password.letter == password.password[password.min-1]
    pos2 = password.letter == password.password[password.max-1]
    return pos1 ^ pos2

print("Part two:", sum([valid2(x) for x in passwords]))
