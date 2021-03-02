"""Test leaderboard."""
import unittest
import leaderboard


class TestDiceClass(unittest.TestCase):
    """Test game class."""

    def test_update_leaderboard(self):
        """Test update the leaderboard."""
        # Clears log.txt
        file = open("log.txt", "r+")
        file.truncate(0)
        file.close()

        res = leaderboard.update_leaderboard("hp", "tim", "hp")
        exp = 'Updated'

        self.assertEqual(res, exp)

        res = leaderboard.update_leaderboard("hp", "tim", "tim")
        exp = 'Updated'

        self.assertEqual(res, exp)

    def test_show_leaderboard(self):
        """Test display leaderboard."""
        res = leaderboard.show_leaderboard()
        exp = 'done'

        self.assertEqual(res, exp)
