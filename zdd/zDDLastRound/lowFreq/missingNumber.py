class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans

    def missingNumberSum(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return Tsum - actual_sum
