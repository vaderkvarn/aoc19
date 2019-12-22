from heapq import *

def get_map(filename):
    m = []
    f = open(filename, "r")
    for line in f:
        m.append(list(line.strip()))
    return m

def is_key(v):
    return ord(v) in range(ord('a'), ord('z') + 1)

def is_door(v):
    return ord(v) in range(ord('A'), ord('Z') + 1)

def get_ms(m):
    sps = []
    ms = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            p = (j, i)
            v = m[i][j]
            if v == '@':
                sps.append(p)
    ms.append([row[:sps[0][0] + 1] for row in m[:sps[0][1] + 1]]) 
    ms.append([row[sps[1][0]:] for row in m[:sps[1][1] + 1]]) 
    ms.append([row[:sps[2][0] + 1] for row in m[sps[2][1]:]]) 
    ms.append([row[sps[3][0]:] for row in m[sps[3][1]:]]) 
    return ms

def init(m):
    sp = ()
    keys = []
    doors = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            p = (j, i)
            v = m[i][j]
            if v == '@':
                 sp = p
            elif is_key(v):
                keys.append(v)
            elif is_door(v):
                doors.append(v)
            
    return (sp, set(keys), set(doors))

def has_key_for_door(keys, door):
    return door.lower() in keys

def get_neighs(m, p):
    w, h = (len(m[0]) - 1, len(m) - 1)
    x, y = p
    n = []
    if x > 0: n.append((x-1, y))
    if y > 0: n.append((x, y-1))
    if x < w: n.append((x+1, y))
    if y < h: n.append((x, y+1))
    return n

def run(m):
    sp, all_keys, all_doors = init(m)
    h = []
    keys = set([])
    visited = set([(sp, frozenset(keys))])
    heappush(h, (0, sp, keys))
    while len(h) > 0:
        dist, p, keys = heappop(h)
        if len(keys) == len(all_keys):
            return dist
        for n in get_neighs(m, p):
            x, y = n
            v = m[y][x]
            if v == '#': continue
            new_keys = keys.copy()
            if v in all_keys:
                if not v in keys:
                    new_keys.add(v)
            if v.lower() in all_keys:
                if not has_key_for_door(new_keys, v): continue
            if (n, frozenset(new_keys)) in visited: continue
            visited.add((n, frozenset(new_keys)))
            heappush(h, (dist + 1,  n, new_keys)) 

m = get_map("input")
print(run(m))

ms = get_ms(get_map("input2"))
tot = 0
for m in ms:
    tot += run(m)
print(tot)