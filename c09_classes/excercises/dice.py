from random import randint
"""
Class representing a dice
"""
class Die:
    """
    Die can have a number from 1 to 6
    """
    def __init__(self, sides = 6):
        """
        Constructor
        """
        self.sides = sides
        self.value = 0
    #------------------------------------#
    def roll_die(self):
        """
        Roll a die, print a number from 1 to 6
        """
        print(randint(1, self.sides))
