import math
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        # k present 2 in 132 pattern
        k = -math.inf
        ## loop from back , num[i] represet 1 in pattern
        ## using a monotonic queue, if queue is not empty, which means, top of queue is 3 ,
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] < k:
                return True
            ## we found a value bigger than top of stack, which means, we must have a 3 bigger than 2
            while stack and stack[-1] < nums[i]:
                k = max(k,stack.pop())
            stack.append(nums[i])
        return False

# 作者：宫水三叶
# 链接：https://leetcode.cn/problems/132-pattern/solutions/676970/xiang-xin-ke-xue-xi-lie-xiang-jie-wei-he-95gt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。