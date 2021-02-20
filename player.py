"""This is the player."""


class Player:
    """This is a player class."""

    def __init__(self, Name):
        """Initiating the player."""
        self.Name = Name
        self.Score = 0

    def get_player_name(self):
        """Get player's name."""
        return self.Name

    def get_Score(self):
        """Get player's score."""
        return self.Score

    def add_Score(self, Score):
        """Add to player's score."""
        self.Score += Score
