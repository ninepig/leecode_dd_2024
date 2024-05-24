'''
ou are given a 0-indexed integer array nums. In one operation, you can:

Choose an index i in the range 0 <= i < nums.length
Set nums[i] to nums[i] + 1 or nums[i] - 1
Return the minimum number of operations to make nums non-decreasing or non-increasing.
'''
import math
from collections import defaultdict
from typing import List

'''
dp题
很巧妙
dp[cur_level] 是到目前num为止 到达这个数 我们需要做的最小move
每次iteration，我们都需要重置这个数 
直到全部的num 全部的 level都走一遍 
类似暴力法 + memo table 
'''

def convertArray(self, nums: List[int]) -> int:
    levels = sorted(set(nums))

    def helper(nums):
        dp = defaultdict(int)
        for num in nums:
            ## 对于当前number， 我们重置所有的值
            cur_res = math.inf
            for cur_level in levels:
                ##  smaller for current level
                cur_res = min(cur_res, dp[cur_level] + abs(num - cur_level))
                dp[cur_level] = cur_res
        return dp[levels[-1]]

    return min(helper(nums), helper(nums[::-1]))