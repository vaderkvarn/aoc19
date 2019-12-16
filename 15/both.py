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

def map_from_coords(coords):
    ps = coords.keys()
    min_x = min([p[0] for p in ps])
    max_x = max([p[0] for p in ps])
    min_y = min([p[1] for p in ps])
    max_y = max([p[1] for p in ps])
    m = [[' ' for x in range((max_x - min_x) + 1)] for y in range((max_y - min_y) + 1)]
    for i in range((max_y - min_y) + 1):
        for j in range((max_x - min_x) + 1):
            p = (min_x + j, min_y + i)
            if p in coords:
                m[i][j] = coords[p]
    return m

def get_map(program):
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
            if len(path) == 0:
                c.pause()
                return
            next = rev(path[-1])
        path.append(next)
        return next

    def cb(c, o):
        nonlocal p
        new_p = next_p(p, path[-1])
        if new_p in coords: #backtrack
            p = new_p
            path.pop()
            path.pop()
            return
        if o == 0:
            coords[new_p] = '#'
            path.pop()
            return
        if o == 1:
            coords[new_p] = '.'
        if o == 2:
            coords[new_p] = 'O'
        p = new_p

    def oe(c):
        pass

    c = Comp(program, get_input, cb, oe)
    c.run()
    return map_from_coords(coords)

def get_end_points(m):
    s = (); e = ()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'X':
                s = (j, i)
            if m[i][j] == 'O':
                e = (j, i)
    return (s, e)

def get_neighs(p, m):
    x, y = p
    ns = []
    if x + 1 < len(m[0]) and m[y][x + 1] != '#': ns.append((x + 1, y))
    if x - 1 >= 0        and m[y][x - 1] != '#': ns.append((x - 1, y))
    if y + 1 < len(m)    and m[y + 1][x] != '#': ns.append((x, y + 1))
    if y - 1 >= 0        and m[y - 1][x] != '#': ns.append((x, y - 1))
    return ns

def solve(m):
    start, end = get_end_points(m)
    q = deque([(0, end)])
    visited = set([end])
    max_dist = 0
    while len(q) > 0:
        dist, p = q.popleft()
        if p == start:
            print(dist)
        for n in get_neighs(p, m):
            if not n in visited:
                q.append((dist + 1, n))
                visited.add(n)
        max_dist = dist
    print(max_dist)
solve(get_map(program))