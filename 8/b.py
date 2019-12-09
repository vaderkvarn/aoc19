input = open("input", "r").readline().rstrip()
width = 25
height = 6

def merge_layers(layers):
    res = []
    for i in range(width*height):
        j = 0
        while layers[j][i] == "2":
            j += 1
        res.append(layers[j][i])
    return res

def print_image(layer):
    print('P2', width, height, 1)
    for i in range(height):
        print(" ".join(layer[i*width:i*width + width]))
            
def get_layers():
    layers = []
    for i in range(0, len(input), width*height):
        layers.append(input[i:i + width*height])
    return layers

print_image(merge_layers(get_layers()))
