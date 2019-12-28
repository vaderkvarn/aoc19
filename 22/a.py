from parse import parse

num_cards = 10007

def deal_into_stack(cards):
    return cards[::-1]

def cut(n, cards):
    if n < 0:
        n += num_cards
    return cards[n:] + cards[:n]

def deal_with_increment(n, cards):
    new_deck = [0]*num_cards
    for i in range(num_cards):
        new_deck[(i*n)%num_cards] = cards[i]
    return new_deck

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
        if not p: 
            print("Bad input")
            exit(1)
        instructions.append((2, 0))
    return instructions

def run(cards, instructions):
    for ins in instructions:
        type, arg = ins
        if type == 0:
            cards = deal_with_increment(arg, cards)
        elif type == 1:
            cards = cut(arg, cards)
        elif type == 2:
            cards = deal_into_stack(cards)

    return cards

cards = list(range(num_cards))
cards = run(cards, get_instructions("input"))
for i in range(len(cards)):
    if cards[i] == 2019: print(i)

