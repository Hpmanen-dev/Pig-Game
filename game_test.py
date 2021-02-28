"""Unit test for the game logic."""

from unittest.mock import patch
from unittest import mock
import unittest
import game


class TestGameClass(unittest.TestCase):
    """Test game class."""

    def test_init_default_object(self):
        the_game = game.Game()
        exp = game.Game
        self.assertIsInstance(the_game, exp)

    def test_start(self):
        """
        Test what happens if player chooses singleplayer,
        Test what happpens if player chooses multiplayer,
        Test what happens if player writes a wrong input and then a correct one,
        Test what happens if player2 tries to name themselves the same as player1.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['singleplayer', 'name1']):
            res = the_game.start()
            exp = "You chose to play singleplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=['multiplayer', 'name1', 'name2']):
            res = the_game.start()
            exp = "You chose to play multiplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=['test', 'singleplayer', 'name']):
            res = the_game.start()
            exp = "You chose to play singleplayer!"
            self.assertEqual(res, exp)

        with mock.patch('builtins.input', side_effect=["multiplayer", "name1", "name1", "name2"]):
            res = the_game.start()
            exp = "You chose to play multiplayer!"
            self.assertEqual(res, exp)

    @patch('random.randint')
    def test_roll(self, mocked_randint):
        """
        Test rolling a 1,
        Test rolling something other than 1.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['multiplayer', 'name1', 'name2']):
            the_game.start()
            mocked_randint.return_value = 1
            res = the_game.roll()
            exp = (f"{the_game.otherplayer.get_name()} "
                   "got 0 points this round")
            self.assertEqual(res, exp)
            mocked_randint.return_value = 5
            res = the_game.roll()
            exp = (f"{the_game.currentplayer.get_name()} rolled a 5")
            self.assertEqual(res, exp)

    def test_hold(self):
        """Test if player can hold to get points."""
        with mock.patch('builtins.input', side_effect=['singleplayer', 'name1']):
            the_game = game.Game()
            the_game.start()
            res = the_game.hold()
            exp = the_game.dice_score
            self.assertEqual(res, exp)

    def test_computer(self):
        """
        Test if the computer auto roll works.
        Test if the computer normal roll works.
        Test if the computer hold works.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['singleplayer', 'name']):
            the_game.start()

            self.assertEqual(the_game.computer_logic(), "auto roll")

            with mock.patch('random.randint', return_value = 2):
                the_game.computer.set_rolls(1)
                self.assertEqual(the_game.computer_logic(), "rolled")

            with mock.patch('random.randint', return_value = 1):
                the_game.computer.set_rolls(1)
                self.assertEqual(the_game.computer_logic(), "hold")

    def test_cheat(self):
        """Test cheat command."""
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['singleplayer', 'name']):
            the_game.start()
        self.assertEqual(the_game.cheat(), 'cheater')


if __name__ == '__main__':
    unittest.main()