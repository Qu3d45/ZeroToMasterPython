some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


# Find the duplicates
duplicates = [item for item in some_list if some_list.count(item) > 1]

print(duplicates)

# transform in to a set because set only show unique items
duplicates_v2 = set([item for item in some_list if some_list.count(item) > 1])

print(duplicates_v2)

# converting to list
duplicates_v3 = list(
    set([item for item in some_list if some_list.count(item) > 1]))

print(duplicates_v3)
