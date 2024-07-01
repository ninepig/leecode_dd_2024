class Solution:
    '''这种max最长 无外乎是dp 或者 local + max 的贪心'''
    # o(n)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local = 0
        global_max = 0
        for i in range(len(nums)):
            if nums[i] == 1 :
                local += 1
                global_max = max(local,global_max)
            else:
                local = 0

        return global_max