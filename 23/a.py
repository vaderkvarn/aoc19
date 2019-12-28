#!/usr/bin/env python3
import sys
from comp import Comp
from collections import deque

nc = 50

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

class Worker():
    def __init__(self, in_q, out_q, addr):
        self.in_q = in_q
        self.out_q = out_q
        self.addr = addr
        self.msg = []
        self.in_q.append(self.addr)
        self.comp = Comp(p[:], self.get_input, self.cb)

    def get_input(self, comp):
        if len(self.in_q) == 0:
            comp.pause()
            return -1
        return self.in_q.popleft()

    def cb(self, comp, x):
        self.msg.append(x)        
        if len(self.msg) == 3:
            self.out_q.append(tuple(self.msg))
            self.msg = []

    def run(self):
        self.comp.run()

out_q = deque()
workers = []
for i in range(nc):
    worker = Worker(deque(), out_q, i)
    workers.append(worker)

cur_comp = -1
while True:
    cur_comp = (cur_comp + 1)%nc
    workers[cur_comp].run()
    if len(out_q) == 0: continue
    addr, x, y = out_q.popleft()
    if addr < 50:
        c = workers[addr]
        c.in_q.append(x)
        c.in_q.append(y)
        c.run()
    else:
        print(y)
        break