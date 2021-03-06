"""The die of the game :^)."""
import random


class Dice():
    """Create a six-sided dice."""

    def __init__(self):
        """Initiate the dice."""
        self._sides = 6
        random.seed()

    def roll(self):
        """Roll the dice and return the number."""
        return random.randint(1, self._sides)

    @property
    def sides(self):
        """Get sides of the die."""
        return self._sides
