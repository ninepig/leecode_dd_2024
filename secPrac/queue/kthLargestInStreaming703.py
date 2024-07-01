import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topK = k
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.minHeap,num)
            ## pq，只要保证有k个元素就行，超过了就把顶pop就行。这样可以维护k个
            if len(self.minHeap) > k :
                heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.topK :
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

