"""Test Computer."""
import unittest
import computer


class TestComputerClass(unittest.TestCase):
    """Test Computer class."""

    def test_init(self):
        """Test initiating the computer."""
        res = computer.Computer(1)
        exp = computer.Computer
        self.assertIsInstance(res, exp)

    def test_name(self):
        """Test creating computer and check its name."""
        computer1 = computer.Computer(1)
        res = computer1.get_name()
        exp = "CPU"
        self.assertEqual(res, exp)

    def test_getscore(self):
        """Test if player score works."""
        computer1 = computer.Computer(1)
        res = computer1.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_addscore(self):
        """Test if adding score works."""
        computer1 = computer.Computer(1)
        computer1.add_score(10)
        res = computer1.get_score()
        exp = 10
        self.assertEqual(res, exp)

    def test_rolls(self):
        """Test if computer rolls correctly."""
        computer1 = computer.Computer(1)
        res = computer1.get_rolls()
        exp = 0
        self.assertEqual(res, exp)

    def test_get_intelligence(self):
        """Test computers intelligence."""
        computer1 = computer.Computer(1)
        res = computer1.get_intelligence()
        exp = 1
        self.assertEqual(res, exp)

    def test_set_intelligence(self):
        """Test computers intelligence is set correctly."""
        computer1 = computer.Computer(1)
        computer1.set_intelligence(2)
        res = computer1.get_intelligence()
        exp = 2
        self.assertEqual(res, exp)

    def test_get_greediness(self):
        """Test computers greediness."""
        computer1 = computer.Computer(1)
        res = computer1.get_greediness()
        exp = 7
        self.assertEqual(res, exp)
