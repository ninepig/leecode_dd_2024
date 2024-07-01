class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        index = len(nums) - 1
        left = 0
        right = index
        while left < right:
            if abs(nums[left]) < abs(nums[right]):
                res[index] = nums[right] * nums[right]
                right -= 1
            elif abs(nums[left]) > abs(nums[right]):
                res[index] = nums[left] * nums[left]
                left += 1
            else:
                res[index] = nums[left] * nums[left]
                left += 1
            index -= 1

        return res