from computer import Computer
from itertools import permutations
from pprint import pprint

# read program from file
########################################
input_file = "input.txt"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

ops = [int(x) for x in lines[0].rstrip().split(",")]

# print("program length:", len(ops))


# execute programs
########################################

# inputs = [4, 3, 2, 1, 0]    # inputs for test1.txt, expect output 43210
# inputs = [0, 1, 2, 3, 4]    # inputs for test2.txt, expect output 54321
# inputs = [1, 0, 4, 3, 2]    # inputs for test3.txt, expect output 65210

all_inputs = permutations([0, 1, 2, 3, 4])
# pprint(list(all_inputs))


max_output = 0

for inputs in all_inputs:

    # initialize thruster computers
    thruster_computers = [Computer() for i in range(5)]
    for c in thruster_computers:
        c.load_program(ops)

    previous_output = 0

    for comp, i in zip(thruster_computers, inputs):
        comp.set_inputs([i, previous_output])
        comp.run_program()
        previous_output = comp.get_outputs()[0]

    print("{} -> {}".format(inputs, previous_output))

    if previous_output > max_output:
        max_output = previous_output


print("max output:", max_output)
