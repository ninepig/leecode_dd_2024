class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = float('-inf')
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                ans = max(ans,sum)
                left += 1
            else:
                right -= 1
        # we could have possibility, does not exit, so need check
        return ans if ans != float('-inf') else -1