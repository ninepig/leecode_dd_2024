from typing import List


'''
用dict作为额外空间 来减少循环次数
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = dict()
        for i in range(len(nums)):
            if target - nums[i] in helper:
                return [i, helper[target - nums[i]]]
            else:
                helper[nums[i]] = i

        return [0,0]