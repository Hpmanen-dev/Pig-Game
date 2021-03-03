"""Unit test for the game logic."""

from unittest.mock import patch
from unittest import mock
import unittest
import game
import player


class TestGameClass(unittest.TestCase):
    """Test game class."""

    def test_init_default_object(self):
        """Test initiating the game."""
        the_game = game.Game()
        exp = game.Game
        self.assertIsInstance(the_game, exp)

    def test_start(self):
        """.

        Test what happens if player chooses singleplayer,
        Test what happpens if player chooses multiplayer,
        Test what happens if player writes a wrong input
        and then a correct one,
        Test what happens if player2
        tries to name themselves the same as player1.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['singleplayer', 'n1']):
            res = the_game.start()
            exp = "You chose to play singleplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=['multi', 'n1', 'n2']):
            res = the_game.start()
            exp = "You chose to play multiplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=['test', 'single', 'n']):
            res = the_game.start()
            exp = "You chose to play singleplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=["m", "n1", "n1", "n2"]):
            res = the_game.start()
            exp = "You chose to play multiplayer!"
            self.assertEqual(res, exp)

    @patch('random.randint')
    def test_roll(self, mocked_randint):
        """Test rolling a die.

        Test rolling a 1,
        Test rolling something other than 1.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['multi', 'n1', 'n2']):
            the_game.start()
            mocked_randint.return_value = 1
            res = the_game.roll()
            exp = (f"{the_game.otherplayer.get_name()} rolled a 1 and "
                   "got 0 points this round!")
            self.assertEqual(res, exp)
            mocked_randint.return_value = 5
            res = the_game.roll()
            exp = (f"{the_game.curplayer.get_name()} rolled a 5")
            self.assertEqual(res, exp)

    def test_hold(self):
        """Test if player can hold to get points."""
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game = game.Game()
            the_game.start()
            res = the_game.hold()
            exp = (f"{the_game.curplayer.get_name()} decided to hold\n"
                   f"{the_game.curplayer.get_name()} received "
                   f"{the_game.dice_score} points\n"
                   f"{the_game.curplayer.get_name()} now have "
                   f"{the_game.curplayer.get_score()} points in total!")
            self.assertEqual(res, exp)

    def test_computer(self):
        """Test Computer Logic.

        Test if the computer auto roll works.
        Test if the computer normal roll works.
        Test if the computer hold works.
        Test if the computer calculated works.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game.start()

            self.assertEqual(the_game.computer_logic(), "auto roll")

            with mock.patch('random.randint', return_value=2):
                the_game.computer.inc_rolls()
                self.assertEqual(the_game.computer_logic(), "rolled")

            with mock.patch('random.randint', return_value=1):
                the_game.computer.set_rolls(0)
                self.assertEqual(the_game.computer_logic(), "auto roll")

            computer_int = the_game.computer.get_intelligence()
            with mock.patch('random.randint', return_value=computer_int):
                the_game.computer.inc_rolls()
                self.assertEqual(the_game.computer_logic(), "hold")

            the_game.computer.inc_rolls()
            the_game.computer.add_score(100)
            self.assertEqual(the_game.computer_logic(), "calculated")

    def test_cheat(self):
        """Test cheat command."""
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game.start()
        self.assertEqual(the_game.cheat(), 'cheater')

    @patch('random.randint')
    def test_choose_starter(self, mocked_randint):
        """Test chosing which player starts."""
        the_game = game.Game()
        player1 = player.Player("Test1")
        player2 = player.Player("Test2")

        mocked_randint.return_value = 1
        res = the_game.choose_starter(player1, player2)
        exp = "Player 1 starts"
        self.assertEqual(res, exp)

        mocked_randint.return_value = 2
        res = the_game.choose_starter(player1, player2)
        exp = "Player 2 starts"
        self.assertEqual(res, exp)
