import heapq

from sortedcontainers import SortedList


class SolutionSortedList:
    # o(n*k) 时间复杂度
    def maxSlidingWindow(self, nums, k):
        left , right = 0 ,0
        res = []
        windows = SortedList()
        while right < len(nums):
            windows.add(nums[right])
            if right - left + 1 >= k:
               # res.append(windows[right])
               res.append(windows[-1]) # right 肯定不对.要么k 要么-1
               windows.remove(nums[left])
               left += 1
            right += 1

        return res

class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def push(self, n):
        # 将小于 n 的元素全部删除
        while self.maxq and self.maxq[-1] < n:
            self.maxq.pop()
        # 然后将 n 加入尾部
        self.maxq.append(n)

    def max(self):
        return self.maxq[0]

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)

class monoSolotion:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []

        for i in range(len(nums)):
            if i < k - 1:
                # 先填满窗口的前 k - 1
                window.push(nums[i])
            else:

                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                # 记录当前窗口的最大值
                res.append(window.max())
                # 移出旧数字
                window.pop(nums[i - k + 1])
        return res

class solutionHeap:
    def maxSlidingWindowHeap(self, nums, k):
        # inital k size heap , max queue, if biggest element move out of k, pop that.
        initial_array = [(-nums[i], i) for i in range(k)]
        heapq.heapify(initial_array)
        res = [-initial_array[0][0]]  # 头部值的value

        for i in range(k, len(nums)):
            heapq.heappush(initial_array, (-nums[i], i))
            # 这里要注意, 是 <= 是闭合区间. 也就是 比如 i = 5 k = 3 你在第2位就要pop , 因为是0 based, 3 , 4 5 位是满足窗口的
            if initial_array[0][1] <= i - k:  # top value out of k range
                heapq.heappop(initial_array)
            res.append(-initial_array[0][0])

        return res



solution = Solution()
target =[1,2,3,4,5,6,7]
print(solution.maxSlidingWindow(target,3))



