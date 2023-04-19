# Documentation for the project Bowling Game:

## Overview:

- This document will provide the steps taken to complete this assessment.
- Code will be also be commented during this project when necessary.

## Set up:

- Initial set up of the environment.
- Comment on guidelines for the Github Commits
- Creation of the MarkDown file
- Installation of the Markdown Preview ('Cmd+k v' to open the preview, once install)

## Debugging:

#### By inspection:

- _Syntax:_ `_ def stickeScore(self,rollIndex) To def strikeScore**(self, rollIndex)`

- _Syntax:_ `result += self.StrikeScore(rollIndex) To result += self.strikeScore(rollIndex)`, Keeping consistency with camelCase convention of the original code.

- _TypeError:_ `self.game.rolls(n) To self.game.roll(n)`- calling the roll() method. rolls refer to the list.

- **_Logic:_** The placement of the `return result` **statement inside the loop** in the score method cause the function to return the result after the first iteration of the loop, resulting in an incorrect score calculation. **Moving the return result statement outside the loop** ensures that the score is calculated for all frames, which is the correct logic for calculating the overall score.

- **_Logic:_** The placement of the `rollIndex +=2` **statement inside the loop** in the score method is executed in every iteration of the loop, resulting in an incorrect score calculation. **Moving it outside the loop** ensures it is execute just once for every iteration of the loop.

- _Syntax:_ def testOneSpare(self): already exist, the second method under that name should refer logically to all Spare`def testOneSpare(self) To  def testAllSapre(self)`.

#### By Testing:

- **_Logic:_** Need additional statement fo check in `def isSpare(self, rollIndex):` that is is not being a strike by adding: `and not self.isStrike(rollIndex)`

- **_Logic:_** Check if ther are at least 2 more rolls remaining in the self.rolls list after the current rollindex. If condition is True, there is enough rolls and the first expression is valid in `def strikeScore(self, rollIndex):` by adding: `if rollIndex + 2 < len(self.rolls) else 10`

- **_Logic:_** With this modification, `def spareScore(self, rollIndex):` would `return 10 + self.rolls[rollIndex+1]` for the 10th frame (index 9), where rollIndex + 2 would be out of bounds for the self.rolls list, and the calculated score would be correct so adding conditional statment correct the issue of `defectID:ErrIndex001` reported in the test case `BPTC003`

## Refactoring:

#### By inspection and Testing:

All **_Logic:_** Bugs have been fixed and the changes made to the code correcting its behavior and align it with the intended logic or rules.

#### Organise:

ErrIndex001
