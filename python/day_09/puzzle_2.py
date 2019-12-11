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

#### day 5 pt 1 tests
# ops = [3,0,4,0,99]      # outputs what's input
# ops = [1002,4,3,4,33]   # sets last op to an ENDS and halts correctly
# ops = [1101,100,-1,4,0] # also sets END and halts correctly
#### day 5 pt 2 tests
# ops = [3,9,8,9,10,9,4,9,99,-1,8]        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# ops = [3,9,7,9,10,9,4,9,99,-1,8]        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
# ops = [3,3,1108,-1,8,3,4,3,99]          # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# ops = [3,3,1107,-1,8,3,4,3,99]          # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).

# ops = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]    # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero: (using position mode)
# ops = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]         # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero: (using immediate mode)

# outputs 999 if input < 8, 1000 if input == 8, 1001 if input > 8
# ops = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#### day 9 tests
# ops = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # test 1
# ops = [1102,34915192,34915192,7,4,7,99,0] # test 2
# ops = [104,1125899906842624,99] # test 3

# reddit user's test cases
# ops = [109, -1, 4, 1, 99]               # should output -1
# ops = [109, -1, 104, 1, 99]             # should output 1
# ops = [109, -1, 204, 1, 99]             # should output 109
# ops = [109, 1, 9, 2, 204, -6, 99]       # should output 204
# ops = [109, 1, 109, 9, 204, -6, 99]     # should output 204
# ops = [109, 1, 209, -1, 204, -106, 99]  # should output 204
# ops = [109, 1, 3, 3, 204, 2, 99]        # should output the input
# ops = [109, 1, 203, 2, 204, 2, 99]      # should output the input

# print("program length:", len(ops))


# execute program
########################################


comp = Computer()
comp.load_program(ops)
comp.run_program()

outputs = comp.get_outputs()

print("outputs:", outputs)


# # inputs = [4, 3, 2, 1, 0]    # inputs for test1.txt, expect output 43210
# # inputs = [0, 1, 2, 3, 4]    # inputs for test2.txt, expect output 54321
# # inputs = [1, 0, 4, 3, 2]    # inputs for test3.txt, expect output 65210

# all_inputs = permutations([0, 1, 2, 3, 4])
# # pprint(list(all_inputs))


# max_output = 0

# for inputs in all_inputs:

#     # initialize thruster computers
#     thruster_computers = [Computer() for i in range(5)]
#     for c in thruster_computers:
#         c.load_program(ops)

#     previous_output = 0

#     for comp, i in zip(thruster_computers, inputs):
#         comp.set_inputs([i, previous_output])
#         comp.run_program()
#         previous_output = comp.get_outputs()[0]

#     print("{} -> {}".format(inputs, previous_output))

#     if previous_output > max_output:
#         max_output = previous_output


# print("max output:", max_output)
