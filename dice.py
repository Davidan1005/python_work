from random import randint


class Die:
    """An attempt to simulte a die"""

    def __init__(self, sides=6):
        """Initializes our dice"""
        self.sides = sides

    def roll_die(self):
        """Simulates a dice roll"""
        print(randint(1, self.sides))


six_sided_die = Die()
six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()
