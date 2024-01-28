class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        # state, and initial 1 for each state
        dp = [1 for _ in range(size)]

        # state transfer
        for i in range(1,size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 对于i的数,找他之前所有的数,只要小于num[i] 我们就把它最长的lis放入dp之中
                    # 内部循环是根据i 找他之前所有的数
                    dp[i] = max(dp[i],dp[j] + 1 )

        return max(dp
                   )
