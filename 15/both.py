#!/usr/bin/env python3
import sys
from comp import Comp
from collections import deque

if len(sys.argv) == 1:
    print("Usage: python3 both.py <program>")
    exit(1)

program = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

def next_p(p, i):
    x, y = p
    if i == 1: y -= 1
    if i == 2: y += 1
    if i == 3: x -= 1
    if i == 4: x += 1
    return (x, y)

def rev(i):
    return i - 1 if i%2 == 0 else i + 1

def get_coords(program):
    path = []
    p = (0, 0)
    coords = {(0, 0): 'X'}
    def get_input(c):
        nonlocal p
        next = 0
        for i in range(1, 5):
            new_p = next_p(p, i)
            if not new_p in coords:
                next = i
                break
        if next == 0: #backtrack 
            if len(path) == 0: #done
                c.pause()
                return
            next = rev(path[-1])
        path.append(next)
        return next

    def cb(c, o):
        nonlocal p
        new_p = next_p(p, path[-1])
        if o == 0:
            coords[new_p] = '#'
            path.pop()
        else:
            if new_p in coords: #backtrack
                path.pop()
                path.pop()
            elif o == 1: coords[new_p] = '.'
            elif o == 2: coords[new_p] = 'O'
            p = new_p

    c = Comp(program, get_input, cb, None)
    c.run()
    return coords

def solve(cs):
    start = (); end = ()
    for k, v in cs.items():
        if v == 'X': start = k
        if v == 'O': end = k
    q = deque([(0, end)])
    visited = set([end])
    max_dist = 0
    while len(q) > 0:
        dist, p = q.popleft()
        if p == start:
            print(dist)
        x, y = p
        for n in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if n in cs and not n in visited and cs[n] != '#':
                q.append((dist + 1, n))
                visited.add(n)
        max_dist = dist
    print(max_dist)

solve(get_coords(program))