input = open("test_input1", "r").readline().strip()

def repeat_input(st, n):

    input = ""
    for i in range(n):
        input += st
    s = [int(x) for x in input]
    return s

s = repeat_input(input, 2)
p0 = [0, 1, 0, -1]
num_phases = 2
for phase in range(num_phases):
    out = []
    for i in range(len(s)):
        p = []
        for a in p0:
            p.append([a]*(i+1))
        p = [a for l in p for a in l]
        tot = 0
        cur_p = (1 + i)%len(p)
        for j in range(i, len(s)):
            print(s[j]*p[cur_p], end='\t')

            tot += s[j]*p[cur_p]
            cur_p = (cur_p + 1)%len(p)
        #print()
        out.append(int(str(tot)[-1]))
    s = out
    #print()
print("".join(map(str, s))[:8])

