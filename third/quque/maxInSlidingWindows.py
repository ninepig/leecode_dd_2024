from collections import deque


class MonotonicQueue(object):
    def __init__(self):
        # 双端队列
        self.data = deque()

    def push(self, n):
        # 实现单调队列的push方法
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    def max(self):
        # 取得单调队列中的最大值
        return self.data[0]

    def pop(self, n):
        # 实现单调队列的pop方法
        if self.data and self.data[0] == n:
            self.data.popleft()


## 239的单调栈解法
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列实现的窗口
        window = MonotonicQueue()

        # 结果
        res = []

        for i in range(0, len(nums)):

            if i < k - 1:
                # 先填满窗口前k-1
                window.push(nums[i])
            else:
                # 窗口向前滑动
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i - k + 1])
        return res
