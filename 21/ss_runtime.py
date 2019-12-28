#!/usr/bin/env python3
import sys
from comp import Comp

if len(sys.argv) == 1:
    print("Usage: python3 ss_runtime.py <intcode> <springscript>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

def run():
    prog = open(sys.argv[2], "r").readlines()
    prog = [row for row in prog if row[0] != '#']
    prog =  list("".join(prog))
    row = []
    m = []
    def get_input(comp):
        nonlocal prog
        return prog.pop(0)
    def cb(comp, x):
        nonlocal row
        nonlocal m
        if isinstance(x, int):
            print(x)
            exit()
        if x == '\n' and len(row) > 0:
            m.append(row)
            row = []
        else: 
            row.append(x)
    c = Comp(p, get_input, cb, ascii_mode=True)
    c.run()
    for row in m:
        print("".join(row))
run()