import heapq


class Solution:
    # maxHeap to keep queue top's value is biggest
    ## 必须加入索引, 因为才能判断最大值在索引范围内.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []
        for i in range(k):
            heapq.heappush(-nums[i],i)
        res.append(-pq[0][0]) # top for first k

        size = len(nums)
        for i in range(k,size):
            # from 4th
            while pq[0][1] < i - k: # index smaller than i -k means out of windows, need pop
                heapq.heappop()
            heapq.heappush(pq,(-nums[i],i))
            res.append(-pq[0[0]])

        return res
