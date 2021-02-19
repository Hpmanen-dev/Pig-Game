"""This is the player."""
class Player():
    Name = None
    Score = 0

    def __init__(self):
        self.Name = input("Enter your name: ")
        self.Score = 0

    def get_player_name(self):
        return self.Name
    
    def get_Score(self):
        return self.Score
