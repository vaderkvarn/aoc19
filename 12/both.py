from parse import parse
from math import gcd

from functools import reduce
f = open("input", "r")
moons = []
for line in f:
    position = parse('<x={:d}, y={:d}, z={:d}>', line).fixed
    moons.append((position, (0, 0, 0)))

start_moons = moons[:]

def comp(p):
    a, b = p
    if a < b : return  1
    if a > b : return -1
    return 0

def apply_gravity(moon, moons):
    pos, vel = moon
    x, y, z = vel
    for other in moons:
        if other == moon: continue
        grav = map(lambda p: comp(p), zip(pos, other[0]))
        vel = tuple(map(sum, zip(vel, grav)))
    pos = tuple(map(sum, zip(pos, vel)))
    return (pos, vel)

def lcm (a, b):
    return  a * b // gcd(a, b)


def get_energy(moons):
    def f(p):
        return sum(map(abs, p))
    return sum(map(lambda moon: f(moon[0])*f(moon[1]), moons))

def run_a(moons):
    for step in range(1000):
        new_moons = []
        for moon in moons:
            new_moons.append(apply_gravity(moon, moons))
        moons = new_moons[:]
    return get_energy(moons)

print(run_a(moons))

def run_b(moons):
    intervals = [0, 0, 0]
    step = 0
    while True:
        new_moons = []
        for moon in moons:
            new_moons.append(apply_gravity(moon, moons))
        for axis in range(3):
            if intervals[axis] > 0: continue
            found = True
            for i in range(4):
                pos, vel = moons[i]
                p = pos[axis]
                v = vel[axis]
                if  p != start_moons[i][0][axis] or v != 0:
                    found = False
            if found: 
                intervals[axis] = step                   
        if all(intervals): 
            break
        moons = new_moons[:]
        step += 1
    return reduce(lcm, intervals)

print(run_b(moons))