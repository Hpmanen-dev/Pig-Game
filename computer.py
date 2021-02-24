"""This is the Computer Player."""


class Computer():
    """This is the Computer Class."""

    def __init__(self, intelligence):
        """Initiate Computer."""
        self.score = 0
        self.intelligence = intelligence
        self.name = "CPU"
        self.greediness = 7
        self.rolls = 0

    def get_score(self):
        """Get Score."""
        return self.score

    def get_name(self):
        """Get Computer Name."""
        return self.name

    def add_score(self, score):
        """Add to Computer's score."""
        self.score += score

    def set_score(self, score):
        """Set Computer's score."""
        self.score = score

    def get_intelligence(self):
        """Get intelligence."""
        return self.intelligence

    def set_intelligence(self, intelligence):
        """Change intelligence."""
        self.intelligence = intelligence

    def get_greediness(self):
        """Get the greediness of the computer."""
        return self.greediness

    def set_greediness(self, change):
        """Change greediness."""
        self.greediness = change

    def get_rolls(self):
        """Get the rolls."""
        return self.rolls

    def set_rolls(self, change):
        """Set the rolls."""
        self.rolls = change
