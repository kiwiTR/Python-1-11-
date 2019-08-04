from random import randint
class Die():
    def __init__(self):
        self.sides=6

    def roll_die(self):
        self.sides=randint(1,6)
        print(str(self.sides))

die=Die()
for i in range(10):
    die.roll_die()