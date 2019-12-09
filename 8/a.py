input = open("input", "r").readline().rstrip()
width = 25
height = 6

min_num_zeros = 9999999
min_layer = []
for i in range(0, len(input), width*height):
    layer = input[i:i + width*height]
    num_zeros = len([x for x in layer if x == "0"])
    if num_zeros < min_num_zeros:
        min_num_zeros = num_zeros
        min_layer = layer

ones = len([x for x in min_layer if x == "1"])
twos = len([x for x in min_layer if x == "2"])
print(ones*twos)