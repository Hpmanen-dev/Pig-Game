"""This is the Pig Dice Game."""

import player
import computer
import dice
import random


class Game():
    """Game class."""

    Player1 = None
    Player2 = None
    Computer = None
    currentPlayer = None
    otherPlayer = None
    win_condition = 100
    dice_score = 0

    def __init__(self):
        """Initiate the game."""
        self.Die = dice.Dice()

    def start(self):
        """Ask user if he/she wants to play single or multiplayer."""
        print('Do you want to play "singleplayer" or "multiplayer"?')
        decision = input()
        if decision in "singleplayer" "s":
            self.singleplayer()
        elif decision in "multiplayer" "m":
            self.multiplayer()
    
    def singleplayer(self):
        """Initiate a singleplayer game."""
        self.Player1 = player.Player(input("Enter your name: "))
        self.Computer = computer.Computer()
        print(f"{self.Player1.get_player_name()} starts.")
        self.currentPlayer = self.Player1
        self.otherPlayer = self.Computer

    def multiplayer(self):
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
        print(f"{self.currentPlayer.get_player_name()} starts.")
        print("Do you want to roll or hold?")

    def Player_turn(self, decision):
        """Player turns."""
        prev_player = self.currentPlayer
        if decision in "roll":
            roll = self.Die.roll()
            print(f"{self.currentPlayer.get_player_name()} rolled a {roll}")
            if roll != 1:
                self.dice_score += roll
            else:
                print(f"{self.currentPlayer.get_player_name()} got 0 points this round")
                self.dice_score = 0
                self.currentPlayer = self.otherPlayer
                self.otherPlayer = prev_player
        elif decision in "hold":
            self.currentPlayer.add_Score(self.dice_score)
            print(f"{self.currentPlayer.get_player_name()} received {self.dice_score} points")
            print(f"{self.currentPlayer.get_player_name()} now have {self.currentPlayer.get_Score()} points in total!")
            self.currentPlayer = self.otherPlayer
            self.otherPlayer = prev_player
            self.dice_score = 0
        print(f"{self.currentPlayer.get_player_name()}'s turn")
