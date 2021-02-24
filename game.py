"""This is the Pig Dice Game."""

from time import sleep
import random
import leaderboard
import player
import dice


class Game():
    """Game class."""

    player1 = None
    player2 = None
    computer = None
    currentplayer = None
    otherplayer = None
    winner = None
    mode = None

    def __init__(self):
        """Initiate the game."""
        self.die = dice.Dice()
        self.win_condition = 100
        self.dice_score = 0

    def start(self, computer):
        """Ask user if he/she wants to play single or multiplayer."""
        print('Do you want to play "singleplayer" or "multiplayer"?')
        while True:
            decision = input()
            if decision in "singleplayer":
                self.singleplayer(computer)
            elif decision in "multiplayer":
                self.multiplayer()
            else:
                print("Choose either 'singleplayer' or 'multiplayer'")

    def singleplayer(self, computer):
        """Initiate a singleplayer game."""
        self.mode = "Singleplayer"
        self.player1 = player.Player(input("Enter your name: "))
        self.computer = computer
        print(f"{self.player1.get_name()} starts.")
        self.currentplayer = self.player1
        self.otherplayer = self.computer
        self.computer.set_score(0)
        print("Do you want to roll or hold?")

    def multiplayer(self):
        """Initiate a multiplayer game."""
        self.mode = "Multiplayer"
        self.player1 = player.Player(input("Enter your name: "))
        self.player2 = player.Player(input("Enter your name: "))
        while self.player2.get_name() == self.player1.get_name():
            print("Can't have the same name as player one!")
            self.player2 = player.Player(input("Enter a new valid name: "))
        select_player = random.randint(1, 2)
        if select_player == 1:
            self.currentplayer = self.player1
            self.otherplayer = self.player2
        else:
            self.currentplayer = self.player2
            self.otherplayer = self.player1
        print(f"{self.currentplayer.get_name()} starts.")
        print("Do you want to roll or hold?")

    def player_turn(self, decision):
        """Player turn."""
        check = False
        if decision in "roll":
            roll = self.die.roll()
            print(f"{self.currentplayer.get_name()} rolled a {roll}")
            if roll != 1:
                self.dice_score += roll
            else:
                msg = (f"{self.currentplayer.get_name()} "
                       "got 0 points this round")
                print(msg)
                if self.currentplayer == self.computer:
                    self.computer.set_greediness(7)
                    self.computer.set_rolls(0)
                self.switch_player()
        elif decision in "hold":
            self.currentplayer.add_score(self.dice_score)
            msg = (f"{self.currentplayer.get_name()} decided to hold\n"
                   f"{self.currentplayer.get_name()} received "
                   f"{self.dice_score} points\n"
                   f"{self.currentplayer.get_name()} now have "
                   f"{self.currentplayer.get_score()} points in total!")
            print(msg)
            check = self.check_winner_condition()
            self.switch_player()
        if check is False:
            print(f"{self.currentplayer.get_name()}'s turn")
        else:
            msg = (f"The game is over {self.winner.get_name()} won!"
                   " To start a new game type 'start' or type 'exit' to exit.")
            print(msg)
            return
        if self.currentplayer == self.computer:
            sleep(1)
            self.computer_logic()

    def check_winner_condition(self):
        """Check if the current player has 100 or more points."""
        if self.currentplayer.get_score() >= 100:
            print(f"Congratulations {self.currentplayer.get_name()}, You won!")
            self.winner = self.currentplayer
            self.update_leaderboard()
            self.currentplayer = None
            self.otherplayer = None
            return True
        return False

    def computer_logic(self):
        """How the computer works."""
        intelligence = self.computer.get_intelligence()
        greediness = self.computer.get_greediness()
        rolls = self.computer.get_rolls()
        if rolls == 0:
            add_roll = rolls + 1
            self.computer.set_rolls(add_roll)
            self.player_turn("roll")
            self.computer.set_rolls(0)
        elif self.currentplayer.get_score() + self.dice_score >= 100:
            self.player_turn("hold")
        else:
            random.seed()
            decision = random.randint(intelligence, greediness)
            if decision != intelligence:
                add_roll = rolls + 1
                self.computer.set_rolls(add_roll)
                change = greediness - 1
                self.computer.set_greediness(change)
                self.player_turn("roll")
            else:
                self.computer.set_greediness(7)
                self.computer.set_rolls(0)
                self.player_turn("hold")

    def switch_player(self):
        """Change player turn."""
        prev_player = self.currentplayer
        self.currentplayer = self.otherplayer
        self.otherplayer = prev_player
        self.dice_score = 0

    def update_leaderboard(self):
        """Update leaderboard."""
        try:
            win = self.winner
            pl1 = self.currentplayer
            pl2 = self.otherplayer
            leaderboard.update_leaderboard(pl1, pl2, win)
        except AttributeError:
            print("Something went wrong, could not update logfile.")
            return
