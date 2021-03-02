"""This is the Computer Player."""


class Computer:
    """This is the Computer Class."""

    def __init__(self, intelligence):
        """Initiate Computer."""
        self.score = 0
        self.intelligence = intelligence
        self.name = "CPU"
        self.greediness = 7
        self.rolls = 0

    def reset_computer(self):
        """Reset the computer rolls and greediness."""
        self.greediness = 7
        self.rolls = 0

    def get_score(self):
        """Get Score."""
        return self.score

    def add_score(self, score):
        """Add to Computer's score."""
        self.score += score

    def get_name(self):
        """Get Computer Name."""
        return self.name

    def get_intelligence(self):
        """Get intelligence."""
        return self.intelligence

    def set_intelligence(self, intelligence):
        """Change intelligence."""
        self.intelligence = intelligence

    def get_greediness(self):
        """Get the greediness of the computer."""
        return self.greediness

    def dec_greediness(self):
        """Decrease greediness by 1."""
        self.greediness -= 1

    def get_rolls(self):
        """Get the rolls."""
        return self.rolls

    def set_rolls(self, rolls):
        """Set the amount of rolls."""
        self.rolls = rolls

    def inc_rolls(self):
        """Increase rolls by one."""
        self.rolls += 1
