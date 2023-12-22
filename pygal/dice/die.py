from random import randint

class Die:
    """ Class representing single die"""

    def __init__(self, num_sides = 6):
        """ Assume six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random value form 1 to num_side"""
        return randint(1, self.num_sides)
