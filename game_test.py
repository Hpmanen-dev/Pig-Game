"""Unit test for the game logic."""

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
        with mock.patch('builtins.input', return_value='singleplayer'):
            assert the_game.start() == "singleplayer"

        with mock.patch('builtins.input', side_effect=['multiplayer', 'name1', 'name2']):
            assert the_game.start() == "multiplayer"

        with mock.patch('builtins.input', return_value='something'):
            assert the_game.start() == "Choose either 'singleplayer' or 'multiplayer'"
        
        with mock.patch('builtins.input', side_effect=['name', 'name', 'another name']):
            assert the_game.start() == "Can't have the same name as player one!"
    
    def test_game_loop(self):
        the_game = game.Game()
        the_game.game_loop("roll")
        
