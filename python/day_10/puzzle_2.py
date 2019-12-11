from pprint import pprint
from collections import defaultdict
import math

# read program from file
########################################
input_file = "input.txt"
base_x = 29
base_y = 28

# input_file = "test1.txt"        # best asteroid is (3,4), sees 8 asteroids
# input_file = "test2.txt"        # best asteroid is (5,8), sees 33 asteroids
# input_file = "test3.txt"        # best asteroid is (1,2), sees 35 asteroids
# input_file = "test4.txt"        # best asteroid is (6,3), sees 41 asteroids
# input_file = "test5.txt"        # best asteroid is (11,13), sees 210 asteroids
# base_x = 11
# base_y = 13

# input_file = "test6.txt"        # scan from base at (8, 3)
# base_x = 8
# base_y = 3

with open(input_file, "r") as ifh:
    map = [l.rstrip() for l in ifh.readlines()]

map = [[char for char in row] for row in map]
map[base_y][base_x] = "X"

for row in map:
    print("".join(row))

width = len(map[0])
height = len(map)

print("width:", width)
print("height:", height)


num_asteroids_to_blast = 0
for row in map:
    for elem in row:
        if elem == "#":
            num_asteroids_to_blast += 1
num_asteroids_to_blast -= 1

print("num asteroids to blast:", num_asteroids_to_blast)

# functions
########################################


def read_coordinate(x, y):
    global width, height

    if x < 0 or x > width - 1:
        return None
    elif y < 0 or y > height - 1:
        return None

    return map[y][x]


angles_asteroids_seen = []
visible_asteroid_count = 0


def check_location(x, y):
    global angles_asteroids_seen, visible_asteroid_count, base_x, base_y
    # print("checking coordinate ({}, {})".format(x, y))

    result = read_coordinate(x, y)
    if result is None:
        # print("off grid, continuing")
        pass
    elif result == "#":
        # print("found asteroid (#)!")

        offset_x = x - base_x
        offset_y = y - base_y

        # calc angle
        if offset_x == 0:
            # handle case where asteroid is directly up or down from base
            if offset_y < 0:
                angle = 999999
                category = 1
            else:
                angle = -999999
                category = 3
        else:
            angle = math.atan(offset_y / offset_x)
            if offset_x < 0:
                # angle = float("{0:.8f}".format(angle))
                category = 4
            else:
                # angle = float("{0:.8f}".format(angle))
                category = 2

        angles_asteroids_seen[category][angle].append([x, y])
        visible_asteroid_count += 1
        # map[y][x] = "W"

    elif result == ".":
        # print("found empty space (.)")
        pass

# iterate around selected asteroid


angles_asteroids_seen = {}
for i in range(4):
    angles_asteroids_seen[i+1] = defaultdict(list)
asteroids_blasted = []
asteroids_blasted_count = 0


# sweep around for asteroids
cur_x = base_x
cur_y = base_y
search_radius = 1

while search_radius < width or search_radius < height:

    # set inital search location for this radius
    cur_x += 1
    cur_y += 1

    # sweep left
    for i in range(2 * search_radius):
        cur_x -= 1
        check_location(cur_x, cur_y)
    # sweep up
    for i in range(2 * search_radius):
        cur_y -= 1
        check_location(cur_x, cur_y)
    # sweep right
    for i in range(2 * search_radius):
        cur_x += 1
        check_location(cur_x, cur_y)
    # sweep down
    for i in range(2 * search_radius):
        cur_y += 1
        check_location(cur_x, cur_y)

    search_radius += 1

# for category in sorted(angles_asteroids_seen.keys()):
#         # print("CATEGORY:", category)
#     for angle in sorted(angles_asteroids_seen[category].keys()):
#         print("category: {0}    angle: {1:09.2f}    asteroids: {2}".format(
#             category, angle, angles_asteroids_seen[category][angle]))

# print("visible_asteroid_count:", visible_asteroid_count)
# for row in map:
#     print("".join(row))
# quit()


while asteroids_blasted_count < num_asteroids_to_blast:

    # print("blasted {}/{}".format(asteroids_blasted_count, num_asteroids_to_blast))

    # blast 'em
    # pprint(angles_asteroids_seen)
    for category in sorted(angles_asteroids_seen.keys()):
        # print("CATEGORY:", category)
        for angle in sorted(angles_asteroids_seen[category].keys()):
            # print("category: {0}    angle: {1:09.2f}    asteroids: {2}".format(category, angle, angles_asteroids_seen[category][angle]))

            if len(angles_asteroids_seen[category][angle]) > 0:
                ast = angles_asteroids_seen[category][angle].pop(0)
                asteroids_blasted.append(ast)
                map[ast[1]][ast[0]] = "."
                asteroids_blasted_count += 1

                if len(angles_asteroids_seen[category][angle]) == 0:
                    del angles_asteroids_seen[category][angle]

    # quit()

    # print("=--------------------------------------------------=")


# for row in map:
#     print("".join(row))
# quit()

# print results
########################################

print()
# for a_idx, a in enumerate(asteroids_blasted):
#     print("{0:4d}: {1}".format(a_idx, a))

#     # # out_map = [["." for j in range(width)] for i in range(height)]
#     # out_map = map.copy()
#     # out_map[base_y][base_x] = "X"
#     # out_map[a[1]][a[0]] = "o"

#     # for row in out_map:
#     #     print("".join(row))

#     # input()

print("The 1st asteroid to be vaporized is at {},{}".format(asteroids_blasted[1-1][0], asteroids_blasted[1-1][1]))
print("The 2nd asteroid to be vaporized is at {},{}".format(asteroids_blasted[2-1][0], asteroids_blasted[2-1][1]))
print("The 3rd asteroid to be vaporized is at {},{}".format(asteroids_blasted[3-1][0], asteroids_blasted[3-1][1]))
print("The 10th asteroid to be vaporized is at {},{}".format(asteroids_blasted[10-1][0], asteroids_blasted[10-1][1]))
print("The 20th asteroid to be vaporized is at {},{}".format(asteroids_blasted[20-1][0], asteroids_blasted[20-1][1]))
print("The 50th asteroid to be vaporized is at {},{}".format(asteroids_blasted[50-1][0], asteroids_blasted[50-1][1]))
print("The 100th asteroid to be vaporized is at {},{}".format(asteroids_blasted[100-1][0], asteroids_blasted[100-1][1]))
print("The 199th asteroid to be vaporized is at {},{}".format(asteroids_blasted[199-1][0], asteroids_blasted[199-1][1]))
print()
print("The 200th asteroid to be vaporized is at {},{}".format(asteroids_blasted[200-1][0], asteroids_blasted[200-1][1]))
print("calculated value: {}".format(asteroids_blasted[200-1][0] * 100 + asteroids_blasted[200-1][1]))
print()
print("The 201st asteroid to be vaporized is at {},{}".format(asteroids_blasted[201-1][0], asteroids_blasted[201-1][1]))
print("The 299th and final asteroid to be vaporized is at {},{}".format(asteroids_blasted[299-1][0], asteroids_blasted[299-1][1]))
