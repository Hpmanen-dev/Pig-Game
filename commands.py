"""Commands used in the game."""

import sys
import cmd
import game
import leaderboard


class Commands(cmd.Cmd):
    """This is the commands class, which includes all the commands."""

    prompt = "(Game)"
    intro = 'Please type ? or help for a list of all the commands.'

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_rules(self, _):
        # pylint: disable=no-self-use
        """Show how the game works."""
        msg = (
            "Each turn, a player repeatedly rolls a die until the player"
            " decides to hold or rolls a 1.\n"
            "If the player decides to hold he/she will add the total sum"
            " of all the dice he/she has rolled during that turn to his/her"
            "total points.\n"
            "If the dice shows a 1 the player will not receive any points"
            " and his/her turn will end letting the other player roll."
        )
        print(msg)

    def do_start(self, _):
        """Start the game."""
        self.game.start()

    def do_roll(self, _):
        """Roll the dice."""
        try:
            self.game.roll()
        except AttributeError:
            msg = ("You need to start before you can play.\n"
                   "Please type 'Start' to start the game.")
            print(msg)

    def do_r(self, _):
        """Roll the dice."""
        self.do_roll(_)

    def do_hold(self, _):
        """Hold the points."""
        try:
            self.game.hold()
        except AttributeError:
            msg = ("You need to start before you can play.\n"
                   "Please type 'start' to start the game.")
            print(msg)

    def do_h(self, _):
        """Hold the points."""
        self.do_hold(_)

    def do_cheat(self, _):
        """Immediately wins the game."""
        try:
            self.game.cheat()

        except AttributeError:
            msg = ("You need to start the game before you can cheat!\n"
                   "Please type 'start' to start the game.")
            print(msg)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Exit the game."""
        print("See ya later!")
        sys.exit()

    def do_restart(self, _):
        """Restart the game."""
        self.do_start(_)

    def do_intelligence(self, arg):
        """Change the intelligence of the computer."""
        if not arg:
            print("Try to type 'intelligence (number)'")
        try:
            int_arg = int(arg)
            self.game.computer.intelligence = int_arg
        except ValueError:
            print("Please enter an integer")
            return
        except AttributeError:
            print("You have to start a singleplayer game first.")
            return

    def do_leaderboard(self, _):
        # pylint: disable=no-self-use
        """Display leaderboard."""
        try:
            leaderboard.show_leaderboard()
        except FileNotFoundError:
            print("You have not played any games yet!")
