"""The die of the game :^)."""
import random


class Dice():
    """A dice with 6 sides."""

    faces = 6

    def __init__(self):
        """Initializes a dice with 0 rolls made."""
        random.seed()
        self.rolls_made = 0

    def roll(self):
        """Roll a dice once and return the value."""
        self.rolls_made += 1
        return random.randint(1, self.faces)

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made
