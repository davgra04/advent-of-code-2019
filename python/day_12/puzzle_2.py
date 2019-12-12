from pprint import pprint
from itertools import combinations
import math

# read program from file
########################################
input_file = "input.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

pprint(lines)

# helper functions
########################################

class moon:
    def __init__(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    



moons = [
    moon(1, 4, 4),
    moon(-4, -1, 19),
    moon(-15, -14, 12),
    moon(-17, 1, 10),
]


# moons = [
#     moon(-1, 0, 2),
#     moon(2, -10, -7),
#     moon(4, -8, 8),
#     moon(3, 5, -1),
# ]


states = {}

def check_state():
    global states, moons

    state = ""
    for m in moons:
        state += "{}{}{}{}{}{}".format(m.pos_x, m.pos_y, m.pos_z, m.vel_x, m.vel_y, m.vel_z)

    if state in states:
        return True
    else:

        states[state] = 1
        return False




pairs = list(combinations([i for i in range(len(moons))], 2))

pprint(list(pairs))
# quit()

steps = 0


# for step in range(1000):
while True:


    if steps % 10000 == 0:
        print("step:", steps)

    # if step == 5:
    #     quit()

    # apply gravity
    for pair in pairs:
        idx1 = pair[0]
        idx2 = pair[1]

        # print("comparing {} and {}".format(idx1, idx2))


        # handle x axis
        if moons[idx1].pos_x < moons[idx2].pos_x:
            moons[idx1].vel_x += 1
            moons[idx2].vel_x -= 1
        elif moons[idx1].pos_x > moons[idx2].pos_x:
            moons[idx1].vel_x -= 1
            moons[idx2].vel_x += 1

        # handle y axis
        if moons[idx1].pos_y < moons[idx2].pos_y:
            moons[idx1].vel_y += 1
            moons[idx2].vel_y -= 1
        elif moons[idx1].pos_y > moons[idx2].pos_y:
            moons[idx1].vel_y -= 1
            moons[idx2].vel_y += 1

        # handle z axis
        if moons[idx1].pos_z < moons[idx2].pos_z:
            moons[idx1].vel_z += 1
            moons[idx2].vel_z -= 1
        elif moons[idx1].pos_z > moons[idx2].pos_z:
            moons[idx1].vel_z -= 1
            moons[idx2].vel_z += 1

    # apply velocity
    for moon in moons:
        moon.pos_x += moon.vel_x
        moon.pos_y += moon.vel_y
        moon.pos_z += moon.vel_z


    steps += 1

    if check_state():
        break


    # print("After {} steps:".format(step+1))
    # for moon in moons:
    #     print("pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(moon.pos_x, moon.pos_y, moon.pos_z, moon.vel_x, moon.vel_y, moon.vel_z))
    # print()




print("steps:", steps)


