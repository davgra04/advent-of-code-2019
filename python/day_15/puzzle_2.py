from pprint import pprint
from computer import Computer


def coord_int_to_str(x, y):
    return ",".join([str(x), str(y)])


def coord_str_to_int(s):
    (x, y) = s.split(",")
    return (int(x), int(y))


# read program from file
########################################
input_file = "input.txt"
# input_file = "test0.txt"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

ops = [int(x) for x in lines[0].rstrip().split(",")]


# set up map keeping vars
size = 300

map = [[" " for j in range(size)] for i in range(size)]

(pos_x, pos_y) = (size//2, size//2)
map[pos_x][pos_y] = "X"


visited = {
    coord_int_to_str(pos_x, pos_y): 1
}

move_stack = [{
    "back": None,
    "coord": coord_int_to_str(pos_x, pos_y),
    "to_search": [1, 2, 3, 4],
}]


found_oxygen = False


# set up computer and run
########################################


comp = Computer(pause_on_output=True)
comp.load_program(ops)

step = 0

# breadth first search

(next_x, next_y) = (pos_x, pos_y)
(prev_x, prev_y) = (pos_x, pos_y)
back = 0



def get_dir_incr(dir):

    if next_direction == 1:     # north
        x_incr = 0
        y_incr = -1
        back = 2
    elif next_direction == 2:   # south
        x_incr = 0
        y_incr = 1
        back = 1
    elif next_direction == 3:   # west
        x_incr = -1
        y_incr = 0
        back = 4
    elif next_direction == 4:   # east
        x_incr = 1
        y_incr = 0
        back = 3

    return (x_incr, y_incr, back)


moves = 0


###############################################################################
# TRAVEL TO THE OXYGEN
###############################################################################


while True:

    # debug print
    ########################################
    step += 1

    if step % 200 == 0:
        # draw stuff
        print("step:", step)
        with open("out_{}.txt".format(step), "w") as ofh:
            ofh.writelines(["".join(row) + "\n" for row in map])



    # get current node
    ########################################

    # get current node
    cur_node = move_stack[-1]
    # pprint(cur_node)

    (pos_x, pos_y) = coord_str_to_int(cur_node["coord"])


    # check if we need to move back or are done
    ########################################

    if len(cur_node["to_search"]) == 0:

        if cur_node["back"] is None: # searched whole space
            #ASDF print("donezo")
            break
        else:                       # need to move back

            moves -= 1
            back_dir = cur_node["back"]
            (x_incr, y_incr, _) = get_dir_incr(back_dir)
            pos_x += x_incr
            pos_y += y_incr

            # if back_dir == 1:
            #     #ASDF print("no more to search, moving back north")
            # elif back_dir == 2:
            #     #ASDF print("no more to search, moving back south")
            # elif back_dir == 3:
            #     #ASDF print("no more to search, moving back west")
            # elif back_dir == 4:
            #     #ASDF print("no more to search, moving back east")

            # run bot
            comp.set_inputs([back_dir])
            comp.resume_program()
            result = comp.get_outputs()[0]
            if result == 0:
                print("Got bad result moving back!")
                quit()

            # remove this node since we're done with it
            move_stack.pop()
            continue

    # determine next direction and position
    ########################################

    next_direction = cur_node["to_search"].pop()

    (x_incr, y_incr, back) = get_dir_incr(next_direction)
    next_x = pos_x + x_incr
    next_y = pos_y + y_incr

    if next_direction == 1:
        dirstr = "north"
    elif next_direction == 2:
        dirstr = "south"
    elif next_direction == 3:
        dirstr = "west"
    elif next_direction == 4:
        dirstr = "east"


    # continue if already visited next location
    ########################################

    if coord_int_to_str(next_x, next_y) in visited:
        print("already visited {} ({}, {})", dirstr, next_x, next_y)
        continue


    # run bot and evaluate
    ########################################

    comp.set_inputs([next_direction])
    comp.resume_program()
    result = comp.get_outputs()[0]


    # continue if hit a wall (and draw to map)
    ########################################
    if result == 0:         # hit a wall
        map[next_y][next_x] = "#"
        #ASDF print("found wall to", dirstr)
        continue



    # update position (and draw to map)
    ########################################

    pos_x = next_x
    pos_y = next_y
    moves += 1

    if result == 1:         # move success
        map[pos_y][pos_x] = "."
        #ASDF print("moved", dirstr)
    elif result == 2:         # move success and found oxygen!
        map[pos_y][pos_x] = "O"
        print("took {} moves to find oxygen!".format(moves))
        break
        #ASDF print("moved", dirstr, "and found oxygen!")


    # add position to visited dict
    ########################################

    visited[coord_int_to_str(pos_x, pos_y)] = 1


    # add node to move stack
    ########################################

    to_search = [1,2,3,4]
    to_search.remove(back)

    move_stack.append({
        "back": back,
        "coord": coord_int_to_str(pos_x, pos_y),
        "to_search": to_search,
    })





# 1 north
# 2 south
# 3 west
# 4 east

# class node:

#     def __init__(self):


# draw map
########################################

# with open("out_final.txt".format(step), "w") as ofh:
#     ofh.writelines(["".join(row) + "\n" for row in map])




###############################################################################
# CALCULATE OXYGEN SPREAD
###############################################################################

max_time = 0
cur_time = 0


visited = {
    coord_int_to_str(pos_x, pos_y): 1
}

move_stack = [{
    "back": None,
    "coord": coord_int_to_str(pos_x, pos_y),
    "to_search": [1, 2, 3, 4],
}]




while True:

    # get current node
    ########################################

    # get current node
    cur_node = move_stack[-1]
    # pprint(cur_node)

    (pos_x, pos_y) = coord_str_to_int(cur_node["coord"])


    # check if we need to move back or are done
    ########################################

    if len(cur_node["to_search"]) == 0:

        if cur_node["back"] is None: # searched whole space
            #ASDF print("donezo")
            break
        else:                       # need to move back

            cur_time -= 1
            back_dir = cur_node["back"]
            (x_incr, y_incr, _) = get_dir_incr(back_dir)
            pos_x += x_incr
            pos_y += y_incr

            # if back_dir == 1:
            #     #ASDF print("no more to search, moving back north")
            # elif back_dir == 2:
            #     #ASDF print("no more to search, moving back south")
            # elif back_dir == 3:
            #     #ASDF print("no more to search, moving back west")
            # elif back_dir == 4:
            #     #ASDF print("no more to search, moving back east")

            # run bot
            comp.set_inputs([back_dir])
            comp.resume_program()
            result = comp.get_outputs()[0]
            if result == 0:
                print("Got bad result moving back!")
                quit()

            # remove this node since we're done with it
            move_stack.pop()
            continue

    # determine next direction and position
    ########################################

    next_direction = cur_node["to_search"].pop()

    (x_incr, y_incr, back) = get_dir_incr(next_direction)
    next_x = pos_x + x_incr
    next_y = pos_y + y_incr

    if next_direction == 1:
        dirstr = "north"
    elif next_direction == 2:
        dirstr = "south"
    elif next_direction == 3:
        dirstr = "west"
    elif next_direction == 4:
        dirstr = "east"


    # continue if already visited next location
    ########################################

    if coord_int_to_str(next_x, next_y) in visited:
        print("already visited {} ({}, {})", dirstr, next_x, next_y)
        continue


    # run bot and evaluate
    ########################################

    comp.set_inputs([next_direction])
    comp.resume_program()
    result = comp.get_outputs()[0]


    # continue if hit a wall (and draw to map)
    ########################################
    if result == 0:         # hit a wall
        map[next_y][next_x] = "#"
        #ASDF print("found wall to", dirstr)
        continue



    # update position (and draw to map)
    ########################################

    pos_x = next_x
    pos_y = next_y
    cur_time += 1

    if cur_time > max_time:
        max_time = cur_time


    if result == 1:         # move success
        map[pos_y][pos_x] = "."
        #ASDF print("moved", dirstr)
    elif result == 2:         # move success and found oxygen!
        map[pos_y][pos_x] = "O"

        #ASDF print("moved", dirstr, "and found oxygen!")


    # add position to visited dict
    ########################################

    visited[coord_int_to_str(pos_x, pos_y)] = 1


    # add node to move stack
    ########################################

    to_search = [1,2,3,4]
    to_search.remove(back)

    move_stack.append({
        "back": back,
        "coord": coord_int_to_str(pos_x, pos_y),
        "to_search": to_search,
    })


print("max_time:", max_time)



