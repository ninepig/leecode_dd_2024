import heapq
from typing import List

'''
kth largest
就是排除掉 n-k 个最小的数
heapq 默认是 最小堆
所以排除掉n-k 个最小的数
heaptop就是第k大的数


这道题最优解是quickSelect 
刷到再做吧。

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            elif num > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, num)
        return heapq.heappop(res)

    def findKthLargestBasic(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

res = [3,5,1,4,6,8]
# 最大堆
# https://www.techiedelight.com/zh/max-heap-implementation-in-python-using-heapq/
# 利用入栈的数据为负数
heapq._heapify_max(res)
print(res[0])
# 默认最小堆
heapq.heapify(res)
print(res[0])
print(heapq.heappop(res))