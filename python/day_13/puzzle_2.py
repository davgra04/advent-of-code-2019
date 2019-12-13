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

for i in range(23):
    screen.append(["." for j in range(50)])


def draw_screen():
    global screen

    for row in screen:
        print("".join(row))


last_ball_pos = -1
paddle_pos = -1
ball_pos = -1
ball_moving_right = True



# set up computer and run
########################################

comp = Computer(pause_on_output=True)
comp.load_program(ops)

# set free play
comp.memory[0] = 2


ball_motion = 1

def set_input():
    global comp, screen, paddle_pos, ball_pos, ball_motion


    # last_ball_pos = ball_pos

    # find horizontal position of ball and paddle
    for row in screen:
        for pos, tile in enumerate(row):
            if tile == "o":
                last_ball_pos = ball_pos
                ball_pos = pos

                if ball_pos < last_ball_pos:
                    ball_motion = 1
                elif ball_pos > last_ball_pos:
                    ball_motion = -1
                else:
                    ball_motion = 0
            elif tile == "=":
                paddle_pos = pos

    print("ball_pos:", ball_pos)
    print("paddle_pos:", paddle_pos)


    # ball_going_left = True
    # if last_ball_pos > ball_pos:
    #     ball_going_left = False

    if paddle_pos < ball_pos + ball_motion:# and ball_moving_right:
        comp.inputs = [1, 1, 1]
        print("moving right")
    elif paddle_pos > ball_pos + ball_motion:# and not ball_moving_right:
        comp.inputs = [-1, -1, -1]
        print("moving left")
    else:
        comp.inputs = [0, 0, 0]





# comp.inputs = [1, 1]

while True:



    # resume program twice to obtain 3 outputs
    comp.resume_program()
    draw_screen()
    set_input()
    comp.resume_program()
    draw_screen()
    set_input()
    comp.resume_program()
    outputs = comp.get_outputs()
    set_input()
    # print("outputs:", outputs)





    # i = ""

    # while i != "":
    #     i = input("give input:")
    #     print("input:", i)
    #     if i == "a":
    #         comp.inputs = [-1]
    #     elif i == "s":
    #         comp.inputs = [0]
    #     elif i == "d":
    #         comp.inputs = [1]


    if comp.halted:
        break

    # draw
    x = outputs[0]
    y = outputs[1]
    tile = outputs[2]

    if x == -1 and y == 0:
        print("score:", tile)
        # input()
        continue

    if tile == 0:
        screen[y][x] = "."
        # pass
    elif tile == 1:
        screen[y][x] = "W"
    elif tile == 2:
        screen[y][x] = "B"
    elif tile == 3:
        screen[y][x] = "="
    elif tile == 4:
        screen[y][x] = "o"



    draw_screen()
    print()


block_tile_count = 0



for row in screen:

    for tile in row:
        if tile == "B":
            block_tile_count += 1


print(block_tile_count)
