import heapq

from LinkedList import List

'''
k大 就用最小堆
全部加入堆
pop出k-1个
剩下的就是第k大
出去的是k-1个最小的
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.hea) > k :
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

