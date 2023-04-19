"""
Organisation of the commits format:

[Feature]: Commits that introduce new functionality or features to the codebase.
[Bugfix]: Commits that address and fix bugs or defects, syntax errors in the codebase.
[Refactoring]:Commits that improve the structure, design, or readability of the code without changing its functionality. 
[Testing]:Commits related to testing activities, such as adding or modifying test cases, fixing test failures, or improving the overall test suite.
[Style]:Commits that update coding style, formatting, or code conventions. This could include changes to indentation, line spacing, variable naming, or other style-related updates.
[Markdown]: Commits that update the Markdown file documenting the project processes

"""
# Please refer to Markdown File documenting processes for this project


class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        # Adding any attempt to roll a negative number of pins will result in a ValueError with the message "Cannot roll a negative number of pins."
        if pins < 0:
            raise ValueError("Cannot roll a negative number of pins.")
        self.rolls.append(pins)

    def score(self):
        # Helper for recursion
        return self._score_helper(0, 0)

    def _score_helper(self, frame, roll_index):
        # Use of recursion
        if frame == 10:
            return 0

        score = 0
        if self.isStrike(roll_index):
            score += 10 + self.strikeBonus(roll_index)
            score += self._score_helper(frame + 1, roll_index + 1)
        elif self.isSpare(roll_index):
            score += 10 + self.spareBonus(roll_index)
            score += self._score_helper(frame + 1, roll_index + 2)
        else:
            score += self.sumOfBallInFrame(roll_index)
            score += self._score_helper(frame + 1, roll_index + 2)

        return score

    # Definition of the 3 types of scoring

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.sumOfBallInFrame(rollIndex) == 10

    def sumOfBallInFrame(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
    # Bonuses:

    def strikeBonus(self, rollIndex):
        return self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareBonus(self, rollIndex):
        return self.rolls[rollIndex+2]
