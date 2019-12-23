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
    return portals

def get_neighs(m, p, portals):
    x, y = p
    w = len(m[0])
    h = len(m)
    n = []
    if p in portals:
        ls = portals[p]
        for p2 in portals:
            if p == p2: continue
            if portals[p2] == ls:
                n.append(p2)
    if x - 1 >= 0 and m[y][x - 1] == '.': n.append((x - 1, y))
    if x + 1 <  w and m[y][x + 1] == '.': n.append((x + 1, y))
    if y - 1 >= 0 and m[y - 1][x] == '.': n.append((x, y - 1))
    if y + 1 <  h and m[y + 1][x] == '.': n.append((x, y + 1))
    return n

def run(m):
    portals = init(m)
    start_pos = [p for p in portals if portals[p] == ('A', 'A')][0]
    end_pos = [p for p in portals if portals[p] == ('Z', 'Z')][0]
    q = deque([(0, start_pos)])
    visited = set([start_pos])
    while len(q) > 0:
        dist, p = q.popleft()
        if p == end_pos:
            print(dist)
            return
        for n in get_neighs(m, p, portals):
            if not n in visited:
                visited.add(n)
                q.append((dist + 1, n))
run(m)