#!/usr/bin/env python3
import sys
from comp import Comp
from itertools import combinations

if len(sys.argv) == 1:
    print("Usage: python3 a.py <intcode>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

def save(ic, file="save_file"):
    f = open(file, "w")
    f.write(",".join([str(i) for i in ic]))
    f.close()

def load(file="save_file"):
    f = open(file, "r")
    ic = [int(x) for x in f.readline().split(',')]
    f.close()
    return ic

#Call run() and collect all items manually
#Then type save and exit.
def run():
    prog =  []
    row = []
    def get_input(comp):
        nonlocal prog
        if len(prog) == 0:
            prog =  list("".join(input()))
            if "".join(prog) == "save":
                print("saving")
                prog = []
                save(comp.p)
                return "\n"
            if "".join(prog) == "load":
                print("loading")
                prog = []
                comp.p = load()
                return "\n"
            prog.append('\n')
        return prog.pop(0)
    def cb(comp, x):
        nonlocal row
        if isinstance(x, int):
            print(x)
            exit()
        if x == '\n':
            print("".join(row))
            row = []
        else: 
            row.append(x)
    c = Comp(p, get_input, cb, ascii_mode=True)
    c.run()
#run()

inv = []
def run_auto(prog):
    prog =  list("".join(prog))
    row = []
    p = load()
    def get_input(comp):
        nonlocal prog
        if len(prog) == 0:
            comp.pause()
            return "\n"
        if "".join(prog).startswith("load"):
            prog = prog[4:]
            comp.p = load("save_file")
            return "\n"
        return prog.pop(0)
    getting_inv = False
    def cb(comp, x):
        nonlocal row
        nonlocal getting_inv
        if x == '\n':
            s = "".join(row)
            if s.startswith("\"Oh"):
                print(int(s.split("typing ")[1].split(" ")[0]))
                exit()
            if getting_inv and s.startswith("-"):
                inv.append(s[2:])
            if s.startswith("Items in"): getting_inv = True
            row = []
        else: 
            row.append(x)
    c = Comp(p, get_input, cb, ascii_mode=True)
    c.run()

prog = "inv\n"
run_auto(prog)
for i in range(len(inv)):
    for c in combinations(inv, i):
        prog = ["drop " + item + "\n" for item in c]
        prog.insert(0, "load")
        prog.append("north\n")
        run_auto("".join(prog))