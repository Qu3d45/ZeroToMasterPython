from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def uppercase(item):
    return item.upper()


def only_odd(item):
    return item % 2 != 0


def pass_50(item):
    return item > 50


print(list(map(uppercase, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(filter(only_odd, my_numbers)))

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(pass_50, scores)))

print(list(filter(pass_50, sorted(scores))))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers, 0))

print(reduce(accumulator, (my_numbers+scores)))
