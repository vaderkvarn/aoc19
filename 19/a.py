#!/usr/bin/env python3
import sys
from comp import Comp

size = 50
if len(sys.argv) == 1:
    print("Usage: python3 a.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

data = []
tot = 0
for x in range(size):
    for y in range(size):
        data.append(x)
        data.append(y)

pt = []
def get_input(comp):
    return data.pop()
def cb(comp, x):
    global tot
    tot += x
def on_exit(comp):
    pass
while len(data) > 0:
    c = Comp(p[:], get_input, cb, on_exit)
    c.run()

print(tot)