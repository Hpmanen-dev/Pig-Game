"""Test leaderboard."""
import unittest
import os
import leaderboard


class TestDiceClass(unittest.TestCase):
    """Test game class."""

    def test_update_leaderboard(self):
        """Test update the leaderboard."""
        leaderboard.reset_leaderboard()

        leaderboard.update_leaderboard("hp", "tim", "hp")

        with open("log.txt", "r") as file:
            lines = file.readlines()
            check1 = lines[0] == "Name: hp\n"
            check2 = lines[1] == "Games: 1\n"
            check3 = lines[2] == "Wins: 1\n"

        exp = check1 is True and check2 is True and check3 is True

        self.assertTrue(exp)

        leaderboard.update_leaderboard("hp", "tim", "tim")

        with open("log.txt", "r") as file:
            lines = file.readlines()
            check1 = lines[3] == "Name: tim\n"
            check2 = lines[4] == "Games: 2\n"
            check3 = lines[5] == "Wins: 1\n"

        self.assertTrue(exp)

    def test_add_new_user(self):
        """Test adding a new user to leaderboard."""
        leaderboard.reset_leaderboard()

        leaderboard.add_new_user("n1", "n2")
        with open("log.txt", "r") as file:
            lines = file.readlines()
            check1 = lines[0] == "Name: n1\n"
            check2 = lines[1] == "Games: 1\n"
            check3 = lines[2] == "Wins: 0\n"

        exp = check1 is True and check2 is True and check3 is True

        self.assertTrue(exp)

        leaderboard.add_new_user("n2", "n2")
        with open("log.txt", "r") as file:
            lines = file.readlines()
            check1 = lines[3] == "Name: n2\n"
            check2 = lines[4] == "Games: 1\n"
            check3 = lines[5] == "Wins: 1\n"

        exp = check1 is True and check2 is True and check3 is True

        self.assertTrue(exp)

    def test_show_leaderboard(self):
        """Test display leaderboard."""
        leaderboard.update_leaderboard("hp", "tim", "hp")

        res = leaderboard.show_leaderboard()
        exp = 'done'

        self.assertEqual(res, exp)

    def test_reset_leaderboard(self):
        """Test reset leaderboard."""
        leaderboard.reset_leaderboard()
        exp = os.stat('log.txt').st_size == 0

        self.assertTrue(exp)
