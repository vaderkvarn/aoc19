p0 = [int(x) for x in open("input", "r").readline().split(',')]
for j in range(100):
    for k in range(100):
        p = p0[:]
        p[1] = j
        p[2] = k
        i = 0
        while p[i] != 99:
            if p[i] == 1:
                p[p[i+3]] = p[p[i+1]] + p[p[i+2]]
            elif p[i] == 2:
                p[p[i+3]] = p[p[i+1]] * p[p[i+2]]
            i += 4
        if p[0] == 19690720:
            print(100*j+k)
