'''
很有意思的应用题
类似1423
将 x 减到 0 的最小操作数可以转换为求和等于 sum(nums) - x 的最长连续子数组长度。我们可以维护一个区间和为 sum(nums) - x 的滑动窗口，求出最长的窗口长度。具体做法如下：

令 target = sum(nums) - x，使用 max_len 维护和等于 target 的最长连续子数组长度。然后用滑动窗口 window_sum 来记录连续子数组的和，设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中的和刚好等于 target。

一开始，left、right 都指向 0。
向右移动 right，将最右侧元素加入当前窗口和 window_sum 中。
如果 window_sum > target，则不断右移 left，缩小滑动窗口长度，并更新窗口和的最小值，直到 window_sum <= target。
如果 window_sum == target，则更新最长连续子数组长度。
然后继续右移 right，直到 right >= len(nums) 结束。
输出 len(nums) - max_len 作为答案。
注意判断题目中的特殊情况
'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        size = len(nums)
        if target < 0:
            return -1
        if target == 0:
            return size
        left, right = 0, 0
        window_sum = 0
        max_len = float('-inf')

        while right < size:
            window_sum += nums[right]

            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                max_len = max(max_len, right - left + 1)
            right += 1
        return len(nums) - max_len if max_len != float('-inf') else -1
