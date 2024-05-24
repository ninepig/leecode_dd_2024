class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        ans = size + 1
        left , right = 0 , 0
        window_sum = 0
        while right < size:
            window_sum += nums[right]
            while window_sum > target:
                ans = min( ans, right - left + 1)
                window_sum -= nums[left]
                left += 1

            right += 1

        return ans if ans != size + 1 else 0
