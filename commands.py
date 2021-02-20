"""Commands used in the game."""

import cmd
import game


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
        "Roll the dice."
        self.game.Player_turn("roll")
    
    def do_r(self, _):
        "Roll the dice."
        self.do_roll(_)
    
    def do_hold(self, _):
        "Hold the points."
        self.game.Player_turn("hold")
    
    def do_h(self, _):
        "Hold the points."
        self.do_hold(_)
    
    def do_cheat(self, _):
        """Immediately wins the game."""
        print(f"{self.game.currentPlayer.get_player_name} has gained 100 points")
        self.game.currentPlayer.add_Score(100)
        self.game.Check_winner_condition()
    
    def do_exit(self, _):
        """Exits the game."""
        print("See ya later!")
        exit()
    
    def do_restart(self, _):
        """Restarts the game."""
        self.do_start(_)
