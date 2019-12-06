# List, set, dictionary

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# Can be substitud by this!!!

# my_other_list = [param for param in iterable]

my_other_list = [char for char in 'hello']

print(my_other_list)

my_other_list2 = [num for num in range(0, 100)]

print(my_other_list2)

# if we need every number multiplid by 2
my_other_list3 = [num*2 for num in range(0, 100)]

print(my_other_list3)

# keep only even numbers
my_other_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_other_list4)
