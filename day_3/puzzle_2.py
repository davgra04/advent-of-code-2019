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
cost = 0

for edge in line1:

    direction = edge[0]
    distance = int(edge[1:])

    # print("Travelling {} units {}".format(distance, direction))

    for i in range(distance):

        cost += 1

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
        if grid_data[position_string] == 0:
            grid_data[position_string] = cost

### process line2
########################################

intersection_costs = []

cur_x = 0
cur_y = 0
cost = 0

for edge in line2:

    direction = edge[0]
    distance = int(edge[1:])

    # print("Travelling {} units {}".format(distance, direction))

    for i in range(distance):

        cost += 1

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
        if grid_data[position_string] > 0:
            intersection_costs.append(grid_data[position_string] + cost)

# pprint(grid_data)


### determine closest intersection
########################################

min_cost = min(intersection_costs)

print("costs:", intersection_costs)
print("min_cost:", min_cost)

