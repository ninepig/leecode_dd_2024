import heapq


class Solution:
    '''經典'''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        # 最小堆變成最大堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        #反向輸出最大堆 用負數
        res = [-q[0][0]]

        for i in range(k, size):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res
