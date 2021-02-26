import unittest
import player
class player_test(unittest.TestCase):

    def test_init(self):
        res = player.Player("name")
        exp = player.Player

        self.assertIsInstance(res, exp)
        
    def test_name(self):
        playerOne = player.Player("name")
        res = playerOne.get_name()
        exp = "name"
        self.assertEqual(res, exp)

    def test_getScore(self):
        playerOne = player.Player("name")
        res = playerOne.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_addScore(self):
        playerOne = player.Player("name")
        playerOne.add_score(10)
        res = playerOne.get_score()
        exp = 10
        self.assertEqual(res, exp)
        