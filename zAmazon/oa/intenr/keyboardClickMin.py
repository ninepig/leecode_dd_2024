# https://www.fastprep.io/problems/amazon-find-minimum-keypad-click-count
# 国内
'''

A recently launched supplemental typing keypad gained significant popularity on Amazon Shopping due to its flexibility.

This keypad can be connected to any electronic device and has 9 buttons, where each button can have up to 3 lowercase English letters. The buyer has the freedom to choose which letters to place on a button while ensuring that the arrangement is valid. A keypad design is said to be valid if:

All 26 letters of the English alphabet exist on the keypad.
Each letter is mapped to exactly one button.
A button has at most 3 letters mapped to it.

'''

from collections import defaultdict
class Solution:
  def findMinimumKeypadClickCount(self, letters: str) -> int:
    map = defaultdict(int)
    for i in letters:
      map[i] += 1

    sort_map = sorted(map.items(), key = lambda x: -x[1])
    res = 0
    for i in range(len(sort_map)):
      if i>=0 and i <=8:
        res += 1*sort_map[i][1]
      elif i>8 and i <=17:
        res += 2*sort_map[i][1]
      else:
        res += 3*sort_map[i][1]
    return res