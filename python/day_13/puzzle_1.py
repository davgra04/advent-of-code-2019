from pprint import pprint
from computer import Computer
from collections import defaultdict

# read program from file
########################################
input_file = "input.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

ops = [int(x) for x in lines[0].rstrip().split(",")]



screen = []

for i in range(50):
    screen.append(["." for j in range(50)])



# set up computer and run
########################################

comp = Computer(pause_on_output=True)
comp.load_program(ops)

while True:



    # resume program twice to obtain 3 outputs
    comp.resume_program()
    comp.resume_program()
    comp.resume_program()
    outputs = comp.get_outputs()
    print("outputs:", outputs)

    if comp.halted:
        break

    # draw
    x = outputs[0]
    y = outputs[1]
    tile = outputs[2]

    if tile == 0:
        screen[y][x] = "."
    elif tile == 1:
        screen[y][x] = "W"
    elif tile == 2:
        screen[y][x] = "B"
    elif tile == 3:
        screen[y][x] = "="
    elif tile == 4:
        screen[y][x] = "o"


block_tile_count = 0



for row in screen:

    for tile in row:
        if tile == "B":
            block_tile_count += 1


print(block_tile_count)
