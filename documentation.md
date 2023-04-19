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

- **_Logic:_** `def testNegatifValue(self):
  with self.assertRaises(ValueError):
  `self.game.roll(-5)` Failed test.
  No implementation of handling errors due to negative values in the bowling game. Changes have been made with the following implementation:
  ```
  def roll(self, pins):
    Adding any attempt to roll a negative number of pins will result in a ValueError with the message "Cannot roll a negative number of pins.
    if pins < 0:
        raise ValueError("Cannot roll a negative number of pins.")
    self.rolls.append(pins)
  ```

## Refactoring:

##### By inspection and Testing:

All **_Logic:_** Bugs have been fixed and the changes made to the code correcting its behavior and align it with the intended logic or rules.

##### Eliminate Dead code:

`if frameIndex in range(10):` is unnecessary because it only checks whether the frameIndex is between 0 and 9, which is always True. The statement was intended to ensure that the extra roll in the 10th frame is not counted in the score, but it does not achieve that purpose.

`for frameIndex in range(10):` Variable is now unused and not necessary, can be replaced by `for _ in range(10):`

##### Reuse of code:

`return self.rolls[rollIndex] + self.rolls[rollIndex+1]` is defined in :
`def frameScore(self, rollIndex):`
`return self.rolls[rollIndex] + self.rolls[rollIndex + 1]`
So This part of the code defining roll combination bonus and scores can be arrange as the following:

````
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
        return self.rolls[rollIndex+2]```
````

followed by:

##### Recursion:

```
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
```

`score(self)`

- This function calculates the score of the bowling game. It uses a helper function `_score_helper` that is called recursively to calculate the score for each frame in the game.

`_score_helper(self, frame, roll_index)`

- This is the helper function that is called recursively by the score function to calculate the score for each frame in the game. It takes two arguments: frame, which represents the current frame being scored, and roll_index, which represents the index of the current roll being scored.

```
if self.isStrike(roll_index):
            score += 10 + self.strikeBonus(roll_index)
            score += self._score_helper(frame + 1, roll_index + 1)
```

- `if self.isStrike(roll_index):` - This line checks whether the current roll (indicated by roll_index) is a strike. If it is, then the following actions are taken:
- `score += 10 + self.strikeBonus(roll_index)` - This line adds 10 to the score for the current frame (since a strike is worth 10 points on its own), and then adds the "strike bonus" to the score. The strike bonus is the sum of the next two rolls, and is calculated using the strikeBonus method.
- `score += self._score_helper(frame + 1, roll_index + 1)` - This line recursively calls the \_score_helper method with an updated frame and roll_index. Since a strike counts as a complete frame on its own, the frame variable is incremented by 1. And since a strike only uses one roll, the roll_index variable is incremented by 1 as well. The result of this recursive call is added to the score.
- Same logic for the other conditionals
