f = open("input", "r")

def calc(n):
    tot = 0
    while True:
        n = n//3 - 2
        if n <= 0:
            return tot
        tot += n

tot = 0
for l in f:
    tot += calc(int(l))

print(tot)
