from pprint import pprint

# read program from file
########################################
input_file = "input.txt"
# input_file = "test1.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

data = lines[0].rstrip()
[width, height] = [25, 6]

# data = "123456789012" # test data
# [width, height] = [3, 2]

num_pixels = width * height

# pprint(data)

# separate into layers
########################################

layers = []
remaining = data

while remaining != "":
    layers.append(remaining[:num_pixels])
    remaining = remaining[num_pixels:]


pprint(layers)

# determine layer with fewest 0's
########################################

min_zero_layer = None
min_num_zeroes = 999999999999999

for l_idx, l in enumerate(layers):
    num_zeroes = 0
    for digit in l:
        if digit == "0":
            num_zeroes += 1

    if num_zeroes < min_num_zeroes:
        min_num_zeroes = num_zeroes
        min_zero_layer = l_idx

print("min_zero_layer:", min_zero_layer)
print("min_num_zeroes:", min_num_zeroes)

# evaluate requested value on layer with fewest 0's
########################################

num_ones = 0
num_twos = 0

for digit in layers[min_zero_layer]:
    if digit == "1":
        num_ones += 1
    elif digit == "2":
        num_twos += 1

calculation = num_ones * num_twos

print("num_ones:", num_ones)
print("num_twos:", num_twos)
print("calculation:", calculation)