from typing import List

'''
构造一个答案数组 res，长度和数组 nums 长度一致。先从左到右遍历一遍 nums 数组，将 nums[i] 左侧的元素乘积累积起来，
存储到 res 数组中。再从右到左遍历一遍，将 nums[i] 右侧的元素乘积累积起来，再乘以原本 res[i] 的值，即为 nums 中除了 nums[i] 之外的其他所有元素乘积。
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brutal force way
        # get all result , then divide by current num
        size = len(nums)
        res = [1 for _ in range(size)]
        left = 1
        ## get left side
        for idx in range(size):
            res[idx] *= left
            left *= nums[idx]

        right = 1
        for idx in range(size - 1 , -1 , -1):
            res[idx] *= right
            right *= nums[idx]

        return res