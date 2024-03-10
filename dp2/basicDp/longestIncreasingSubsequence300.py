class Solution:
    '''
    比如说输入 nums=[10,9,2,5,3,7,101,18]，其中最长的递增子序列是 [2,3,7,101]，所以算法的输出应该是 4。
    dp[n] 代表到达 index n， 我们可以做到的最长LIS。 不需要DP[n+1] 我们不需要哨兵
    dp[0] -->dp[n] 初始化1 ，最初的lis就是本身
    dp[i] = max（dp[i], dp[j] + 1) 如果 num[j] < num[i]
    然后取所有dp之中最大的纸
    '''
    def lengthOfLIS(nums: List[int]) -> int:
        if not nums: return 0
        #state, initial
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)

        res = max(dp)
        return res
