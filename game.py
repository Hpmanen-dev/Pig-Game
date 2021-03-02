"""This is the Pig Dice Game."""

from time import sleep
import random
import leaderboard
import player
import dice
import computer


class Game():
    """Game class."""

    def __init__(self):
        """Initiate the game."""
        self.die = dice.Dice()
        self.dice_score = 0
        self.curplayer = None
        self.otherplayer = None
        self.computer = computer.Computer(1)

    def start(self):
        """Decide gamemode, singleplayer or multiplayer."""
        self.dice_score = 0
        loop = True
        print("Do you want to play singleplayer or multiplayer?")
        while loop:
            decision = input()
            if decision in "singleplayer":
                self.curplayer = player.Player(input("Enter your name: "))
                self.otherplayer = self.computer
                self.otherplayer.score = 0
                msg = "You chose to play singleplayer!"
                loop = False

            elif decision in "multiplayer":
                player1 = input("Enter your name: ")
                player2 = input("Enter your name: ")
                while player2 == player1:
                    msg = ("Can't have the same name as player one!")
                    print(msg)
                    player2 = input("Enter a new valid input: ")
                select_player = random.randint(1, 2)
                if select_player == 1:
                    self.curplayer = player.Player(player1)
                    self.otherplayer = player.Player(player2)
                else:
                    self.curplayer = player.Player(player2)
                    self.otherplayer = player.Player(player1)
                msg = "You chose to play multiplayer!"
                loop = False
            elif decision not in ("singleplayer", "multiplayer"):
                msg = ("Choose either 'singleplayer' or 'multiplayer'")
                print(msg)
        print(f"{msg}\n")
        print(f"{self.curplayer.get_name()} starts.")
        print("Do you want to roll or hold?")
        return msg

    def roll(self):
        """Player rolls a die and adds the number to the dice score."""
        roll = self.die.roll()
        if roll != 1:
            msg = (f"{self.curplayer.get_name()} rolled a {roll}")
            self.dice_score += roll
            print(msg)
            if isinstance(self.curplayer, computer.Computer):
                sleep(1)
                self.computer_logic()
            return msg
        else:
            msg = (f"{self.curplayer.get_name()} rolled a 1 and "
                   "got 0 points this round!")
            if isinstance(self.curplayer, computer.Computer):
                print(msg)
                self.curplayer.set_greediness(7)
                self.curplayer.set_rolls(0)
            try:
                self.switch_player()
            finally:
                return msg

    def hold(self):
        """Hold and add the dice score to players total score."""
        self.curplayer.add_score(self.dice_score)
        msg = (f"{self.curplayer.get_name()} decided to hold\n"
               f"{self.curplayer.get_name()} received "
               f"{self.dice_score} points\n"
               f"{self.curplayer.get_name()} now have "
               f"{self.curplayer.get_score()} points in total!")
        if isinstance(self.curplayer, computer.Computer):
            print(msg)
            self.curplayer.set_greediness(7)
            self.curplayer.set_rolls(0)
        self.switch_player()
        self.check_winner_condition()
        return msg

    def cheat(self):
        """Give the player 100 points to win the game."""
        self.curplayer.add_score(100)
        msg = (f"{self.curplayer.get_name()}"
               " has gained 100 points from cheating!")
        print(msg)
        self.check_winner_condition()
        return 'cheater'

    def check_winner_condition(self):
        """Check if the cur player has 100 or more points."""
        if self.curplayer.get_score() >= 100:
            print(f"Congratulations {self.curplayer.get_name()}, You won!")
            winner = self.curplayer
            self.update_leaderboard(winner)
            self.curplayer = None
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
            return "auto roll"
        elif self.computer.get_score() + self.dice_score >= 100:
            self.hold()
            return "calculated"
        else:
            random.seed()
            decision = random.randint(intelligence, greediness)
            if decision != intelligence:
                add_roll = rolls + 1
                self.computer.set_rolls(add_roll)
                change = greediness - 1
                self.computer.set_greediness(change)
                self.roll()
                return "rolled"
            else:
                self.hold()
                return "hold"

    def switch_player(self):
        """Change player turn."""
        self.curplayer, self.otherplayer = self.otherplayer, self.curplayer
        self.dice_score = 0
        msg = (f"It is {self.curplayer.get_name()}'s turn.")
        print(msg)
        print("Do you want to roll or hold?")
        if isinstance(self.curplayer, computer.Computer):
            sleep(1)
            self.computer_logic()
        return 'Player switched'

    def update_leaderboard(self, winner):
        """Update leaderboard."""
        win = winner.get_name()
        pl1 = self.curplayer.get_name()
        pl2 = self.otherplayer.get_name()
        leaderboard.update_leaderboard(pl1, pl2, win)
