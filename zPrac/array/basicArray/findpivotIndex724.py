class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftpreSum = 0
        totalSum = sum(nums)
        for i in range(len(nums) - 1):
            leftpreSum += nums[i]
            if leftpreSum * 2 + nums[i+1] == totalSum:
                return i + 1
        return -1

'''o(n) time'''
    def pivotIndexAnswer(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            # 先比较,这样就不用考虑加当前位,同时可以handle 和为0的情况,这样直接pivot就是0
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1