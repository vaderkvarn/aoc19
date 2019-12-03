from sys import maxsize

f = open("input", "r")
def parse(l):
    return [(p[0], int(p[1:])) for p in l.rstrip().split(',')]

w1 = parse(f.readline())
w2 = parse(f.readline())
visited = set([])

def add(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dir = 1 if x1 < x2 or y1 < y2 else -1
    for i in range(x1, x2, dir):
        visited.add((i, y1))
    for i in range(y1, y2, dir):
        visited.add((x1, i))

def get_crossings(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    crossings = []
    dir = 1 if x1 < x2 or y1 < y2 else -1
    for i in range(x1, x2, dir):
        if (i, y1) in visited:
            crossings.append((i, y1))
    for i in range(y1, y2, dir):
        if (x1, i) in visited:
            crossings.append((x1, i))
    return crossings

def move(p, m):
    x, y = p
    dir, num = m
    if   dir == 'U': y -= num
    elif dir == 'R': x += num
    elif dir == 'D': y += num
    elif dir == 'L': x -= num
    return (x, y)

pos = (0, 0)
for w in w1:
    new_pos = move(pos, w)
    add(pos, new_pos)
    pos = new_pos

pos = (0, 0)
min_dist = maxsize
for w in w2:
    new_pos = move(pos, w)
    cs = get_crossings(pos, new_pos)
    for c in cs:
        dist = abs(c[0]) + abs(c[1])
        if dist < min_dist and dist > 0: min_dist = dist
    pos = new_pos
print(min_dist)