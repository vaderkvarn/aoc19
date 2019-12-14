#!/usr/bin/env python3
from comp import Comp
import time
import termios
import sys, tty

if len(sys.argv) == 1:
    print("Usage: python3 both.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]

raw_output = []

state = [[' ' for x in range(44)] for y in range(44)] 

mode = 2

def get_tile_char(tile):
    c = ' '
    if tile == 1: c = '|'
    if tile == 2: c = '#'
    if tile == 3: c = '_'
    if tile == 4: c = 'O'
    return c

def printGame(state):
    for row in state:
        print("".join(row))

def update(state, val):
    (x, y, tile) = val
    state[y][x] = get_tile_char(tile)

def _find_getch():
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

def next_move(state):
    player_x = 0
    ball_x = 0
    for i in range(len(state)):
        for j in range(len(state[0])): 
            if state[i][j] == '_':
                player_x = j
            if state[i][j] == 'O':
                ball_x = j
    if player_x < ball_x:
        return 1
    if player_x == ball_x:
        return 0
    if player_x > ball_x:
        return -1

def get_input(comp):
    if mode < 2:
        printGame(state)
    if mode == 0:
        c = getch()
        if c == 'a': return -1
        if c == 's': return  0
        if c == 'd': return  1
    elif mode == 1:
        time.sleep(0.01)
        return next_move(state)
    elif mode == 2:
        return next_move(state)
    return 0
vals = []
score = 0
def cb(comp, x):
    global vals
    global score
    vals.append(x)
    if len(vals) == 3:
        if vals[0] == -1 and vals[1] == 0:
            score = vals[2]
        else: update(state, vals)
        vals = []

def on_exit(comp):
    print(score)

p[0] = 2
c = Comp(p, get_input, cb, on_exit)
c.run()