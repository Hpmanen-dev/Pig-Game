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
        self.computer.score = 0
        self.dice_score = 0
        loop = True
        print("Do you want to play singleplayer or multiplayer?")
        while loop:
            decision = input()
            if decision in "singleplayer":
                self.curplayer = player.Player(input("Enter your name: "))
                self.otherplayer = self.computer
                msg = "You chose to play singleplayer!"
                loop = False

            elif decision in "multiplayer":
                player1 = input("Enter your name: ")
                player2 = input("Enter your name: ")
                while player2 == player1:
                    msg = ("Can't have the same name as player one!")
                    print(msg)
                    player2 = input("Enter a new valid input: ")
                self.choose_starter(player1, player2)
                msg = "You chose to play multiplayer!"
                loop = False
            elif decision not in ("singleplayer", "multiplayer"):
                msg = ("Choose either 'singleplayer' or 'multiplayer'")
                print(msg)
        print(f"{msg}\n")
        print(f"{self.curplayer.name} starts.")
        print("Do you want to roll or hold?")
        return msg

    def choose_starter(self, player1, player2):
        """Choose which player starts."""
        select_player = random.randint(1, 2)
        print(select_player)
        if select_player == 1:
            self.curplayer = player.Player(player1)
            self.otherplayer = player.Player(player2)
            return_msg = "Player 1 starts"
        else:
            self.curplayer = player.Player(player2)
            self.otherplayer = player.Player(player1)
            return_msg = "Player 2 starts"
        return return_msg

    def roll(self):
        """Player rolls a die and adds the number to the dice score."""
        roll = self.die.roll()
        if roll != 1:
            msg = (f"{self.curplayer.name} rolled a {roll}")
            self.dice_score += roll
            print(msg)
            self.check_computer_turn()
        else:
            msg = (f"\n{self.curplayer.name} rolled a 1 and "
                   "got 0 points this round!\n")
            print(msg)
            if isinstance(self.curplayer, computer.Computer):
                self.curplayer.reset_computer()
            self.switch_player()
        return msg

    def hold(self):
        """Hold and add the dice score to players total score."""
        self.curplayer.add_score(self.dice_score)
        msg = (f"\n{self.curplayer.name} decided to hold\n"
               f"{self.curplayer.name} received "
               f"{self.dice_score} points\n"
               f"{self.curplayer.name} now have "
               f"{self.curplayer.score} points in total!\n")
        print(msg)
        self.check_winner_condition()
        self.switch_player()
        return msg

    def cheat(self):
        """Give the player 100 points to win the game."""
        self.curplayer.add_score(100)
        msg = (f"{self.curplayer.name}"
               " has gained 100 points from cheating!")
        print(msg)
        self.hold()
        return 'cheater'

    def check_winner_condition(self):
        """Check if the current player has 100 or more points."""
        if self.curplayer.score >= 100:
            print(f"Congratulations {self.curplayer.name}, You won!")
            print("Type 'restart' to play again!")
            winner = self.curplayer
            self.update_leaderboard(winner)
            self.curplayer = None
            self.otherplayer = None
            return winner.name
        return None

    def computer_logic(self):
        """How the computer works."""
        intelligence = self.computer.intelligence
        greediness = self.computer.greediness
        rolls = self.computer.rolls
        if rolls == 0:
            self.computer.inc_rolls()
            self.computer.dec_greediness()
            self.roll()
            return_msg = "auto roll"
        elif self.computer.score + self.dice_score >= 100:
            self.hold()
            return_msg = "calculated"
        else:
            random.seed()
            decision = random.randint(intelligence, greediness)
            if decision != intelligence:
                self.computer.inc_rolls()
                self.computer.dec_greediness()
                self.roll()
                return_msg = "rolled"
            else:
                self.computer.reset_computer()
                self.hold()
                return_msg = "hold"
        return return_msg

    def switch_player(self):
        """Change player turn."""
        self.curplayer, self.otherplayer = self.otherplayer, self.curplayer
        self.dice_score = 0
        if self.curplayer is not None:
            msg = (f"It is {self.curplayer.name}'s turn.")
            print(msg)
            print("Do you want to roll or hold?")
            self.check_computer_turn()

    def check_computer_turn(self):
        """Check if it is computers turn."""
        if isinstance(self.curplayer, computer.Computer):
            sleep(1)
            self.computer_logic()
            return "Computer turn"
        return None

    def update_leaderboard(self, winner):
        """Update leaderboard."""
        win = winner.name
        pl1 = self.curplayer.name
        pl2 = self.otherplayer.name
        leaderboard.update_leaderboard(pl1, pl2, win)
