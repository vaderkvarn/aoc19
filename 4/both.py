
min_n = 245318
max_n = 765747

def c1(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False

def c2(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return False
    return True

def c3(s):
    for i in range(2, len(s) + 1):
        c = s[i-1]
        if s[i-2] == c and (i == 2 or s[i-3] != c) and (i == len(s) or s[i] != c):
            return True
    return False

num_p1 = 0
num_p2 = 0
for i in range(min_n, max_n):
    s = str(i)
    if c1(s) and c2(s):
        num_p1 += 1
    if c3(s) and c2(s):
        num_p2 += 1

print(num_p1)
print(num_p2)