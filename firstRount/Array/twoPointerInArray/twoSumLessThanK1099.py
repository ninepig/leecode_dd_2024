class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = float('-inf')
        while left < right:
            sum = nums[left] + nums[right]
            if sum > k :
                right -= 1
            else:
                res = max(sum,res)
                left += 1

        return res