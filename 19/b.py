#!/usr/bin/env python3
import sys
from comp import Comp

if len(sys.argv) == 1:
    print("Usage: python3 b.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

cur = []
out = 0

def get_input(comp):
    global cur
    return cur.pop(0)
def cb(comp, x):
    global out
    out = x
def on_exit(comp):
    pass

def compute(x, y):
    cur.append(x)
    cur.append(y)
    c = Comp(p[:], get_input, cb, on_exit)
    c.run()


def test(x, y, size):
    compute(x, y + size)
    if out == 1:
        compute(x + size, y)
        if out == 1:
            return True
    return False

def get_next_x(y):
    x = int(0.6*y)
    while True:
        compute(x, y)
        if out == 1: return x
        x += 1

def run(y, size):
    global out
    x = get_next_x(y)
    while True:
        compute(x, y)
        if out == 0: return (False, (x, y))
        success = test(x, y, size)
        if success:
            return (True, (x, y))
        x += 1

def search(min_y, max_y, size):
    best_res = ()
    while min_y < max_y:
        mid = (min_y + max_y)//2 
        success, (x, y) = run(mid, size)
        if success:
            max_y = mid
            best_res = (x, y)
        else: 
            min_y = mid + 1
    x, y = best_res
    min_dist = 9999999999
    minp = ()
    for y2 in range(y-10, y):
        success, (x, y) = run(y2, 99)
        if success:
            dist = x+y
            if dist < min_dist:
                min_dist = dist
                minp = (x, y)

    x, y = minp
    print(x*10000 + y)
search(0, 6000, 99)