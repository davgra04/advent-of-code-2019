from pprint import pprint
from computer import Computer
from collections import defaultdict

# read program from file
########################################
input_file = "input.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

ops = [int(x) for x in lines[0].rstrip().split(",")]

# helper functions
########################################

def coord_to_str(coord):
    return "{},{}".format(coord[0], coord[1])

def str_to_coord(s):
    return s.split(",")

def move_forward(bot_pos, direction):
    if direction == 0:      # up
        return [bot_pos[0], bot_pos[1]+1]
    elif direction == 1:    # right
        return [bot_pos[0]+1, bot_pos[1]]
    elif direction == 2:    # down
        return [bot_pos[0], bot_pos[1]-1]
    elif direction == 3:    # left
        return [bot_pos[0]-1, bot_pos[1]]

# set up bot and panel state
########################################

visited = defaultdict(int)  # indicates which panels are visited
color = defaultdict(int)    # indicates color of each panel

bot_pos = [0, 0]
bot_dir = 0

color[coord_to_str(bot_pos)] = 1    # start bot on a white panel

# keep track of min/max coordinates for drawing later
min_x = 0
max_x = 0
min_y = 0
max_y = 0

# set up computer and run
########################################

comp = Computer(pause_on_output=True)
comp.load_program(ops)

while True:

    # read current panel color and set input
    cur_color = color[coord_to_str(bot_pos)]
    comp.set_inputs([cur_color])
    # print("cur_color:", cur_color)

    # resume program twice to obtain 2 outputs
    comp.resume_program()
    comp.resume_program()
    outputs = comp.get_outputs()
    # print("outputs:", outputs)

    if comp.halted:
        break

    to_paint = outputs[0]
    to_turn = outputs[1]

    # paint panel
    color[coord_to_str(bot_pos)] = to_paint
    visited[coord_to_str(bot_pos)] = 1

    # turn and move
    if to_turn:
        bot_dir = (bot_dir + 1) % 4
    else:
        bot_dir = (bot_dir - 1) % 4

    bot_pos = move_forward(bot_pos, bot_dir)

    # update min/max positions
    if bot_pos[0] < min_x:
        min_x = bot_pos[0]
    if bot_pos[0] > max_x:
        max_x = bot_pos[0]
    if bot_pos[1] < min_y:
        min_y = bot_pos[1]
    if bot_pos[1] > max_y:
        max_y = bot_pos[1]

# print out registration identifier
########################################

for y in range(max_y, min_y-1, -1):
    row = []
    for x in range(min_x, max_x+1):
        if color[coord_to_str([x, y])] == 1:
            row.append(u"\u2588")
        else:
            row.append(" ")

    print("".join(row))
