from pprint import pprint
from computer import Computer
from collections import defaultdict

# read program from file
########################################
input_file = "input.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

# pprint(lines)
ops = [int(x) for x in lines[0].rstrip().split(",")]




visited = defaultdict(int)
color = defaultdict(int)



# directions
### 0 up
### 1 right
### 2 down
### 3 left


bot_pos = [0, 0]
bot_dir = 0


def coord_to_str(coord):
    return "{},{}".format(coord[0], coord[1])

def str_to_coord(s):
    return s.split(",")


def move_forward(direction):
    global bot_pos
    if direction == 0:
        bot_pos = [bot_pos[0], bot_pos[1]+1]
    elif direction == 1:
        bot_pos = [bot_pos[0]+1, bot_pos[1]]
    elif direction == 2:
        bot_pos = [bot_pos[0], bot_pos[1]-1]
    elif direction == 3:
        bot_pos = [bot_pos[0]-1, bot_pos[1]]


comp = Computer(pause_on_output=True)
comp.load_program(ops)

while not comp.halted:

    cur_color = color[coord_to_str(bot_pos)]

    print("cur_color:", cur_color)

    comp.set_inputs([cur_color])

    # run until first output
    comp.resume_program()
    # run until second output
    comp.resume_program()
    outputs = comp.get_outputs()

    if comp.halted:
        break

    print("outputs:", outputs)
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

    move_forward(bot_dir)

    # quit()




pprint(len(visited.keys()))
# pprint(visited)

