from pprint import pprint


# read data
########################################
input_file = "input.txt"
# input_file = "test2.txt"

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

# pprint(system)

# find common parent
########################################

my_location = system["YOU"]["parent"]
santa_location = system["SAN"]["parent"]

# build list of parents to my location
my_parents = []
parent = system[my_location]["parent"]
while parent is not None:
    my_parents.append(parent)
    body = parent
    parent = system[body]["parent"]

# check santa's location's parents for common parent
common_parent = None
parent = system[santa_location]["parent"]
while parent is not None:
    if parent in my_parents:
        common_parent = parent
        print("Found parent! (" + common_parent + ")")
        break
    body = parent
    parent = system[body]["parent"]

if common_parent is None:
    print("No common parent found!")
    quit()

# count orbits
########################################

system[common_parent]["parent"] = None      # cut off at common parent to measure orbital distance
total_orbits = 0

for body in [my_location, santa_location]:
    # print("body", body)

    parent = system[body]["parent"]

    while parent is not None:
        total_orbits += 1
        body = parent
        parent = system[body]["parent"]

print("num orbital transfers:", total_orbits)
