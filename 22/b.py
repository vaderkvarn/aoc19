from parse import parse

def get_instructions(f):
    instructions = []
    for line in open(f):
        p = parse('deal with increment {:d}', line)
        if p:
            instructions.append((0, p.fixed[0]))
            continue
        p = parse('cut {:d}', line)
        if p:
            instructions.append((1, p.fixed[0]))
            continue
        p = parse('deal into new stack', line)
        instructions.append((2, 0))
    return instructions

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def get_f(instructions, num_cards):
    a = 1
    b = 0
    for ins in instructions[::-1]:
        type, n = ins
        if type == 0:
            z = egcd(n, num_cards)[1]%num_cards
            a = (a*z)%num_cards
            b = (b*z)%num_cards
        elif type == 1:
            b = (b+n)%num_cards
        elif type == 2:
            a = -a
            b = num_cards - b - 1 
    return a, b

def poly_mod(A, b, c):
    if b == 0: return 1, 0
    a1, a2 = A
    if b%2 == 1:
        b1, b2 = poly_mod(A, b - 1, c)
        return a1*b1%c, (a1*b2 + a2)%c
    return poly_mod((a1*a1%c, (a1*a2 + a2)%c), b//2, c) 

pos = 2020
N =        119315717514047
num =      101741582076661
instructions = get_instructions("input")

a, b = poly_mod(get_f(instructions, N), num, N)

print((pos*a + b)%N)