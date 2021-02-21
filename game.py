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
    win_condition = 100
    dice_score = 0
    computer_rolls = 0

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
        prev_player = self.currentPlayer
        if decision in "roll":
            roll = self.Die.roll()
            print(f"{self.currentPlayer.get_name()} rolled a {roll}")
            if roll != 1:
                self.dice_score += roll
            else:
                print(f"{self.currentPlayer.get_name()} got 0 points this round")
                self.dice_score = 0
                self.currentPlayer = self.otherPlayer
                self.otherPlayer = prev_player
                self.computer_rolls = 0
        elif decision in "hold":
            self.currentPlayer.add_Score(self.dice_score)
            msg = (f"{self.currentPlayer.get_name()} decided to hold\n"
                f"{self.currentPlayer.get_name()} received {self.dice_score} points\n"
            f"{self.currentPlayer.get_name()} now have {self.currentPlayer.get_Score()} points in total!")
            print(msg)
            check = self.Check_winner_condition()
            self.currentPlayer = self.otherPlayer
            self.otherPlayer = prev_player
            self.dice_score = 0
        if check == False:
            print(f"{self.currentPlayer.get_name()}'s turn")
        else:
            msg = (f"The game is over {prev_player.get_name()} won!"
                " To start a new game type 'start' or type 'exit' to exit.")
            print(msg)
            prev_player = None
            return
        if self.currentPlayer == self.Computer:
            sleep(1)
            self.Computer_logic()

    def Check_winner_condition(self):
        """Check if the current player has 100 or more points."""
        if self.currentPlayer.get_Score() >= 100:
            print(f"Congratulations {self.currentPlayer.get_name()}, You won!")
            self.currentPlayer = None
            self.otherPlayer = None
            return True
        else:
            return False

    def Computer_logic(self):
        intelligence = self.Computer.get_intelligence()
        safety = 7
        if self.computer_rolls == 0:
            self.computer_rolls += 1
            self.Player_turn("roll")
        elif self.currentPlayer.get_Score() + self.dice_score >= 100:
            self.Player_turn("hold")
        else:
            decision = random.randint(intelligence, safety)
            if decision != intelligence:
                safety -= 1
                self.Player_turn("roll")
            else:
                safety = 7
                self.Player_turn("hold")
