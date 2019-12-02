f = open("input", "r")

def calc(n):
    return n//3 - 2

tot = 0
for l in f:
    tot += calc(int(l))

print(tot)
