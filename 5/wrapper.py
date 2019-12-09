#!/usr/bin/env python3
import sys
from comp import Comp

if len(sys.argv) == 1:
    print("Usage: python3 both.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

def get_input(comp):
    return int(input())
def cb(comp, x):
    print(x)
def on_exit(comp):
    exit(0)
c = Comp(p, get_input, cb, on_exit)
c.run()
