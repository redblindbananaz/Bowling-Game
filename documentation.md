# Documentation for the project Bowling Game:

## Overview:

- This document will provide the steps taken to complete this assessment.
- Code will be also be commented during this project when necessary.

## Set up:

- Initial set up of the environment.
- Comment on guidelines for the Github Commits
- Creation of the MarkDown file
- Installation of the Markdown Preview('Cmd+k v' to preview)

## Debugging:

### By inspection:

- _Syntax:_ def **stickeScore**(self,rollIndex) **To** def **strikeScore**(self, rollIndex):
- _Syntax:_ result += self.**StrikeScore**(rollIndex) **To** result += self.**strikeScore**(rollIndex), Keeping consistency with camelCase convention of the original code.
- _TypeError:_ self.game.rolls(n) **To** self.game.roll(n)- calling the roll() method. rolls refer to the list
- _Syntax:_ The return result statement is indented too far to the left, causing it to be inside the for loop, which would result in an incorrect calculation of the score.
- _Syntax:_ def testOneSpare(self): already exist, the second method under that name should refer logically to all Spare.
  def **testOneSpare**(self) **To** **testAllSapre**(self)
- _Syntax:_ if frameIndex in range(10): should be:self.isStrike(rollIndex): as we chacking condition for the different scoring( strike, spare, openframe)

## Refactoring:

### By inspection:
