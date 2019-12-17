st = open("test_input1", "r").readline().strip()
for r in range(1, 10):
    input = ""
    for i in range(r):
        input += st
    s = [int(x) for x in input]
    p0 = [0, 1, 0, -1]
    num_phases = 100
    for phase in range(num_phases):
        out = []
        for i in range(len(s)):
            p = []
            for a in p0:
                p.append([a]*(i+1))
            p = [a for l in p for a in l]
            tot = 0
            cur_p = 1
            for j in range(len(s)):
                tot += s[j]*p[cur_p]
                cur_p = (cur_p + 1)%len(p)
            out.append(int(str(tot)[-1]))
        s = out[:]
    print("".join(map(str, s))[:8])

