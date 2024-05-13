#https://www.fastprep.io/problems/amazon-get-max-racers



from collections import Counter
from typing import List

'''
HackerLand Sports Club wants to send a team for a relay race. There are n racers in the group indexed from 0 to n - 1. The ith racer has a speed of speed[i] units.

The coach decided to send some contiguous subsegments of racers for the race i.e. racers with index i, i + 1, i + 2 ..., j such that each racer has the same speed in the group to ensure smooth baton transfer. To achieve the goal, the coach decided to remove some racers from the group such that the number of racers with the same speed in some contiguous segment is maximum.

Given the array, racers, and an integer k, find the maximum possible number of racers in some contiguous segment of racers with the same speed after at most k racers are removed.

'''
## sliding windows
class Solution:
  def getMaxRacers(self, speed: List[int], k: int) -> int:
    speedCounter = Counter()
    maxFreq = 0

    left = 0
    for right in range(len(speed)):
      speedCounter[speed[right]] += 1
      maxFreq = max(speedCounter[speed[right]], maxFreq)
      ##可以跳过最多k个。 来统计连续相同
      if right - left + 1 - maxFreq > k:
        speedCounter[speed[left]] -= 1
        left += 1

    return maxFreq