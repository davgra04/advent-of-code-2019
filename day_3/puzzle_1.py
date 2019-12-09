from pprint import pprint, pformat
from collections import defaultdict

grid_data = defaultdict(int)

### load line data
########################################
input_file = "input.txt"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"
with open(input_file, "r") as ifh:
    lines = ifh.readlines()

line1 = lines[0].rstrip().split(",")
line2 = lines[1].rstrip().split(",")

# print("line 1:", line1)
# print("line 2:", line2)

### process line1
########################################

cur_x = 0
cur_y = 0
for edge in line1:

    direction = edge[0]
    distance = int(edge[1:])

    # print("Travelling {} units {}".format(distance, direction))

    for i in range(distance):
        if direction == "R":
            cur_x += 1
        elif direction == "L":
            cur_x -= 1
        elif direction == "U":
            cur_y += 1
        elif direction == "D":
            cur_y -= 1
        else:
            print("ERROR")
            quit()

        position_string = "{},{}".format(cur_x, cur_y)
        grid_data[position_string] = "a"

### process line2
########################################

cur_x = 0
cur_y = 0
for edge in line2:

    direction = edge[0]
    distance = int(edge[1:])

    # print("Travelling {} units {}".format(distance, direction))

    for i in range(distance):
        if direction == "R":
            cur_x += 1
        elif direction == "L":
            cur_x -= 1
        elif direction == "U":
            cur_y += 1
        elif direction == "D":
            cur_y -= 1
        else:
            print("ERROR")
            quit()

        position_string = "{},{}".format(cur_x, cur_y)
        if grid_data[position_string] == "a":
            grid_data[position_string] = "X"
        else:
            grid_data[position_string] = "b"

# pprint(grid_data)

### determine closest intersection
########################################

distance = 99999999999
final_x = 0
final_y = 0

for position in grid_data.keys():

    if grid_data[position] == "X":
        print("inspecting", position)

        [x, y] = position.split(",")

        x = int(x)
        y = int(y)

        dist_x = x
        dist_y = y

        if dist_x < 0:
            dist_x = -dist_x
        if dist_y < 0:
            dist_y = -dist_y

        cur_dist = dist_x + dist_y

        if cur_dist < distance:
            distance = cur_dist
            final_x = x
            final_y = y

        # print("inspecting ({}, {})".format(x, y))
        print("distance: {}".format(x + y))
    # print(position)

print("=-=-=-=-=-=-=-=-=-=")
print("distance:", distance)
print("final_x:", final_x)
print("final_y:", final_y)



