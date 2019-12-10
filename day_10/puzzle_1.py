from pprint import pprint
import math

# read program from file
########################################
input_file = "input.txt"
# input_file = "test1.txt"        # best asteroid is (3,4), sees 8 asteroids
# input_file = "test2.txt"        # best asteroid is (5,8), sees 33 asteroids
# input_file = "test3.txt"        # best asteroid is (1,2), sees 35 asteroids
# input_file = "test4.txt"        # best asteroid is (6,3), sees 41 asteroids
# input_file = "test5.txt"        # best asteroid is (11,13), sees 210 asteroids
with open(input_file, "r") as ifh:
    map = [l.rstrip() for l in ifh.readlines()]

pprint(map)
width = len(map[0])
height = len(map)

print("width:", width)
print("height:", height)

final_out_map = [["." for j in range(width)] for i in range(height)]



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
base_x = 0
base_y = 0

def check_location(x, y):
    global angles_asteroids_seen, visible_asteroid_count, base_x, base_y, out_map
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
                angle_str = "up"
            else:
                angle_str = "down"
        else:
            angle = math.tan(offset_y / offset_x)
            if offset_x < 0:
                angle_str = "neg_{0:5.8f}".format(angle)
            else:
                angle_str = "pos_{0:5.8f}".format(angle)

        # print("    angle:", angle_str)
        if angle_str in angles_asteroids_seen:
            # print("    angle seen before: yes")
            out_map[y][x] = "o"
            pass
        else:
            # print("    angle seen before: no")
            angles_asteroids_seen.append(angle_str)
            visible_asteroid_count += 1
            out_map[y][x] = "#"

        # have we seen an asteroid at this angle before?

    elif result == ".":
        # print("found empty space (.)")
        out_map[y][x] = "."
        pass

# iterate around selected asteroid

# cur_x = 0
# cur_y = 0
# search_radius = 1

most_seen = -1
most_seen_x = -1
most_seen_y = -1

for x in range(width):

    for y in range(height):

        # print("testing ({}, {})".format(x, y))

        if read_coordinate(x, y) == "#":

            angles_asteroids_seen = []
            visible_asteroid_count = 0
            base_x = x
            base_y = y
            cur_x = x
            cur_y = y
            search_radius = 1

            out_map = [["." for j in range(width)] for i in range(height)]
            out_map[y][x] = "X"

            while search_radius < width and search_radius < height:

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

            if visible_asteroid_count > most_seen:
                most_seen = visible_asteroid_count
                most_seen_x = base_x
                most_seen_y = base_y
                final_out_map = out_map.copy()

print()
print("FINAL OUT MAP:")
# pprint(final_out_map)
for row in final_out_map:
    print("".join(row))

print()
print("best asteroid is ({}, {}), sees {} asteroids".format(most_seen_x, most_seen_y, most_seen))