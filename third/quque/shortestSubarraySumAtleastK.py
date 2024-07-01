'''
 https://algo.itcharge.cn/Solutions/0800-0899/shortest-subarray-with-sum-at-least-k/#%E6%80%9D%E8%B7%AF-1-%E5%89%8D%E7%BC%80%E5%92%8C-%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97

这个题是一个综合的数据结构
首先我们要想到 子数组array sum 大于k
所以 前缀和是我们可以利用的工具

然后又是shorted
所以利用滑动数组（单调队列）可以考虑。 类似239
'''
import collections
import math
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = len(nums)

        pre_sum = [0 for _ in range(size + 1)]
        for i in range(size):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        ans = math.inf
        queue = collections.deque()

        for i in range(size + 1):
            while queue and pre_sum[i] - pre_sum[queue[0]] >= k :
                ## if we found presum[i] - presum[j] >= k, we found a range
                ans = min(ans, i - queue.popleft())
            while queue and pre_sum[queue[-1]] >= pre_sum[i] :
                queue.pop()
            queue.append(i)

        if ans == math.inf:
            return -1
        return ans