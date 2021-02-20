"""This is the Computer Player."""

import random

class Computer():
    """This is the Computer Class."""
    Score = 0
    Name = "Computer Player"

    def __init__(self):
        self.Score = 0

    def get_Score(self):
        return self.Score
    
    def get_name(self):
        return self.Name
    
    def add_Score(self, Score):
        self.Score += Score