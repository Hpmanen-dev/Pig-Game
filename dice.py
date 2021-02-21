"""The die of the game :^)."""
import random


class Dice():
    """Create a six-sided dice."""

    sides = 6

    def __init__(self):
        """Initiate a dice."""
        random.seed()

    def roll(self):
        """Roll the dice and return the number."""
        return random.randint(1, self.sides)
