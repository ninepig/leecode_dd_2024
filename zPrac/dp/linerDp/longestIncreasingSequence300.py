class Solution:
    # o(n2) time
    # o(n) space
    ''' 最长sequence
    state---> dp[n] means lis when we reach to nth of pos of string
    state inital --> dp[0] -- dp[n-1] = 1
    state transfer --> num[i] > num[j] --> max(dp[i],dp[j] + 1)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0 : return 0
        dp = [1] * len(nums)
        # j 是在后方追赶i的 所以是 num[I]》num【j】
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)

        return dp[-1]