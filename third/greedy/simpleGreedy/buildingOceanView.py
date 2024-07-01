## 贪心
## https://leetcode.ca/2021-04-14-1762-Buildings-With-an-Ocean-View/
## e commercial
from typing import List

'''
For index i where 0 <= i < n, the building at index i has an ocean view if and only if for all i < j < n, there is heights[i] > heights[j]. 
Obviously, the building at index n - 1 has an ocean view.
Loop over heights backwards and maintain the maximum height. For the building at index i, if heights[i] is greater than the maximum height, then the building has an ocean view.
 Update the maximum height using heights[i] after determining whether the building at index i has an ocean view.
 这道题类似贪心。 其实就是个脑经急转弯
 从后往前看。只有前面的比后面的所有的都高 才可以有view。 
 所以我们从后往前找，维护一个从后面看的最高高度。 往前loop的时候 只有前面的view 比后面最高的高的时候 才可以加到answer里 
 这个都不是单调栈。 而是贪心
'''
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        last = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > last:
                ans.append(i)
                last = heights[i]
        ans.reverse()
        return ans

