# --- Day 1: The Tyranny of the Rocket Equation --- PART 1

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
# required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually
# calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

import math


def mass_reduction(mass):
    return math.floor(mass / 3)-2


# open file with inputs
my_list = open("day1_my_input.txt", "r")

my_mass = []

for line in my_list:
    # append and convert string to int
    my_mass.append(int(line))

# Test if values are ok
#print(list(map(mass_reduction, my_mass)))

# passing each number in the list to the function and creat a new list
fuel_module = list(map(mass_reduction, my_mass))

# sum all the values
total_fuel = sum(fuel_module)
print(total_fuel)

# Result = 3481005
