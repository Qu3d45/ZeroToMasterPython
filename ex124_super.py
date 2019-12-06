class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

    def attack(self):
        print(" do nothing")


class Wizard(User):
    def __init__(self, name, power, email):
        # super() refers to User without "self" = User.__init__(self, email)
        super().__init__(email)
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


wizard1 = Wizard("Merlin", 50, 'merlin@gmail.com')
archer1 = Archer("Robin", 100)

print(wizard1.email)
