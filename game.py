"""This is the Pig Game."""

import player
import computer

class Game():
    Die_score = 0

    def start(self):
        """Ask user if he/she wants to play single or multiplayer."""
        print("Do you want to play single or multiplayer?")
        decision = input()
        if decision == "singleplayer":
            self.singleplayer()
        elif decision == "multiplayer":
            self.multiplayer()
    
    def singleplayer(self):
        """Start a singleplayer game."""
        Player1 = player.Player()
        Computer = computer.Computer()
    
    def multiplayer(self):
        """Start a multiplayer game."""
        Player1 = player.Player()
        Player2 = player.Player()