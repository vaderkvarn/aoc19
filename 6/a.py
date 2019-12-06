from collections import defaultdict
from functools import reduce
nodes = defaultdict(list)

f = open("input", "r")
for line in f:
    parts = line.rstrip().split(")")
    nodes[parts[0]].append(parts[1])

def run(node, dist):
    children = nodes[node]
    sum = dist
    for c in children:
        sum += run(c, dist + 1)
    return sum

print(run("COM", 0))

