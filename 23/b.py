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



nat_vals = (0, 0)
last_sent = (0, 0)
cur_comp = -1
num_idle = 0
while True:
    all_idle = True
    for w in workers:
        if len(w.in_q) > 0:
            all_idle = False
            break
    num_idle = num_idle + 1 if all_idle else 0
    if num_idle == 50:
        c = workers[0]
        nx, ny = nat_vals
        lx, ly = last_sent
        if ny == ly:
            print(ly)
            break
        c.in_q.append(nx)
        c.in_q.append(ny)
        last_sent = nat_vals
    cur_comp = (cur_comp + 1)%nc
    workers[cur_comp].run()
    if len(out_q) == 0: 
        continue
    num_idle = 0
    addr, x, y = out_q.popleft()
    if addr < 50:
        c = workers[addr]
        c.in_q.append(x)
        c.in_q.append(y)
        c.run()
    else:
        nat_vals = (x, y)