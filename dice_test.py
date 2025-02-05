"""Test dice."""
import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """Test Dice class."""

    def test_init(self):
        """Test initiating the die."""
        res = dice.Dice()
        exp = dice.Dice
        self.assertIsInstance(res, exp)

    def test_roll(self):
        """Test if the die rolls correctly."""
        die = dice.Dice()
        res = 1 <= die.roll() <= 6
        self.assertTrue(res)

    def test_sides(self):
        """Test if the die have the specified amount of sides."""
        die = dice.Dice()
        res = die.sides
        exp = 6
        self.assertEqual(res, exp)
