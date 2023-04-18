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
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2

        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        # Need to add conditional for not being a strike
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10 and not self.isStrike(rollIndex)

    def strikeScore(self, rollIndex):
        # Check if ther are at least 2 more rolls remaining in the self.rolls list after the current rollindex. If condition is True, there is enough rolls and the first expression is valid. That was the the cause of the indexing error.
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]if rollIndex + 2 < len(self.rolls) else 10

    def spareScore(self, rollIndex):
        if rollIndex + 2 < len(self.rolls):
            return 10 + self.rolls[rollIndex+2]
        else:
            return 10 + self.rolls[rollIndex+1]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
