from collections import defaultdict
from collections import deque

nodes = defaultdict(list)

f = open("input", "r")
for line in f:
    parts = line.rstrip().split(")")
    nodes[parts[0]].append(parts[1])
    nodes[parts[1]].append(parts[0])

def run(start, end):
    visited = set([start])
    q = deque([(0, start)])
    while len(q) > 0:
        dist, node = q.popleft()
        if node == end:
            return dist - 2
        for c in nodes[node]:
            if not c in visited:
                visited.add(c)
                q.append((dist + 1, c))

print(run("YOU", "SAN"))

