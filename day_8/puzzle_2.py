from pprint import pprint

# read program from file
########################################
input_file = "input.txt"
# input_file = "test1.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

data = lines[0].rstrip()
[width, height] = [25, 6]

# data = "0222112222120000" # test data 2
# [width, height] = [2, 2]

num_pixels = width * height

# pprint(data)

# separate into layers
########################################

layers = []
remaining = data

while remaining != "":
    layers.append(remaining[:num_pixels])
    remaining = remaining[num_pixels:]


# pprint(layers)

# composite image
########################################

reversed_layers = layers.copy()
reversed_layers.reverse()

# pprint(reversed_layers)

image = [char for char in reversed_layers[0]]
# pprint(image)

for l in reversed_layers[1:]:

    # print("image:", image)
    
    for p_idx, pixel in enumerate(l):

        # print("p_idx:", p_idx)
        # print("pixel:", pixel)

        if pixel == "0" or pixel == "1":
            image[p_idx] = pixel

image = "".join(image)

# draw image
########################################

rendered_image = ""

for p_idx, pixel in enumerate(image):

    if pixel == "0":
        rendered_image += "#"
    elif pixel == "1":
        rendered_image += "_"
    elif pixel == "2":
        rendered_image += " "


    if p_idx % width == width - 1:
        rendered_image += "\n"

print("OUTPUT:")
print(rendered_image)