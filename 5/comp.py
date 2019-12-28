from __future__ import annotations
from dataclasses import dataclass
from typing import List, Callable, Any

@dataclass
class Ins:
    modes: List[int]
    args: List[int]
    comp: Comp
    def next(self):
        return len(self.args) + self.comp.i + 1
    def get_arg(self, i):
        if self.modes[i] == 0:
            if self.args[i] >= len(self.comp.p):
                return 0
            return self.comp.p[self.args[i]]
        elif self.modes[i] == 1:
            return self.args[i] 
        elif self.modes[i] == 2:
            if self.args[i] + self.comp.rel >= len(self.comp.p):
                return 0
            return self.comp.p[self.args[i] + self.comp.rel]
    def write(self, i, val):
        addr = self.args[i] if self.modes[i] == 0 else self.args[i] + self.comp.rel
        if addr >= len(self.comp.p):
            for j in range(addr+1):
                self.comp.p.append(0)
        self.comp.p[addr] = val

class Add(Ins):
    def exec(self):
        self.write(2, self.get_arg(0) + self.get_arg(1))
        return self.next()
class Mul(Ins):
    def exec(self):
        self.write(2, self.get_arg(0) * self.get_arg(1))
        return self.next()
class Input(Ins):
    def exec(self):
        arg = self.comp.get_input(self.comp)
        if self.comp.ascii_mode:
            arg = ord(arg)
        self.write(0, arg)
        return self.next()
class Output(Ins):
    def exec(self):
        arg = self.get_arg(0)
        if self.comp.ascii_mode:
            if arg < 128:
                arg = chr(arg)
        self.comp.cb(self.comp, arg)
        return self.next()
class Halt(Ins):
    def exec(self):
        self.comp.on_exit(self.comp)
        self.comp.running = False
        self.comp.done = True
class Jit(Ins):
    def exec(self):
        return self.get_arg(1) if self.get_arg(0) != 0 else self.next()
class Jif(Ins):
    def exec(self):
        return self.get_arg(1) if self.get_arg(0) == 0 else self.next()
class Le(Ins):
    def exec(self):
        self.write(2, 1 if self.get_arg(0) < self.get_arg(1) else 0)
        return self.next()
class Eq(Ins):
    def exec(self):
        self.write(2, 1 if self.get_arg(0) == self.get_arg(1) else 0)
        return self.next()
class Rel(Ins):
    def exec(self):
        self.comp.rel += self.get_arg(0)
        return self.next()

class Comp: 
    def __init__(self, p, get_input, on_output, on_exit=lambda c: 0, ascii_mode=False):
        self.p = p
        self.get_input = get_input
        self.cb = on_output
        self.on_exit = on_exit
        self.running = True
        self.i = 0
        self.done = False
        self.rel = 0
        self.ascii_mode = ascii_mode
        self.instructions = {
            1:  Add,
            2:  Mul,
            3:  Input,
            4:  Output,
            5:  Jit,
            6:  Jif,
            7:  Le,
            8:  Eq,
            9:  Rel,
            99: Halt
        }
    
    def parse_modes(self, n):
        s = str(n)[::-1]
        modes = [0]*4
        if len(s) == 1: return  (int(s), modes)
        op = int(s[1])*10 + int(s[0])
        for i in range(2, len(s)):
            modes[i-2] = int(s[i])
        if op < 1 or (op > 9 and op != 99):
            print("Could not parse", n)
            exit(1)
        return (op, modes)

    def parse(self, i):
        op, modes = self.parse_modes(self.p[i])
        num_args = 1
        if op in [3, 4, 9]: num_args = 2
        if op in [5, 6]: num_args = 3
        if op in [1, 2, 7, 8]: num_args = 4
        args = self.p[i+1:i+num_args]
        return self.instructions[op](modes, args, self)

    def pause(self):
        self.running = False
    def run(self):
        self.running = True
        while self.running:
            ins = self.parse(self.i)
            self.i = ins.exec()
