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
            exp = (f"\n{the_game.otherplayer.name} rolled a 1 and "
                   "got 0 points this round!\n")
            self.assertEqual(res, exp)
            mocked_randint.return_value = 5
            res = the_game.roll()
            exp = (f"{the_game.curplayer.name} rolled a 5")
            self.assertEqual(res, exp)

    def test_hold(self):
        """Test if player can hold to get points."""
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game = game.Game()
            the_game.start()
            res = the_game.hold()
            exp = (f"\n{the_game.curplayer.name} decided to hold\n"
                   f"{the_game.curplayer.name} received "
                   f"{the_game.dice_score} points\n"
                   f"{the_game.curplayer.name} now have "
                   f"{the_game.curplayer.score} points in total!\n")
            self.assertEqual(res, exp)

    def test_computer(self):
        """Test Computer Logic.

        Test if the computer auto roll works as intended.
        Test if the computer normal roll works as intended.
        Test if the computer hold works as intended.
        Test if the computer calculated works as intended.
        """
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game.start()

            self.assertEqual(the_game.computer_logic(), "auto roll")

            with mock.patch('random.randint', return_value=2):
                the_game.computer.inc_rolls()
                self.assertEqual(the_game.computer_logic(), "rolled")

            computer_int = the_game.computer.intelligence
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
            the_game.cheat()
            res = the_game.curplayer.score == 100
        self.assertTrue(res)

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

    def test_check_winner(self):
        """Test checking for a winner."""
        the_game = game.Game()
        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game.start()
            res = the_game.check_winner_condition()
            self.assertIsNone(res)

            the_game.curplayer.add_score(100)
            res = the_game.check_winner_condition()
            exp = "n1"
            self.assertEqual(res, exp)

    def test_switch_player(self):
        """Test switching player turn."""
        the_game = game.Game()

        with mock.patch('builtins.input', side_effect=['multi', 'n1', 'n2']):
            the_game.start()
            second_player = the_game.otherplayer.name
            the_game.switch_player()
            res = second_player
            exp = the_game.curplayer.name
            self.assertEqual(res, exp)

    def test_check_computer_turn(self):
        """Test checking if it is computers turn."""
        the_game = game.Game()

        with mock.patch('builtins.input', side_effect=['single', 'n1']):
            the_game.start()
            res = the_game.check_computer_turn()
            self.assertIsNone(res)
