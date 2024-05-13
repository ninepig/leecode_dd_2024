#https://www.fastprep.io/problems/amazon-find-unique-values
'''
There are n developers working at Amazon where the ith developer has the experience points experience[i].
The company decided to pair the developers by iteratively pairing the developers with the highest
 and lowest remaining experience points for a hackathon. The combined experience of a pair is the average of the experience points of the two developers. Find the number of unique values among the combined experience of the pairs formed.

Function Description

Complete the function findUniqueValues in the editor below.

findUniqueValues has the following parameter:

int experience[n]: the experience points for each developer
'''
from typing import List

'''
这个题比较简单
就是sort 以后前后相加 放到set就可以'''

class Solution:
  def findUniqueValues(self, experience: List[int]) -> int:
    experience.sort()
    experienceSet = set()

    left, right = 0, len(experience) - 1
    while left < right:
      experienceSet.add((experience[left] + experience[right]) / 2)
      left += 1
      right -= 1

    return len(experienceSet)

sol = Solution()
ex = [1, 100, 10, 1000]
print(sol.findUniqueValues(ex))