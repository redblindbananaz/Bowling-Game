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
            # Addition to the code to add requirement for if a strike onthe 10th frame:

            if frameIndex == 9:  # Check if it's the 10th frame
                # If the first roll of 10th frame is a strike
                if self.isStrike(rollIndex - 1):
                    # Add the first bonus roll score
                    result += self.rolls[rollIndex]
                    # If the second roll of 10th frame is also a strike
                    if self.isStrike(rollIndex):
                        # Add the second bonus roll score
                        result += self.rolls[rollIndex + 1]
                # If the second roll of 10th frame is a spare
                elif self.isSpare(rollIndex - 2):
                    result += self.rolls[rollIndex]  # Add the bonus roll score

        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
