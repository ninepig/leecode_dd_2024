'''
题目要求在打乱顺序后，数组的所有排列应该是等可能的。对于长度为 n 的数组，我们可以把问题转换为：分别在 n 个位置上，选择填入某个数的概率是相同。

python 技巧题

'''
from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        self.shuffle_nums = self.nums.copy()
        for i in range(len(self.shuffle_nums)):
            swap_index = random.randrange(i, len(self.shuffle_nums))
            self.shuffle_nums[i], self.shuffle_nums[swap_index] = self.shuffle_nums[swap_index], self.shuffle_nums[i]
        return self.shuffle_nums