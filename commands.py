"""Commands used in the game."""

import cmd
import game
import player


class Commands(cmd.Cmd):
    """This is the commands class, which includes all the commands."""

    prompt = "(Game)"
    intro = 'Please type ? or help for a list of all the commands.'

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

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
        self.game.start()
    
    def do_roll(self, _):
        self.game.Player_turn("roll")
    
    def do_r(self, _):
        self.do_roll(_)
    
    def do_hold(self, _):
        self.game.Player_turn("hold")
    
    def do_h(self, _):
        self.do_hold(_)
