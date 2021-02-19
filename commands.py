import cmd
import game

class commands(cmd.Cmd):
    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()