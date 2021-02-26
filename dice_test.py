import unittest
import dice

class dice_test(unittest.TestCase):

    def test_init(self):
        res = dice.Dice()
        exp = dice.Dice

        self.assertIsInstance(res, exp)
        
    def test_roll(self):
        die = dice.Dice()
        res = 1 <= die.roll() <= 6
        self.assertTrue(res)

    def test_sides(self):
        die = dice.Dice()
        side = die.get_sides()
        exp = 6
        self.assertEqual(side, exp)