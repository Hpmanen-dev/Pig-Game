"""This is the Pig Dice Game."""

import player
import computer
import dice
import random
from time import sleep
import subprocess
import platform


class Game():
    """Game class."""

    Player1 = None
    Player2 = None
    Computer = None
    currentPlayer = None
    otherPlayer = None
    Winner = None
    win_condition = 100
    dice_score = 0

    def __init__(self):
        """Initiate the game."""
        self.Die = dice.Dice()

    def Start(self, Computer):
        """Ask user if he/she wants to play single or multiplayer."""
        print('Do you want to play "singleplayer" or "multiplayer"?')
        while True:
            decision = input()
            if decision in "singleplayer":
                self.Singleplayer(Computer)
                break
            elif decision in "multiplayer":
                self.Multiplayer()
                break
            else:
                print("Choose either 'singleplayer' or 'multiplayer'")

    def Singleplayer(self, Computer):
        """Initiate a singleplayer game."""
        self.Player1 = player.Player(input("Enter your name: "))
        self.Computer = Computer
        print(f"{self.Player1.get_name()} starts.")
        self.currentPlayer = self.Player1
        self.otherPlayer = self.Computer

    def Multiplayer(self):
        """Initiate a multiplayer game."""
        self.Player1 = player.Player(input("Enter your name: "))
        self.Player2 = player.Player(input("Enter your name: "))
        select_player = random.randint(1, 2)
        if select_player == 1:
            self.currentPlayer = self.Player1
            self.otherPlayer = self.Player2
        else:
            self.currentPlayer = self.Player2
            self.otherPlayer = self.Player1
        print(f"{self.currentPlayer.get_name()} starts.")
        print("Do you want to roll or hold?")

    def Player_turn(self, decision):
        """Player turns."""
        check = False
        if decision in "roll":
            roll = self.Die.roll()
            print(f"{self.currentPlayer.get_name()} rolled a {roll}")
            if roll != 1:
                self.dice_score += roll
            else:
                print(f"{self.currentPlayer.get_name()} got 0 points this round")
                self.Switch_player()
                self.Computer.set_rolls(0)
                self.Computer.set_greediness(7)
        elif decision in "hold":
            self.currentPlayer.add_Score(self.dice_score)
            msg = (f"{self.currentPlayer.get_name()} decided to hold\n"
                f"{self.currentPlayer.get_name()} received {self.dice_score} points\n"
            f"{self.currentPlayer.get_name()} now have {self.currentPlayer.get_Score()} points in total!")
            print(msg)
            check = self.Check_winner_condition()
            self.Switch_player()
        if check == False:
            print(f"{self.currentPlayer.get_name()}'s turn")
        else:
            msg = (f"The game is over {self.Winner} won!"
                " To start a new game type 'start' or type 'exit' to exit.")
            print(msg)
            return
        if self.currentPlayer == self.Computer:
            sleep(1)
            self.Computer_logic()

    def Check_winner_condition(self):
        """Check if the current player has 100 or more points."""
        if self.currentPlayer.get_Score() >= 100:
            print(f"Congratulations {self.currentPlayer.get_name()}, You won!")
            self.Winner = self.currentPlayer.get_name()
            self.currentPlayer = None
            self.otherPlayer = None
            return True
        else:
            return False

    def Computer_logic(self):
        intelligence = self.Computer.get_intelligence()
        greediness = self.Computer.get_greediness()
        rolls = self.Computer.get_rolls()
        if rolls == 0:
            add_roll = rolls + 1
            self.Computer.set_rolls(add_roll)
            self.Player_turn("roll")
        elif self.currentPlayer.get_Score() + self.dice_score >= 100:
            self.Player_turn("hold")
        else:
            decision = random.randint(intelligence, greediness)
            if decision != intelligence:
                add_roll = rolls +  1
                self.Computer.set_rolls(add_roll)
                change = greediness - 1
                self.Computer.set_greediness(change)
                self.Player_turn("roll")
            else:
                self.Computer.set_greediness(7)
                self.Computer.set_rolls(0)
                self.Player_turn("hold")
    
    def Switch_player(self):
        """Changes player turn."""
        prev_player = self.currentPlayer
        self.currentPlayer = self.otherPlayer
        self.otherPlayer = prev_player
        self.dice_score = 0
