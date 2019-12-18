input = open("input", "r").readline().strip()

def repeat_input(input, n):
    s = ""
    for i in range(n):
        s += input
    return s

index = int(input[:7])

data = repeat_input(input, 10000)[index:]

s = [int(x) for x in data]
num_phases = 100
for phase in range(num_phases):
    for i in range(len(s) - 2, -1, -1):
        s[i] = (s[i] + s[i + 1]) % 10
res = "".join(map(str, s))
print(res[:8])
