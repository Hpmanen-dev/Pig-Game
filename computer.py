"""This is the Computer Player."""

import game
import random

class Computer():
    """This is the Computer Class."""

    def __init__(self, intelligence):
        """Initiate Computer."""
        random.seed()
        self.the_game = game.Game()
        self.Score = 0
        self.intelligence = intelligence
        self.Name = "Computer player"
        self.greediness = 7
        self.rolls = 0

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
        """Change intelligence."""
        self.intelligence = intelligence
    
    def get_greediness(self):
        """Get the greediness of the computer."""
        return self.greediness
    
    def set_greediness(self, change):
        """Change greediness."""
        self.greediness = change
    
    def get_rolls(self):
        return self.rolls

    def set_rolls(self, change):
        self.rolls = change
