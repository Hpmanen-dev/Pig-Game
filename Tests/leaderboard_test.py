"""Test leaderboard."""
import unittest
import leaderboard


class TestDiceClass(unittest.TestCase):
    """Test game class."""

    def test_update_leaderboard(self):
        """Test update the leaderboard."""
        leaderboard.reset_leaderboard()

        res = leaderboard.update_leaderboard("hp", "tim", "hp")
        exp = 'Updated'

        self.assertEqual(res, exp)

        res = leaderboard.update_leaderboard("hp", "tim", "tim")
        exp = 'Updated'

        self.assertEqual(res, exp)

    def test_add_new_user(self):
        """Test adding a new user to leaderboard."""
        res = leaderboard.add_new_user("n1", "n2")
        exp = 'done'
        self.assertEqual(res, exp)

        res = leaderboard.add_new_user("n1", "n2")
        exp = 'done'
        self.assertEqual(res, exp)

    def test_show_leaderboard(self):
        """Test display leaderboard."""
        res = leaderboard.show_leaderboard()
        exp = 'done'

        self.assertEqual(res, exp)
