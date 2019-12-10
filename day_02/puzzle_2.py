from pprint import pprint

def run_program(ops):
    ### execute program
    pc = 0
    quit = False

    while not quit:

        opcode = ops[pc]

        if opcode == 99:
            quit = True
        elif opcode == 1:
            a_addr = ops[pc + 1]
            b_addr = ops[pc + 2]
            out_addr = ops[pc + 3]
            ops[out_addr] = ops[a_addr] + ops[b_addr]
        elif opcode == 2:
            a_addr = ops[pc + 1]
            b_addr = ops[pc + 2]
            out_addr = ops[pc + 3]
            ops[out_addr] = ops[a_addr] * ops[b_addr]

        pc += 4


    return ops


### load program
with open("input.txt", "r") as ifh:
    lines = ifh.readlines()

ops = [int(x) for x in lines[0].rstrip().split(",")]

for noun in range(100):
    for verb in range(100):

        print("trying noun:{} verb:{}".format(noun, verb))
        cur_ops = ops[:]
        cur_ops[1] = noun
        cur_ops[2] = verb
        # print(cur_ops[:4])

        try:
            # print("    asdf:", cur_ops[0])
            out = run_program(cur_ops)
            # print("    asdf:", out[0])
        except Exception as e:
            print("  exception!:", e)
            continue

        if out[0] == 19690720:
            print("Found inputs!")
            print("  noun:", noun)
            print("  verb:", verb)
            print("  100 * noun + verb:", 100 * noun + verb)
            quit()


# ### view result
# print("FINAL STATE:")
# print(ops)

# print("value at position 0: {}".format(ops[0]))

