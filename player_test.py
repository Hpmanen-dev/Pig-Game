"""Test the player class."""
import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Player testclass."""

    def test_init(self):
        """Test initiating the player."""
        res = player.Player("name")
        exp = player.Player

        self.assertIsInstance(res, exp)

    def test_name(self):
        """Test creating a player and check players name."""
        player1 = player.Player("name")
        res = player1.get_name()
        exp = "name"
        self.assertEqual(res, exp)

    def test_getscore(self):
        """Test if player score works."""
        player1 = player.Player("name")
        res = player1.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_addscore(self):
        """Test if adding score works."""
        player1 = player.Player("name")
        player1.add_score(10)
        res = player1.get_score()
        exp = 10
        self.assertEqual(res, exp)
