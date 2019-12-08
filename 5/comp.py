from __future__ import annotations
from dataclasses import dataclass
from typing import List, Callable, Any

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
@dataclass
class Input(Ins):
    comp: Comp
    get_input: Callable[[Comp], int] 
    def exec(self, p, i):
        p[self.args[0]] = self.get_input(self.comp)
        return self.next(i)
@dataclass
class Output(Ins):
    comp: Comp
    cb: Callable[[Comp, int], None] 
    def exec(self, p, i):
        self.cb(self.comp, self.get_arg(0, p))
        return self.next(i)
@dataclass
class Halt(Ins):
    comp: Comp
    on_exit: Callable[[Comp], None] 
    def exec(self, p, i):
        self.on_exit(self.comp)
        self.comp.done = True
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

class Comp: 
    def __init__(self, p, get_input, on_output, on_exit):
        self.p = p
        self.get_input = get_input
        self.cb = on_output
        self.on_exit = on_exit
        self.running = True
        self.i = 0
        self.done = False
    
    def ins_factory(self, op, modes, args):
        if op == 1: return Add(modes, args)
        if op == 2: return Mul(modes, args)
        if op == 3: return Input(modes, args, self, self.get_input)
        if op == 4: return Output(modes, args, self, self.cb)
        if op == 5: return Jit(modes, args)    
        if op == 6: return Jif(modes, args)    
        if op == 7: return Le(modes, args)    
        if op == 8: return Eq(modes, args)    
        if op == 99: 
            self.running = False
            return Halt(modes, args, self, self.on_exit)

    def parse_modes(self, n):
        s = str(n)[::-1]
        modes = [0]*4
        if len(s) == 1: return  (int(s), modes)
        op = int(s[1])*10 + int(s[0])
        for i in range(2, len(s)):
            modes[i-2] = int(s[i])
        return (op, modes)
    def parse(self, i):
        op, modes = self.parse_modes(self.p[i])
        num_args = 1
        if op in [3, 4]: num_args = 2
        if op in [5, 6]: num_args = 3
        if op in [1, 2, 7, 8]: num_args = 4
        args = self.p[i+1:i+num_args]
        ins = self.ins_factory(op, modes, args)
        return ins 

    def pause(self):
        self.running = False
    def run(self):
        self.running = True
        while self.running:
            ins = self.parse(self.i)
            self.i = ins.exec(self.p, self.i)

