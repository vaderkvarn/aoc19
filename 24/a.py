f = open("input", "r")
tiles = []
for line in f:
    tiles.append(list(line.strip()))

def next_tiles(tiles):
    new_tiles = [r[:] for r in tiles]
    for i in range(5):
        for j in range(5):
            num_bugs = 0
            if i > 0 and tiles[i-1][j] == '#': num_bugs += 1 
            if j > 0 and tiles[i][j-1] == '#': num_bugs += 1 
            if i < 4 and tiles[i+1][j] == '#': num_bugs += 1 
            if j < 4 and tiles[i][j+1] == '#': num_bugs += 1 
            if num_bugs == 1: new_tiles[i][j] = '#'
            elif num_bugs == 2 and tiles[i][j] == '.': new_tiles[i][j] = '#'
            else: new_tiles[i][j] = '.'
    return new_tiles

def hash(tiles):
    val = ""
    for i in range(5):
        for j in range(5):
            val += tiles[i][j]
    return val

def run(tiles):
    seen = set([hash(tiles)])
    while True:
        tiles = next_tiles(tiles)
        if hash(tiles) in seen:
            break
        seen.add(hash(tiles))
    tot = 0
    h = hash(tiles)
    for i in range(25):
        if h[i] == '#':
            tot += 2**i
    print(tot)

run(tiles)