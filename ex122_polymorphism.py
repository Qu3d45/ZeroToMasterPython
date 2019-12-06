﻿class User():
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print(" do nothing")


class Wizard(User):
    def __init__(self, name, power):

        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, number_arrows):
        self.name = name
        self.number_arrows = number_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left {self.number_arrows}")


def player_attack(char):
    char.attack()


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)


player_attack(wizard1)
player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()
