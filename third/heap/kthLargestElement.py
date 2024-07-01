'''
这个题 这么多年了。。
1基本排序 库
2 heap
3 快排。。

'''
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nums.sort()[len(nums) - k] ## 第k大 就是
    
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        ## if we want to use heap, we need min heap , big element will be in bottom, so when we keep poping
        # heap size is k, top will be kth largest
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
            elif num > heap[0]: ## if size reach k and num is bigger than top of the heap, need pop
                heapq.heappushpop(heap,num)

        return heapq.heappop(heap)
