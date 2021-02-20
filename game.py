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
        self.Die = dice.Dice()

    def start(self):
        """Ask user if he/she wants to play single or multiplayer."""
        while True:
            print('Do you want to play "singleplayer" or "multiplayer"?')
            decision = input()
            if decision in "singleplayer" "s":
                self.singleplayer()
            elif decision in "multiplayer" "m":
                self.multiplayer()
    
    def singleplayer(self):
        """Start a singleplayer game."""
        self.Player1 = player.Player(input("Enter your name: "))
        self.Computer = computer.Computer()
        print(f"{self.Player1.get_player_name()} starts.")
        self.currentPlayer = self.Player1
        self.otherPlayer = self.Computer
        while self.currentPlayer == self.Player1:
            self.Player_turn()
        while self.currentPlayer == self.Computer:
            print("Lets go computer")
            return

    def multiplayer(self):
        """Start a multiplayer game."""
        self.Player1 = player.Player(input("Enter your name: "))
        self.Player2 = player.Player(input("Enter your name: "))
        select_player = random.randint(1, 2)
        if select_player == 1:
            self.currentPlayer = self.Player2
            self.otherPlayer = self.Player1
        else:
            self.currentPlayer = self.Player1
            self.otherPlayer = self.Player2

        while self.currentPlayer.get_Score() < 100:
            prev_player = self.currentPlayer
            self.currentPlayer = self.otherPlayer
            self.otherPlayer = prev_player
            self.Player_turn()
        print(f"{self.currentPlayer.get_player_name()} won the game!")

    def Player_turn(self):
        """Player turns."""
        turn = True
        while turn == True:
            print(f"{self.currentPlayer.get_player_name()}'s turn")
            print("Do you want to roll or hold?")
            decision = input()
            if decision in "roll" "r":
                roll = self.Die.roll()
                print(f"{self.currentPlayer.get_player_name()} rolled a {roll}")
                if roll != 1:
                    self.dice_score += roll
                else:
                    print(f"{self.currentPlayer.get_player_name()} got 0 points this round")
                    self.dice_score = 0
                    turn = False
            elif decision in "hold" "h":
                self.currentPlayer.add_Score(self.dice_score)
                print(f"{self.currentPlayer.get_player_name()} received {self.dice_score} points")
                print(f"{self.currentPlayer.get_player_name()} now have {self.currentPlayer.get_Score()} points in total!")
                self.dice_score = 0
                turn = False
