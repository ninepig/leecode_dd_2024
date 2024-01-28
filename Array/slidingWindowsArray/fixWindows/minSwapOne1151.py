'''
sliding windows 应用题
把题目转换成滑动

将数组中任何位置上的 1 组合到一起，并要求最少的交换次数。
也就是说交换之后，某个连续子数组中全是 1，数组其他位置全是 0。为此，我们可以维护一个固定长度为 1 的个数的滑动窗口，
找到滑动窗口中 0 最少的个数，这样最终交换出去的 0 最少，交换次数也最少。
'''

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = 0
        for item in data:
            if item == 1:
                window_size += 1
        if window_size == 0:
            return 0

        left, right = 0, 0
        window_count = 0
        ans = float('inf')
        while right < len(data):
            if data[right] == 0:
                window_count += 1

            if right - left + 1 >= window_size:
                ans = min(ans, window_count)
                if data[left] == 0:
                    window_count -= 1
                left += 1
            right += 1
        return ans if ans != float('inf') else 0
