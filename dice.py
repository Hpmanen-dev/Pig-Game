"""The die of the game :^)."""
import random


class Dice():
    """A dice with 6 sides."""

    faces = 6

    def __init__(self):
        """Initiate a dice"""
        random.seed()

    def roll(self):
        """Roll a dice once and return the value."""
        return random.randint(1, self.faces)
