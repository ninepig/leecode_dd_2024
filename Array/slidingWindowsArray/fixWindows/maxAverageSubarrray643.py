class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left , right = 0 , 0
        windows_sum = 0
        ans = float('-inf') # floating number
        while right < len(nums):
            windows_sum += nums[right]

            # k windows
            if right - left + 1 >= k:
                # handle logic
                ans = max(ans, windows_sum/k)
                # pop left
                windows_sum -= nums[left]
                left += 1
            right += 1

        return ans