"""This is the player."""


class Player:
    """This is a player class."""

    def __init__(self, name):
        """Initiate the player."""
        self._name = name
        self._score = 0

    def get_name(self):
        """Get player's name."""
        return self._name

    def get_score(self):
        """Get player's score."""
        return self._score

    def add_score(self, score):
        """Add to player's score."""
        self._score += score
