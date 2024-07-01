'''
力扣315
这个题是真他妈难啊。。
多种方法
https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solutions/1308773/4chong-jie-fa-yi-wang-da-jin-pai-xu-shu-5vvds/
'''
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = SortedList()

        for i in range(n - 1, -1, -1):  # 反向遍历
            ##利用binary sort， 找到当前cnt的index， 也就是这个index左侧的数就是我们的目标数。
            cnt = sl.bisect_left(nums[i])  # 找到右边比当前值小的元素个数
            res[i] = cnt  # 记入答案
            sl.add(nums[i])  # 将当前值加入有序数组中

        return res

