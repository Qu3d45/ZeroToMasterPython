class User():
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, number_arrows):
        self.name = name
        self.number_arrows = number_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left {self.number_arrows}")


wizard1 = Wizard("Merlin", 50)
print(wizard1.sign_in())
wizard1.attack()

archer1 = Archer("Robin", 100)
archer1.attack()
