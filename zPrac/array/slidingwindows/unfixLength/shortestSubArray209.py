class Solution:
    '''
    滑动窗口
    这道题因为是正数,才可以这么做, 862其实就是难度增强版
    不固定窗口
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        size = float('inf') # 或者等于 len(nums) + 1
        windows_sum = 0
        while right < len(nums):
            windows_sum += nums[right]
            while windows_sum >= target:
                size = min(right -left + 1, size)
                windows_sum -= nums[left]
                left += 1
            right += 1

        return size if size != float('inf') else 0
