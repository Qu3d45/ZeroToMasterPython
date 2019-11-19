# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('fofi', 3)
cat2 = Cat('gati', 5)
cat3 = Cat('rodi', 1)

print(cat1.name)
print(cat2.age)
print(cat3.name)


# 2 Create a function that finds the oldest cat


def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
