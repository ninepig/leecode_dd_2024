import math
from typing import List


class Solution(object):
    def find132pattern(self, nums):
        N = len(nums)
        numsi = nums[0]
        for j in range(1, N):
            for k in range(N - 1, j, -1):
                if numsi < nums[k] and nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

# 作者：负雪明烛
# 链接：https://leetcode.cn/problems/132-pattern/solutions/676741/fu-xue-ming-zhu-cong-bao-li-qiu-jie-dao-eg78f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = -math.inf
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] < k : ## stack 此时肯定不为空
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k,stack.pop())
            stack.append(nums[i])
        return False

# 作者：宫水三叶
# 链接：https://leetcode.cn/problems/132-pattern/solutions/676970/xiang-xin-ke-xue-xi-lie-xiang-jie-wei-he-95gt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。