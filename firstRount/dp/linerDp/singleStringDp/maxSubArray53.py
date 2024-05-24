'''
貪心/dp
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local = nums[0]
        max_ans = nums[0]
        #貪心只考慮當前狀態.當前狀態只需要考慮local是否小於0
        for i in range(1,len(nums)):
            if local < 0:
                local = nums[i] # if local smaller than 0, we start over from current nums
            else:
                local += nums[i] # we can still try to add
            max_ans = max(local,max_ans)

        return max_ans

    def maxSubArrayDp(self, nums: List[int]) -> int:
        size = len(nums)
        # dp[i]表示到达第i位 最大的子数组和
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]

        for i in range(1,size):
            # state transfer
            if dp[i-1] < 0:
                # 如果dp[i-1] 小于0,当前dp[i] 就是num[i]
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        return max(dp)