"""This is the player."""


class Player:
    """This is a player class."""

    def __init__(self, name):
        """Initiate the player."""
        self.name = name
        self.score = 0

    def get_name(self):
        """Get player's name."""
        return self.name

    def get_score(self):
        """Get player's score."""
        return self.score

    def add_score(self, score):
        """Add to player's score."""
        self.score += score
