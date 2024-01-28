class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            #删掉一个元素,所以长度要减少zero_count
            ans = max(right - left + 1 - zero_count, ans)

            right += 1

        return ans