class Solution:
    ##极度简单题
    def missingNumber(self, nums: List[int]) -> int:
        # initialize missing_num to n
        missing_num = len(nums)

        # loop through the array nums
        for i, num in enumerate(nums):
            # perform XOR operation with index and element
            missing_num ^= i ^ num

        # return the missing number
        return missing_num

    def missingNumberSum(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return Tsum - actual_sum
