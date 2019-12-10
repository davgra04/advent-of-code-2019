from computer import Computer
from itertools import permutations
from pprint import pprint

# read program from file
########################################
input_file = "input.txt"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"
# input_file = "test4.txt"
# input_file = "test5.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

ops = [int(x) for x in lines[0].rstrip().split(",")]

# print("program length:", len(ops))


# execute programs
########################################

# all_inputs = [[9,8,7,6,5]]    # inputs for test4.txt, expect output 139629729
# all_inputs = [[9,7,8,5,6]]    # inputs for test5.txt, expect output 18216


all_inputs = permutations([5, 6, 7, 8, 9])
# pprint(list(all_inputs))


max_output = 0

for inputs in all_inputs:

    # initialize thruster computers
    thruster_computers = [Computer(pause_on_output=True) for i in range(5)]
    for c in thruster_computers:
        c.load_program(ops)

    intermediate_output = 0
    current_output = 0

    completed = False
    first_round = True

    while not completed:

        idx = 0
        for comp, i in zip(thruster_computers, inputs):

            # print("COMPUTER", idx)
            # print("i:", i)
            # print("intermediate output:", intermediate_output)

            if first_round:
                comp.set_inputs([i, intermediate_output])
            else:
                comp.set_inputs([intermediate_output])

            if comp.paused:
                comp.resume_program()
            else:
                comp.run_program()

            if not comp.halted:
                outputs = comp.get_outputs()
                # print("outputs:", outputs)
                intermediate_output = outputs[0]

            idx += 1
            # print("=-------------------------=")
        # print("===========================================")

        first_round = False

        if thruster_computers[-1].halted:
            completed = True
            current_output = intermediate_output

    print("{} -> {}".format(inputs, current_output))

    if current_output > max_output:
        max_output = current_output


print("max output:", max_output)
