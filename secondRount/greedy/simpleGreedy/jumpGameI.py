'''
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
https://leetcode.cn/problems/jump-game/description/
'''
from typing import List


## 贪心。 看当前点是否能reach， 如果能reach 就延申max reach pos 基于当前点的可跳跃长度
## 看看中间是否到达目标位置
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0  # 记录最远能跳到哪
        for idx, val in enumerate(nums[:-1]): # 忽略最后一个位置
            right_most = max(right_most, idx+val)  # 当前位置上，最远能跳到哪
            # 如果最远都无法超过当前位置，那肯定无法到达最后一个位置，提前结束
            if right_most <= idx:
                return False 
        return True