from comp import Comp
import sys

from itertools import permutations; import sys;

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]
 
max_thrust = 0
for perm in permutations(range(5)):
    def get_input(comp):
        return s.pop()
    def on_output(comp, n):
        s.append(n)
    def on_exit(comp):
        pass

    s = [0]
    for d in perm:
        c = Comp(p[:], get_input, on_output, on_exit)
        s.append(d)
        c.run()

    if s[0] > max_thrust:
        max_thrust = s[0]
print(max_thrust)