import math


class Solution:
    '''
    珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，
她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

dd 题
https://leetcode.com/discuss/interview-question/2028170/doordash-phone-screen
    '''
    # binary search nlogn
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        while left < right :
            mid = left + (right - left) // 2
            if self.canEat(mid,piles) < h:
                left = mid + 1
            else:
                right = mid

        return left

    def canEat(self, speed, piles):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed # equal = math.ceiling

        return hours