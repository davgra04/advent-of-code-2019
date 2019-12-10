from pprint import pprint

debug = False

# exec functions


class Computer:

    def __init__(self):
        pass

    def exec_ADD(self, params, param_modes):
        if debug:
            print("called ADD with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a_param_mode = int(param_modes[2])
        if a_param_mode == 0:
            a = self.memory[params[0]]
        else:
            a = params[0]

        # get b
        b_param_mode = int(param_modes[1])
        if b_param_mode == 0:
            b = self.memory[params[1]]
        else:
            b = params[1]

        if debug:
            print("a:", a)
            print("b:", b)

        # get out addr
        out_addr = params[2]

        # compute
        self.memory[out_addr] = a + b

        return False

    def exec_MULT(self, params, param_modes):
        if debug:
            print("called MULT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a_param_mode = int(param_modes[2])
        if a_param_mode == 0:
            a = self.memory[params[0]]
        else:
            a = params[0]

        # get b
        b_param_mode = int(param_modes[1])
        if b_param_mode == 0:
            b = self.memory[params[1]]
        else:
            b = params[1]

        if debug:
            print("a:", a)
            print("b:", b)

        # get out addr
        out_addr = params[2]

        # compute
        self.memory[out_addr] = a * b

        return False

    def exec_INPUT(self, params, param_modes):
        if debug:
            print("called INPUT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get input
        got_input = False
        while not got_input:
            i = input("Enter an integer: ")
            try:
                i = int(i)
                got_input = True
            except:
                print("  ERROR! Input must be an integer!")
                continue

        # write to memory
        write_addr = params[0]
        self.memory[write_addr] = i

        return False

    def exec_OUTPUT(self, params, param_modes):
        if debug:
            print("called OUTPUT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        out_param_mode = int(param_modes[2])
        if out_param_mode == 0:
            val = self.memory[params[0]]
        else:
            val = params[0]

        print("output:", val)

        return False

    def exec_END(self, params, param_modes):
        if debug:
            print("called END with:")
            print("    params:", params)
            print("    param_modes:", param_modes)
        return True

    def get_instructions(self):
        return {
            # ADD
            1: {
                "n_params": 3,
                "exec": self.exec_ADD,
            },
            # MULT
            2: {
                "n_params": 3,
                "exec": self.exec_MULT,
            },
            # INPUT
            3: {
                "n_params": 1,
                "exec": self.exec_INPUT,
            },
            # OUTPUT
            4: {
                "n_params": 1,
                "exec": self.exec_OUTPUT,
            },
            # END PROGRAM
            99: {
                "n_params": 0,
                "exec": self.exec_END,
            },
        }

    def load_program(self, memory):
        self.memory = memory.copy()

    def run_program(self, print_state=False):

        # instruction definition
        instructions = self.get_instructions()

        if print_state:
            print("INITIAL STATE:")
            print(self.memory)

        # execute program
        pc = 0
        quit = False

        while not quit:

            # parse instruction
            opcode_str = "{0:05d}".format(self.memory[pc])
            param_modes = opcode_str[:3]
            opcode = int(opcode_str[3:])
            # print("opcode_str:", opcode_str)
            # print("param_modes:", param_modes)
            # print("opcode:", opcode)

            # get instruction details
            inst = instructions[opcode]
            n_params = inst["n_params"]
            exec = inst["exec"]
            if n_params == 0:
                params = []
            else:
                params = self.memory[pc+1:pc+1+n_params]

            # execute instruction
            quit = exec(params, param_modes)

            # increment program counter
            pc += n_params + 1

        if print_state:
            print("FINAL STATE:")
            print(self.memory)

        return self.memory


# read program from file
########################################
input_file = "input.txt"
# input_file = "day_2_input.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

ops = [int(x) for x in lines[0].rstrip().split(",")]
# ops = [1,0,0,0,99]
# ops = [2, 3, 0, 3, 99]
# ops = [2,4,4,5,99,0]
# ops = [1,1,1,4,99,5,6,0,99]
# ops = [3,0,4,0,99]

# initialize computer
########################################

comp = Computer()
comp.load_program(ops)


# execute program
########################################

memory = comp.run_program(True)
print("value at position 0: {}".format(memory[0]))
