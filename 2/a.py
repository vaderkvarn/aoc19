p = [int(x) for x in open("input", "r").readline().split(',')]
p[1] = 12
p[2] = 2

i = 0
while p[i] != 99:
    if p[i] == 1:
        p[p[i+3]] = p[p[i+1]] + p[p[i+2]]
    elif p[i] == 2:
        p[p[i+3]] = p[p[i+1]] * p[p[i+2]]
    i += 4

print(p[0])
