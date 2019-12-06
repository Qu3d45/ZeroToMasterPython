# Square
my_list = [5, 4, 3]

new_list = list(map(lambda item: item ** 2, my_list))

print(new_list)

# List Sorting by the second key
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

a1 = a
a1.sort(key=lambda x: x[0])
print(a1)
