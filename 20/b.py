from collections import deque, defaultdict

f = open("input", "r")
m = []
for line in f:
    m.append(list(line.replace("\n", "")))

def is_capital_letter(v):
    return ord(v) in range(ord('A'), ord('Z') + 1)

def is_letters(m, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    v1 = m[y1][x1]
    v2 = m[y2][x2]
    w = len(m[0])
    h = len(m)
    return x2 >= 0 and x2 < w and y2 >= 0 and y2 < h and is_capital_letter(v1) and is_capital_letter(v2)  

def init(m):
    portals = {}
    for i in range(1, len(m) - 1):
        for j in range(1, len(m[0]) - 1):
            v = m[i][j]
            if v == '.':
                if is_letters(m, (j, i + 1), (j, i + 2)): portals[(j, i)] = (m[i + 1][j], m[i + 2][j])
                if is_letters(m, (j, i - 1), (j, i - 2)): portals[(j, i)] = (m[i - 2][j], m[i - 1][j])
                if is_letters(m, (j + 1, i), (j + 2, i)): portals[(j, i)] = (m[i][j + 1], m[i][j + 2])
                if is_letters(m, (j - 1, i), (j - 2, i)): portals[(j, i)] = (m[i][j - 2], m[i][j - 1])
    inner = {}
    outer = {}
    def closest(p1, p2):
        x1, y1 = p1; x2, y2 = p2
        if x1 == 2 or x1 == len(m[0]) - 3 or y1 == 2 or y1 == len(m) - 3:
            return (p2, p1)
        return (p1, p2)
    for p1 in portals:
        ls = portals[p1]
        if ls in [('A', 'A'), ('Z', 'Z')]: 
            outer[p1] = ls 
            continue
        for p2 in portals:
            if p1 == p2: continue
            if ls == portals[p2]:
                i, o = closest(p1, p2)
                inner[i] = ls
                outer[o] = ls
    return (inner, outer)

def get_neighs(m, p, portals, level):
    inner, outer = portals
    x, y = p
    w = len(m[0])
    h = len(m)
    n = []
    if p in outer:
        if level > 0:
            ls = outer[p]
            for p2 in inner:
                if inner[p2] == ls:
                    n.append((p2, level - 1))
    if p in inner:
        ls = inner[p]
        for p2 in outer:
            if outer[p2] == ls:
                n.append((p2, level + 1))

    if x - 1 >= 0 and m[y][x - 1] == '.': n.append(((x - 1, y), level))
    if x + 1 <  w and m[y][x + 1] == '.': n.append(((x + 1, y), level))
    if y - 1 >= 0 and m[y - 1][x] == '.': n.append(((x, y - 1), level))
    if y + 1 <  h and m[y + 1][x] == '.': n.append(((x, y + 1), level))
    return n

def run(m):
    inner, outer = init(m)
    start_pos = [p for p in outer if outer[p] == ('A', 'A')][0]
    end_pos = [p for p in outer if outer[p] == ('Z', 'Z')][0]
    q = deque([(0, start_pos, 0)])
    visited = set([(start_pos, 0)])
    while len(q) > 0:
        dist, p, level = q.popleft()
        if p == end_pos and level == 0:
            print(dist)
            return
        for n, level in get_neighs(m, p, (inner, outer), level):
            if not (n, level) in visited:
                visited.add((n, level))
                q.append((dist + 1, n, level))
run(m)