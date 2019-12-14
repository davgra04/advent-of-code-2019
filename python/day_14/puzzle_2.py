from pprint import pprint
import math
from collections import defaultdict

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


# read program from file
########################################
input_file = "input.txt"
# input_file = "test0.txt"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"

with open(input_file, "r") as ifh:
    lines = [l.rstrip() for l in ifh.readlines()]


# build recipe dict
########################################

recipes = {}

for reaction in lines:

    # pprint(reaction)

    (ins, out) = reaction.split(" => ")

    ins = ins.split(", ")

    print("ins:", ins)
    print("out:", out)

    (count, out_type) = out.split(" ")

    # print("out_type:", out_type)
    # print("count:", count)

    recipes[out_type] = {
        "count": int(count),
        "inputs": {}
    }

    for i in ins:
        (in_count, in_type) = i.split(" ")
        recipes[out_type]["inputs"][in_type] = int(in_count)

    # print()


pprint(recipes)






def calc_required_ore(fuel_count=1):



    reduced = False
    req = defaultdict(int)
    req["FUEL"] = fuel_count




    leftover = defaultdict(int)

    while not reduced:

        # iterate through each key and reduce
        reduced = True

        req_to_iterate = req.copy()

        for i_to_reduce in req_to_iterate.keys():

            if i_to_reduce in recipes.keys():
                reduced = False

                ing_count = req[i_to_reduce]

                # print("reducing", i_to_reduce, ". Need", ing_count, "units.")

                # how many "units" of this recipe do we need?
                reaction_count = math.ceil(ing_count / recipes[i_to_reduce]["count"])

                # print("  reaction_count:", reaction_count)
                

                # remove ingredient
                del req[i_to_reduce]

                # add components
                for added_component in recipes[i_to_reduce]["inputs"].keys():
                    req[added_component] += recipes[i_to_reduce]["inputs"][added_component] * reaction_count - leftover[added_component]
                    
                    if added_component in leftover:
                        del leftover[added_component]




                leftover[i_to_reduce] += recipes[i_to_reduce]["count"] * reaction_count - ing_count

                # pprint(req)
                # pprint(leftover)
                # print()

    return req["ORE"]



found_max_fuel = False
prev_fuel_count = 0
fuel_count = 2680000

while True:

    ore = calc_required_ore(fuel_count)

    print("{} ore -> {} fuel".format(ore, fuel_count))
    print("1000000000000")

    if ore > 1000000000000:
        break
    
    prev_fuel_count = fuel_count
    fuel_count += 1


print("max_fuel:", prev_fuel_count)



# ore_per_fuel = calc_required_ore(1)

# # ore_per_fuel = 13312

# ore_count = 1000000000000

# print("ore_per_fuel:", ore_per_fuel)
# print("ore_count:", ore_count)
# print("max_fuel:", ore_count / ore_per_fuel)







