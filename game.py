"""This is the Pig Game."""

import player

class Game():
    Die_score = 0
    Computer_score = 0

    def start(self):
        """Ask user if he/she wants to play single or multiplayer"""
        print("Do you want to play single or multiplayer?")
        decision = input()
        if decision == "singleplayer":
            self.singleplayer()
        elif decision == "multiplayer":
            self.multiplayer()
    
    def singleplayer(self):
        """Start a singleplayer game"""
        Player1 = player.Player()
    
    def multiplayer(self):
        Player1 = player.Player()
        Player2 = player.Player()
        """Start a multiplayer game"""