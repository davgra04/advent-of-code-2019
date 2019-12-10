from pprint import pprint


# read data
########################################
input_file = "input.txt"
# input_file = "test.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]

# pprint(lines)

# construct system
########################################

system = {
    "COM": {
        "parent": None
    }
}

for relationship in lines:
    [parent, child] = relationship.split(")")
    # print("parent:", parent)
    # print("child:", child)

    system[child] = {"parent": parent}

pprint(system)

# count orbits
########################################

total_orbits = 0

for body in system.keys():
    # print("body", body)

    parent = system[body]["parent"]

    while parent is not None:
        total_orbits += 1
        body = parent
        parent = system[body]["parent"]

print("total orbits:", total_orbits)
