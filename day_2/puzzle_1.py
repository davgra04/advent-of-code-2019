from pprint import pprint

### load program
with open("input.txt", "r") as ifh:
    lines = ifh.readlines()

ops = [int(x) for x in lines[0].rstrip().split(",")]
# ops = [1,0,0,0,99]
# ops = [2,3,0,3,99]
# ops = [2,4,4,5,99,0]
# ops = [1,1,1,4,99,5,6,0,99]

print("INITIAL STATE:")
print(ops)

### modify program
ops[1] = 12
ops[2] = 2

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

### view result
print("FINAL STATE:")
print(ops)

print("value at position 0: {}".format(ops[0]))

