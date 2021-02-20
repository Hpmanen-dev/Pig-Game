"""This is the Pig Game."""

import player
import computer
import dice

class Game():
    Dice_score = 0
    def __init__(self):
        self.Die = dice.Dice()

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
        Player1 = player.Player(input("Enter your name: "))
        Computer = computer.Computer()
        print(f"{Player1.get_player_name()} starts.")
        currentPlayer = Player1
        while currentPlayer == Player1:
            print("Do you want to roll or hold?")
            decision = input()
            if decision == "roll":
                roll = self.Die.roll()
                print(f"{Player1.get_player_name()} rolled a {roll}")
                if roll != 1:
                    self.Dice_score += roll
                else:
                    print(f"{Player1.get_player_name()} got 0 points this round")
                    self.Dice_score = 0
                    currentPlayer = Computer
            elif decision == "hold":
                Player1.add_Score(self.Dice_score)
                print(f"{Player1.get_player_name()} received {self.Dice_score} points")
                print(f"{Player1.get_player_name()} now have {Player1.get_Score} points in total!")
                    

    def multiplayer(self):
        """Start a multiplayer game."""
        Player1 = player.Player(input("Enter your name: "))
        Player2 = player.Player(input("Enter your name: "))