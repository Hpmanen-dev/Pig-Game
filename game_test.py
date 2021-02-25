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
            assert the_game.start() == "singleplayer"

        with mock.patch('builtins.input', side_effect=['multiplayer', 'name1', 'name2']):
            assert the_game.start() == "multiplayer"

        with mock.patch('builtins.input', return_value='something'):
            assert the_game.start() == "Choose either 'singleplayer' or 'multiplayer'"

    @patch('random.randint')
    def test_roll(self, mocked_randint):
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['singleplayer', 'name1']):
            the_game.start()
            mocked_randint.return_value = 1
        assert the_game.roll() is None
        mocked_randint.return_value = 5
        assert the_game.roll() == 5
