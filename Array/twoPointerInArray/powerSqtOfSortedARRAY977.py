class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left, right = 0, size - 1
        index = size - 1
        res = [0 for _ in range(size)]

        while left < right:
            if abs(nums[left]) < abs(nums[right]):
                res[index] = nums[right] * nums[right]
                right -= 1
            else:
                res[index] = nums[left] * nums[left]
                left += 1
            index -= 1
        res[index] = nums[left] * nums[left]

        return res
