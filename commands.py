"""Commands used in the game."""

import cmd
import game
import computer


class Commands(cmd.Cmd):
    """This is the commands class, which includes all the commands."""

    prompt = "(Game)"
    intro = 'Please type ? or help for a list of all the commands.'

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()
        self.computer = computer.Computer(1)

    def do_rules(self, _):
        """Description of how the game works."""
        msg = (
            "Each turn, a player repeatedly rolls a die until the player"
            " decides to hold or rolls a 1.\n"
            "If the player decides to hold he/she will add the total sum"
            " of all the dice he/she has rolled during that turn to his/her total points.\n"
            "If the dice shows a 1 the player will not receive any points"
            " and his/her turn will end letting the other player roll."
        )
        print(msg)

    def do_start(self, _):
        """Start the game."""
        self.game.Start(self.computer)
    
    def do_roll(self, _):
        """Roll the dice."""
        try:
            self.game.Player_turn("roll")
        except AttributeError:
            msg =  ("You need to start before you can play.\n"
            "Please type 'Start' to start the game.")
            print(msg)
    
    def do_r(self, _):
        """Roll the dice."""
        try:
            self.game.Player_turn("roll")
        except AttributeError:
            msg =  ("You need to start before you can play.\n"
            "Please type 'start' to start the game.")
            print(msg)
    
    def do_hold(self, _):
        """Hold the points."""
        try:
            self.game.Player_turn("hold")
        except AttributeError:
            msg =  ("You need to start before you can play.\n"
            "Please type 'start' to start the game.")
            print(msg)
    
    def do_h(self, _):
        """Hold the points."""
        try:
            self.game.Player_turn("hold")
        except AttributeError:
            msg =  ("You need to start before you can play.\n"
            "Please type 'start' to start the game.")
            print(msg)
    
    def do_cheat(self, _):
        """Immediately wins the game."""
        try:
            print(f"{self.game.currentPlayer.get_name()} has gained 100 points")
            self.game.currentPlayer.add_Score(100)
            self.game.Check_winner_condition()
        except:
            msg = ("You need to start the game before you can cheat!\n"
            "Please type 'start' to start the game.")
            print(msg)
    
    def do_exit(self, _):
        """Exits the game."""
        print("See ya later!")
        exit()
    
    def do_restart(self, _):
        """Restarts the game."""
        self.do_start(_)
    
    def do_intelligence(self, arg):
        """Changes the intelligence of the computer."""
        print(f"Set the computer intelligence to {arg}")
        self.computer.set_intelligence(arg)

