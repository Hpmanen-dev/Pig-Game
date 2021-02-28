import unittest
import player
class player_test(unittest.TestCase):

    def test_init(self):
        """Test initiating the player."""
        res = player.Player("name")
        exp = player.Player

        self.assertIsInstance(res, exp)
        
    def test_name(self):
        """Test creating a player and check players name."""
        playerOne = player.Player("name")
        res = playerOne.get_name()
        exp = "name"
        self.assertEqual(res, exp)

    def test_getScore(self):
        """Test if player score works."""
        playerOne = player.Player("name")
        res = playerOne.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_addScore(self):
        """Test if adding score works."""
        playerOne = player.Player("name")
        playerOne.add_score(10)
        res = playerOne.get_score()
        exp = 10
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()