"""This is the Computer Player."""

import random

class Computer():
    """This is the Computer Class."""
    Score = 0
    Name = "Computer Player"

    def __init__(self):
        """Initiate Computer."""
        self.Score = 0

    def get_Score(self):
        """Get Score."""
        return self.Score
    
    def get_name(self):
        """Get Computer Name."""
        return self.Name
    
    def add_Score(self, Score):
        """Add to Computer's score."""
        self.Score += Score