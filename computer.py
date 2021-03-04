"""This is the Computer Player."""


class Computer:
    """This is the Computer Class."""

    def __init__(self, intelligence):
        """Initiate Computer."""
        self._score = 0
        self._intelligence = intelligence
        self._name = "CPU"
        self._greediness = 7
        self._rolls = 0

    def reset_computer(self):
        """Reset the computer rolls and greediness."""
        self._greediness = 7
        self._rolls = 0

    def get_score(self):
        """Get Score."""
        return self._score

    def add_score(self, score):
        """Add to Computer's score."""
        self._score += score

    def get_name(self):
        """Get Computer Name."""
        return self._name

    def get_intelligence(self):
        """Get intelligence."""
        return self._intelligence

    def set_intelligence(self, intelligence):
        """Change intelligence."""
        self._intelligence = intelligence

    def get_greediness(self):
        """Get the greediness of the computer."""
        return self._greediness

    def dec_greediness(self):
        """Decrease greediness by 1."""
        self._greediness -= 1

    def get_rolls(self):
        """Get the rolls."""
        return self._rolls

    def set_rolls(self, rolls):
        """Set the amount of rolls."""
        self._rolls = rolls

    def inc_rolls(self):
        """Increase rolls by one."""
        self._rolls += 1
