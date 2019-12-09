from pprint import pprint
import math

def get_fuel_req(mass):
    return math.floor(mass / 3) - 2

with open("input.txt", "r") as ifh:
    lines = ifh.readlines()

masses = [int(x) for x in lines]
total_fuel = 0

for m in masses:

    fuel_req = get_fuel_req(m)
    total_fuel += fuel_req

    while (get_fuel_req(fuel_req) > 0):
        fuel_req = get_fuel_req(fuel_req)
        total_fuel += fuel_req

print("total fuel:", total_fuel)
