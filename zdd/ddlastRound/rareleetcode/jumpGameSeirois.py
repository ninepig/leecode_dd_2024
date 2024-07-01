## 是否可以到达最后
## 这个就是个贪心
from collections import deque
from functools import lru_cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if not nums or len(nums) == 0 : return True
        max_can_reach = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= max_can_reach:
                max_can_reach = curr + nums[curr]
            if curr == max_can_reach: ## can not move any more
                break
        return  max_can_reach >= len(nums) - 1


    '''
    We start travering the array from start
    While traversing, we keep a track on maximum reachable index and update it accordingly.
    If we reach the previous reachable index, this implies we have reached this index with current jumps and now we can reach the next maximum possible index by current jumps+1 jumps and update the previous reachable index to maximum reachable index. Now, if updated previous reachable index is greater than equal to last index, just return the jump count.
    class Solution:
    贪心
'''
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0

        reachableIndex = 0
        previousReachableIndex = 0
        jump = 0

        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]

            if curr == previousReachableIndex:
                jump += 1
                previousReachableIndex = reachableIndex
                if previousReachableIndex >= len(nums) - 1:
                    return jump

        return jump


    '''
    You are given a 0-indexed integer array nums and an integer k.

    You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
    
    You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
    
    Return the maximum score you can get.
    关键是这个值可以是负的 所以要找范围最大值
    
    dp + decreasing queue  （sliding windows maxmum）
    
    dp[0] = num[0]
    dp[i] = max (dp[ i - k] --- dp[i-1]) + num[i]
    '''

    # Author: Huahua 52/58 Passed (TLE)
    class Solution:
        def maxResult(self, nums: list[int], k: int):
            @lru_cache(None)
            def dp(i: int):
                return nums[0] if i == 0 else nums[i] + max(dp(j) for j in range(max(0, i - k), i))

            return dp(len(nums) - 1)

        ## we need find a way to improve, using a deque to do a sliding windows max way
        def maxResultQueue(self, nums: list[int], k: int) -> int:
            n = len(nums)
            deq = deque()
            deq.append(0)
            dp = [0] * n
            dp[0] = nums[0]
            for i in range(1, n):
                dp[i] = nums[i] + dp[deq[0]]  # Maximum Value in deque within that window
                if deq[0] < i - k + 1:
                    deq.popleft()  # Check whether left bound is still accessible or not
                while deq and dp[deq[-1]] < dp[i]:
                    deq.pop()  # Update deque with current i'th element
                deq.append(i)
            return dp[-1]  # Return total score