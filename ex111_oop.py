class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('manuel', 37)
player2 = PlayerCharacter('berto', 25)

print(player1.name)
print(player1.age)

print(player1.run())
