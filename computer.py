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

    @property
    def score(self):
        """Get Score."""
        return self._score

    @score.setter
    def score(self, score):
        """Set Score."""
        self._score = score

    def add_score(self, score):
        """Add to Computer's score."""
        self._score += score

    @property
    def name(self):
        """Get Computer Name."""
        return self._name

    @property
    def intelligence(self):
        """Get intelligence."""
        return self._intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        """Change intelligence."""
        if 1 <= intelligence <= 3:
            print("Intelligence has been set to 3")
            self._intelligence = intelligence
        else:
            msg = ("Intelligence can only be set between 1 - 3")
            print(msg)
            return msg

    @property
    def greediness(self):
        """Get the greediness of the computer."""
        return self._greediness

    def dec_greediness(self):
        """Decrease greediness by 1."""
        self._greediness -= 1

    @property
    def rolls(self):
        """Get the rolls."""
        return self._rolls

    @rolls.setter
    def rolls(self, rolls):
        """Set the amount of rolls."""
        self._rolls = rolls

    def inc_rolls(self):
        """Increase rolls by one."""
        self._rolls += 1
