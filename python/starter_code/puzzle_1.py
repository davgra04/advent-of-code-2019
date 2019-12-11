from pprint import pprint

# read program from file
########################################
input_file = "input.txt"

with open(input_file, "r") as ifh:
    lines = ifh.readlines()

pprint(lines)
