#!/usr/bin/env python3
import sys
from comp import Comp

if len(sys.argv) == 1:
    print("Usage: python3 both.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

row = []
m = []
def cb(comp, x):
    global row
    global m
    if chr(x) == '\n' and len(row) > 0:
        m.append(row)
        row = []
    else: row.append(chr(x))
c = Comp(p, None, cb)
c.run()

s = 0
for i in range(1, len(m) - 1):
    for j in range(1, len(m[0]) - 1):
        if m[i+1][j] == '#' and m[i-1][j] == '#' and m[i][j+1] == '#' and m[i][j-1] == '#':
            s += i*j
print(s)