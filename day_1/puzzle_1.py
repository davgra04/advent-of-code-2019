from pprint import pprint
import math

def get_fuel_req(mass):
    return math.floor(mass / 3) - 2

with open("input.txt", "r") as ifh:
    lines = ifh.readlines()

masses = [int(x) for x in lines]
fuel_reqs = [get_fuel_req(m) for m in masses]

total_fuel = 0
for f in fuel_reqs:
    total_fuel += f

print("total fuel:", total_fuel)
