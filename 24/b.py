f = open("input", "r")
tiles = []
for line in f:
    tiles.append(list(line.strip()))

num_minutes = 200

def is_empty(level):
    return level == [['.' for j in range(5)] for i in range(5)]
def next_levels(levels, minutes):
    if not is_empty(levels[1]):
        levels.insert(0, [['.' for j in range(5)] for i in range(5)])
    if not is_empty(levels[-2]):
        levels.append([['.' for j in range(5)] for i in range(5)])
    new_levels = []
    for i in range(len(levels)):
        if i == 0 or i == len(levels) - 1:
            new_levels.append([['.' for j in range(5)] for i in range(5)])
            continue
        tiles = levels[i]
        new_tiles = [r[:] for r in tiles]
        inner_tiles = levels[i+1]
        outer_tiles = levels[i-1]
        for i in range(5):
            for j in range(5):
                num_bugs = 0
                if i == 2 and j == 2: continue
                if i > 0 and tiles[i-1][j] == '#': num_bugs += 1 
                if j > 0 and tiles[i][j-1] == '#': num_bugs += 1 
                if i < 4 and tiles[i+1][j] == '#': num_bugs += 1 
                if j < 4 and tiles[i][j+1] == '#': num_bugs += 1 
                if i == 0 and outer_tiles[1][2] == '#': num_bugs += 1
                if j == 0 and outer_tiles[2][1] == '#': num_bugs += 1
                if i == 4 and outer_tiles[3][2] == '#': num_bugs += 1
                if j == 4 and outer_tiles[2][3] == '#': num_bugs += 1
                if (i, j) == (1, 2): num_bugs += sum([1 for t in inner_tiles[0] if t == '#'])
                if (i, j) == (2, 1): num_bugs += sum([1 for row in inner_tiles if row[0] == '#'])
                if (i, j) == (3, 2): num_bugs += sum([1 for t in inner_tiles[4] if t == '#'])
                if (i, j) == (2, 3): num_bugs += sum([1 for row in inner_tiles if row[4] == '#'])

                if num_bugs == 1: new_tiles[i][j] = '#'
                elif num_bugs == 2 and tiles[i][j] == '.': new_tiles[i][j] = '#'
                else: new_tiles[i][j] = '.'

        new_levels.append(new_tiles) 
    return new_levels

def run(levels):
    for i in range(num_minutes):
        levels = next_levels(levels, i)
    tot = 0
    for l in levels:
        for row in l:
            for tile in row:
                if tile == '#':
                    tot += 1
    
    print(tot)

levels = [tiles]
levels.insert(0, [['.' for j in range(5)] for i in range(5)])
levels.append([['.' for j in range(5)] for i in range(5)])
run(levels)
