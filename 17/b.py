#!/usr/bin/env python3
import sys
from comp import Comp
from collections import defaultdict
from itertools import chain


if len(sys.argv) == 1:
    print("Usage: python3 b.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

def get_map(p):
    row = []
    m = []
    def cb(comp, x):
        nonlocal row
        nonlocal m
        if chr(x) == '\n' and len(row) > 0:
            m.append(row)
            row = []
        else: row.append(chr(x))
    c = Comp(p, None, cb)
    c.run()
    return m

def get_start_values(m):
    start_pos = ()
    start_dir = ""
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] in "^>v<":
                start_pos = (j, i)
                start_dir = "^>v<".index(m[i][j]) 
    return (start_pos, start_dir)

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def is_scaffold(m, pos, size):
    x, y = pos
    w, h = size
    return x >= 0 and x < w and y >= 0 and y < h and m[y][x] == '#'

def next_pos_from_dir(pos, dir):
    x, y = pos
    if dir == NORTH: y -= 1
    if dir == EAST:  x += 1
    if dir == SOUTH: y += 1
    if dir == WEST:  x -= 1
    return (x, y)

def one_step(m, pos, dir, size):
    next_pos = next_pos_from_dir(pos, dir)
    return next_pos if is_scaffold(m, next_pos, size) else pos

def go_straight(m, pos, dir, size):
    num = 0
    while True:
        new_pos = one_step(m, pos, dir, size)
        if pos == new_pos: break
        num += 1
        pos = new_pos
    return (num, pos)

def make_turn(m, pos, dir, size):
    for i in [1, -1]:
        if is_scaffold(m, next_pos_from_dir(pos, (dir + i)%4), size):
            return (i, (dir + i)%4)
    return (0, 0)

def get_full_path(m, pos, dir):
    path = []
    size = (len(m[0]), len(m))
    dir = start_dir
    while True:
        turn, dir = make_turn(m, pos, dir, size)
        if turn == 0:
            break
        num, pos = go_straight(m, pos, dir, size)
        path.append(("R" if turn == 1 else "L", num))
    return path

def path_to_ascii(path):
    l = []
    for p in path:
        t, n = p
        l += [ord(t)] + [ord(",")] + [ord(x) for x in list(str(n))] + [ord(",")]
    l[-1] = ord("\n")
    
    return l


def get_largest_repeating_sequences(path):
    paths = defaultdict(int)
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            if len(path_to_ascii(path[i:j])) <= 20:
                paths[tuple(path[i:j])] += 1
    return list(map(list, sorted(paths.keys(), key=lambda p: paths[p]*len(p), reverse=True)))


letters = []
funcs = []
def build(path, i, rs, parts, res):
    if len(parts) > 3: return
    if list(chain.from_iterable(res)) == path:
        for p in parts: funcs.append(p)
        for r in res:
            if r == parts[0]: letters.append('A')
            if r == parts[1]: letters.append('B')
            if r == parts[2]: letters.append('C')
        return
    for part in parts:
        if path[i:i + len(part)] == part:
            build(path, i + len(part), rs[:], parts[:], res[:] + [part])
    for r in rs:
        if path[i:i + len(r)] == r:
            build(path, i + len(r), rs[:], parts[:] + [r], res[:] + [r])

m = get_map(p[:])
start_pos, start_dir = get_start_values(m)
path = get_full_path(m, start_pos, start_dir)
rs = get_largest_repeating_sequences(path)

build(path, 0, rs, [], [])

main = list(map(ord, list(",".join(letters))))
main.append(ord("\n"))
funcs = [path_to_ascii(f) for f in funcs]

def run(p, main, funcs, vid):
    p[0] = 2
    [a, b, c] = funcs
    inputs = main + a + b + c + vid
    output = 0
    def cb(comp, x):
        nonlocal output
        output = x
    def get_input(comp):
        return inputs.pop(0)
    c = Comp(p, get_input, cb)
    c.run()
    print(output)

run(p[:], main, funcs, [ord("n"), ord("\n")])
