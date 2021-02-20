"""This is the Computer Player."""

import game
import random

class Computer():
    """This is the Computer Class."""
    Score = 0
    Name = "Computer Player"
    the_game = None
    intelligence = 0

    def __init__(self, intelligence):
        """Initiate Computer."""
        random.seed()
        self.the_game = game.Game()
        self.Score = 0
        self.intelligence = intelligence

    def get_Score(self):
        """Get Score."""
        return self.Score
    
    def get_name(self):
        """Get Computer Name."""
        return self.Name
    
    def add_Score(self, Score):
        """Add to Computer's score."""
        self.Score += Score

    def get_intelligence(self):
        """Get intelligence."""
        return self.intelligence
    
    def set_intelligence(self, intelligence):
        """Change intelligence"""
        self.intelligence = intelligence
