from math import pi, atan2
from collections import defaultdict
f = open("input", "r")
grid = []
for line in f:
    grid.append(list(line.rstrip()))

w = len(grid[0])
h = len(grid)

def get_angles(a, grid):
    x0, y0 = a
    angles = defaultdict(list)
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '.' or (x == x0 and y == y0): continue
            angle = atan2(x - x0, y0 - y)
            if angle < 0: angle += 2*pi
            angles[angle].append((x, y))
    return angles

def solve_a(grid):
    max_visible = 0
    max_a = ()
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '.': continue
            num_visible = len(get_angles((x, y), grid))
            if num_visible > max_visible:
                max_visible = num_visible
                max_a = (x, y)

    return (max_visible, max_a)

def solve_b(a0, grid):
    num_vaporized = 0
    while True:
        angles = get_angles(a0, grid)
        ks = sorted(list(angles.keys()))
        for a in ks:
            if len(angles[a]) > 0:
                x, y = angles[a].pop(0)
                num_vaporized += 1 
                grid[y][x] = '.'
                if num_vaporized == 200:
                    return (x, y)

visible, a = solve_a(grid)
print(visible)
x, y = solve_b(a, grid)
print(x*100 + y)