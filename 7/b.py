from comp import Comp
import sys

from itertools import permutations; import sys;

p = [int(x) for x in open(sys.argv[1], "r").readline().split(',')]
 
max_thrust = 0
for perm in permutations(range(5, 10)):
    amp_data = []
    cur_amp_id = 0
    for i in range(len(perm)):
        amp_data.append([perm[i]])

    amp_data[4].append(0)
    amps = []
    def get_input(comp):
        return amp_data[(cur_amp_id-1)%5].pop(0)
    def on_output(comp, n):
        prev_amp_data = amp_data[(cur_amp_id-1)%5]
        if len(prev_amp_data) == 0:
            comp.pause()
        amp_data[cur_amp_id].append(n)
    def on_exit(comp):
        pass

    for d in perm:
        amps.append(Comp(p[:], get_input, on_output, on_exit))

    def all_done():
        for amp in amps:
            if not amp.done: return False
        return True

    while not all_done():
        amp = amps[cur_amp_id]
        if not amp.done:
            amps[cur_amp_id].run()
        cur_amp_id = (cur_amp_id + 1)%5

    if amp_data[-1][0] > max_thrust:
        max_thrust = amp_data[-1][0]
print(max_thrust)