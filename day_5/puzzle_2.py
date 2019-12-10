from pprint import pprint

debug = False

class Computer:

    def __init__(self):
        pass

    def print_program(self):
        for m_idx, m in enumerate(self.memory):
            print("{0:04d}: {1}".format(m_idx, m))

    def get_param_value(self, param, param_mode):
        if int(param_mode) == 0:
            return self.memory[param]
        else:
            return param

    def exec_ADD(self, params, param_modes):
        if debug:
            print("called ADD with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a = self.get_param_value(params[0], param_modes[2])

        # get b
        b = self.get_param_value(params[1], param_modes[1])

        # get out addr
        out_addr = self.get_param_value(params[2], 1)  # param_modes[0])

        if debug:
            print("a:", a)
            print("b:", b)
            print("out_addr:", out_addr)

        # compute
        self.memory[out_addr] = a + b

        return False

    def exec_MULT(self, params, param_modes):
        if debug:
            print("called MULT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a = self.get_param_value(params[0], param_modes[2])

        # get b
        b = self.get_param_value(params[1], param_modes[1])

        # get out addr
        out_addr = self.get_param_value(params[2], 1)  # param_modes[0])

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
        write_addr = self.get_param_value(params[0], 1)  # param_modes[2])
        self.memory[write_addr] = i

        return False

    def exec_OUTPUT(self, params, param_modes):
        if debug:
            print("called OUTPUT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        val = self.get_param_value(params[0], param_modes[2])

        print("#########################")
        print("## output:", val)
        print("#########################")

        return False

    def exec_JIT(self, params, param_modes):
        if debug:
            print("called JIT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get condition
        condition = self.get_param_value(params[0], param_modes[2])

        # get jumpaddr
        jumpaddr = self.get_param_value(params[1], param_modes[1])

        if condition != 0:
            self.pc = jumpaddr
        else:
            self.pc += len(params) + 1

    def exec_JIF(self, params, param_modes):
        if debug:
            print("called JIF with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get condition
        condition = self.get_param_value(params[0], param_modes[2])

        # get jumpaddr
        jumpaddr = self.get_param_value(params[1], param_modes[1])

        if condition == 0:
            self.pc = jumpaddr
        else:
            self.pc += len(params) + 1

    def exec_LT(self, params, param_modes):
        if debug:
            print("called LT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a = self.get_param_value(params[0], param_modes[2])

        # get b
        b = self.get_param_value(params[1], param_modes[1])

        # get out addr
        out_addr = self.get_param_value(params[2], 1)  # param_modes[0])

        # compute
        if a < b:
            self.memory[out_addr] = 1
        else:
            self.memory[out_addr] = 0

    def exec_EQ(self, params, param_modes):
        if debug:
            print("called EQ with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get a
        a = self.get_param_value(params[0], param_modes[2])

        # get b
        b = self.get_param_value(params[1], param_modes[1])

        # get out addr
        out_addr = self.get_param_value(params[2], 1)  # param_modes[0])

        # compute
        if a == b:
            self.memory[out_addr] = 1
        else:
            self.memory[out_addr] = 0

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
                "increment_pc": True
            },
            # MULT
            2: {
                "n_params": 3,
                "exec": self.exec_MULT,
                "increment_pc": True
            },
            # INPUT
            3: {
                "n_params": 1,
                "exec": self.exec_INPUT,
                "increment_pc": True
            },
            # OUTPUT
            4: {
                "n_params": 1,
                "exec": self.exec_OUTPUT,
                "increment_pc": True
            },
            # JIT
            5: {
                "n_params": 2,
                "exec": self.exec_JIT,
                "increment_pc": False
            },
            # JIF
            6: {
                "n_params": 2,
                "exec": self.exec_JIF,
                "increment_pc": False
            },
            # LT
            7: {
                "n_params": 3,
                "exec": self.exec_LT,
                "increment_pc": True
            },
            # EQ
            8: {
                "n_params": 3,
                "exec": self.exec_EQ,
                "increment_pc": True
            },
            # END PROGRAM
            99: {
                "n_params": 0,
                "exec": self.exec_END,
                "increment_pc": True
            },
        }

    def load_program(self, memory):
        self.memory = memory.copy()

    def run_program(self, print_state=False):

        # instruction definition
        instructions = self.get_instructions()

        if print_state:
            print("INITIAL STATE:")
            self.print_program()
            # print(self.memory)

        # execute program
        self.pc = 0
        quit = False

        while not quit:

            if debug:
                print()

            # parse instruction
            opcode_str = "{0:05d}".format(self.memory[self.pc])
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
                params = self.memory[self.pc+1:self.pc+1+n_params]

            # execute instruction
            quit = exec(params, param_modes)

            # increment program counter
            if inst["increment_pc"]:
                self.pc += n_params + 1

        if print_state:
            print("FINAL STATE:")
            self.print_program()
            # print(self.memory)

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
# ops = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
# ops = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]           # position mode day5_part2 test
# ops = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]                               # immediate mode day5_part2 test

# print("program length:", len(ops))

# initialize computer
########################################
comp = Computer()
comp.load_program(ops)


# execute program
########################################
memory = comp.run_program(debug)
