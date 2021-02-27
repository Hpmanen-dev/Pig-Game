"""This is the Pig Dice Game."""

from time import sleep
import random
import leaderboard
import player
import dice
import computer


class Game():
    """Game class."""

    player1 = None
    player2 = None
    computer = None
    currentplayer = None
    otherplayer = None

    def __init__(self):
        """Initiate the game."""
        self.die = dice.Dice()
        self.dice_score = 0

    def start(self):
        """Decide gamemode, single or multiplayer."""
        self.dice_score = 0
        loop = True
        print("Do you want to play singleplayer or multiplayer?")
        while loop:
            decision = input()
            if decision in "singleplayer":
                self.player1 = player.Player(input("Enter your name: "))
                self.computer = computer.Computer(1)
                self.currentplayer = self.player1
                self.otherplayer = self.computer
                self.computer.set_score(0)
                msg = "You chose to play singleplayer!"
                loop = False

            elif decision in "multiplayer":
                self.player1 = player.Player(input("Enter your name: "))
                self.player2 = player.Player(input("Enter your name: "))
                while self.player2.get_name() == self.player1.get_name():
                    msg = ("Can't have the same name as player one!")
                    print(msg)
                    self.player2 = player.Player(input("Enter a new valid name: "))
                select_player = random.randint(1, 2)
                if select_player == 1:
                    self.currentplayer = self.player1
                    self.otherplayer = self.player2
                else:
                    self.currentplayer = self.player2
                    self.otherplayer = self.player1
                msg = "You chose to play multiplayer!"
                loop = False
            elif decision not in ("singleplayer", "multiplayer"):
                msg = ("Choose either 'singleplayer' or 'multiplayer'")
                print(msg)
        print(f"{msg}\n")
        print(f"{self.currentplayer.get_name()} starts.")
        print("Do you want to roll or hold?")
        return msg

        

    def roll(self):
        roll = self.die.roll()
        msg = (f"{self.currentplayer.get_name()} rolled a {roll}")
        print(msg)
        if roll != 1:
            self.dice_score += roll
            if self.currentplayer == self.computer:
                sleep(1)
                self.computer_logic()
        else:
            msg = (f"{self.currentplayer.get_name()} "
                    "got 0 points this round")
            print(msg)
            if self.currentplayer == self.computer:
                self.computer.set_greediness(7)
                self.computer.set_rolls(0)
            self.switch_player()
        return msg
    

    def hold(self):
        self.currentplayer.add_score(self.dice_score)
        msg = (f"{self.currentplayer.get_name()} decided to hold\n"
                f"{self.currentplayer.get_name()} received "
                f"{self.dice_score} points\n"
                f"{self.currentplayer.get_name()} now have "
                f"{self.currentplayer.get_score()} points in total!")
        print(msg)
        if self.currentplayer == self.computer:
            self.computer.set_greediness(7)
            self.computer.set_rolls(0)
        self.check_winner_condition()
        self.switch_player()
        return self.dice_score
    

    def cheat(self):
        self.currentplayer.add_score(100)
        msg = (f"{self.currentplayer.get_name()}"
            " has gained 100 points from cheating!")
        print(msg)
        self.check_winner_condition()
        return 'cheater'


    def check_winner_condition(self):
        """Check if the current player has 100 or more points."""
        if self.currentplayer.get_score() >= 100:
            print(f"Congratulations {self.currentplayer.get_name()}, You won!")
            winner = self.currentplayer
            self.update_leaderboard(winner)
            self.currentplayer = None
            self.otherplayer = None
            return winner
        return None

    def computer_logic(self):
        """How the computer works."""
        intelligence = self.computer.get_intelligence()
        greediness = self.computer.get_greediness()
        rolls = self.computer.get_rolls()
        if rolls == 0:
            add_roll = rolls + 1
            self.computer.set_rolls(add_roll)
            self.roll()
            msg = "auto roll"
        elif self.currentplayer.get_score() + self.dice_score >= 100:
            msg = 'Calculated'
        else:
            random.seed()
            decision = random.randint(intelligence, greediness)
            if decision != intelligence:
                add_roll = rolls + 1
                self.computer.set_rolls(add_roll)
                change = greediness - 1
                self.computer.set_greediness(change)
                self.roll()
                msg = "rolled"
            else:
                self.hold()
                msg = "hold"
        return msg

    def switch_player(self):
        """Change player turn."""
        prev_player = self.currentplayer
        self.currentplayer = self.otherplayer
        self.otherplayer = prev_player
        self.dice_score = 0
        msg = (f"It is {self.currentplayer.get_name()}'s turn.")
        print(msg)
        print("Do you want to roll or hold?")
        if self.currentplayer == self.computer:
            sleep(1)
            self.computer_logic()
        return 'Player switched'

    def update_leaderboard(self, winner):
        """Update leaderboard."""
        win = winner
        pl1 = self.currentplayer
        pl2 = self.otherplayer
        leaderboard.update_leaderboard(pl1, pl2, win)
