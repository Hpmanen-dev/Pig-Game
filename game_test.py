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

    @patch('random.randint')
    def test_roll(self, mocked_randint):
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['multiplayer', 'name1', 'name2']):
            the_game.start()
            mocked_randint.return_value = 1
            self.assertIsNone(the_game.roll())
            mocked_randint.return_value = 5
            self.assertEqual(the_game.roll(), 5)