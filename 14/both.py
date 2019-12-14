from parse import parse
from collections import defaultdict
from math import ceil, floor
f = open("input", "r")
reactions = []

for line in f:
    parts = line.split(' => ')
    inputs = [parse("{:d} {}", i).fixed for i in parts[0].split(', ')]
    output = parse("{:d} {}", parts[1]).fixed 
    reactions.append((inputs, output))

def get_needed_output(o, n):
    if n <= 0: return (0, abs(n))
    needed_ouput = 1 if o >= n else ceil(n/o)
    leftover_output = o - n if o >= n else needed_ouput*o - n
    return (needed_ouput, leftover_output)

def react(reaction, reactions, needed, left_overs):
    inputs, output = reaction
    o_amount, o_chemical = output
    needed_output, leftover_ouput = get_needed_output(o_amount, needed - left_overs[o_chemical])
    left_overs[o_chemical] = leftover_ouput
    if inputs[0][1] == "ORE": 
        amount, chemical = inputs[0]
        return amount*needed_output
    
    ores = 0
    for input in inputs:
        amount, chemical = input
        for r in reactions:
            if r[1][1] == chemical:
                ores += react(r, reactions, amount*needed_output, left_overs)
    return ores

reaction = ()
for r in reactions:
    if r[1][1] == "FUEL":
        reaction = r

left_overs = defaultdict(int)
print(react(reaction, reactions, 1, left_overs))

big_number = 1000000000000
min_i = 0
max_i = big_number
i = (max_i/2)
num_ores = 0
while min_i < max_i:
    left_overs = defaultdict(int)
    num_ores = react(reaction, reactions, int(i), left_overs)
    if num_ores > big_number: 
        max_i = i
    else:
        min_i = i + 1
    i = (min_i + max_i)/2
print(int(i))