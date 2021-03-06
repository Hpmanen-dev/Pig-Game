"""This is the player."""


class Player:
    """This is a player class."""

    def __init__(self, name):
        """Initiate the player."""
        self._name = name
        self._score = 0

    @property
    def name(self):
        """Get player's name."""
        return self._name

    @property
    def score(self):
        """Get player's score."""
        return self._score

    def add_score(self, add):
        """Add to player's score."""
        self._score += add
