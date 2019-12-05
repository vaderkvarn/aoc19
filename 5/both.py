from dataclasses import dataclass
from typing import List

p = [int(x) for x in open("input", "r").readline().split(',')]

def ins_factory(op, modes, args):
    if op == 1: return Add(modes, args)
    if op == 2: return Mul(modes, args)
    if op == 3: return Input(modes, args)
    if op == 4: return Output(modes, args)
    if op == 5: return Jit(modes, args)    
    if op == 6: return Jif(modes, args)    
    if op == 7: return Le(modes, args)    
    if op == 8: return Eq(modes, args)    
    if op == 99: return Halt(modes, args)

@dataclass
class Ins:
    modes: List[int]
    args: List[int]
    def next(self, i):
        return len(self.args) + i + 1
    def get_arg(self, i, p):
        return self.args[i] if self.modes[i] == 1 else p[self.args[i]]

class Add(Ins):
    def exec(self, p, i):
        p[self.args[2]] = self.get_arg(0, p) + self.get_arg(1, p)
        return self.next(i)
class Mul(Ins):
    def exec(self, p, i):
        p[self.args[2]] = self.get_arg(0, p) * self.get_arg(1, p)
        return self.next(i)
class Input(Ins):
    def exec(self, p, i):
        p[self.args[0]] = int(input("Enter value: "))
        return self.next(i)
class Output(Ins):
    def exec(self, p, i):
        if self.get_arg(0, p) != 0: print(self.get_arg(0, p))
        return self.next(i)
class Halt(Ins):
    def exec(self, p, i):
        exit(0)
class Jit(Ins):
    def exec(self, p, i):
        return self.get_arg(1, p) if self.get_arg(0, p) != 0 else self.next(i)
class Jif(Ins):
    def exec(self, p, i):
        return self.get_arg(1, p) if self.get_arg(0, p) == 0 else self.next(i)
class Le(Ins):
    def exec(self, p, i):
        p[self.args[2]] = 1 if self.get_arg(0, p) < self.get_arg(1, p) else 0
        return self.next(i)
class Eq(Ins):
    def exec(self, p, i):
        p[self.args[2]] = 1 if self.get_arg(0, p) == self.get_arg(1, p) else 0
        return self.next(i)

def parse_modes(n):
    s = str(n)[::-1]
    modes = [0]*4
    if len(s) == 1: return  (int(s), modes)
    op = int(s[1]*10) + int(s[0])
    for i in range(2, len(s)):
        modes[i-2] = int(s[i])
    return (op, modes)
def parse(p, i):
    op, modes = parse_modes(p[i])
    num_args = 1
    if op in [3, 4]: num_args = 2
    if op in [5, 6]: num_args = 3
    if op in [1, 2, 7, 8]: num_args = 4
    args = p[i+1:i+num_args]
    ins = ins_factory(op, modes, args)
    return ins 

def run():
    i = 0
    while p[i] != 99:
        ins = parse(p, i)
        i = ins.exec(p, i)

run()
