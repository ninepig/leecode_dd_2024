import collections
'''
sliding windows 题  用两个dequeue来做
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
'''
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        minDeq = collections.deque()
        maxDeq = collections.deque()

        res = 0
        start = 0
        for end in range(len(nums)):
            num = nums[end]
            while len(minDeq) > 0 and num < minDeq[-1]:
                minDeq.pop()

            while len(maxDeq) > 0 and num > maxDeq[-1]:
                maxDeq.pop()

            minDeq.append(num)
            maxDeq.append(num)

            while not abs(minDeq[0] - maxDeq[0]) <= limit and start <= end:
                if minDeq[0] == nums[start]:
                    minDeq.popleft()

                if maxDeq[0] == nums[start]:
                    maxDeq.popleft()

                start += 1

            res = max(res, end - start + 1)

        return res