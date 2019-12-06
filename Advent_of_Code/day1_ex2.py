# --- Day 1: The Tyranny of the Rocket Equation --- PART 2

# Fuel itself requires fuel just like a module - take its mass, divide by three,
# round down, and subtract 2. However, that fuel also requires fuel, and that
# fuel requires fuel, and so on. Any mass that would require negative fuel should
# instead be treated as if it requires zero fuel; the remaining mass, if any, is instead
# handled by wishing really hard, which has no mass and is outside the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total.
# Then, treat the fuel amount you just calculated as the input mass and repeat the process,
# continuing until a fuel requirement is zero or negative. For example:

# A module of mass 14 requires 2 fuel. This fuel requires no further fuel
# (2 divided by 3 and rounded down is 0, which would call for a negative fuel),
# so the total fuel required is still just 2.
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216
# more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel,
# which requires 5 fuel, which requires no further fuel. So, the total fuel required
# for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is:
# 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

# What is the sum of the fuel requirements for all of the modules on your spacecraft
#  when also taking into account the mass of the added fuel? (Calculate the fuel requirements
# for each module separately, then add them all up at the end.)

import math


def mass_reduction(mass):
    return math.floor(mass / 3) - 2


def extra_fuel(item):
    sum_item = []
    while item > 0:
        item = math.floor(item / 3) - 2
        if item > 0:
            sum_item.append(item)

    return sum_item


# sum of nested list in Python with "flatten" also works with nested tuples and sets


def flatten(L):
    '''Flattens nested lists or tuples with non-string items'''
    for item in L:
        try:
            for i in flatten(item):
                yield i
        except TypeError:
            yield item


# open file with inputs
my_list = open("day1_my_input.txt", "r")

my_mass = []

for line in my_list:
    # append and convert string to int
    my_mass.append(int(line))


# Test if values are ok
# print(list(map(mass_reduction, my_mass)))

# passing each number in the list to the function and creat a new list
fuel_module = list(map(mass_reduction, my_mass))

extra_fuel = list(map(extra_fuel, fuel_module))

print(sum(flatten(fuel_module)))
a = sum(flatten(fuel_module))

print(sum(flatten(extra_fuel)))
b = sum(flatten(extra_fuel))

# sum all the values
total_fuel = a + b
print(total_fuel)

# Result = 5218616
