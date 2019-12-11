import sys
from comp import Comp

if len(sys.argv) == 1:
    print("Usage: python3 both.py <program>")
    exit(1)

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]
p_orig = p[:]

up = 0
right = 1
down = 2
left = 3

visited = {}
cur = (0, 0)
output = []
direction =  up

def move(direction, cur):
    x, y = cur
    if direction == up:    y -= 1
    if direction == right: x += 1
    if direction == down:  y += 1
    if direction == left:  x -= 1
    return (x, y)

def get_input(comp):
    return visited[cur] if cur in visited else 0
def cb(comp, x):
    global cur
    global direction
    output.append(x)
    if len(output) == 2:
        turn = output.pop()
        color = output.pop()
        visited[cur] = color
        if turn == 1: direction = (direction + 1)%4
        else:         direction = (direction - 1)%4
        cur = move(direction, cur)
def run_a():
    def on_exit(comp):
        print(len(visited))

    visited[cur] = 0
    c = Comp(p, get_input, cb, on_exit)
    c.run()

def run_b():
    def on_exit(comp):
        max_x = 0
        max_y = 0
        for (x, y) in visited:
            if x >= max_x: max_x = x + 1
            if y >= max_y: max_y = y + 1
        print('P2', max_x, max_y, 1)
        for y in range(max_y):
            for x in range(max_x):
                if (x, y) in visited:
                    print(visited[(x, y)], end=' ')
                else:
                    print(0, end=' ')
            print()

    visited[cur] = 1
    c = Comp(p_orig, get_input, cb, on_exit)
    c.run()

run_a()
visited = {}
cur = (0, 0)
output = []
direction =  up
run_b()