debug = False


class Computer:

    # Constructor
    ################################################################################################

    def __init__(self, pause_on_output=False):
        self.inputs = []
        self.outputs = []
        self.pause_on_output = pause_on_output
        self.paused = False
        self.halted = False

        self.instructions = {
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

    # Helper functions
    ################################################################################################

    def print_program(self):
        for m_idx, m in enumerate(self.memory):
            print("{0:04d}: {1}".format(m_idx, m))

    def get_param_value(self, param, param_mode):
        if int(param_mode) == 0:
            return self.memory[param]
        else:
            return param

    # Opcode functions
    ################################################################################################

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

    def exec_INPUT(self, params, param_modes):
        if debug:
            print("called INPUT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        # get input
        if len(self.inputs):
            # use input list
            i = self.inputs.pop(0)
        else:
            # prompt for user input

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

    def exec_OUTPUT(self, params, param_modes):
        if debug:
            print("called OUTPUT with:")
            print("    params:", params)
            print("    param_modes:", param_modes)

        val = self.get_param_value(params[0], param_modes[2])

        print("#########################")
        print("## output:", val)
        print("#########################")

        self.outputs.append(val)

        if self.pause_on_output:
            self.paused = True

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
        self.halted = True
        print("Computer halted!")

    # Setting program, inputs, outputs
    ################################################################################################

    def load_program(self, memory):
        self.memory = memory.copy()

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_outputs(self):
        outputs = self.outputs
        self.outputs = []
        return outputs

    # Running the program
    ################################################################################################

    def run_program(self):

        if debug:
            print("INITIAL STATE:")
            self.print_program()
            # print(self.memory)

        # execute program
        self.pc = 0
        self.quit = False

        self.main_loop()

        if debug:
            print("FINAL STATE:")
            self.print_program()
            # print(self.memory)

        return self.memory

    def resume_program(self):
        if self.paused and not self.halted:
            self.paused = False
            self.main_loop()

    def main_loop(self):

        while not self.halted and not self.paused:

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
            inst = self.instructions[opcode]
            n_params = inst["n_params"]
            exec = inst["exec"]
            if n_params == 0:
                params = []
            else:
                params = self.memory[self.pc+1:self.pc+1+n_params]

            # execute instruction
            exec(params, param_modes)

            # increment program counter
            if inst["increment_pc"]:
                self.pc += n_params + 1
