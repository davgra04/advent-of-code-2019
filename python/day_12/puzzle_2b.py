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


states_x = {}
states_y = {}
states_z = {}

period_x = 0
period_y = 0
period_z = 0

period_x_found = False
period_y_found = False
period_z_found = False

steps = 0

def check_state():
    global moons, steps, period_x, period_y, period_z, period_x_found, period_y_found, period_z_found, states_x, states_y, states_z


    state_x = ""
    state_y = ""
    state_z = ""
    for m in moons:
        state_x += "{},{},".format(m.pos_x, m.vel_x)
        state_y += "{},{},".format(m.pos_y, m.vel_y)
        state_z += "{},{},".format(m.pos_z, m.vel_z)

    if not period_x_found:
        if state_x in states_x:
            period_x_found = True
            period_x = steps - states_x[state_x]
            print("FOUND PERIOD X: state1: {} [{} steps] state2: {} [{} steps]".format(state_x, states_x[state_x], state_x, steps))
        else:
            states_x[state_x] = steps

    if not period_y_found:
        if state_y in states_y:
            period_y_found = True
            period_y = steps - states_y[state_y]
            print("FOUND PERIOD Y: state1: {} [{} steps] state2: {} [{} steps]".format(state_y, states_y[state_y], state_y, steps))
        else:
            states_y[state_y] = steps

    if not period_z_found:
        if state_z in states_z:
            period_z_found = True
            period_z = steps - states_z[state_z]
            print("FOUND PERIOD Z: state1: {} [{} steps] state2: {} [{} steps]".format(state_z, states_z[state_z], state_z, steps))
        else:
            states_z[state_z] = steps

    if period_x_found and period_y_found and period_z_found:
        return True




pairs = list(combinations([i for i in range(len(moons))], 2))

pprint(list(pairs))
# quit()



# for step in range(1000):
while True:

    # if step == 5:
    #     quit()

    # apply gravity
    for pair in pairs:
        idx1 = pair[0]
        idx2 = pair[1]

        # print("comparing {} and {}".format(idx1, idx2))


        # handle x axis
        if not period_x_found:
            if moons[idx1].pos_x < moons[idx2].pos_x:
                moons[idx1].vel_x += 1
                moons[idx2].vel_x -= 1
            elif moons[idx1].pos_x > moons[idx2].pos_x:
                moons[idx1].vel_x -= 1
                moons[idx2].vel_x += 1

        # handle y axis
        if not period_y_found:
            if moons[idx1].pos_y < moons[idx2].pos_y:
                moons[idx1].vel_y += 1
                moons[idx2].vel_y -= 1
            elif moons[idx1].pos_y > moons[idx2].pos_y:
                moons[idx1].vel_y -= 1
                moons[idx2].vel_y += 1

        # handle z axis
        if not period_z_found:
            if moons[idx1].pos_z < moons[idx2].pos_z:
                moons[idx1].vel_z += 1
                moons[idx2].vel_z -= 1
            elif moons[idx1].pos_z > moons[idx2].pos_z:
                moons[idx1].vel_z -= 1
                moons[idx2].vel_z += 1

    # apply velocity
    for moon in moons:
        if not period_x_found:
            moon.pos_x += moon.vel_x
        if not period_y_found:
            moon.pos_y += moon.vel_y
        if not period_z_found:
            moon.pos_z += moon.vel_z


    steps += 1

    if check_state():
        break


    # print("After {} steps:".format(step+1))
    # for moon in moons:
    #     print("pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(moon.pos_x, moon.pos_y, moon.pos_z, moon.vel_x, moon.vel_y, moon.vel_z))
    # print()



# calc lcm of periods

print("period_x: {}".format(period_x))
print("period_y: {}".format(period_y))
print("period_z: {}".format(period_z))

def lcm(x, y):
    return x * y // math.gcd(x, y)

l = lcm(period_x, period_y)
l = lcm(l, period_z)


print("steps:", steps)
print("steps:", l)


