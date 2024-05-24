import heapq
from collections import deque
from typing import List

## https://leetcode.com/problems/sliding-window-maximum/solutions/3918847/video-ex-amazon-explains-a-solution-with-python-javascript-java-and-c/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        left = right = 0
        q = deque()

        while right < len(nums):
            ## decreasing queue
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1

        return res

    class Solution:
        '''
        初始的时候将前 k 个元素加入优先队列的二叉堆中。存入优先队列的是数组值与索引构成的元组。优先队列将数组值作为优先级。
        然后滑动窗口从第 k 个元素开始遍历，将当前数组值和索引的元组插入到二叉堆中。
        当二叉堆堆顶元素的索引已经不在滑动窗口的范围中时，即 q[0][1] <= i - k 时，不断删除堆顶元素，直到最大值元素的索引在滑动窗口的范围中。
        将最大值加入到答案数组中，继续向右滑动。
        滑动结束时，输出答案数组
        '''
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            size = len(nums)
            q = [(-nums[i], i) for i in range(k)]
            heapq.heapify(q)
            res = [-q[0][0]]

            for i in range(k, size):
                heapq.heappush(q, (-nums[i], i))
                while q[0][1] <= i - k:
                    heapq.heappop(q)
                res.append(-q[0][0])
            return res
