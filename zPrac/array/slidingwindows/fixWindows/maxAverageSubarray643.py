class Solution:
    # 最大平均数， size k
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        res = float('-inf')
        windows_sum = 0
        while right < len(nums):
            windows_sum += nums[right]
            if right - left + 1 >= k: # meet windows size
                res = max(res, windows_sum/k)
                left += 1
                windows_sum -= nums[left]
            right += 1

        return res