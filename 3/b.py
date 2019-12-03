from sys import maxsize

f = open("input", "r")
def parse(l):
    return [(p[0], int(p[1:])) for p in l.rstrip().split(',')]

w1 = parse(f.readline())
w2 = parse(f.readline())
visited = {}

def add(p1, p2, count):
    x1, y1 = p1
    x2, y2 = p2
    dir = 1 if x1 < x2 or y1 < y2 else -1
    for i in range(x1, x2, dir):
        visited[(i, y1)] = count
        count += 1
    for i in range(y1, y2, dir):
        visited[(x1, i)] = count
        count += 1
    return count

def get_crossings(p1, p2, count):
    x1, y1 = p1
    x2, y2 = p2
    crossings = []
    dir = 1 if x1 < x2 or y1 < y2 else -1
    for i in range(x1, x2, dir):
        if (i, y1) in visited:
            crossings.append(count + visited[(i, y1)])
        count += 1
    for i in range(y1, y2, dir):
        if (x1, i) in visited:
            crossings.append(count + visited[(x1, i)])
        count += 1
    return (crossings, count)

def move(p, m):
    x, y = p
    dir, num = m
    if   dir == 'U': y -= num
    elif dir == 'R': x += num
    elif dir == 'D': y += num
    elif dir == 'L': x -= num
    return (x, y)

pos = (0, 0)
count = 0
for w in w1:
    new_pos = move(pos, w)
    count = add(pos, new_pos, count)
    pos = new_pos

pos = (0, 0)
min_dist = maxsize
count = 0
for w in w2:
    new_pos = move(pos, w)
    dists, count = get_crossings(pos, new_pos, count)
    for dist in dists:
        if dist < min_dist and dist > 0: min_dist = dist
    pos = new_pos
print(min_dist)