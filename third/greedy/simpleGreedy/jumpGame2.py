'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

这个题测试例子保证能到达 nums[n-1]

维护几个变量：当前所能达到的最远位置 end，下一步所能跳到的最远位置 max_pos，最少跳跃次数 setps。
遍历数组 nums 的前 len(nums) - 1 个元素：
每次更新第 i 位置下一步所能跳到的最远位置 max_pos。
如果索引 i 到达了 end 边界，则：更新 end 为新的当前位置 max_pos，并令步数 setps 加 1。
最终返回跳跃次数 steps。

'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end, max_pos = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)
            if max_pos < i: ## we can not reach, which against question
                return -1
            if i == end:## when we reach where we can reach, we add one step. end will be maxstep we can get
                end = max_pos
                steps += 1

        return steps
