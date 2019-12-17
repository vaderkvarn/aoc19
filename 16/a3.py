input = open("input", "r").readline().strip()

def repeat_input(st, n):

    input = ""
    for i in range(n):
        input += st
    s = [int(x) for x in input]
    return s


index = int(input[:7])
rev_index = len(input)*10000 - index - 8
print("rev", rev_index)
print("index", index)
num_repeat = index//(len(input) - 1)
print("num_repeat", num_repeat)
s = repeat_input(input, num_repeat)
print(len(s))
print(s[index:index+8])
exit()
ss = []
for r in range(100):
    s = repeat_input(input, r)
    print(len(s))
    p0 = [0, 1, 0, -1]
    num_phases = 10
    for phase in range(num_phases):
        out = []
        for i in range(len(s)):
            j = 0
            tot = 0
            nums = []
            while (j+1)*i + j < len(s):
                start = (j+1)*i + j
                end = (j+2)*i + j + 1
                if j%4 == 0:
                    #nums += s[start:end]
                    tot += sum(s[start:end])
                else:
                    tot -= sum(s[start:end])
                    #nums += map(lambda x: -1*x, s[start:end])
                j += 2
            #print(sum(pos) - sum(neg))
            #print(nums)
            #print(tot, end= '\t')
            out.append(int(str(tot)[-1]))
        s = out
        #print("s", s)
        #print(len(s))
        #print()
    #print("".join(map(str, s)))
    ss.append("".join(map(str, s)))
for i in range(1, len(ss)):
    s1 = ss[i-1][::-1]
    s2 = ss[i][::-1]
    num_equal = 0
    j = 0
    str = ""
    while j < len(s1) and s1[j] == s2[j]:
        str += s1[j]
        j += 1
    num_unique = len(s2) - j
    print((i, i - 1), j, str)